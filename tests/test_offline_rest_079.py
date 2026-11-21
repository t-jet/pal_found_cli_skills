"""REST-079 SDK transport and cross-field semantic regression checks."""

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
BASE = ROOT / '.agents/skills/pal-found-dev/examples/rest/079'
ORACLE = json.loads((ROOT / 'tests/fixtures/offline/rest-acceptance/source-oracle.json').read_text())
RESOURCES = {'ActionType', 'ActionTypeFullMetadata', 'ObjectType', 'Ontology',
             'OntologyInterface', 'OntologyValueType', 'QueryType'}
OPERATIONS = {key: row for key, row in ORACLE['operations'].items()
              if key.startswith('v2.ontologies.') and key.split('.')[2] in RESOURCES}


def load(resource, method):
    path = BASE / f'v2/ontologies/{resource}/invoke_{method}.py'
    if resource == 'ObjectType' and method == 'get':
        path = BASE / 'object_type_schema.py'
    return runpy.run_path(str(path))['verify'].__globals__


@pytest.fixture(scope='module')
def offline_event_loop():
    # Windows creates its local event-loop socket pair before connection denial.
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True)
def deny_network(monkeypatch, offline_event_loop):
    def denied(*args, **kwargs):
        raise AssertionError('Public socket/DNS access denied in REST-079 tests')

    for name in ('connect', 'connect_ex'):
        monkeypatch.setattr(socket.socket, name, denied)
    for name in ('create_connection', 'getaddrinfo', 'gethostbyname', 'gethostbyname_ex'):
        monkeypatch.setattr(socket, name, denied)
    monkeypatch.setattr(httpx.HTTPTransport, 'handle_request', denied)
    monkeypatch.setattr(httpx.AsyncHTTPTransport, 'handle_async_request', denied)


def test_source_bindings_match_frozen_sdk101():
    assert ORACLE['sdk_release'] == '1.101.0'
    assert len(OPERATIONS) == 32
    for row in OPERATIONS.values():
        module = importlib.import_module(row['module'])
        assert hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest() == row['source_sha256']
    model_oracle = json.loads((ROOT / 'tests/fixtures/offline/rest-acceptance/model-source-oracle.json').read_text())
    symbols = ('ModifyInterfaceObjectRule', 'ModifyInterfaceLogicRule', 'OntologyInterfaceObjectType',
               'ActionParameterV2', 'PropertyV2', 'ObjectTypeInterfaceImplementation',
               'InterfaceType', 'ApproximateDistinctAggregationV2', 'AggregationDurationGroupingV2',
               'CreateEdit', 'ObjectPrimaryKeyV2', 'StringValue', 'OntologyObjectV2',
               'OntologyValueType', 'StructConstraint')
    models = importlib.import_module('foundry_sdk.v2.ontologies.models')
    digest = hashlib.sha256(Path(models.__file__).read_bytes()).hexdigest()
    for symbol in symbols:
        assert model_oracle['symbols']['foundry_sdk.v2.ontologies.models.' + symbol]['source_sha256'] == digest


@pytest.mark.parametrize('operation', sorted(OPERATIONS))
def test_every_owned_operation_uses_real_sdk_without_network(operation):
    _, _, resource, method = operation.split('.')
    load(resource, method)['verify']()


@pytest.mark.parametrize('method', ('get', 'list'))
def test_action_rejects_summary_full_rule_contradiction(method):
    example = load('ActionTypeFullMetadata', method)
    value = example['SUCCESS'] if method == 'get' else example['SUCCESS']['data'][0]
    value['actionType']['operations'][0]['type'] = 'deleteInterfaceObject'
    with pytest.raises(AssertionError, match='summary/full rule mismatch'):
        example['verify']()


@pytest.mark.parametrize('fault', ('missing_parameter', 'parameter_type', 'undeclared_property'))
def test_action_arguments_resolve_to_typed_parameters(fault):
    example = load('ActionTypeFullMetadata', 'get')
    value = example['SUCCESS']
    if fault == 'missing_parameter':
        value['actionType']['parameters'].pop('target')
    elif fault == 'parameter_type':
        value['actionType']['parameters']['newName']['dataType'] = {'type': 'date'}
    else:
        value['fullLogicRules'][0]['sharedPropertyArguments']['absent'] = {'type': 'parameterId', 'parameterId': 'newName'}
    with pytest.raises((AssertionError, KeyError)):
        example['verify']()


@pytest.mark.parametrize('method', ('get_by_rid_batch', 'list', 'get_full_metadata'))
@pytest.mark.parametrize('selector', ('primaryKey', 'titleProperty'))
def test_object_schema_rejects_missing_identity_property(method, selector):
    example = load('ObjectType', method)
    value = example['SUCCESS']['objectType'] if method == 'get_full_metadata' else example['SUCCESS']['data'][0]
    value['properties'].pop(value[selector])
    with pytest.raises(AssertionError, match='identity property missing'):
        example['verify']()


@pytest.mark.parametrize('fault', ('api_name', 'interface_mapping', 'shared_mapping'))
def test_full_metadata_rejects_incoherent_identity_and_mapping(fault):
    example = load('ObjectType', 'get_full_metadata')
    value = example['SUCCESS']
    if fault == 'api_name':
        value['objectType']['apiName'] = 'Other'
    elif fault == 'interface_mapping':
        value['implementsInterfaces2'].clear()
    else:
        value['sharedPropertyTypeMapping']['name'] = 'absent'
    with pytest.raises(AssertionError):
        example['verify']()


@pytest.mark.parametrize('fault', ('empty_key', 'different_created_key', 'timestamp'))
def test_history_identifies_created_object(fault):
    example = load('ObjectType', 'get_edits_history')
    entry = example['SUCCESS']['data'][0]
    if fault == 'empty_key':
        entry['objectPrimaryKey'] = {}
    elif fault == 'different_created_key':
        entry['edit']['properties']['assetId'] = 'other'
    else:
        entry['timestamp'] = '2026-10-08T00:00:00+00:00'
    with pytest.raises(AssertionError):
        example['verify']()


@pytest.mark.parametrize('method', ('get', 'list'))
def test_interface_rejects_self_inheritance(method):
    example = load('OntologyInterface', method)
    value = example['SUCCESS'] if method == 'get' else example['SUCCESS']['data'][0]
    value['extendsInterfaces'] = value['allExtendsInterfaces'] = ['Trackable']
    with pytest.raises(AssertionError, match='inherit itself'):
        example['verify']()


@pytest.mark.parametrize('method', ('list_interface_linked_objects', 'list_objects_for_interface', 'search'))
@pytest.mark.parametrize('fault', ('empty', 'wrong_type', 'wrong_key'))
def test_interface_objects_have_business_identity(method, fault):
    example = load('OntologyInterface', method)
    obj = example['SUCCESS']['data'][0]
    if fault == 'empty':
        obj.clear()
    elif fault == 'wrong_type':
        obj['__apiName'] = 'Other'
    else:
        obj['__primaryKey'] = 'other'
    with pytest.raises(AssertionError):
        example['verify']()


@pytest.mark.parametrize('fault', ('missing_field', 'both_fields', 'unknown_field', 'wrong_duration_type', 'invalid_duration', 'metric_name'))
def test_aggregation_rejects_source_constraint_violations(fault):
    example = load('OntologyInterface', 'aggregate')
    body = copy.deepcopy(example['EXPECTED_BODY'])
    value = copy.deepcopy(example['SUCCESS'])
    if fault == 'missing_field':
        body['aggregation'][0].pop('field')
    elif fault == 'both_fields':
        body['aggregation'][0]['propertyIdentifier'] = {'type': 'property', 'apiName': 'assetId'}
    elif fault == 'unknown_field':
        body['aggregation'][0]['field'] = 'absent'
    elif fault == 'wrong_duration_type':
        body['groupBy'][0]['field'] = 'name'
    elif fault == 'invalid_duration':
        body['groupBy'][0].update(unit='MONTHS', value=2)
    else:
        value['data'][0]['metrics'][0]['name'] = 'other'
    with pytest.raises(AssertionError):
        example['check_aggregate'](body, value)


@pytest.mark.parametrize('method', ('get', 'list'))
def test_date_value_type_rejects_struct_constraint(method):
    example = load('OntologyValueType', method)
    value = example['SUCCESS'] if method == 'get' else example['SUCCESS']['data'][0]
    value['constraints'] = [{'type': 'struct', 'properties': {}}]
    with pytest.raises(AssertionError, match='no struct constraint'):
        example['verify']()


CASES = [tuple(identity.split('.')[2:]) for identity in sorted(OPERATIONS)]
MODES = ('ordinary', 'raw', 'stream')


def inputs(resource, method):
    """Use example inputs, with expected contracts derived separately from SDK source."""
    if (resource, method) == ('ObjectType', 'get'):
        return {'ontology': 'demo', 'object_type': 'Asset', 'branch': 'master', 'request_timeout': 30}
    class Capture:
        @property
        def with_raw_response(self):
            return self

        def __getattr__(self, name):
            return lambda **kwargs: kwargs

    return copy.deepcopy(load(resource, method)['invoke'](Capture()))


def success_payload(resource, method):
    namespace = load(resource, method)
    return namespace['ASSET' if (resource, method) == ('ObjectType', 'get') else 'SUCCESS']


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
        'query': evaluate(fields['query_params']),
        'body': evaluate(fields['body']),
        'response': evaluate(fields['response_type']),
        'errors': evaluate(fields['throwable_errors']),
        'iterator': evaluate(fields['response_mode']) == 'ITERATOR',
    }


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
    assert urllib.parse.unquote(request.url.path) == '/api' + source['path']
    assert request.headers['Authorization'] == 'Bearer offline-fixture-token'
    assert request.extensions['timeout']['read'] == 30
    for name, value in source['headers'].items():
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


@pytest.mark.parametrize('resource,method', CASES)
@pytest.mark.parametrize('mode', MODES)
@pytest.mark.parametrize('asynchronous', (False, True))
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


@pytest.mark.parametrize('resource,method', CASES)
@pytest.mark.parametrize('mode', MODES)
@pytest.mark.parametrize('asynchronous', (False, True))
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


@pytest.mark.parametrize('resource,method', CASES)
@pytest.mark.parametrize('mode', MODES)
@pytest.mark.parametrize('asynchronous', (False, True))
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


@pytest.mark.parametrize('resource,method', CASES)
@pytest.mark.parametrize('mode', MODES)
@pytest.mark.parametrize('asynchronous', (False, True))
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


@pytest.mark.parametrize('resource,method', PAGED_CASES)
@pytest.mark.parametrize('mode', MODES)
@pytest.mark.parametrize('asynchronous', (False, True))
def test_paging_crosses_empty_intermediate_page_and_stops_at_finite_end(
        resource, method, mode, asynchronous, offline_event_loop):
    source = source_contract(resource, method)
    arguments = inputs(resource, method)
    payload = success_payload(resource, method)
    expected = normalized(TypeAdapter(source['response']).validate_python(payload))['data']
    calls, responses = [], []

    def page(request):
        check_source_wire(source, request, paged=True)
        body = json.loads(request.content) if request.content else {}
        token = request.url.params.get('pageToken', body.get('pageToken'))
        calls.append(token)
        assert len(calls) <= 3, 'Caller page budget exceeded'
        assert calls == [None, 'empty-page', 'final-page'][:len(calls)]
        value = copy.deepcopy(payload)
        value.pop('nextPageToken', None)
        if len(calls) > 1:
            value['data'] = []
        if len(calls) < 3:
            value['nextPageToken'] = ('empty-page', 'final-page')[len(calls) - 1]
        response = httpx.Response(200, json=value)
        responses.append(response)
        return response

    if mode == 'ordinary' and source['iterator']:
        actual = normalized(exercise(resource, method, mode, asynchronous, page, offline_event_loop))
    else:
        actual = []
        for _ in range(3):
            result = exercise(resource, method, mode, asynchronous, page, offline_event_loop, arguments)
            value = json.loads(result) if mode == 'stream' else normalized(result)
            actual.extend(value['data'])
            token = value.get('nextPageToken')
            if token is None:
                break
            arguments['page_token'] = token
        else:
            pytest.fail('Pagination did not terminate within three pages')
    assert actual == expected
    assert calls == [None, 'empty-page', 'final-page']
    assert len(responses) == 3 and all(response.is_closed for response in responses)


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
                assert not body.closed and body.chunks_read == 1
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


@pytest.mark.parametrize('resource,method', [('ObjectType', 'get'), ('OntologyInterface', 'aggregate')])
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
        url = url.copy_with(path=url.path + '/incorrect')
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
