"""SDK101 transport checks and source-derived semantic regression guards."""

import ast
import asyncio
import copy
import hashlib
import importlib
import importlib.metadata
import inspect
import io
import json
import re
import runpy
import socket
import textwrap
import zipfile
from pathlib import Path
from functools import lru_cache
from urllib.parse import quote, unquote

import httpx
import pytest
from foundry_sdk import ReadTimeout
from foundry_sdk._errors import PermissionDeniedError
from pydantic import TypeAdapter, ValidationError
from foundry_sdk.v2.connectivity import models as connectivity
from foundry_sdk.v2.connectivity.connection import ConnectionClient
from foundry_sdk.v2.sql_queries.sql_query import SqlQueryClient
from foundry_sdk.v2.streams.stream import StreamClient
from foundry_sdk.v2.streams.subscriber import SubscriberClient

ROOT = Path(__file__).parents[1]
DEV = ROOT / '.agents/skills/pal-found-dev'
EXAMPLES = DEV / 'examples/rest/089/v2'
FILES = sorted(EXAMPLES.rglob('invoke_*.py'))


@pytest.fixture(scope='module')
def offline_event_loop():
    # Windows initializes its local self-pipe before network access is denied.
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True)
def deny_network(monkeypatch, offline_event_loop):
    def denied(*args, **kwargs):
        raise AssertionError('Network forbidden in offline REST089 tests')
    for name in ('connect', 'connect_ex'):
        monkeypatch.setattr(socket.socket, name, denied)
    for name in ('create_connection', 'getaddrinfo', 'gethostbyname', 'gethostbyname_ex'):
        monkeypatch.setattr(socket, name, denied)
    monkeypatch.setattr(httpx.HTTPTransport, 'handle_request', denied)
    monkeypatch.setattr(httpx.AsyncHTTPTransport, 'handle_async_request', denied)


@pytest.mark.parametrize('path', FILES, ids=lambda path: str(path.relative_to(EXAMPLES)))
def test_all_owned_examples_use_real_sdk_with_mock_http(path):
    runpy.run_path(str(path))['verify']()


def load(resource, method):
    return runpy.run_path(str(EXAMPLES / resource / f'invoke_{method}.py'))


def assert_semantics(case, example):
    body = example['EXPECTED_BODY']
    if case == 'connection':
        assert body['worker']['type'] == 'foundryWorker'
        assert body['worker']['networkEgressPolicyRids']
        assert body['configuration']['bucketUrl'].startswith('s3://')
        assert body['configuration']['bucketUrl'].endswith('/')
        assert example['SUCCESS']['configuration'] == body['configuration']
        assert example['SUCCESS']['worker'] == body['worker']
    elif case == 'secret':
        assert body['secrets'] and all(body['secrets'].values())
    elif case == 'jdbc':
        name = example['EXPECTED_QUERY']['fileName']
        assert name.endswith('.jar')
        with zipfile.ZipFile(io.BytesIO(body)) as jar:
            assert 'META-INF/MANIFEST.MF' in jar.namelist()
        config = example['SUCCESS']['configuration']
        assert config['type'] == 'jdbc'
        assert name in config['uploadedJdbcDrivers']
        connectivity.JdbcConnectionConfiguration.model_validate(config)
    elif case == 'query':
        assert body['config']['query'] == 'SELECT order_id, total FROM main.sales.orders LIMIT 100'
        assert example['SUCCESS']['config'] == body['config']
    elif case == 'record':
        records = [body['record']] if 'record' in body else body['records']
        assert records
        for record in records:
            assert set(record) == {'orderId', 'quantity'}
            assert isinstance(record['orderId'], str) and record['orderId']
            assert type(record['quantity']) is int
        assert example['SUCCESS'] is None
    elif case == 'reset':
        position = body['position']
        assert position['type'] == 'specific' and position['offsets']
        assert all(type(offset) is int and offset >= 0 for offset in position['offsets'].values())
        assert example['SUCCESS'] == position['offsets']
    elif case == 'end':
        assert example['SUCCESS']['0'] == 53 and example['SUCCESS']['1'] == 0


CASES = [
    ('connection', 'connectivity/Connection', 'create'),
    ('secret', 'connectivity/Connection', 'update_secrets'),
    ('jdbc', 'connectivity/Connection', 'upload_custom_jdbc_drivers'),
    ('query', 'connectivity/TableImport', 'create'),
    ('query', 'connectivity/TableImport', 'replace'),
    ('record', 'streams/Stream', 'publish_record'),
    ('record', 'streams/Stream', 'publish_records'),
    ('reset', 'streams/Subscriber', 'reset_offsets'),
    ('end', 'streams/Stream', 'get_end_offsets'),
]


@pytest.mark.parametrize('case,resource,method', CASES)
def test_meaningful_examples_reject_original_semantic_mutations(case, resource, method):
    example = load(resource, method)
    assert_semantics(case, example)
    mutated = dict(example)
    mutated['EXPECTED_BODY'] = copy.deepcopy(example['EXPECTED_BODY'])
    mutated['SUCCESS'] = copy.deepcopy(example['SUCCESS'])
    mutated['EXPECTED_QUERY'] = copy.deepcopy(example['EXPECTED_QUERY'])
    body = mutated['EXPECTED_BODY']
    if case == 'connection':
        body['worker'] = {'type': 'unknownWorker'}
    elif case == 'secret':
        body['secrets'] = {}
    elif case == 'jdbc':
        mutated['EXPECTED_QUERY']['fileName'] = 'synthetic-value'
    elif case == 'query':
        body['config']['query'] = 'synthetic-value'
    elif case == 'record':
        body.update({'record': {}} if 'record' in body else {'records': [{}]})
    elif case == 'reset':
        body['position']['offsets'] = {}
    elif case == 'end':
        mutated['SUCCESS'] = {}
    with pytest.raises((AssertionError, KeyError)):
        assert_semantics(case, mutated)


def test_sdk_source_contracts_ground_semantic_guards():
    assert 'trailing slash' in inspect.getsource(connectivity.S3ConnectionConfiguration)
    assert 'UnknownWorkerCannotBeUsedForCreatingOrUpdatingConnections' in inspect.getsource(ConnectionClient.create)
    assert '.jar' in inspect.getdoc(ConnectionClient.upload_custom_jdbc_drivers)
    assert 'next record' in inspect.getdoc(StreamClient.get_end_offsets)
    assert 'specific' in inspect.getdoc(SubscriberClient.reset_offsets)
    assert 'Arrow' in inspect.getdoc(SqlQueryClient.execute_ontology)
    assert inspect.signature(StreamClient.publish_record).return_annotation is None


def test_ontology_arrow_decode_and_budgets_reject_invalid_results():
    example = load('sql_queries/SqlQuery', 'execute_ontology')
    assert example['EXPECTED_BODY']['rowLimit'] == 10
    assert example['EXPECTED_BODY']['query'] == 'SELECT orderId FROM Orders LIMIT 10'
    assert example['EXPECTED_BODY']['ontologyIdentifier']
    decode = example['decode_result']
    assert decode(example['SUCCESS']) == [{'orderId': 'order-001'}]
    import pyarrow as pa
    with pytest.raises(pa.ArrowInvalid):
        decode(b'offline synthetic content')
    with pytest.raises(ValueError, match='byte budget'):
        decode(b'x' * (example['MAX_RESULT_BYTES'] + 1))
    sink = pa.BufferOutputStream()
    with pa.ipc.new_stream(sink, pa.schema([('orderId', pa.string())])) as writer:
        writer.write_table(pa.table({'orderId': ['order-001'] * 11}))
    with pytest.raises(ValueError, match='row budget'):
        decode(sink.getvalue().to_pybytes())


def test_dataset_and_publish_guidance_match_actual_return_shapes():
    dataset = load('streams/Dataset', 'create')
    assert set(dataset['SUCCESS']) == {'rid', 'name', 'parentFolderRid'}
    guide = (DEV / 'references/rest/v2/streams/Dataset.md').read_text()
    assert 'Stream.get(dataset_rid, stream_branch_name)' in guide
    assert 'response contains no stream or view identity' in guide
    stream = (DEV / 'references/rest/v2/streams/Stream.md').read_text()
    assert 'SDK returns `None`' in stream
    assert 'Confirm the returned write result' not in stream


REGISTER = json.loads((ROOT / 'maintainer/rest-domain-authoring-register.json').read_text())
ORACLE = json.loads((ROOT / 'tests/fixtures/offline/rest-acceptance/source-oracle.json').read_text())
ROWS = {row['id']: row for row in REGISTER['operations'] if row['story'] == 'DEV-STORY-089'}
IDS = sorted(ROWS)


@lru_cache
def source_contract(identity):
    """Extract wire definitions from the installed frozen SDK, independently of examples."""
    version, service, resource, operation = identity.split('.')
    snake = re.sub(r'(?<!^)(?=[A-Z])', '_', resource).lower()
    module = importlib.import_module(f'foundry_sdk.{version}.{service}.{snake}')
    client = getattr(module, resource + 'Client')
    method = getattr(client, operation)
    tree = ast.parse(textwrap.dedent(inspect.getsource(method)))
    calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
             and isinstance(node.func, ast.Attribute) and node.func.attr == 'RequestInfo']
    assert len(calls) == 1
    return module, client, method, {item.arg: item.value for item in calls[0].keywords}


def source_value(module, expression, arguments=None):
    return eval(compile(ast.Expression(expression), '<SDK101 contract>', 'eval'),
                vars(module), arguments or {})


def owned_example(identity):
    return runpy.run_path(str(DEV / ROWS[identity]['example']))


def operation_inputs(example):
    """Capture adaptable example inputs without using its expected wire constants."""
    class Capture:
        @property
        def with_raw_response(self):
            return self

        def __getattr__(self, name):
            return lambda **kwargs: kwargs

    return copy.deepcopy(example['invoke'](Capture()))


def expected_field(identity, name, arguments=None):
    module, _, method, fields = source_contract(identity)
    bound = inspect.signature(method).bind_partial(None, **(arguments or {}))
    bound.apply_defaults()
    return source_value(module, fields[name], bound.arguments)


def check_source_request(identity, arguments, request):
    assert request.method == expected_field(identity, 'method', arguments)
    path = expected_field(identity, 'resource_path', arguments)
    for key, value in expected_field(identity, 'path_params', arguments).items():
        path = path.replace('{' + key + '}', quote(str(value), safe=''))
    assert unquote(request.url.path) == '/api' + unquote(path)
    assert request.headers['Authorization'] == 'Bearer offline-fixture-token'
    for name, value in expected_field(identity, 'header_params', arguments).items():
        if value is None:
            assert name not in request.headers
        else:
            assert request.headers[name] == str(value)
    query = httpx.QueryParams({key: value for key, value in
                              expected_field(identity, 'query_params', arguments).items()
                              if value is not None})
    assert sorted(request.url.params.multi_items()) == sorted(query.multi_items())
    body = expected_field(identity, 'body', arguments)
    if isinstance(body, bytes):
        assert request.content == body
    elif body is not None:
        expected = TypeAdapter(type(body)).dump_python(body, mode='python', by_alias=True,
                                                      exclude_none=True)
        assert json.loads(request.content) == expected
    else:
        assert request.content == b''
    assert request.extensions['timeout']['read'] == arguments.get('request_timeout', 30)


def payload_for(identity, example):
    # get_results defaults to Arrow. The accepted reader lifecycle separately requests CSV.
    if identity == 'v2.sql_queries.SqlQuery.get_results':
        import pyarrow as pa
        sink = pa.BufferOutputStream()
        with pa.ipc.new_stream(sink, pa.schema([('row_count', pa.int64())])) as writer:
            writer.write_table(pa.table({'row_count': [1]}))
        return sink.getvalue().to_pybytes()
    if identity == 'v2.streams.Stream.get_records':
        return [{'offset': '50', 'value': {'orderId': 'A', 'quantity': 2}}]
    if identity == 'v2.streams.Subscriber.read_records':
        return {'recordsByPartition': {'0': [
            {'offset': '50', 'value': {'orderId': 'A', 'quantity': 2}},
            {'offset': '52', 'value': {'orderId': 'B', 'quantity': 3}},
        ]}}
    return copy.deepcopy(example['SUCCESS'])


def normalized(value):
    if hasattr(value, 'model_dump'):
        return value.model_dump(mode='json', by_alias=True, exclude_none=True)
    if isinstance(value, dict):
        return {key: normalized(child) for key, child in value.items()}
    if isinstance(value, (list, tuple)):
        return [normalized(child) for child in value]
    return value


def response_for(payload):
    if payload is None:
        return httpx.Response(204)
    if isinstance(payload, bytes):
        return httpx.Response(200, content=payload)
    return httpx.Response(200, json=payload)


def assert_typed_result(identity, payload, actual, native=False):
    expected = TypeAdapter(expected_field(identity, 'response_type')).validate_python(payload)
    if native and identity.endswith('.list'):
        expected = expected.data
    assert actual == expected
    if identity in ('v2.sql_queries.SqlQuery.get_results', 'v2.sql_queries.SqlQuery.execute_ontology'):
        import pyarrow as pa
        rows = pa.ipc.open_stream(actual).read_all().to_pylist()
        assert rows == ([{'row_count': 1}] if identity.endswith('get_results')
                        else [{'orderId': 'order-001'}])


def execute_mode(identity, example, handler, asynchronous, mode, loop, arguments=None):
    """Run actual SDK signatures, including direct asynchronous resource iterators."""
    module, client_type, _, _ = source_contract(identity)
    operation = identity.rsplit('.', 1)[1]
    arguments = operation_inputs(example) if arguments is None else arguments
    mock = importlib.import_module('mock_transport')

    def target(client):
        return client if mode == 'ordinary' else getattr(client, 'with_' + mode + '_response')

    def decode_stream(data):
        response_type = expected_field(identity, 'response_type')
        return data if isinstance(payload_for(identity, example), bytes) else TypeAdapter(
            response_type).validate_json(data)

    if asynchronous:
        async def exercise():
            async with mock.mock_async_resource(getattr(module, 'Async' + client_type.__name__), handler) as client:
                if mode == 'streaming' and expected_field(identity, 'response_type') is None:
                    with pytest.raises(AttributeError):
                        getattr(target(client), operation)
                    return 'absent'
                pending = getattr(target(client), operation)(**arguments)
                if mode == 'streaming':
                    assert not inspect.isawaitable(pending)
                    async with pending as response:
                        return decode_stream(b''.join([chunk async for chunk in response.aiter_bytes()]))
                if mode == 'ordinary' and hasattr(pending, '__aiter__'):
                    assert not inspect.isawaitable(pending)
                    return [item async for item in pending]
                assert inspect.isawaitable(pending)
                result = await pending
                if mode == 'raw':
                    assert not inspect.iscoroutinefunction(result.decode)
                    assert inspect.iscoroutinefunction(result.aclose)
                    try:
                        return result.decode()
                    finally:
                        await result.aclose()
                return result
        return loop.run_until_complete(exercise())
    with mock.mock_resource(client_type, handler) as client:
        if mode == 'streaming' and expected_field(identity, 'response_type') is None:
            with pytest.raises(AttributeError):
                getattr(target(client), operation)
            return 'absent'
        result = getattr(target(client), operation)(**arguments)
        if mode == 'streaming':
            with result as response:
                return decode_stream(b''.join(response.iter_bytes()))
        if mode == 'raw':
            try:
                return result.decode()
            finally:
                result.close()
        return list(result) if hasattr(result, '__next__') else result


def test_partition_source_hashes_and_source_mode_inventory():
    assert importlib.metadata.version('foundry-platform-sdk') == '1.101.0'
    assert importlib.metadata.version('pyarrow') == '23.0.0'
    frozen = {identity for identity in ORACLE['operations'] if identity.startswith(
        ('v2.connectivity.', 'v2.sql_queries.', 'v2.streams.'))}
    assert set(IDS) == frozen
    assert len(IDS) == 40
    for identity in IDS:
        module, _, _, _ = source_contract(identity)
        assert hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest() == (
            ROWS[identity]['source_sha256']) == ORACLE['operations'][identity]['source_sha256']
    assert sum(len(expected_field(identity, 'throwable_errors')) for identity in IDS) == 143
    assert sum(expected_field(identity, 'response_type') is None for identity in IDS) == 9


@pytest.mark.parametrize('identity', IDS)
@pytest.mark.parametrize('asynchronous', (False, True))
@pytest.mark.parametrize('mode', ('ordinary', 'raw', 'streaming'))
def test_all_operation_modes_source_wire_typed_results_and_absence(
        identity, asynchronous, mode, offline_event_loop):
    example = owned_example(identity)
    arguments = operation_inputs(example)
    payload = payload_for(identity, example)
    responses = []

    def handler(request):
        check_source_request(identity, arguments, request)
        response = response_for(payload)
        responses.append(response)
        return response

    actual = execute_mode(identity, example, handler, asynchronous, mode, offline_event_loop)
    if mode == 'streaming' and expected_field(identity, 'response_type') is None:
        assert actual == 'absent' and responses == []
    else:
        assert_typed_result(identity, payload, actual, native=mode == 'ordinary')
        assert len(responses) == 1 and responses[0].is_closed


STREAM_IDS = [identity for identity in IDS if expected_field(identity, 'response_type') is not None]
PAGED_IDS = [identity for identity in IDS
             if 'page_token' in inspect.signature(source_contract(identity)[2]).parameters]
AVAILABLE_MODES = [(identity, asynchronous, mode) for identity in IDS
                   for asynchronous in (False, True) for mode in ('ordinary', 'raw', 'streaming')
                   if mode != 'streaming' or identity in STREAM_IDS]


@pytest.mark.parametrize('identity,asynchronous,mode', AVAILABLE_MODES)
def test_missing_required_input_fails_before_http(identity, asynchronous, mode, offline_event_loop):
    example = owned_example(identity)
    arguments = operation_inputs(example)
    signature = inspect.signature(source_contract(identity)[2])
    required = next(name for name, parameter in signature.parameters.items()
                    if name != 'self' and parameter.default is inspect.Parameter.empty)
    del arguments[required]
    requests = []

    def unexpected(request):
        requests.append(request)
        raise AssertionError('Invalid input reached HTTP')

    with pytest.raises(ValidationError):
        execute_mode(identity, example, unexpected, asynchronous, mode, offline_event_loop, arguments)
    assert requests == []


@pytest.mark.parametrize('identity,asynchronous,mode', AVAILABLE_MODES)
def test_read_timeout_preserves_cause_with_one_attempt(identity, asynchronous, mode, offline_event_loop):
    example = owned_example(identity)
    arguments = operation_inputs(example)
    requests = []

    def stalled(request):
        check_source_request(identity, arguments, request)
        requests.append(request)
        raise httpx.ReadTimeout('Synthetic deadline', request=request)

    with pytest.raises(ReadTimeout, match='Synthetic deadline') as raised:
        execute_mode(identity, example, stalled, asynchronous, mode, offline_event_loop)
    assert isinstance(raised.value.__cause__, httpx.ReadTimeout)
    assert len(requests) == 1


class TrackedStream(httpx.SyncByteStream):
    def __init__(self, data):
        split = max(1, len(data) // 3)
        self.chunks = (data[:split], data[split:split * 2], data[split * 2:])
        self.reads = 0
        self.closed = False

    def __iter__(self):
        for chunk in self.chunks:
            self.reads += 1
            yield chunk

    def close(self):
        self.closed = True


class TrackedAsyncStream(httpx.AsyncByteStream):
    def __init__(self, data):
        self.state = TrackedStream(data)

    async def __aiter__(self):
        for chunk in self.state:
            yield chunk

    async def aclose(self):
        self.state.close()


@pytest.mark.parametrize('identity', STREAM_IDS)
@pytest.mark.parametrize('asynchronous', (False, True))
def test_unbuffered_stream_caller_interrupt_or_cancel_closes_unread_body(
        identity, asynchronous, offline_event_loop):
    example = owned_example(identity)
    arguments = operation_inputs(example)
    payload = payload_for(identity, example)
    data = payload if isinstance(payload, bytes) else json.dumps(payload).encode()
    body = TrackedAsyncStream(data) if asynchronous else TrackedStream(data)
    state = body.state if asynchronous else body
    responses = []

    def handler(request):
        check_source_request(identity, arguments, request)
        response = httpx.Response(200, stream=body)
        assert not response.is_closed and not state.closed and state.reads == 0
        responses.append(response)
        return response

    module, client_type, _, _ = source_contract(identity)
    operation = identity.rsplit('.', 1)[1]
    mock = importlib.import_module('mock_transport')
    if asynchronous:
        async def exercise():
            async with mock.mock_async_resource(getattr(module, 'Async' + client_type.__name__), handler) as client:
                async with getattr(client.with_streaming_response, operation)(**arguments) as response:
                    async for chunk in response.aiter_bytes():
                        assert chunk == state.chunks[0]
                        asyncio.current_task().cancel()
                        await asyncio.sleep(0)
        with pytest.raises(asyncio.CancelledError):
            offline_event_loop.run_until_complete(exercise())
    else:
        with mock.mock_resource(client_type, handler) as client:
            with pytest.raises(RuntimeError, match='Caller byte budget'):
                with getattr(client.with_streaming_response, operation)(**arguments) as response:
                    for chunk in response.iter_bytes():
                        assert chunk == state.chunks[0]
                        raise RuntimeError('Caller byte budget exhausted')
    assert len(responses) == 1 and responses[0].is_closed
    assert state.closed and state.reads == 1


@pytest.mark.parametrize('identity', PAGED_IDS)
@pytest.mark.parametrize('asynchronous', (False, True))
@pytest.mark.parametrize('mode', ('ordinary', 'raw', 'streaming'))
def test_two_finite_pages_preserve_token_and_close_each_response(
        identity, asynchronous, mode, offline_event_loop):
    example = owned_example(identity)
    arguments = operation_inputs(example)
    arguments['page_size'] = 2
    payload = payload_for(identity, example)
    tokens, responses = [], []

    def handler(request):
        token = request.url.params.get('pageToken')
        tokens.append(token)
        assert tokens == ([None] if len(tokens) == 1 else [None, 'finite-next'])
        assert len(tokens) <= 2
        check_source_request(identity, dict(arguments, page_token=token), request)
        page = dict(payload, nextPageToken='finite-next') if token is None else {'data': []}
        response = httpx.Response(200, json=page)
        responses.append(response)
        return response

    first = execute_mode(identity, example, handler, asynchronous, mode, offline_event_loop, arguments)
    expected_rows = TypeAdapter(expected_field(identity, 'response_type')).validate_python(payload).data
    if mode == 'ordinary':
        assert first == expected_rows
    else:
        assert first.data == expected_rows and first.next_page_token == 'finite-next'
        second = execute_mode(identity, example, handler, asynchronous, mode, offline_event_loop,
                              dict(arguments, page_token=first.next_page_token))
        assert second.data == [] and second.next_page_token is None
    assert tokens == [None, 'finite-next'] and all(response.is_closed for response in responses)


@pytest.mark.parametrize('identity', IDS)
@pytest.mark.parametrize('fault', ('method', 'path', 'body'))
def test_source_oracle_rejects_mutated_wire(identity, fault, offline_event_loop):
    example = owned_example(identity)
    arguments = operation_inputs(example)
    requests = []

    def handler(request):
        requests.append(request)
        return response_for(payload_for(identity, example))

    execute_mode(identity, example, handler, False, 'raw', offline_event_loop)
    original = requests[0]
    damaged = httpx.Request('OPTIONS' if fault == 'method' else original.method,
        str(original.url) + ('/incorrect' if fault == 'path' else ''),
        content=b'null' if fault == 'body' else original.content,
        headers=original.headers, extensions=original.extensions)
    with pytest.raises((AssertionError, json.JSONDecodeError)):
        check_source_request(identity, arguments, damaged)


def test_binary_arrow_and_csv_formats_have_real_decoders_and_explicit_budgets():
    import pyarrow as pa
    assert 'Apache Arrow' in inspect.getdoc(SqlQueryClient.get_results)
    payload = payload_for('v2.sql_queries.SqlQuery.get_results', {})

    def decode(data, max_bytes=65536, max_rows=1):
        if len(data) > max_bytes:
            raise ValueError('byte budget')
        table = pa.ipc.open_stream(data).read_all()
        if table.num_rows > max_rows:
            raise ValueError('row budget')
        return table.to_pylist()

    assert decode(payload) == [{'row_count': 1}]
    with pytest.raises(pa.ArrowInvalid):
        decode(b'offline synthetic content')
    with pytest.raises(ValueError, match='byte budget'):
        decode(payload, max_bytes=len(payload) - 1)
    with pytest.raises(ValueError, match='row budget'):
        decode(payload, max_rows=0)
    # This accepted reader journey explicitly requests CSV and parses its matching result.
    runpy.run_path(str(DEV / 'examples/rest/089/sql_query_lifecycle.py'))['verify']()
    runpy.run_path(str(DEV / 'examples/rest/089/subscriber_offsets.py'))['verify']()


def test_public_network_dns_and_native_http_guards_are_active(offline_event_loop):
    with pytest.raises(AssertionError, match='Network forbidden'):
        socket.getaddrinfo('public.example.invalid', 443)
    with socket.socket() as connection:
        with pytest.raises(AssertionError, match='Network forbidden'):
            connection.connect(('198.51.100.1', 443))
    request = httpx.Request('GET', 'https://public.example.invalid')
    with pytest.raises(AssertionError, match='Network forbidden'):
        httpx.HTTPTransport().handle_request(request)

    async def denied():
        with pytest.raises(AssertionError, match='Network forbidden'):
            await httpx.AsyncHTTPTransport().handle_async_request(request)
    offline_event_loop.run_until_complete(denied())


def error_code(error_type):
    base = error_type.__mro__[1].__name__
    return {'BadRequestError': ('INVALID_ARGUMENT', 400),
            'NotFoundError': ('NOT_FOUND', 404), 'PermissionDeniedError': ('PERMISSION_DENIED', 403),
            'ConflictError': ('CONFLICT', 409), 'InternalServerError': ('INTERNAL', 500),
            'FailedPreconditionError': ('FAILED_PRECONDITION', 400)}[base]


@pytest.mark.parametrize('identity,asynchronous,mode', AVAILABLE_MODES)
def test_all_source_error_classes_and_generic_denial_in_available_modes(
        identity, asynchronous, mode, offline_event_loop):
    example = owned_example(identity)
    arguments = operation_inputs(example)
    errors = expected_field(identity, 'throwable_errors')
    fixtures = {item['name']: item for item in example['ERRORS']}
    assert fixtures.keys() == errors.keys()
    for name, error_type in list(errors.items()) + [('UnregisteredOfflineDenial', PermissionDeniedError)]:
        if name in errors:
            adapter = TypeAdapter(error_type.__annotations__['parameters'])
            parameters = fixtures[name]['parameters']
            expected_parameters = adapter.validate_python(parameters)
            code, status = error_code(error_type)
        else:
            parameters, code, status = {'reason': 'fixture denial'}, 'PERMISSION_DENIED', 403
        responses = []

        def handler(request):
            check_source_request(identity, arguments, request)
            response = httpx.Response(status, json={'errorName': name, 'errorCode': code,
                'parameters': parameters, 'errorInstanceId': '00000000-0000-0000-0000-000000000004'})
            responses.append(response)
            return response

        with pytest.raises(error_type) as raised:
            execute_mode(identity, example, handler, asynchronous, mode, offline_event_loop)
        assert raised.value.name == name
        if name in errors:
            assert type(raised.value) is error_type
            assert adapter.validate_python(raised.value.parameters) == expected_parameters
        else:
            assert type(raised.value) is PermissionDeniedError
            assert raised.value.parameters == parameters
        assert len(responses) == 1 and responses[0].is_closed
