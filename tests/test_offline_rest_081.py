"""Source-bound SDK101 modes, finite transport lifetimes and Ontology object semantics."""

import ast
import asyncio
import copy
import datetime
import hashlib
import importlib
import importlib.metadata
import inspect
import json
import runpy
import socket
import textwrap
import urllib.parse
from functools import lru_cache
from pathlib import Path

import httpx
import pytest
from foundry_sdk import PalantirRPCException, PermissionDeniedError, ReadTimeout
from pydantic import TypeAdapter, ValidationError


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.agents/skills/pal-found-dev/examples/rest/081'
ORACLE = json.loads((ROOT / 'tests/fixtures/offline/rest-acceptance/source-oracle.json').read_text())
RESOURCES = {'LinkedObject', 'OntologyObject', 'OntologyObjectSet',
             'OntologyScenario', 'OntologyTransaction'}
OPERATIONS = {key: row for key, row in ORACLE['operations'].items()
              if key.startswith('v2.ontologies.') and key.split('.')[2] in RESOURCES}


def load(resource, method):
    return runpy.run_path(str(BASE / f'v2/ontologies/{resource}/invoke_{method}.py'))['verify'].__globals__


@pytest.fixture(scope='module')
def offline_event_loop():
    # Windows creates its local event-loop socket pair before connection denial.
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True)
def deny_network(monkeypatch, offline_event_loop):
    def denied(*args, **kwargs):
        raise AssertionError('Public socket/DNS access denied in REST-081 tests')

    for name in ('connect', 'connect_ex'):
        monkeypatch.setattr(socket.socket, name, denied)
    for name in ('create_connection', 'getaddrinfo', 'gethostbyname', 'gethostbyname_ex'):
        monkeypatch.setattr(socket, name, denied)
    monkeypatch.setattr(httpx.HTTPTransport, 'handle_request', denied)
    monkeypatch.setattr(httpx.AsyncHTTPTransport, 'handle_async_request', denied)


CASES = [tuple(identity.split('.')[2:]) for identity in sorted(OPERATIONS)]


def inputs(resource, method):
    """Use example inputs, with expected contracts derived separately from SDK source."""
    class Capture:
        @property
        def with_raw_response(self):
            return self

        def __getattr__(self, name):
            return lambda **kwargs: kwargs

    arguments = copy.deepcopy(load(resource, method)['invoke'](Capture()))
    arguments['ontology'] = 'tenant /α?%'
    module = importlib.import_module(OPERATIONS[f'v2.ontologies.{resource}.{method}']['module'])
    parameters = inspect.signature(getattr(getattr(module, resource + 'Client'), method)).parameters
    optional = {'branch': 'review/branch', 'sdk_version': '1.2.3',
                'trace_parent': '00-0123456789abcdef0123456789abcdef-0123456789abcdef-01',
                'trace_state': 'offline=case'}
    arguments.update({key: value for key, value in optional.items() if key in parameters})
    return arguments


def success_payload(resource, method):
    namespace = load(resource, method)
    payload = copy.deepcopy(namespace['SUCCESS'])
    # Individual mode checks use one terminal page; paging is exercised separately.
    if isinstance(payload, dict):
        payload.pop('nextPageToken', None)
    return payload


def function_tree(function):
    return ast.parse(textwrap.dedent(inspect.getsource(function))).body[0]


@lru_cache
def source_contract(resource, method):
    identity = f'v2.ontologies.{resource}.{method}'
    frozen = OPERATIONS[identity]
    module = importlib.import_module(frozen['module'])
    assert hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest() == frozen['source_sha256']
    client = getattr(module, resource + 'Client')
    function = getattr(client, method)
    tree = function_tree(function)
    requests = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute) and node.func.attr == 'RequestInfo']
    assert len(requests) == 1
    fields = {item.arg: item.value for item in requests[0].keywords}
    arguments = inspect.signature(function).bind(None, **inputs(resource, method))
    arguments.apply_defaults()
    context = dict(arguments.arguments)

    def evaluate(node):
        return eval(compile(ast.Expression(node), '<hash-bound SDK source>', 'eval'),
                    vars(module), context)

    return {
        'client': client,
        'async_client': getattr(module, 'Async' + resource + 'Client'),
        'module': module,
        'fields': fields,
        'context': context,
        'method': evaluate(fields['method']),
        'path': evaluate(fields['resource_path']).format(**evaluate(fields['path_params'])),
        'headers': evaluate(fields['header_params']),
        'path_params': evaluate(fields['path_params']),
        'route': evaluate(fields['resource_path']),
        'query': evaluate(fields['query_params']),
        'body': evaluate(fields['body']),
        'response': evaluate(fields['response_type']),
        'errors': evaluate(fields['throwable_errors']),
        'iterator': evaluate(fields['response_mode']) == 'ITERATOR',
    }


def available_modes(resource, method):
    wrappers = OPERATIONS[f'v2.ontologies.{resource}.{method}']['wrappers']
    return [(resource, method, mode, asynchronous)
            for asynchronous in (False, True)
            for mode in ('ordinary', 'raw', 'stream')
            if mode == 'ordinary' or ('async_' if asynchronous else '') + mode in wrappers]


AVAILABLE_MODES = [case for resource, method in CASES for case in available_modes(resource, method)]


def normalized(value):
    if hasattr(value, 'model_dump'):
        return value.model_dump(mode='json', by_alias=True, exclude_none=True)
    if isinstance(value, dict):
        return {key: normalized(child) for key, child in value.items()}
    if isinstance(value, (list, tuple)):
        return [normalized(child) for child in value]
    if isinstance(value, (datetime.datetime, datetime.date)):
        return value.isoformat()
    return value


def check_source_wire(source, request, *, paged=False):
    assert request.method == source['method']
    expected_path = '/api' + source['route'].format(**{
        key: urllib.parse.quote(str(value), safe='') for key, value in source['path_params'].items()})
    assert request.url.raw_path.split(b'?')[0] == expected_path.encode('ascii')
    assert request.headers['Authorization'] == 'Bearer offline-fixture-token'
    assert request.extensions['timeout']['read'] == 30
    for name, value in source['headers'].items():
        if value is None:
            assert name not in request.headers
        else:
            assert request.headers[name] == value
    query = {name: value for name, value in source['query'].items() if value is not None}
    actual = list(request.url.params.multi_items())
    if paged:
        query.pop('pageToken', None)
        actual = [(name, value) for name, value in actual if name != 'pageToken']
    assert sorted(actual) == sorted(httpx.QueryParams(query).multi_items())
    expected = normalized(source['body'])
    actual_body = json.loads(request.content) if request.content else None
    if paged and isinstance(actual_body, dict):
        actual_body.pop('pageToken', None)
        expected = copy.deepcopy(expected)
        expected.pop('pageToken', None)
    assert actual_body == expected


async def consume_async(client, method, arguments, mode, iterator):
    if mode == 'stream':
        async with getattr(client.with_streaming_response, method)(**arguments) as response:
            return b''.join([chunk async for chunk in response.aiter_bytes()])
    target = client.with_raw_response if mode == 'raw' else client
    pending = getattr(target, method)(**arguments)
    if mode == 'ordinary' and iterator:
        core = importlib.import_module('foundry_sdk._core')
        assert type(pending) is core.AsyncResourceIterator
        assert hasattr(pending, '__aiter__') and not inspect.isawaitable(pending)
        return [row async for row in pending]
    assert inspect.isawaitable(pending)
    result = await pending
    if mode == 'raw':
        try:
            assert not inspect.iscoroutinefunction(result.decode)
            return result.decode()
        finally:
            await result.aclose()
    return result


def consume_sync(client, method, arguments, mode, iterator):
    if mode == 'stream':
        with getattr(client.with_streaming_response, method)(**arguments) as response:
            return b''.join(response.iter_bytes())
    target = client.with_raw_response if mode == 'raw' else client
    result = getattr(target, method)(**arguments)
    if mode == 'ordinary' and iterator:
        core = importlib.import_module('foundry_sdk._core')
        assert type(result) is core.ResourceIterator
        assert hasattr(result, '__next__')
        return list(result)
    if mode == 'raw':
        try:
            return result.decode()
        finally:
            result.close()
    return result


def exercise(resource, method, mode, asynchronous, handler, loop, arguments=None):
    namespace = load(resource, method)
    source = source_contract(resource, method)
    arguments = inputs(resource, method) if arguments is None else arguments
    if asynchronous:
        async def run():
            adapter = importlib.import_module('mock_transport').mock_async_resource
            async with adapter(source['async_client'], handler) as client:
                return await consume_async(client, method, arguments, mode, source['iterator'])
        return loop.run_until_complete(run())
    with namespace['mock_resource'](source['client'], handler) as client:
        return consume_sync(client, method, arguments, mode, source['iterator'])


@pytest.mark.parametrize('resource,method', CASES)
def test_exact_source_signatures_and_all_exposed_response_modes(resource, method):
    assert importlib.metadata.version('foundry-platform-sdk') == '1.101.0'
    source = source_contract(resource, method)
    row = OPERATIONS[f'v2.ontologies.{resource}.{method}']
    for asynchronous, key in ((False, 'ordinary'), (True, 'async')):
        client = source['async_client'] if asynchronous else source['client']
        tree = function_tree(getattr(client, method))
        expected = ast.parse(f"def signature({row[key]['signature']}): pass").body[0]
        assert ast.dump(tree.args) == ast.dump(expected.args)
        assert ast.unparse(tree.returns) == row[key]['return']
        assert isinstance(tree, ast.AsyncFunctionDef) == row[key]['coroutine_definition']
        prefix = 'async_' if asynchronous else ''
        for mode in ('raw', 'stream'):
            metadata = row['wrappers'][prefix + mode]
            wrapper = getattr(source['module'], metadata['class'])
            initializer = function_tree(wrapper.__init__)
            payload = next(node for node in initializer.body
                           if isinstance(node, ast.FunctionDef) and node.name == method)
            assert ast.unparse(payload.args.args[0].annotation) == metadata['payload']
            assignment = next(node for node in initializer.body
                              if isinstance(node, ast.Assign)
                              and isinstance(node.targets[0], ast.Attribute)
                              and node.targets[0].attr == method)
            assert assignment.value.func.attr == metadata['helper']
            assert ast.unparse(assignment.value.args[1]) == 'client.' + method
    # Empty source unions are meaningful: no declared typed error may be invented.
    assert source['errors'] == {}
    assert set(row['wrappers']) == {'raw', 'stream', 'async_raw', 'async_stream'}


@pytest.mark.parametrize('resource,method,mode,asynchronous', AVAILABLE_MODES)
def test_all_modes_serialize_source_contract_and_decode_typed_result(
        resource, method, mode, asynchronous, offline_event_loop):
    source = source_contract(resource, method)
    payload = success_payload(resource, method)
    expected = TypeAdapter(source['response']).validate_python(payload)
    responses = []

    def handler(request):
        check_source_wire(source, request)
        response = httpx.Response(200, json=payload)
        responses.append(response)
        return response

    result = exercise(resource, method, mode, asynchronous, handler, offline_event_loop)
    if mode == 'stream':
        assert json.loads(result) == normalized(expected)
    elif mode == 'ordinary' and source['iterator']:
        assert [type(item) for item in result] == [type(item) for item in expected.data]
        assert normalized(result) == normalized(expected.data)
    else:
        assert type(result) is type(expected)
        assert normalized(result) == normalized(expected)
    assert len(responses) == 1 and responses[0].is_closed


@pytest.mark.parametrize('resource,method,mode,asynchronous', AVAILABLE_MODES)
def test_generic_denial_preserves_envelope_and_stops_after_one_request(
        resource, method, mode, asynchronous, offline_event_loop):
    source = source_contract(resource, method)
    assert source['errors'] == {}
    responses = []
    envelope = {'errorName': 'PermissionDenied', 'errorCode': 'PERMISSION_DENIED',
                'parameters': {'syntheticReason': 'schema access denied'},
                'errorInstanceId': '00000000-0000-0000-0000-000000000004'}

    def denied(request):
        check_source_wire(source, request)
        response = httpx.Response(403, json=envelope)
        responses.append(response)
        return response

    with pytest.raises(PalantirRPCException) as raised:
        exercise(resource, method, mode, asynchronous, denied, offline_event_loop)
    assert type(raised.value) is PermissionDeniedError
    assert raised.value.name == envelope['errorName']
    assert raised.value.parameters == envelope['parameters']
    assert raised.value.error_instance_id == envelope['errorInstanceId']
    assert len(responses) == 1 and responses[0].is_closed


@pytest.mark.parametrize('resource,method,mode,asynchronous', AVAILABLE_MODES)
def test_timeout_keeps_native_cause_without_replay(
        resource, method, mode, asynchronous, offline_event_loop):
    calls = []

    def stalled(request):
        check_source_wire(source_contract(resource, method), request)
        calls.append(request)
        raise httpx.ReadTimeout('Synthetic schema deadline', request=request)

    with pytest.raises(ReadTimeout, match='Synthetic schema deadline') as raised:
        exercise(resource, method, mode, asynchronous, stalled, offline_event_loop)
    assert isinstance(raised.value.__cause__, httpx.ReadTimeout)
    assert len(calls) == 1


@pytest.mark.parametrize('resource,method,mode,asynchronous', AVAILABLE_MODES)
@pytest.mark.parametrize('fault', ('unexpected_argument', 'invalid_timeout'))
def test_invalid_signature_or_timeout_rejected_before_http(
        resource, method, mode, asynchronous, fault, offline_event_loop):
    calls = []
    arguments = inputs(resource, method)
    arguments['unknown_schema_argument' if fault == 'unexpected_argument' else 'request_timeout'] = object()

    def forbidden(request):
        calls.append(request)
        raise AssertionError('Invalid arguments reached HTTP')

    with pytest.raises(ValidationError):
        exercise(resource, method, mode, asynchronous, forbidden, offline_event_loop, arguments)
    assert calls == []


PAGED_CASES = [(resource, method) for resource, method in CASES
               if 'page_token' in inspect.signature(
                   getattr(source_contract(resource, method)['client'], method)).parameters]


@pytest.mark.parametrize('resource,method,mode,asynchronous', [
    case for resource, method in PAGED_CASES for case in available_modes(resource, method)])
def test_paging_crosses_empty_intermediate_page_and_stops_at_finite_end(
        resource, method, mode, asynchronous, offline_event_loop):
    source = source_contract(resource, method)
    arguments = inputs(resource, method)
    payload = success_payload(resource, method)
    rows = normalized(TypeAdapter(source['response']).validate_python(payload))['data']
    tokens = [None] + [f'page/{index} ?α' for index in range(1, 11)]
    calls, responses = [], []

    def page(request):
        check_source_wire(source, request, paged=True)
        body = json.loads(request.content) if request.content else {}
        token = request.url.params.get('pageToken', body.get('pageToken'))
        calls.append(token)
        index = len(calls) - 1
        assert index < len(tokens), 'Caller page budget exceeded'
        assert token == tokens[index]
        value = copy.deepcopy(payload)
        value.pop('nextPageToken', None)
        value['data'] = [] if index == 5 else copy.deepcopy(rows)
        if index < len(tokens) - 1:
            value['nextPageToken'] = tokens[index + 1]
        response = httpx.Response(200, json=value)
        responses.append(response)
        return response

    if mode == 'ordinary' and source['iterator']:
        actual = normalized(exercise(resource, method, mode, asynchronous, page, offline_event_loop))
    else:
        actual = []
        for _ in tokens:
            result = exercise(resource, method, mode, asynchronous, page, offline_event_loop, arguments)
            value = json.loads(result) if mode == 'stream' else normalized(result)
            actual.extend(value['data'])
            token = value.get('nextPageToken')
            if token is None:
                break
            arguments['page_token'] = token
        else:
            pytest.fail('Pagination did not terminate within eleven pages')
    assert actual == rows * 10
    assert calls == tokens
    assert len(responses) == 11 and all(response.is_closed for response in responses)


class TrackedSyncStream(httpx.SyncByteStream):
    def __init__(self):
        self.chunks_read = 0
        self.closed = False

    def __iter__(self):
        for chunk in (b'part', b'two!', b'unread'):
            self.chunks_read += 1
            yield chunk

    def close(self):
        self.closed = True


class TrackedAsyncStream(httpx.AsyncByteStream):
    def __init__(self):
        self.chunks_read = 0
        self.closed = False

    async def __aiter__(self):
        for chunk in (b'part', b'two!', b'unread'):
            self.chunks_read += 1
            yield chunk

    async def aclose(self):
        self.closed = True


@pytest.mark.parametrize('resource,method', CASES)
@pytest.mark.parametrize('asynchronous', (False, True))
def test_stream_byte_budget_interrupt_closes_unread_response(
        resource, method, asynchronous, offline_event_loop):
    namespace = load(resource, method)
    source = source_contract(resource, method)
    body = TrackedAsyncStream() if asynchronous else TrackedSyncStream()
    responses = []

    def handler(request):
        check_source_wire(source, request)
        response = httpx.Response(200, stream=body)
        assert not response.is_closed and not body.closed
        responses.append(response)
        return response

    if asynchronous:
        async def run():
            adapter = importlib.import_module('mock_transport').mock_async_resource
            async with adapter(source['async_client'], handler) as client:
                with pytest.raises(RuntimeError, match='Caller byte budget exhausted'):
                    async with getattr(client.with_streaming_response, method)(
                            **inputs(resource, method)) as response:
                        size = 0
                        async for chunk in response.aiter_bytes(chunk_size=4):
                            size += len(chunk)
                            if size > 4:
                                raise RuntimeError('Caller byte budget exhausted')
        offline_event_loop.run_until_complete(run())
    else:
        with namespace['mock_resource'](source['client'], handler) as client:
            with pytest.raises(RuntimeError, match='Caller byte budget exhausted'):
                with getattr(client.with_streaming_response, method)(
                        **inputs(resource, method)) as response:
                    size = 0
                    for chunk in response.iter_bytes(chunk_size=4):
                        size += len(chunk)
                        if size > 4:
                            raise RuntimeError('Caller byte budget exhausted')
    assert len(responses) == 1 and responses[0].is_closed
    assert body.closed and body.chunks_read == 2


@pytest.mark.parametrize('resource,method', CASES)
def test_async_task_cancellation_closes_stream_with_unread_bytes(
        resource, method, offline_event_loop):
    load(resource, method)
    source = source_contract(resource, method)
    body = TrackedAsyncStream()
    responses = []

    def handler(request):
        check_source_wire(source, request)
        response = httpx.Response(200, stream=body)
        responses.append(response)
        return response

    async def run():
        adapter = importlib.import_module('mock_transport').mock_async_resource
        started, hold = asyncio.Event(), asyncio.Event()

        async def reader(client):
            async with getattr(client.with_streaming_response, method)(
                    **inputs(resource, method)) as response:
                async for chunk in response.aiter_bytes(chunk_size=4):
                    assert chunk == b'part'
                    started.set()
                    await hold.wait()

        async with adapter(source['async_client'], handler) as client:
            task = asyncio.create_task(reader(client))
            try:
                await asyncio.wait_for(started.wait(), timeout=1)
                assert_unfinished_stream(body, responses[0], 1)
                task.cancel()
                with pytest.raises(asyncio.CancelledError):
                    await task
            finally:
                if not task.done():
                    task.cancel()
                    await asyncio.gather(task, return_exceptions=True)

    offline_event_loop.run_until_complete(run())
    assert len(responses) == 1 and responses[0].is_closed
    assert body.closed and body.chunks_read == 1


def test_dns_socket_and_native_http_denial_is_active(offline_event_loop):
    with pytest.raises(AssertionError, match='Public socket/DNS access denied'):
        socket.getaddrinfo('public.example.invalid', 443)
    with pytest.raises(AssertionError, match='Public socket/DNS access denied'):
        socket.create_connection(('public.example.invalid', 443))
    with socket.socket() as connection:
        with pytest.raises(AssertionError, match='Public socket/DNS access denied'):
            connection.connect(('192.0.2.1', 443))
    with httpx.Client() as client:
        with pytest.raises(AssertionError, match='Public socket/DNS access denied'):
            client.get('https://public.example.invalid', timeout=1)

    async def run():
        async with httpx.AsyncClient() as client:
            with pytest.raises(AssertionError, match='Public socket/DNS access denied'):
                await client.get('https://public.example.invalid', timeout=1)

    offline_event_loop.run_until_complete(run())


@pytest.mark.parametrize('resource,method', [('OntologyObject', 'get'), ('OntologyObjectSet', 'aggregate')])
@pytest.mark.parametrize('fault', ('method', 'path', 'query', 'body', 'header', 'timeout'))
def test_source_wire_assertions_reject_independent_request_mutations(
        resource, method, fault, offline_event_loop):
    source = source_contract(resource, method)
    captured = []

    def handler(request):
        captured.append(request)
        return httpx.Response(200, json=success_payload(resource, method))

    exercise(resource, method, 'ordinary', False, handler, offline_event_loop)
    original = captured[0]
    headers = dict(original.headers)
    extensions = copy.deepcopy(original.extensions)
    url, content = original.url, original.content
    if fault == 'path':
        url = url.copy_with(raw_path=url.raw_path.split(b'?')[0] + b'/incorrect?' + url.query)
    elif fault == 'query':
        url = url.copy_add_param('unexpectedQuery', 'wrong')
    elif fault == 'body':
        content = b'{"unexpectedBody":true}'
    elif fault == 'header':
        headers['authorization'] = 'Bearer wrong-identity'
    elif fault == 'timeout':
        extensions['timeout']['read'] = 300
    damaged = httpx.Request('DELETE' if fault == 'method' else original.method,
                            url, headers=headers, content=content, extensions=extensions)
    with pytest.raises(AssertionError):
        check_source_wire(source, damaged)



def test_exact_owned_source_inventory_and_available_modes():
    assert ORACLE['sdk_release'] == '1.101.0'
    assert len(OPERATIONS) == 22
    assert hashlib.sha256('\n'.join(sorted(OPERATIONS)).encode()).hexdigest() == (
        'ff2ddcac52a14d423998aa91fbcd9cd3fb78ce56b1a4c3f736a906c84f245a7e')
    assert len(AVAILABLE_MODES) == 132
    sources = [source_contract(*case) for case in CASES]
    assert sum(source['iterator'] for source in sources) == 5
    assert sum(source['response'] is None for source in sources) == 0
    assert all(source['errors'] == {} for source in sources)
    for resource, method in CASES:
        row = OPERATIONS[f'v2.ontologies.{resource}.{method}']
        source = source_contract(resource, method)
        for asynchronous in (False, True):
            client = source['async_client'] if asynchronous else source['client']
            prefix = 'async_' if asynchronous else ''
            for mode in ('raw', 'stream'):
                metadata = row['wrappers'].get(prefix + mode)
                assert metadata is not None
                initializer = function_tree(getattr(source['module'], metadata['class']).__init__)
                assigned = {node.targets[0].attr for node in initializer.body
                            if isinstance(node, ast.Assign)
                            and isinstance(node.targets[0], ast.Attribute)}
                assert method in assigned
            annotation = ast.unparse(function_tree(getattr(client, method)).returns)
            if asynchronous:
                assert ('AsyncResourceIterator' in annotation) == source['iterator']
                assert ('Awaitable' in annotation) != source['iterator']


BETA_CASES = [case for case in CASES
              if 'Beta' in OPERATIONS[f'v2.ontologies.{case[0]}.{case[1]}']['documentation']['stage']]


def assert_preview(example):
    class Capture:
        @property
        def with_raw_response(self):
            return self

        def __getattr__(self, name):
            return lambda **kwargs: kwargs

    assert example['invoke'](Capture())['preview'] is True
    assert example['EXPECTED_QUERY']['preview'] is True


@pytest.mark.parametrize('resource,method', BETA_CASES)
def test_beta_reader_examples_preserve_explicit_preview(resource, method):
    assert len(BETA_CASES) == 14
    assert_preview(load(resource, method))


@pytest.mark.parametrize('fault', ('invocation', 'expected_query'))
def test_preview_guard_rejects_missing_or_false_preview(fault):
    example = load('OntologyObjectSet', 'create_temporary')
    if fault == 'invocation':
        example['invoke'] = lambda client: client.with_raw_response.create_temporary(preview=False)
    else:
        example['EXPECTED_QUERY'] = {'preview': None}
    with pytest.raises(AssertionError):
        assert_preview(example)


@pytest.mark.parametrize('resource,method', CASES)
def test_reader_examples_execute_with_preserved_result_and_error_checks(resource, method):
    load(resource, method)['verify']()


def assert_locator(value):
    assert set(value) == {'__primaryKey', '__apiName'}
    assert isinstance(value['__primaryKey'], (str, int)) and value['__primaryKey'] != ''
    assert isinstance(value['__apiName'], str) and value['__apiName']


def assert_scenario_semantics(method, payload):
    if method == 'list_scenario_edited_objects':
        assert payload['data']
        for locator in payload['data']:
            assert_locator(locator)
            assert locator['__apiName'] == 'Order'
    elif method == 'list_scenario_edited_links':
        assert payload['data']
        for group in payload['data']:
            assert_locator(group['sourceObject'])
            assert group['sourceObject']['__apiName'] == 'Order'
            assert group['linkedObjects']
            for link in group['linkedObjects']:
                assert_locator(link['targetObject'])
                assert link['targetObject']['__apiName'] == 'Worker'
                assert link['linkType'] == 'assignedWorker'
    else:
        assert payload['data'] == [{'objectTypeApiName': 'Order', 'primaryKeyValue': 'ORD-101'}]


@pytest.mark.parametrize('method', ('list_scenario_edited_objects', 'list_scenario_edited_links',
                                    'list_scenario_conflicting_objects'))
def test_scenario_results_preserve_source_locator_distinctions(method):
    models = importlib.import_module('foundry_sdk.v2.ontologies.models')
    for name in ('ListScenarioEditedObjectsResponse', 'LinksFromObject', 'LinkedObjectLocator'):
        assert '__primaryKey' in inspect.getdoc(getattr(models, name))
        assert '__apiName' in inspect.getdoc(getattr(models, name))
    assert_scenario_semantics(method, success_payload('OntologyScenario', method))


@pytest.mark.parametrize('fault', ('full_object', 'wrong_type', 'empty_identity', 'wrong_link'))
def test_scenario_locator_guard_rejects_result_regressions(fault):
    method = 'list_scenario_edited_links'
    payload = success_payload('OntologyScenario', method)
    link = payload['data'][0]['linkedObjects'][0]
    target = link['targetObject']
    if fault == 'full_object':
        target['status'] = 'ACTIVE'
    elif fault == 'wrong_type':
        target['__apiName'] = 'Order'
    elif fault == 'empty_identity':
        target['__primaryKey'] = ''
    else:
        link['linkType'] = 'otherLink'
    with pytest.raises(AssertionError):
        assert_scenario_semantics(method, payload)


@pytest.mark.parametrize('method', ('get', 'create_temporary', 'load', 'load_links',
                                    'load_multiple_object_types', 'load_objects_or_interfaces'))
def test_object_set_results_use_source_selected_model_and_identity(method):
    source = source_contract('OntologyObjectSet', method)
    payload = success_payload('OntologyObjectSet', method)
    result = TypeAdapter(source['response']).validate_python(payload)
    assert normalized(result) == payload
    if method == 'get':
        assert type(result).__name__ == 'ObjectSetBaseType'
        assert result.type == 'base' and result.object_type == 'Asset'
    elif method == 'create_temporary':
        assert result.object_set_rid.startswith('ri.')
    elif method == 'load_links':
        assert type(result.data[0]).__name__ == 'LinksFromObject'
        assert_locator(normalized(result.data[0].source_object))
        assert_locator(normalized(result.data[0].linked_objects[0].target_object))
        assert result.data[0].linked_objects[0].link_type == 'installedAt'
    elif method in ('load_multiple_object_types', 'load_objects_or_interfaces'):
        assert all('$apiName' in row and '$primaryKey' in row for row in result.data)
        assert all('__apiName' not in row and '__primaryKey' not in row for row in result.data)
    else:
        assert result.data[0]['__apiName'] == 'Employee'
        assert result.data[0]['__primaryKey'] == 50030


@pytest.mark.parametrize('fault', ('unknown_union', 'missing_required_field'))
def test_object_set_discriminator_rejected_before_transport(fault, offline_event_loop):
    arguments = inputs('OntologyObjectSet', 'create_temporary')
    arguments['object_set'] = {'type': 'unrecognized'} if fault == 'unknown_union' else {'type': 'base'}
    calls = []

    def forbidden(request):
        calls.append(request)
        raise AssertionError('Invalid object-set union reached transport')

    with pytest.raises(ValidationError):
        exercise('OntologyObjectSet', 'create_temporary', 'ordinary', False,
                 forbidden, offline_event_loop, arguments)
    assert calls == []


def assert_unfinished_stream(body, response, expected_chunks):
    assert not response.is_closed and not body.closed
    assert body.chunks_read == expected_chunks < 3


@pytest.mark.parametrize('asynchronous', (False, True))
def test_prebuffered_response_cannot_prove_unfinished_stream_lifetime(asynchronous, offline_event_loop):
    body = TrackedAsyncStream() if asynchronous else TrackedSyncStream()
    response = httpx.Response(200, stream=body)
    if asynchronous:
        offline_event_loop.run_until_complete(response.aread())
    else:
        response.read()
    assert body.closed and body.chunks_read == 3
    with pytest.raises(AssertionError):
        assert_unfinished_stream(body, response, 1)



@pytest.mark.parametrize('resource,method', [case for case in CASES
                                           if source_contract(*case)['iterator']])
@pytest.mark.parametrize('asynchronous', (False, True))
def test_caller_item_budget_stops_repeated_token_pager(resource, method, asynchronous, offline_event_loop):
    source = source_contract(resource, method)
    payload = success_payload(resource, method)
    payload['data'] = payload['data'][:1]
    payload['nextPageToken'] = 'server-repeats-this-token'
    responses = []

    def page(request):
        check_source_wire(source, request, paged=True)
        assert len(responses) < 3, 'Caller exceeded three-item budget'
        response = httpx.Response(200, json=payload)
        responses.append(response)
        return response

    if asynchronous:
        async def bounded():
            adapter = importlib.import_module('mock_transport').mock_async_resource
            async with adapter(source['async_client'], page) as client:
                rows = []
                async for row in getattr(client, method)(**inputs(resource, method)):
                    rows.append(row)
                    if len(rows) == 3:
                        break
                return rows
        result = offline_event_loop.run_until_complete(bounded())
    else:
        with load(resource, method)['mock_resource'](source['client'], page) as client:
            result = []
            for row in getattr(client, method)(**inputs(resource, method)):
                result.append(row)
                if len(result) == 3:
                    break
    assert normalized(result) == payload['data'] * 3
    assert len(responses) == 3 and all(response.is_closed for response in responses)


@pytest.mark.parametrize('resource,method,mode,asynchronous', AVAILABLE_MODES)
def test_undeclared_named_error_uses_generic_status_class(resource, method, mode, asynchronous, offline_event_loop):
    from foundry_sdk import BadRequestError

    source = source_contract(resource, method)
    assert source['errors'] == {}
    envelope = {'errorName': 'SyntheticUndeclaredObjectFailure', 'errorCode': 'INVALID_ARGUMENT',
                'parameters': {'objectType': 'Order', 'primaryKey': 'ORD-101'},
                'errorInstanceId': '00000000-0000-0000-0000-000000000005'}
    responses = []

    def rejected(request):
        check_source_wire(source, request)
        response = httpx.Response(400, json=envelope)
        responses.append(response)
        return response

    with pytest.raises(PalantirRPCException) as raised:
        exercise(resource, method, mode, asynchronous, rejected, offline_event_loop)
    assert type(raised.value) is BadRequestError
    assert raised.value.name == envelope['errorName']
    assert raised.value.parameters == envelope['parameters']
    assert raised.value.error_instance_id == envelope['errorInstanceId']
    assert len(responses) == 1 and responses[0].is_closed
