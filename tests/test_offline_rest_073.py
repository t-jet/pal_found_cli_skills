"""Frozen SDK101 wire, response, error and lifetime checks for REST-073."""

import ast
import asyncio
import copy
import datetime
import hashlib
import importlib
import importlib.metadata
import inspect
import io
import json
import runpy
import socket
import textwrap
import zipfile
from contextlib import asynccontextmanager, contextmanager
from functools import lru_cache
from pathlib import Path
from unittest.mock import patch
from urllib.parse import quote

import httpx
import pytest
from foundry_sdk import Config, ReadTimeout, UserTokenAuth
from pydantic import TypeAdapter, ValidationError

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.agents/skills/pal-found-dev/examples/rest/073/v2'
ORACLE = json.loads((ROOT / 'tests/fixtures/offline/rest-acceptance/source-oracle.json').read_text())
SERVICES = {'audit', 'filesystem', 'third_party_applications'}
OPERATIONS = {key: value for key, value in ORACLE['operations'].items()
              if key.startswith('v2.') and key.split('.')[1] in SERVICES}
CASES = sorted(OPERATIONS)
FORMS = [(key, mode, asynchronous) for key, row in sorted(OPERATIONS.items())
         for mode in ('ordinary', 'raw', 'stream') for asynchronous in (False, True)
         if mode != 'stream' or ('async_stream' if asynchronous else 'stream') in row['wrappers']]
STREAMS = [key for key, row in sorted(OPERATIONS.items()) if 'stream' in row['wrappers']]


@pytest.fixture(scope='module')
def offline_event_loop():
    # Windows initializes the local event-loop socket pair before network denial.
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True)
def deny_network(monkeypatch, offline_event_loop):
    def denied(*args, **kwargs):
        raise AssertionError('Network forbidden in REST-073 tests')

    for name in ('connect', 'connect_ex'):
        monkeypatch.setattr(socket.socket, name, denied)
    for name in ('create_connection', 'getaddrinfo', 'gethostbyname', 'gethostbyname_ex'):
        monkeypatch.setattr(socket, name, denied)
    monkeypatch.setattr(httpx.HTTPTransport, 'handle_request', denied)
    monkeypatch.setattr(httpx.AsyncHTTPTransport, 'handle_async_request', denied)


def example(key):
    _, service, resource, method = key.split('.')
    path = BASE / service / resource / (method + '.py')
    if (resource, method) == ('Project', 'create'):
        path = path.with_name('invoke_create.py')
    return runpy.run_path(str(path))


def inputs(key):
    """Capture invocation arguments without accepting example wire expectations."""
    class Capture:
        @property
        def with_raw_response(self):
            return self

        def __getattr__(self, name):
            return lambda **kwargs: kwargs

    arguments = copy.deepcopy(example(key)['invoke'](Capture()))
    signature = inspect.signature(getattr(source_module(key), key.split('.')[-2] + 'Client').__dict__[key.split('.')[-1]])
    if 'page_size' in signature.parameters:
        arguments['page_size'] = 2
    if key == 'v2.filesystem.Project.create_from_template':
        arguments.update(variable_values={'department': 'Research'},
                         project_description='Synthetic research project')
    return arguments


@lru_cache
def source_module(key):
    row = OPERATIONS[key]
    module = importlib.import_module(row['module'])
    assert hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest() == row['source_sha256']
    return module


def function_tree(function):
    return ast.parse(textwrap.dedent(inspect.getsource(function))).body[0]


def normalized(value):
    if hasattr(value, 'model_dump'):
        return normalized(value.model_dump(mode='json', by_alias=True, exclude_none=True))
    if isinstance(value, dict):
        return {key: normalized(child) for key, child in value.items()}
    if isinstance(value, (tuple, list)):
        return [normalized(child) for child in value]
    if isinstance(value, (datetime.datetime, datetime.date)):
        return value.isoformat()
    return value


def source_contract(key, arguments=None):
    module = source_module(key)
    resource, method = key.split('.')[-2:]
    client = getattr(module, resource + 'Client')
    function = getattr(client, method)
    tree = function_tree(function)
    requests = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute) and node.func.attr == 'RequestInfo']
    assert len(requests) == 1
    fields = {item.arg: item.value for item in requests[0].keywords}
    bound = inspect.signature(function).bind(None, **(inputs(key) if arguments is None else arguments))
    bound.apply_defaults()

    def evaluate(node):
        return eval(compile(ast.Expression(node), '<frozen SDK source>', 'eval'), vars(module), bound.arguments)

    values = {name: evaluate(node) for name, node in fields.items()}
    path = values['resource_path']
    for name, value in values['path_params'].items():
        path = path.replace('{' + name + '}', quote(value, safe=''))
    return dict(values, client=client, async_client=getattr(module, 'Async' + resource + 'Client'),
                module=module, path='/api' + path, iterator=values['response_mode'] == 'ITERATOR')


def check_wire(source, request, *, page_token=None):
    assert request.method == source['method']
    assert request.url.raw_path.split(b'?')[0] == source['path'].encode('ascii')
    assert request.headers['Authorization'] == 'Bearer offline-fixture-token'
    assert request.extensions['timeout'] == {'connect': 30, 'read': 30, 'write': 30, 'pool': 30}
    for name, value in source['header_params'].items():
        if value is None:
            assert name not in request.headers
        else:
            assert request.headers[name] == value
    query = {name: value for name, value in source['query_params'].items() if value is not None}
    if page_token is not None:
        query['pageToken'] = page_token
    assert sorted(request.url.params.multi_items()) == sorted(httpx.QueryParams(query).multi_items())
    body = normalized(source['body'])
    if isinstance(body, bytes):
        assert request.content == body
    else:
        assert (json.loads(request.content) if request.content else None) == body


@contextmanager
def mock_resource(client_type, handler):
    with httpx.Client(transport=httpx.MockTransport(handler), timeout=30) as transport:
        with patch('foundry_sdk._core.api_client.HttpClient', return_value=transport):
            client = client_type(auth=UserTokenAuth(token='offline-fixture-token'),
                                 hostname='offline.example.invalid',
                                 config=Config(timeout=30, max_retries=1,
                                               propagate_qos='PROPAGATE_429_AND_503_TO_CALLER'))
        yield client


@asynccontextmanager
async def mock_async_resource(client_type, handler):
    async with httpx.AsyncClient(transport=httpx.MockTransport(handler), timeout=30) as transport:
        with patch('foundry_sdk._core.api_client.AsyncHttpClient', return_value=transport):
            client = client_type(auth=UserTokenAuth(token='offline-fixture-token'),
                                 hostname='offline.example.invalid',
                                 config=Config(timeout=30, max_retries=1,
                                               propagate_qos='PROPAGATE_429_AND_503_TO_CALLER'))
        yield client


def consume_sync(client, method, arguments, mode, iterator):
    if mode == 'stream':
        with getattr(client.with_streaming_response, method)(**arguments) as response:
            return b''.join(response.iter_bytes())
    target = client.with_raw_response if mode == 'raw' else client
    result = getattr(target, method)(**arguments)
    if mode == 'raw':
        try:
            return result.decode()
        finally:
            result.close()
    if iterator:
        assert hasattr(result, '__next__')
        return list(result)
    return result


async def consume_async(client, method, arguments, mode, iterator):
    if mode == 'stream':
        async with getattr(client.with_streaming_response, method)(**arguments) as response:
            return b''.join([chunk async for chunk in response.aiter_bytes()])
    target = client.with_raw_response if mode == 'raw' else client
    pending = getattr(target, method)(**arguments)
    if mode == 'ordinary' and iterator:
        assert hasattr(pending, '__aiter__') and not inspect.isawaitable(pending)
        return [item async for item in pending]
    assert inspect.isawaitable(pending)
    result = await pending
    if mode == 'raw':
        try:
            assert not inspect.iscoroutinefunction(result.decode)
            return result.decode()
        finally:
            await result.aclose()
    return result


def exercise(key, mode, asynchronous, handler, loop, arguments=None):
    source = source_contract(key)
    arguments = inputs(key) if arguments is None else arguments
    method = key.split('.')[-1]
    if asynchronous:
        async def run():
            async with mock_async_resource(source['async_client'], handler) as client:
                return await consume_async(client, method, arguments, mode, source['iterator'])
        return loop.run_until_complete(run())
    with mock_resource(source['client'], handler) as client:
        return consume_sync(client, method, arguments, mode, source['iterator'])


def response_for(payload):
    if payload is None:
        return httpx.Response(204)
    if isinstance(payload, bytes):
        return httpx.Response(200, content=payload)
    return httpx.Response(200, json=payload)


def test_exact_frozen_inventory():
    assert importlib.metadata.version('foundry-platform-sdk') == '1.101.0'
    assert ORACLE['source_commit'] == '168d51910570b6966afa2320333ab36f6a3f7ccf'
    assert len(CASES) == 48 and len(FORMS) == 258 and len(STREAMS) == 33
    assert len({OPERATIONS[key]['module'] for key in CASES}) == 11
    assert sum(len(source_contract(key)['throwable_errors']) for key in CASES) == 165
    assert sum(source_contract(key)['iterator'] for key in CASES) == 8


@pytest.mark.parametrize('key', CASES)
def test_source_signatures_wire_and_wrapper_assignments(key):
    row = OPERATIONS[key]
    source = source_contract(key)
    method = key.split('.')[-1]
    for asynchronous, name in ((False, 'ordinary'), (True, 'async')):
        client = source['async_client'] if asynchronous else source['client']
        tree = function_tree(getattr(client, method))
        expected = ast.parse('def signature(' + row[name]['signature'] + '): pass').body[0]
        assert ast.dump(tree.args) == ast.dump(expected.args)
        assert ast.unparse(tree.returns) == row[name]['return']
        assert isinstance(tree, ast.AsyncFunctionDef) == row[name]['coroutine_definition']
        requests = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Attribute) and node.func.attr == 'RequestInfo']
        actual_wire = {item.arg: ast.unparse(item.value) for item in requests[0].keywords}
        assert actual_wire == row['wire']
        for mode in ('raw', 'stream'):
            wrapper_name = ('_Async' if asynchronous else '_') + key.split('.')[-2] + 'Client' + ('Raw' if mode == 'raw' else 'Streaming')
            initializer = function_tree(getattr(source['module'], wrapper_name).__init__)
            assignment = [node for node in initializer.body if isinstance(node, ast.Assign)
                          and isinstance(node.targets[0], ast.Attribute) and node.targets[0].attr == method]
            metadata = row['wrappers'].get(('async_' if asynchronous else '') + mode)
            if metadata is None:
                assert not assignment and source['response_type'] is None
            else:
                assert len(assignment) == 1
                assert assignment[0].value.func.attr == metadata['helper']
                assert ast.unparse(assignment[0].value.args[1]) == 'client.' + method
                payload = next(node for node in initializer.body if isinstance(node, ast.FunctionDef) and node.name == method)
                assert ast.unparse(payload.args.args[0].annotation) == metadata['payload']


@pytest.mark.parametrize('key,mode,asynchronous', FORMS)
def test_native_modes_serialize_and_decode(key, mode, asynchronous, offline_event_loop):
    source = source_contract(key)
    payload = example(key)['SUCCESS']
    expected = TypeAdapter(source['response_type']).validate_python(payload)
    responses = []

    def handler(request):
        check_wire(source, request)
        response = response_for(payload)
        responses.append(response)
        return response

    result = exercise(key, mode, asynchronous, handler, offline_event_loop)
    if mode == 'stream':
        assert (result if isinstance(payload, bytes) else json.loads(result)) == normalized(expected)
    elif mode == 'ordinary' and source['iterator']:
        assert [type(item) for item in result] == [type(item) for item in expected.data]
        assert normalized(result) == normalized(expected.data)
    else:
        assert type(result) is type(expected)
        assert normalized(result) == normalized(expected)
    assert len(responses) == 1 and responses[0].is_closed


ERROR_FORMS = [(key, mode, asynchronous, error) for key, mode, asynchronous in FORMS
               for error in example(key)['ERRORS']]


@pytest.mark.parametrize('key,mode,asynchronous,error', ERROR_FORMS,
                         ids=lambda value: value['name'] if isinstance(value, dict) else str(value))
def test_declared_named_errors_keep_typed_parameters(key, mode, asynchronous, error, offline_event_loop):
    source = source_contract(key)
    error_type = source['throwable_errors'][error['name']]
    expected = TypeAdapter(error_type.__annotations__['parameters']).validate_python(error['parameters'])
    envelope = {'errorName': error['name'], 'errorCode': error['code'], 'parameters': error['parameters'],
                'errorInstanceId': '00000000-0000-0000-0000-000000000004'}
    responses = []

    def handler(request):
        check_wire(source, request)
        response = httpx.Response(error['status'], json=envelope)
        responses.append(response)
        return response

    with pytest.raises(error_type) as raised:
        exercise(key, mode, asynchronous, handler, offline_event_loop)
    assert type(raised.value) is error_type
    assert raised.value.name == envelope['errorName']
    assert raised.value.error_instance_id == envelope['errorInstanceId']
    assert type(raised.value.parameters) is type(expected)
    assert normalized(raised.value.parameters) == normalized(expected)
    assert len(responses) == 1 and responses[0].is_closed


@pytest.mark.parametrize('key,mode,asynchronous', FORMS)
def test_timeout_stops_after_one_attempt(key, mode, asynchronous, offline_event_loop):
    requests = []

    def handler(request):
        check_wire(source_contract(key), request)
        requests.append(request)
        raise httpx.ReadTimeout('finite timeout', request=request)

    with pytest.raises(ReadTimeout):
        exercise(key, mode, asynchronous, handler, offline_event_loop)
    assert len(requests) == 1


PAGER_FORMS = [(key, mode, asynchronous) for key, mode, asynchronous in FORMS
               if source_contract(key)['iterator']]


@pytest.mark.parametrize('key,mode,asynchronous', PAGER_FORMS)
def test_two_page_traversal_crosses_empty_first_page(key, mode, asynchronous, offline_event_loop):
    source = source_contract(key)
    payload = example(key)['SUCCESS']
    token = 'next /?= page'
    responses = []

    def handler(request):
        assert len(responses) < 2, 'Pagination exceeded finite request budget'
        check_wire(source, request, page_token=token if responses else None)
        body = copy.deepcopy(payload) if responses else {'data': [], 'nextPageToken': token}
        response = httpx.Response(200, json=body)
        responses.append(response)
        return response

    if mode == 'ordinary':
        result = exercise(key, mode, asynchronous, handler, offline_event_loop)
        assert normalized(result) == normalized(TypeAdapter(source['response_type']).validate_python(payload).data)
    else:
        arguments = inputs(key)
        for page in range(2):
            result = exercise(key, mode, asynchronous, handler, offline_event_loop, arguments)
            result = json.loads(result) if mode == 'stream' else normalized(result)
            if page == 0:
                assert result['data'] == [] and result['nextPageToken'] == token
                arguments['page_token'] = result['nextPageToken']
            else:
                assert result['data'] == payload['data']
                assert result.get('nextPageToken') is None
    assert len(responses) == 2 and all(response.is_closed for response in responses)


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


@pytest.mark.parametrize('key', STREAMS)
@pytest.mark.parametrize('asynchronous', (False, True))
def test_byte_budget_closes_unfinished_native_stream(key, asynchronous, offline_event_loop):
    source = source_contract(key)
    body = TrackedAsyncStream() if asynchronous else TrackedSyncStream()
    responses = []

    def handler(request):
        check_wire(source, request)
        response = httpx.Response(200, stream=body)
        responses.append(response)
        return response

    method = key.split('.')[-1]
    if asynchronous:
        async def run():
            async with mock_async_resource(source['async_client'], handler) as client:
                async with getattr(client.with_streaming_response, method)(**inputs(key)) as response:
                    async for chunk in response.aiter_bytes(chunk_size=4):
                        assert chunk == b'part' and body.chunks_read == 1 and not body.closed
                        raise RuntimeError('Caller byte budget exhausted')
        with pytest.raises(RuntimeError, match='Caller byte budget exhausted'):
            offline_event_loop.run_until_complete(run())
    else:
        with mock_resource(source['client'], handler) as client:
            with pytest.raises(RuntimeError, match='Caller byte budget exhausted'):
                with getattr(client.with_streaming_response, method)(**inputs(key)) as response:
                    for chunk in response.iter_bytes(chunk_size=4):
                        assert chunk == b'part' and body.chunks_read == 1 and not body.closed
                        raise RuntimeError('Caller byte budget exhausted')
    assert len(responses) == 1 and responses[0].is_closed
    assert body.closed and body.chunks_read == 1


def require_unfinished(response, body):
    # httpx marks a stream consumed when iteration starts, before exhaustion.
    assert not response.is_closed
    assert not body.closed and body.chunks_read == 1


@pytest.mark.parametrize('key', STREAMS)
def test_async_cancellation_closes_with_unread_bytes(key, offline_event_loop):
    source = source_contract(key)
    body = TrackedAsyncStream()
    responses = []

    def handler(request):
        check_wire(source, request)
        response = httpx.Response(200, stream=body)
        responses.append(response)
        return response

    async def run():
        started, hold = asyncio.Event(), asyncio.Event()

        async def reader(client):
            async with getattr(client.with_streaming_response, key.split('.')[-1])(**inputs(key)) as response:
                async for chunk in response.aiter_bytes(chunk_size=4):
                    assert chunk == b'part'
                    require_unfinished(responses[0], body)
                    started.set()
                    await hold.wait()

        async with mock_async_resource(source['async_client'], handler) as client:
            task = asyncio.create_task(reader(client))
            try:
                await asyncio.wait_for(started.wait(), 2)
                require_unfinished(responses[0], body)
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


def test_prebuffered_response_cannot_prove_stream_cancellation():
    body = TrackedSyncStream()
    response = httpx.Response(200, stream=body)
    response.read()
    assert body.chunks_read == 3 and body.closed
    with pytest.raises(AssertionError):
        require_unfinished(response, body)


@pytest.mark.parametrize('key,mode,asynchronous', FORMS)
def test_invalid_timeout_rejected_before_transport(key, mode, asynchronous, offline_event_loop):
    def forbidden(request):
        raise AssertionError('Invalid input reached transport')

    arguments = inputs(key)
    arguments['request_timeout'] = 'invalid-timeout'
    with pytest.raises((ValidationError, TypeError, ValueError)):
        exercise(key, mode, asynchronous, forbidden, offline_event_loop, arguments)


@pytest.mark.parametrize('fault', ('method', 'path', 'query', 'body', 'header', 'timeout'))
def test_wire_oracle_rejects_independent_request_faults(fault, offline_event_loop):
    key = 'v2.third_party_applications.Version.upload'
    source = source_contract(key)
    captured = []

    def handler(request):
        captured.append(request)
        return response_for(example(key)['SUCCESS'])

    exercise(key, 'ordinary', False, handler, offline_event_loop)
    original = captured[0]
    headers, extensions = dict(original.headers), copy.deepcopy(original.extensions)
    method, url, content = original.method, original.url, original.content
    if fault == 'method':
        method = 'DELETE'
    elif fault == 'path':
        url = url.copy_with(path='/api/wrong')
    elif fault == 'query':
        url = url.copy_with(query=b'version=wrong')
    elif fault == 'body':
        content = b'not-a-zip'
    elif fault == 'header':
        headers['content-type'] = 'application/json'
    else:
        extensions['timeout']['read'] = None
    mutated = httpx.Request(method, url, content=content, headers=headers, extensions=extensions)
    with pytest.raises(AssertionError):
        check_wire(source, mutated)


def test_upload_is_binary_zip_and_version_matches_response(offline_event_loop):
    key = 'v2.third_party_applications.Version.upload'
    arguments = inputs(key)
    with zipfile.ZipFile(io.BytesIO(arguments['body'])) as archive:
        assert archive.namelist() == ['index.html']
        assert archive.read('index.html').startswith(b'<!doctype html>')
    assert arguments['version'] == example(key)['SUCCESS']['version']


@pytest.mark.parametrize('mode', ('ordinary', 'raw', 'stream'))
@pytest.mark.parametrize('asynchronous', (False, True))
def test_log_file_identifier_is_one_escaped_segment(mode, asynchronous, offline_event_loop):
    key = 'v2.audit.LogFile.content'
    arguments = inputs(key)
    arguments['log_file_id'] = 'audit /?#% caf\u00e9'
    source = source_contract(key, arguments)
    responses = []
    payload = b'\x00audit\n\xffbinary'

    def handler(request):
        check_wire(source, request)
        assert b'audit%20%2F%3F%23%25%20caf%C3%A9/content' in request.url.raw_path
        assert not request.url.query
        response = httpx.Response(200, content=payload)
        responses.append(response)
        return response

    assert exercise(key, mode, asynchronous, handler, offline_event_loop, arguments) == payload
    assert len(responses) == 1 and responses[0].is_closed


@pytest.mark.parametrize('asynchronous', (False, True))
def test_template_variables_reach_the_server_with_aliases(asynchronous, offline_event_loop):
    key = 'v2.filesystem.Project.create_from_template'
    arguments = inputs(key)
    requests = []

    def handler(request):
        check_wire(source_contract(key), request)
        body = json.loads(request.content)
        assert body == {'templateRid': arguments['template_rid'],
                        'variableValues': {'department': 'Research'},
                        'projectDescription': 'Synthetic research project'}
        requests.append(request)
        return response_for(example(key)['SUCCESS'])

    result = exercise(key, 'ordinary', asynchronous, handler, offline_event_loop)
    assert result.rid == example(key)['SUCCESS']['rid']
    assert len(requests) == 1


@pytest.mark.parametrize('key', ('v2.filesystem.Resource.get', 'v2.filesystem.Folder.get',
                               'v2.filesystem.Project.get', 'v2.third_party_applications.Version.get'))
@pytest.mark.parametrize('mode', ('ordinary', 'raw'))
@pytest.mark.parametrize('asynchronous', (False, True))
def test_required_response_fields_are_validated(key, mode, asynchronous, offline_event_loop):
    source = source_contract(key)
    payload = copy.deepcopy(example(key)['SUCCESS'])
    required = next(field.alias or name for name, field in source['response_type'].model_fields.items()
                    if field.is_required())
    payload.pop(required)
    responses = []

    def handler(request):
        check_wire(source, request)
        response = httpx.Response(200, json=payload)
        responses.append(response)
        return response

    with pytest.raises(ValidationError):
        exercise(key, mode, asynchronous, handler, offline_event_loop)
    assert len(responses) == 1 and responses[0].is_closed


def test_named_error_fixture_union_is_exact():
    for key in CASES:
        source = source_contract(key)
        names = [error['name'] for error in example(key)['ERRORS']]
        assert len(names) == len(set(names))
        assert set(names) == set(source['throwable_errors'])


def test_network_denial_is_active(offline_event_loop):
    with pytest.raises(AssertionError, match='Network forbidden'):
        socket.getaddrinfo('public.example.invalid', 443)
    with httpx.Client() as client:
        with pytest.raises(AssertionError, match='Network forbidden'):
            client.get('https://public.example.invalid', timeout=1)

    async def run():
        async with httpx.AsyncClient() as client:
            with pytest.raises(AssertionError, match='Network forbidden'):
                await client.get('https://public.example.invalid', timeout=1)

    offline_event_loop.run_until_complete(run())
