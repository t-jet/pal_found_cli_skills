"""Execute approved REST075 cases through the installed SDK without network access."""
import argparse
import asyncio
import copy
import hashlib
import importlib
import importlib.metadata
import inspect
import json
import socket
from contextlib import asynccontextmanager, contextmanager
from datetime import date, datetime, timezone
from pathlib import Path
from unittest.mock import patch
from urllib.parse import unquote

import httpx
import pydantic
from foundry_sdk import Config, PalantirRPCException, UserTokenAuth
from foundry_sdk._errors import SDKInternalError

TMP = Path(__file__).resolve().parent
SKILL = TMP / 'feature015_integration/.agents/skills/pal-found-dev'
CASES = TMP / 'rest075_formal_cases.json'
PENDING = TMP / 'rest075_formal_execution.json'
LOG = TMP / 'rest075_formal_execute.log'
ROWS = []


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def record(case, check, **detail):
    row = dict(case_id=case, check=check, result='PASS', **detail)
    ROWS.append(row)
    with LOG.open('a', encoding='utf-8') as stream:
        stream.write(json.dumps(row, default=str) + '\n')
    print(json.dumps(row, default=str), flush=True)


def denied(*args, **kwargs):
    raise AssertionError('PUBLIC_SOCKET_DENIED')


def normalized(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, pydantic.BaseModel):
        return normalized(value.model_dump(mode='python', by_alias=True, exclude_unset=True))
    if isinstance(value, dict):
        return {key: normalized(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [normalized(item) for item in value]
    if isinstance(value, str) and 'T' in value:
        try:
            return datetime.fromisoformat(value.replace('Z', '+00:00')).isoformat()
        except ValueError:
            pass
    return value


@contextmanager
def resource(cls, handler):
    with httpx.Client(transport=httpx.MockTransport(handler), timeout=7) as transport:
        with patch('foundry_sdk._core.api_client.HttpClient', return_value=transport):
            client = cls(auth=UserTokenAuth(token='independent-qa-075'),
                         hostname='independent-qa.invalid',
                         config=Config(timeout=7, max_retries=0,
                                       propagate_qos='PROPAGATE_429_AND_503_TO_CALLER'))
        yield client, transport
    assert transport.is_closed


@asynccontextmanager
async def async_resource(cls, handler):
    async with httpx.AsyncClient(transport=httpx.MockTransport(handler), timeout=7) as transport:
        with patch('foundry_sdk._core.api_client.AsyncHttpClient', return_value=transport):
            client = cls(auth=UserTokenAuth(token='independent-qa-075'),
                         hostname='independent-qa.invalid',
                         config=Config(timeout=7, max_retries=0,
                                       propagate_qos='PROPAGATE_429_AND_503_TO_CALLER'))
        yield client, transport
    assert transport.is_closed


async def async_success(case, cls, method):
    for raw in (False, True):
        calls, responses = [], []
        def handler(request):
            calls.append(request)
            wire_check(request, case['request']['expected_wire'])
            reply = case['success']
            reply_response = response(reply)
            responses.append(reply_response)
            return reply_response
        async with async_resource(cls, handler) as (client, _):
            result = await invoke(client, method, case['request']['kwargs'], raw)
            if raw:
                wrapper = result
                try:
                    assert wrapper.status_code == case['success']['http_status']
                    result = wrapper.decode()
                finally:
                    await wrapper.aclose()
                assert responses[0].is_closed
            assert normalized(result) == expected_decoded(case, case['success'])
            semantic_check(case, case['request']['kwargs'], normalized(result), 'success')
        assert len(calls) == 1
        record(case['case_id'], 'async_raw_closed' if raw else 'async_typed', requests=1)


def wire_check(request, expected, prefix='/api'):
    path = expected['resource_path'].format(**expected['path_params'])
    assert request.method == expected['method'], (request.method, expected)
    assert unquote(request.url.path) == prefix + path, (request.url.path, path)
    query = []
    for key, value in expected['query_params'].items():
        if value is None:
            continue
        for item in value if isinstance(value, list) else [value]:
            query.append((key, str(item).lower() if isinstance(item, bool) else str(item)))
    assert sorted(request.url.params.multi_items()) == sorted(query), request.url
    assert request.headers['authorization'] == 'Bearer independent-qa-075'
    for key, value in expected['header_params'].items():
        if value is not None:
            assert request.headers[key] == value, (key, request.headers)
    expected_body = materialize(expected['body'])
    body = request.content if isinstance(expected_body, bytes) else (json.loads(request.content) if request.content else None)
    assert body == expected_body, (body, expected_body)
    assert request.extensions['timeout']['read'] == 7


def invoke(client, method, kwargs, raw=False):
    if raw:
        return getattr(client.with_raw_response, method)(**materialize(copy.deepcopy(kwargs)), request_timeout=7)
    return getattr(client, method)(**materialize(copy.deepcopy(kwargs)), request_timeout=7, _sdk_internal={'response_mode': 'DECODED'})


def semantic_check(case, kwargs, value, label):
    if value is None:
        return
    name, method = case['operation'].split('.')[-2:]
    if method == 'get_batch':
        key = name[0].lower() + name[1:] + 'Rid'
        requested = [item[key] for item in kwargs['body']]
        assert len(requested) == 2 and requested[0] != requested[1]
        assert set(value['data']) == {requested[0]}
        assert value['data'][requested[0]]['rid'] == requested[0]
        assert requested[1] not in value['data']
        return
    if name == 'ScheduleVersion' and method == 'schedule':
        assert value['rid'] != kwargs['schedule_version_rid']
        assert value['currentVersionRid'] == kwargs['schedule_version_rid']
        return
    rows = value.get('data', [value]) if isinstance(value, dict) else value
    for item in rows:
        if name == 'Record':
            if method == 'get':
                assert item['rid'] == kwargs['record_rid']
            if method == 'search':
                assert item['justification']['response'] == kwargs['where']['filter']['query']
            assert item['type'] == 'RUN_BUILD'
            assert item['checkpointedItems'][0]['type'] == 'checkpointedJob'
        if name == 'Check':
            if 'check_rid' in kwargs:
                assert item['rid'] == kwargs['check_rid']
            if 'config' in kwargs:
                assert item['config'] == kwargs['config']
        if name == 'CheckReport':
            assert item['check']['rid'] == kwargs['check_rid']
            if 'check_report_rid' in kwargs:
                assert item['rid'] == kwargs['check_report_rid']
        if name == 'Build':
            if method == 'jobs':
                assert item['buildRid'] == kwargs['build_rid']
            elif method == 'get':
                assert item['rid'] == kwargs['build_rid']
            elif method == 'create':
                assert item['branchName'] == kwargs.get('branch_name', None) or item['branchName'] == 'master'
                assert item['fallbackBranches'] == kwargs['fallback_branches']
            elif method == 'search':
                boundary = datetime.fromisoformat(kwargs['where']['value'].replace('Z', '+00:00'))
                started = case['search_state']['started_time_by_build_rid'][item['rid']]
                assert datetime.fromisoformat(started.replace('Z', '+00:00')) >= boundary
        if name == 'Job' and method == 'get':
            assert item['rid'] == kwargs['job_rid']
        if name == 'Schedule':
            if method == 'get_affected_resources':
                assert value['datasets'] == ['ri.qa.main.dataset-output.independent075']
                continue
            if method == 'get':
                assert item['rid'] == kwargs['schedule_rid']
            if method in ('create', 'replace'):
                assert item['action'] == kwargs['action']
                target = item['action']['target']
                assert set(target['targetRids']).isdisjoint(target['ignoredRids'])
            if method in ('run', 'runs'):
                assert item['scheduleRid'] == kwargs['schedule_rid']
                assert item['result']['type'] == 'submitted'
        if name == 'ScheduleVersion' and method == 'get':
            assert item['rid'] == kwargs['schedule_version_rid']


def materialize(value):
    if isinstance(value, dict):
        if set(value) == {'__bytes_hex__'}:
            return bytes.fromhex(value['__bytes_hex__'])
        return {key: materialize(item) for key, item in value.items()}
    if isinstance(value, list):
        return [materialize(item) for item in value]
    return value


def response(reply):
    if 'content_hex' in reply:
        return httpx.Response(reply['http_status'], content=bytes.fromhex(reply['content_hex']))
    if reply['http_status'] == 204:
        return httpx.Response(204)
    return httpx.Response(reply['http_status'], json=reply['json'])


def expected_result(reply):
    return bytes.fromhex(reply['content_hex']) if 'content_hex' in reply else reply['json']


def expected_decoded(case, reply):
    module = importlib.import_module(case['source']['module'])
    declared = eval(case['source']['request_expressions']['response_type'], vars(module))
    return normalized(pydantic.TypeAdapter(declared).validate_python(expected_result(reply)))


def success(case, cls, method, kwargs=None, expected_wire=None, reply=None, label='success'):
    kwargs = case['request']['kwargs'] if kwargs is None else kwargs
    expected_wire = case['request']['expected_wire'] if expected_wire is None else expected_wire
    reply = case['success'] if reply is None else reply
    for raw in (False, True):
        calls = []
        responses = []
        def handler(request):
            calls.append(request)
            wire_check(request, expected_wire, case['request']['path_prefix'])
            reply_response = response(reply)
            responses.append(reply_response)
            return reply_response
        with resource(cls, handler) as (client, transport):
            result = invoke(client, method, kwargs, raw)
            if raw:
                wrapper = result
                try:
                    assert wrapper.status_code == reply['http_status']
                    result = wrapper.decode()
                finally:
                    wrapper.close()
                assert responses[0].is_closed
            expected = expected_result(reply)
            assert normalized(result) == expected_decoded(case, reply), (case['operation'], normalized(result), expected)
            semantic_check(case, kwargs, normalized(result), label)
            module = importlib.import_module(case['source']['module'])
            declared = eval(case['source']['request_expressions']['response_type'], vars(module))
            if inspect.isclass(declared) and issubclass(declared, pydantic.BaseModel):
                assert isinstance(result, declared), type(result)
        assert len(calls) == 1, len(calls)
        record(case['case_id'], label + ('_raw_closed' if raw else '_typed'), requests=1)


def failure(case, cls, method, status, name, code, parameters, expected_class=None, kwargs=None, wire=None):
    calls = []
    envelope = dict(errorName=name, errorCode=code, parameters=parameters,
                    errorInstanceId='00000000-0000-0000-0000-000000000075')
    def handler(request):
        calls.append(request)
        wire_check(request, wire or case['request']['expected_wire'])
        return httpx.Response(status, json=envelope)
    with resource(cls, handler) as (client, _):
        try:
            invoke(client, method, kwargs or case['request']['kwargs'])
        except PalantirRPCException as error:
            if expected_class:
                module, class_name = expected_class.rsplit('.', 1)
                assert type(error) is getattr(importlib.import_module(module), class_name), type(error)
            assert error.name == name
            assert normalized(error.parameters) == normalized(parameters)
            assert error.error_instance_id == envelope['errorInstanceId']
            if expected_class:
                # Named errors are dataclasses; SDK does not retain error_code on them.
                base_name = {400: 'BadRequestError', 403: 'PermissionDeniedError',
                             404: 'NotFoundError', 409: 'ConflictError',
                             413: 'RequestEntityTooLargeError',
                             422: 'UnprocessableEntityError'}.get(status)
                if base_name:
                    assert isinstance(error, getattr(importlib.import_module('foundry_sdk._errors'), base_name))
            else:
                assert error.error_code == code
        else:
            raise AssertionError('service failure was accepted')
    assert len(calls) == 1, len(calls)
    record(case['case_id'], 'error_' + name, status=status, requests=1)


def iterator_fixture(case):
    fixture = next(row for row in case['additional_cases'] if row['name'] == 'finite continuation')
    assert fixture['expected_terminal_token'] is None
    assert not fixture['responses'][-1].get('nextPageToken')
    return fixture


async def ordinary_async_iterator(case, cls, method):
    fixture, calls = iterator_fixture(case), []
    def handler(request):
        index = len(calls)
        assert index < fixture['expected_request_count'], 'iterator exceeded finite page budget'
        wire_check(request, fixture['expected_wires'][index])
        calls.append(request)
        return httpx.Response(200, json=fixture['responses'][index])
    async with async_resource(cls, handler) as (client, _):
        iterator = getattr(client, method)(**fixture['requests'][0], request_timeout=7)
        assert not inspect.isawaitable(iterator)
        items = []
        async for item in iterator:
            items.append(normalized(item))
            assert len(items) <= 2
        assert items == normalized([item for page in fixture['responses'] for item in page['data']])
    assert len(calls) == fixture['expected_request_count']
    record(case['case_id'], 'ordinary_async_iterator_terminal_closed', requests=len(calls), items=items)


def ordinary_iterator(case, module, cls, method):
    fixture, calls = iterator_fixture(case), []
    def handler(request):
        index = len(calls)
        assert index < fixture['expected_request_count'], 'iterator exceeded finite page budget'
        wire_check(request, fixture['expected_wires'][index])
        calls.append(request)
        return httpx.Response(200, json=fixture['responses'][index])
    with resource(cls, handler) as (client, _):
        iterator = getattr(client, method)(**fixture['requests'][0], request_timeout=7)
        items = [normalized(item) for item in iterator]
        assert items == normalized([item for page in fixture['responses'] for item in page['data']])
    assert len(calls) == fixture['expected_request_count']
    record(case['case_id'], 'ordinary_sync_iterator_terminal_closed', requests=len(calls), items=items)
    EVENT_LOOP.run_until_complete(ordinary_async_iterator(case, getattr(module, 'Async' + cls.__name__), method))


def streaming_success(case, cls, method):
    calls, responses = [], []
    def handler(request):
        wire_check(request, case['request']['expected_wire'])
        calls.append(request)
        reply = response(case['success'])
        responses.append(reply)
        return reply
    with resource(cls, handler) as (client, _):
        available = hasattr(client.with_streaming_response, method)
        assert available == case['available_modes']['sync_stream']
        if not available:
            record(case['case_id'], 'sync_stream_absent_in_source', requests=0)
            return
        with getattr(client.with_streaming_response, method)(**materialize(case['request']['kwargs']), request_timeout=7) as wrapper:
            chunks = bounded_chunks(wrapper.iter_bytes(chunk_size=5), max_bytes=1048576, max_chunks=10000)
            assert chunks == bytes.fromhex(case['success']['content_hex']) if 'content_hex' in case['success'] else (json.loads(chunks) == case['success']['json'] if case['success']['http_status'] != 204 else chunks == b'')
            assert normalized(wrapper.decode()) == expected_decoded(case, case['success'])
        assert responses[0].is_closed
    assert len(calls) == 1
    record(case['case_id'], 'sync_stream_closed', requests=1)


async def async_streaming_success(case, cls, method):
    calls, responses = [], []
    def handler(request):
        wire_check(request, case['request']['expected_wire'])
        calls.append(request)
        reply = response(case['success'])
        responses.append(reply)
        return reply
    async with async_resource(cls, handler) as (client, _):
        available = hasattr(client.with_streaming_response, method)
        assert available == case['available_modes']['async_stream']
        if not available:
            record(case['case_id'], 'async_stream_absent_in_source', requests=0)
            return
        async with getattr(client.with_streaming_response, method)(**materialize(case['request']['kwargs']), request_timeout=7) as wrapper:
            parts = []
            total = 0
            async for chunk in wrapper.aiter_bytes(chunk_size=5):
                total += len(chunk)
                assert total <= 1048576 and len(parts) < 10000, 'REST075_RESPONSE_BUDGET_EXCEEDED'
                parts.append(chunk)
            chunks = b''.join(parts)
            assert chunks == bytes.fromhex(case['success']['content_hex']) if 'content_hex' in case['success'] else (json.loads(chunks) == case['success']['json'] if case['success']['http_status'] != 204 else chunks == b'')
            assert normalized(wrapper.decode()) == expected_decoded(case, case['success'])
        assert responses[0].is_closed
    assert len(calls) == 1
    record(case['case_id'], 'async_stream_closed', requests=1)


def execute(manifest):
    for case in manifest['operations']:
        module = importlib.import_module(case['source']['module'])
        name, method = case['operation'].split('.')[-2:]
        cls = getattr(module, name + 'Client')
        if 'ITERATOR' in case['source']['request_expressions']['response_mode']:
            ordinary_iterator(case, module, cls, method)
        success(case, cls, method)
        EVENT_LOOP.run_until_complete(async_success(case, getattr(module, 'Async' + name + 'Client'), method))
        streaming_success(case, cls, method)
        EVENT_LOOP.run_until_complete(async_streaming_success(case, getattr(module, 'Async' + name + 'Client'), method))
        for error in case['errors']:
            failure(case, cls, method, error['status'], error['name'], error['errorCode'],
                    error['parameters'], error['expected']['exception_class'],
                    error.get('request'), error.get('expected_wire'))
        for status in (401, 403):
            failure(case, cls, method, status, 'IndependentUnauthorized' if status == 401 else 'IndependentPermissionDenied', 'UNAUTHORIZED' if status == 401 else 'PERMISSION_DENIED', {})
        calls = []
        def timeout(request):
            calls.append(request)
            wire_check(request, case['request']['expected_wire'])
            raise httpx.ReadTimeout('independent fixture timeout', request=request)
        with resource(cls, timeout) as (client, _):
            try:
                invoke(client, method, case['request']['kwargs'])
            except Exception as error:
                assert 'timeout' in type(error).__name__.lower(), type(error)
            else:
                raise AssertionError('timeout was accepted')
        assert len(calls) == 1
        record(case['case_id'], 'timeout_no_retry', requests=1)
        if case['success']['http_status'] != 204 and 'content_hex' not in case['success']:
            with resource(cls, lambda request: httpx.Response(200, content=b'{invalid',
                           headers={'content-type': 'application/json'})) as (client, _):
                try:
                    invoke(client, method, case['request']['kwargs'])
                except (ValueError, pydantic.ValidationError):
                    pass
                except SDKInternalError as error:
                    assert isinstance(error.__cause__, json.JSONDecodeError), repr(error.__cause__)
                else:
                    raise AssertionError('malformed response was accepted')
            record(case['case_id'], 'malformed_json')
        signature = inspect.signature(getattr(cls, method))
        required = [key for key, parameter in signature.parameters.items()
                    if key != 'self' and parameter.default is inspect.Parameter.empty
                    and parameter.kind not in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD)]
        for key in required:
            kwargs = copy.deepcopy(case['request']['kwargs'])
            del kwargs[key]
            with resource(cls, denied) as (client, _):
                try:
                    invoke(client, method, kwargs)
                except pydantic.ValidationError:
                    pass
                else:
                    raise AssertionError('missing required argument accepted: ' + key)
            record(case['case_id'], 'missing_required_' + key, requests=0)
        for extra in case.get('execution_variants', []):
            success(case, cls, method, extra['kwargs'], extra['expected_wire'],
                    extra.get('success', case['success']), extra['name'])
        for extra in case.get('execution_error_variants', []):
            failure(case, cls, method, extra['status'], extra['name'], extra['errorCode'],
                    extra['parameters'], extra.get('exception_class'), extra['kwargs'], extra['expected_wire'])
        for extra in case.get('additional_cases', []):
            label = extra['name']
            if 'expected_exception' in extra:
                with resource(cls, denied) as (client, _):
                    try:
                        invoke(client, method, extra['request'])
                    except Exception as error:
                        expected_module, expected_name = extra['expected_exception'].rsplit('.', 1)
                        assert type(error) is getattr(importlib.import_module(expected_module), expected_name), (label, type(error))
                    else:
                        raise AssertionError('Invalid request accepted: ' + label)
                record(case['case_id'], label, requests=0)
            elif 'requests' in extra:
                calls = []
                def page(request):
                    index = len(calls)
                    assert index < len(extra['requests']), 'finite page budget exceeded'
                    wire_check(request, extra['expected_wires'][index])
                    calls.append(request)
                    return httpx.Response(200, json=extra['responses'][index])
                with resource(cls, page) as (client, _):
                    token, items = None, []
                    for index, kwargs in enumerate(extra['requests']):
                        assert kwargs.get('page_token') == token
                        result = normalized(invoke(client, method, kwargs))
                        assert result == normalized(extra['responses'][index])
                        semantic_check(case, kwargs, result, label)
                        items.extend(result['data'])
                        token = result.get('nextPageToken')
                    assert token == extra['expected_terminal_token']
                    assert len(items) == 2 and items[0] != items[1]
                assert len(calls) == extra['expected_request_count']
                record(case['case_id'], label, requests=len(calls), items=items)
            elif 'error' in extra:
                error = next(row for row in case['errors'] if row['name'] == extra['error'])
                failure(case, cls, method, error['status'], error['name'], error['errorCode'], error['parameters'], error['expected']['exception_class'], extra['request'], extra['expected_wire'])
            elif 'request' in extra and 'expected_wire' in extra:
                reply = extra.get('success', dict(http_status=extra.get('response_status', case['success']['http_status']), json=extra.get('response', extra.get('expected_result'))))
                success(case, cls, method, extra['request'], extra['expected_wire'], reply, label)
            elif label != 'required argument omitted':
                raise AssertionError('Additional case lacks executable expectations: ' + label)


def preflight(manifest):
    assert importlib.metadata.version('foundry-platform-sdk') == manifest['sdk_release']
    assert len(manifest['operations']) == 29
    for path, expected in manifest['model_source_bindings'].items():
        assert digest(path) == expected, path
    for case in manifest['operations']:
        canonical = {key: value for key, value in case.items() if key != 'case_sha256'}
        assert hashlib.sha256(json.dumps(canonical, sort_keys=True, separators=(',', ':')).encode()).hexdigest() == case['case_sha256']
        assert digest(case['source']['path']) == case['source']['sha256']
        for asset in case['assets'].values():
            assert digest(SKILL / asset['path']) == asset['sha256'], asset['path']
        for error in case['errors']:
            assert digest(error['error_source']) == error['error_source_sha256']
        module = importlib.import_module(case['source']['module'])
        resource_name, method = case['operation'].split('.')[-2:]
        hints = inspect.get_annotations(getattr(getattr(module, resource_name + 'Client'), method), eval_str=True)
        async_hints = inspect.get_annotations(getattr(getattr(module, 'Async' + resource_name + 'Client'), method), eval_str=True)
        assert {k: v for k, v in hints.items() if k != 'return'} == \
               {k: v for k, v in async_hints.items() if k != 'return'}, \
               'Sync/async request annotation divergence requires explicit review'
        for key, value in case['request']['kwargs'].items():
            pydantic.TypeAdapter(hints[key]).validate_python(materialize(value))
        for error in case['errors']:
            for key, value in error.get('request', {}).items():
                pydantic.TypeAdapter(hints[key]).validate_python(materialize(value))
        for declared in case['errors']:
            mod_name, class_name = declared['expected']['exception_class'].rsplit('.', 1)
            cls = getattr(importlib.import_module(mod_name), class_name)
            parameter_type = __import__('typing').get_type_hints(cls)['parameters']
            pydantic.TypeAdapter(parameter_type).validate_python(declared['parameters'])
            if declared['name'] == 'ModifyingCheckTypeNotSupported':
                assert declared['parameters']['originalCheckType'] != declared['parameters']['newCheckType']
                assert declared['parameters']['newCheckType'] == declared['request']['config']['type']
        response_type = eval(case['source']['request_expressions']['response_type'], vars(module))
        pydantic.TypeAdapter(response_type).validate_python(expected_result(case['success']))
        semantic_check(case, case['request']['kwargs'], expected_result(case['success']), 'success')
        for extra in case.get('additional_cases', []):
            if 'expected_exception' in extra:
                continue
            requests = extra.get('requests', [extra['request']] if 'request' in extra else [])
            if 'boundary_request' in extra:
                requests = requests + [extra['boundary_request']]
            for kwargs in requests:
                for key, value in kwargs.items():
                    pydantic.TypeAdapter(hints[key]).validate_python(materialize(value))
            responses = ([expected_result(extra['success'])] if 'success' in extra else extra.get('responses', [extra['response']] if 'response' in extra else []))
            if 'boundary_response' in extra:
                responses = responses + [extra['boundary_response']]
            for response in responses:
                pydantic.TypeAdapter(response_type).validate_python(response)
            for kwargs, reply in zip(extra.get('requests', []), extra.get('responses', [])):
                semantic_check(case, kwargs, reply, extra['name'])
            if 'request' in extra and 'expected_wire' in extra and 'error' not in extra and 'error_envelope' not in extra:
                semantic_check(case, extra['request'], expected_result(extra['success']) if 'success' in extra else extra.get('response', extra.get('expected_result')), extra['name'])
            if 'boundary_request' in extra:
                semantic_check(case, extra['boundary_request'], extra['boundary_response'], extra['name'] + '_500')


_typed_failure = failure


def assert_service_error(error, name, code, parameters, expected_class):
    assert isinstance(error, PalantirRPCException), type(error)
    assert error.name == name
    assert normalized(error.parameters) == normalized(parameters)
    assert error.error_instance_id == '00000000-0000-0000-0000-000000000075'
    if expected_class:
        module, cls = expected_class.rsplit('.', 1)
        assert type(error) is getattr(importlib.import_module(module), cls)
    else:
        assert error.error_code == code


def failure(case, cls, method, status, name, code, parameters, expected_class=None, kwargs=None, wire=None):
    _typed_failure(case, cls, method, status, name, code, parameters, expected_class, kwargs, wire)
    kwargs = kwargs or case['request']['kwargs']
    wire = wire or case['request']['expected_wire']
    envelope = dict(errorName=name, errorCode=code, parameters=parameters,
                    errorInstanceId='00000000-0000-0000-0000-000000000075')
    for mode in ('raw', 'stream'):
        if mode == 'stream' and not case['available_modes']['sync_stream']:
            with resource(cls, denied) as (client, _):
                assert not hasattr(client.with_streaming_response, method)
            record(case['case_id'], 'error_' + name + '_sync_stream_absent_in_source', requests=0)
            continue
        calls, responses = [], []
        def handler(request):
            wire_check(request, wire)
            calls.append(request)
            reply = httpx.Response(status, json=envelope)
            responses.append(reply)
            return reply
        with resource(cls, handler) as (client, _):
            try:
                if mode == 'raw':
                    invoke(client, method, kwargs, True)
                else:
                    with getattr(client.with_streaming_response, method)(**materialize(kwargs), request_timeout=7):
                        raise AssertionError('Failed service response entered success stream')
            except PalantirRPCException as error:
                assert_service_error(error, name, code, parameters, expected_class)
            else:
                raise AssertionError('Service error accepted')
        assert len(calls) == 1 and all(reply.is_closed for reply in responses)
        record(case['case_id'], 'error_' + name + '_sync_' + mode + '_closed', requests=1)
    async_cls = getattr(importlib.import_module(case['source']['module']), 'Async' + cls.__name__)
    async def run():
        for mode in ('typed', 'raw', 'stream'):
            if mode == 'stream' and not case['available_modes']['async_stream']:
                async with async_resource(async_cls, denied) as (client, _):
                    assert not hasattr(client.with_streaming_response, method)
                record(case['case_id'], 'error_' + name + '_async_stream_absent_in_source', requests=0)
                continue
            calls, responses = [], []
            def handler(request):
                wire_check(request, wire)
                calls.append(request)
                reply = httpx.Response(status, json=envelope)
                responses.append(reply)
                return reply
            async with async_resource(async_cls, handler) as (client, _):
                try:
                    if mode == 'stream':
                        async with getattr(client.with_streaming_response, method)(**materialize(kwargs), request_timeout=7):
                            raise AssertionError('Failed service response entered success stream')
                    else:
                        await invoke(client, method, kwargs, mode == 'raw')
                except PalantirRPCException as error:
                    assert_service_error(error, name, code, parameters, expected_class)
                else:
                    raise AssertionError('Async service error accepted')
            assert len(calls) == 1 and all(reply.is_closed for reply in responses)
            record(case['case_id'], 'error_' + name + '_async_' + mode + '_closed', requests=1)
    EVENT_LOOP.run_until_complete(run())


def bounded_chunks(chunks, max_bytes, max_chunks):
    collected = bytearray()
    for count, chunk in enumerate(chunks, 1):
        if count > max_chunks or len(collected) + len(chunk) > max_bytes:
            raise RuntimeError('REST075_RESPONSE_BUDGET_EXCEEDED')
        collected.extend(chunk)
    return bytes(collected)


def pipeline_lifecycle(manifest):
    journey = manifest['journeys'][0]
    by_id = {case['operation']: case for case in manifest['operations']}
    observed = {}
    for step in journey['steps']:
        base = by_id[step['operation']]
        case = copy.deepcopy(base)
        case['success'] = copy.deepcopy(step['success'])
        module = importlib.import_module(base['source']['module'])
        name, method = base['operation'].split('.')[-2:]
        success(case, getattr(module, name + 'Client'), method, label='pipeline_' + step['name'])
        observed[step['name']] = step['success']['json']
    assert observed['submitted']['result']['buildRid'] == observed['running']['rid'] == observed['succeeded']['rid']
    assert observed['job']['buildRid'] == observed['succeeded']['rid']
    assert observed['checkpoint']['checkpointedItems'][0]['jobRid'] == observed['job']['rid']
    assert observed['report']['check']['rid'] == observed['check']['rid']
    assert observed['succeeded']['status'] == observed['job']['jobStatus'] == 'SUCCEEDED'
    assert observed['report']['result']['status'] == 'PASSED'
    assert observed['paused']['paused'] is True
    assert observed['unpaused']['paused'] is False
    assert len(journey['steps']) <= journey['max_requests_per_mode']
    record('J12-REST075', 'bounded_lifecycle_links_and_state', requests=len(journey['steps']) * 2)
    first = by_id['v2.orchestration.Schedule.get']
    module = importlib.import_module(first['source']['module'])
    mutations = []
    with resource(module.ScheduleClient, lambda request: httpx.Response(403, json={
            'errorName': 'IndependentDenied075', 'errorCode': 'PERMISSION_DENIED',
            'errorInstanceId': '00000000-0000-0000-0000-000000000075', 'parameters': {}})) as (client, _):
        try:
            invoke(client, 'get', first['request']['kwargs'])
            mutations.append('run')
            invoke(client, 'run', by_id['v2.orchestration.Schedule.run']['request']['kwargs'])
        except PalantirRPCException as error:
            assert error.error_code == 'PERMISSION_DENIED'
        else:
            raise AssertionError('Denied preflight accepted')
    assert mutations == []
    record('J12-REST075', 'denied_preflight_stops_before_mutation', requests=1)
    for kind in ('bytes', 'chunks'):
        try:
            bounded_chunks([b'abc', b'def'], 4 if kind == 'bytes' else 100, 1 if kind == 'chunks' else 100)
        except RuntimeError as error:
            assert str(error) == 'REST075_RESPONSE_BUDGET_EXCEEDED'
        else:
            raise AssertionError('Response budget accepted')
        record('REST075', kind + '_budget_rejects_overflow')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--execute', action='store_true')
    parser.add_argument('--executor-identity')
    parser.add_argument('--testcase-closed')
    parser.add_argument('--approved-cases-sha256')
    parser.add_argument('--readiness-confirmed', action='store_true')
    parser.add_argument('--reviewer-identity')
    parser.add_argument('--approved-harness-sha256')
    args = parser.parse_args()
    manifest = json.loads(CASES.read_text(encoding='utf-8'))
    preflight(manifest)
    evidence = dict(story='DEV-STORY-075', testcase='TESTCASE-077', executor_identity=args.executor_identity,
                    harness_sha256=digest(__file__), cases_sha256=digest(CASES),
                    operations=len(manifest['operations']), declared_errors=sum(len(c['errors']) for c in manifest['operations']),
                    execution='NOT_RUN', created_at=datetime.now(timezone.utc).isoformat())
    if not args.execute:
        PENDING.write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
        print(json.dumps(evidence))
        return
    assert args.executor_identity and args.executor_identity != manifest['author_identity'], 'Actual independent executor identity required'
    assert args.testcase_closed == 'TESTCASE-077', 'Parent confirmation of actual Closed state required'
    assert args.approved_cases_sha256 == digest(CASES), 'Independent case approval for this exact manifest required'
    assert args.readiness_confirmed, 'Parent readiness confirmation required'
    assert args.reviewer_identity and args.reviewer_identity not in (manifest['author_identity'], args.executor_identity), 'Fresh case reviewer and executor required'
    assert args.approved_harness_sha256 == digest(__file__), 'Approval must bind exact harness'
    evidence['reviewer_identity'] = args.reviewer_identity
    assert not PENDING.exists() or json.loads(PENDING.read_bytes()).get('execution') == 'NOT_RUN', 'Preserve prior execution evidence before rerun'
    LOG.write_text('', encoding='utf-8')
    global EVENT_LOOP
    EVENT_LOOP = asyncio.new_event_loop()
    try:
        with patch('socket.socket.connect', denied), patch('socket.socket.connect_ex', denied), \
             patch('socket.create_connection', denied), patch('socket.getaddrinfo', denied), \
             patch('socket.gethostbyname', denied), patch('socket.gethostbyname_ex', denied), \
             patch('socket.getnameinfo', denied):
            def socket_probe(method):
                with socket.socket() as probe:
                    getattr(probe, method)(('1.1.1.1', 443))
            for probe in (lambda: socket.create_connection(('www.palantir.com', 443)),
                          lambda: socket.getaddrinfo('www.palantir.com', 443),
                          lambda: socket.gethostbyname('www.palantir.com'),
                          lambda: socket.gethostbyname_ex('www.palantir.com'),
                          lambda: socket.getnameinfo(('1.1.1.1', 443), 0),
                          lambda: socket_probe('connect'),
                          lambda: socket_probe('connect_ex')):
                try:
                    probe()
                except AssertionError as error:
                    assert str(error) == 'PUBLIC_SOCKET_DENIED'
                else:
                    raise AssertionError('socket trap inactive')
            record('REST075', 'socket_traps_active')
            execute(manifest)
            pipeline_lifecycle(manifest)
        preflight(manifest)
        assert evidence['cases_sha256'] == digest(CASES), 'Manifest changed during execution'
        evidence.update(execution='PASS', results=ROWS, completed_at=datetime.now(timezone.utc).isoformat())
    except Exception as error:
        evidence.update(execution='FAIL', results=ROWS, failure=repr(error))
        raise
    finally:
        EVENT_LOOP.close()
        PENDING.write_text(json.dumps(evidence, indent=2, default=str) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
