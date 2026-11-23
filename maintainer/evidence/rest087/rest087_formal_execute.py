"""Execute approved REST087 cases through the installed SDK without network access."""
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
CASES = TMP / 'rest087_formal_cases.json'
PENDING = TMP / 'rest087_formal_execution.json'
LOG = TMP / 'rest087_formal_execute.log'
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
            client = cls(auth=UserTokenAuth(token='independent-qa-087'),
                         hostname='independent-qa.invalid',
                         config=Config(timeout=7, max_retries=0,
                                       propagate_qos='PROPAGATE_429_AND_503_TO_CALLER'))
        yield client, transport
    assert transport.is_closed


@asynccontextmanager
async def async_resource(cls, handler):
    async with httpx.AsyncClient(transport=httpx.MockTransport(handler), timeout=7) as transport:
        with patch('foundry_sdk._core.api_client.AsyncHttpClient', return_value=transport):
            client = cls(auth=UserTokenAuth(token='independent-qa-087'),
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
    assert request.headers['authorization'] == 'Bearer independent-qa-087'
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
    if not isinstance(value, dict):
        return
    name, method = case['operation'].split('.')[-2:]
    if name == 'Agent' and method == 'get':
        assert value['rid'] == kwargs['agent_rid']
        if kwargs.get('version'):
            assert value['version'] == kwargs['version']
    if name == 'Experiment' and method == 'get':
        assert value['rid'] == kwargs['experiment_rid']
        assert value['modelRid'] == kwargs['model_rid']
    if name == 'AgentVersion':
        values = value.get('data', [value])
        for version in values:
            assert version['string'] == str(version['version']['major']) + '.' + str(version['version']['minor'])
    if name == 'Session' and method in ('create', 'get'):
        assert value['agentRid'] == kwargs['agent_rid']
        if 'session_rid' in kwargs:
            assert value['rid'] == kwargs['session_rid']
        if kwargs.get('agent_version'):
            assert value['agentVersion'] == kwargs['agent_version']
    if name == 'Model' and method == 'promote_version':
        assert value['rid'] != kwargs['source_model_version_rid']
        assert value['rid'] != kwargs['model_rid']
    if name == 'LiveDeployment' and method in ('create', 'replace'):
        assert value['runtimeConfiguration'] == kwargs['runtime_configuration']
    if name == 'OpenAiModel':
        assert len(value['data']) == len(kwargs['input'])
        assert value['model'] == kwargs['open_ai_model_model_id']
    if name == 'ModelStudioConfigVersion' and 'version' in value:
        if 'model_studio_config_version_version' in kwargs:
            assert value['version'] == kwargs['model_studio_config_version_version']
    if name == 'ModelStudioTrainer' and method == 'get':
        assert value['trainerId'] == kwargs['model_studio_trainer_trainer_id']
        if kwargs.get('version'):
            assert value['version'] == kwargs['version']


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
                    errorInstanceId='00000000-0000-0000-0000-000000000087')
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
        if not hasattr(client.with_streaming_response, method):
            return
        with getattr(client.with_streaming_response, method)(**materialize(case['request']['kwargs']), request_timeout=7) as wrapper:
            chunks = b''.join(wrapper.iter_bytes(chunk_size=5))
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
        if not hasattr(client.with_streaming_response, method):
            return
        async with getattr(client.with_streaming_response, method)(**materialize(case['request']['kwargs']), request_timeout=7) as wrapper:
            chunks = b''.join([chunk async for chunk in wrapper.aiter_bytes(chunk_size=5)])
            assert chunks == bytes.fromhex(case['success']['content_hex']) if 'content_hex' in case['success'] else (json.loads(chunks) == case['success']['json'] if case['success']['http_status'] != 204 else chunks == b'')
            assert normalized(wrapper.decode()) == expected_decoded(case, case['success'])
        assert responses[0].is_closed
    assert len(calls) == 1
    record(case['case_id'], 'async_stream_closed', requests=1)


def native_integer_path_error(error, wrapped):
    message = 'quote_from_bytes() expected bytes'
    if wrapped:
        assert type(error) is SDKInternalError
        assert error.msg == message
        assert type(error.__cause__) is TypeError
        assert str(error.__cause__) == message
    else:
        assert type(error) is TypeError
        assert str(error) == message


def bridge_case(case, module, cls, method):
    import runpy
    calls = []
    def forbidden(request):
        calls.append(request)
        raise AssertionError('Native integer-path request unexpectedly reached HTTP')
    for raw in (False, True):
        with resource(cls, forbidden) as (client, _):
            try:
                invoke(client, method, case['request']['kwargs'], raw)
            except SDKInternalError as error:
                native_integer_path_error(error, wrapped=True)
            else:
                raise AssertionError('Native integer-path limitation disappeared')
        assert calls == []
        record(case['case_id'], 'native_raw_integer_path_denied' if raw else 'native_sync_integer_path_denied', requests=0)
    async def async_native():
        for raw in (False, True):
            async with async_resource(getattr(module, 'Async' + cls.__name__), forbidden) as (client, _):
                try:
                    await invoke(client, method, case['request']['kwargs'], raw)
                except TypeError as error:
                    native_integer_path_error(error, wrapped=False)
                else:
                    raise AssertionError('Native async integer-path limitation disappeared')
            assert calls == []
            record(case['case_id'], 'native_async_raw_integer_path_denied' if raw else 'native_async_integer_path_denied', requests=0)
    EVENT_LOOP.run_until_complete(async_native())
    adapter_path = SKILL / case['direct_rest_adapter']['path']
    assert digest(adapter_path) == case['direct_rest_adapter']['sha256']
    function = runpy.run_path(str(adapter_path))['get_config_version']
    options = copy.deepcopy(case['direct_rest_adapter']['kwargs'])
    responses = []
    def run_bridge(reply, options_override=None, expected_exception=None, expected_named=None):
        requests = []
        def handler(request):
            wire_check(request, case['request']['expected_wire'])
            requests.append(request)
            returned = response(reply)
            responses.append(returned)
            return returned
        with httpx.Client(transport=httpx.MockTransport(handler)) as http:
            selected = dict(options, **(options_override or {}))
            try:
                result = function(http, **selected)
            except Exception as error:
                assert expected_exception and isinstance(error, expected_exception), repr(error)
                if expected_named:
                    assert type(error) is expected_named
                return error
            else:
                assert expected_exception is None, 'Bridge accepted adverse response'
                assert normalized(result) == expected_decoded(case, reply)
                assert len(requests) == 1
                return result
            finally:
                assert all(r.is_closed for r in responses)
    run_bridge(case['success'])
    record(case['case_id'], 'direct_rest_typed_success_closed', requests=1)
    for declared in case['errors']:
        error_module, error_name = declared['expected']['exception_class'].rsplit('.', 1)
        named = getattr(importlib.import_module(error_module), error_name)
        failure = run_bridge({'http_status': declared['status'], 'json': declared['envelope']}, expected_exception=PalantirRPCException, expected_named=named)
        assert normalized(failure.parameters) == normalized(declared['parameters'])
        record(case['case_id'], 'direct_rest_error_' + error_name, requests=1)
    run_bridge({'http_status': 403, 'json': {'errorName': 'IndependentDenied087', 'errorCode': 'PERMISSION_DENIED',
        'errorInstanceId': '00000000-0000-0000-0000-000000000087', 'parameters': {}}}, expected_exception=PalantirRPCException)
    record(case['case_id'], 'direct_rest_unknown_permission_error', requests=1)
    run_bridge(case['success'], {'max_bytes': 1}, RuntimeError)
    record(case['case_id'], 'direct_rest_byte_budget', requests=1)
    class Chunks(httpx.SyncByteStream):
        def __iter__(self):
            yield b'{' 
            yield b'"name":'
            yield b'"not-consumed"}'
    with httpx.Client(transport=httpx.MockTransport(lambda request: httpx.Response(200, stream=Chunks()))) as http:
        try:
            function(http, **dict(options, max_chunks=1))
        except RuntimeError as error:
            assert 'budget' in str(error)
        else:
            raise AssertionError('Bridge chunk budget not enforced')
    record(case['case_id'], 'direct_rest_chunk_budget')
    with httpx.Client(transport=httpx.MockTransport(lambda request: httpx.Response(200, content=b'{invalid'))) as http:
        try:
            function(http, **options)
        except pydantic.ValidationError:
            pass
        else:
            raise AssertionError('Bridge accepted malformed JSON')
    record(case['case_id'], 'direct_rest_malformed_json')
    for invalid in (True, '2'):
        with httpx.Client(transport=httpx.MockTransport(forbidden)) as http:
            try:
                function(http, **dict(options, version=invalid))
            except TypeError:
                pass
            else:
                raise AssertionError('Bridge accepted wrong version type')
        assert calls == []
        record(case['case_id'], 'direct_rest_invalid_version_' + type(invalid).__name__, requests=0)


def journey_j14(manifest):
    by_id = {case['operation']: case for case in manifest['operations']}
    plan = manifest['journeys'][0]
    state = {'session': False, 'continued': False, 'renamed': False, 'deleted': False}
    seen = []
    continuation = by_id['v2.aip_agents.Session.blocking_continue']
    for operation in plan['sequence']:
        case = copy.deepcopy(by_id[operation])
        name, method = operation.split('.')[-2:]
        if name == 'Content':
            case['success']['json'] = {'exchanges': [{'userInput': copy.deepcopy(continuation['request']['kwargs']['user_input']),
                'result': copy.deepcopy(continuation['success']['json'])}]}
        if name == 'Session' and method == 'get':
            case['success']['json']['metadata']['title'] = by_id['v2.aip_agents.Session.update_title']['request']['kwargs']['title']
        module = importlib.import_module(case['source']['module'])
        cls = getattr(module, name + 'Client')
        def handler(request):
            assert len(seen) < len(plan['sequence']), 'Journey exceeded its request budget'
            wire_check(request, case['request']['expected_wire'])
            if name == 'Session' and method == 'create':
                assert not state['session'] and not state['deleted']
                state['session'] = True
            elif name == 'Session' and method == 'blocking_continue':
                assert state['session'] and not state['continued']
                state['continued'] = True
            elif name in ('Content', 'SessionTrace'):
                assert state['continued']
            elif name == 'Session' and method == 'update_title':
                assert state['session']
                state['renamed'] = True
            elif name == 'Session' and method == 'get':
                assert state['renamed']
            elif name == 'Session' and method == 'delete':
                assert state['session'] and not state['deleted']
                state['deleted'] = True
            seen.append(operation)
            return response(case['success'])
        with resource(cls, handler) as (client, _):
            result = invoke(client, method, case['request']['kwargs'])
            assert normalized(result) == expected_decoded(case, case['success'])
            semantic_check(case, case['request']['kwargs'], normalized(result), 'J14')
        record('J14', operation, state=copy.deepcopy(state))
    assert seen == plan['sequence'] and state['deleted']
    agent_case = by_id['v2.aip_agents.Agent.get']
    module = importlib.import_module(agent_case['source']['module'])
    failure(agent_case, getattr(module, 'AgentClient'), 'get', 403, 'IndependentDenied087',
        'PERMISSION_DENIED', {})
    record('J14', 'permission_denial_stops_before_mutation', requests=1, session_mutations=0)


def execute(manifest):
    journey_j14(manifest)
    for case in manifest['operations']:
        module = importlib.import_module(case['source']['module'])
        name, method = case['operation'].split('.')[-2:]
        cls = getattr(module, name + 'Client')
        if case.get('native_sdk_limitation'):
            bridge_case(case, module, cls, method)
            continue
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
            failure(case, cls, method, status, 'IndependentPermissionDenied', 'PERMISSION_DENIED', {})
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
    assert len(manifest['operations']) == 47
    for case in manifest['operations']:
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--execute', action='store_true')
    parser.add_argument('--executor-identity')
    parser.add_argument('--testcase-closed')
    parser.add_argument('--approved-cases-sha256')
    parser.add_argument('--readiness-confirmed', action='store_true')
    args = parser.parse_args()
    manifest = json.loads(CASES.read_text(encoding='utf-8'))
    preflight(manifest)
    evidence = dict(story='DEV-STORY-087', testcase='TESTCASE-068', executor_identity=args.executor_identity,
                    harness_sha256=digest(__file__), cases_sha256=digest(CASES),
                    operations=len(manifest['operations']), declared_errors=sum(len(c['errors']) for c in manifest['operations']),
                    execution='NOT_RUN', created_at=datetime.now(timezone.utc).isoformat())
    if not args.execute:
        PENDING.write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
        print(json.dumps(evidence))
        return
    assert args.executor_identity and args.executor_identity != manifest['author_identity'], 'Actual independent executor identity required'
    assert args.executor_identity != manifest.get('reviewer_identity'), 'Executor must differ from case reviewer'
    assert args.testcase_closed == 'TESTCASE-068', 'Parent confirmation of actual Closed state required'
    assert args.approved_cases_sha256 == digest(CASES), 'Independent case approval for this exact manifest required'
    assert args.readiness_confirmed, 'Parent readiness confirmation required'
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
            record('REST087', 'socket_traps_active')
            execute(manifest)
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
