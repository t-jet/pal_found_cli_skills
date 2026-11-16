"""Legacy Ontology fixtures checked against SDK source and application schemas."""

import ast
import asyncio
import copy
import hashlib
import importlib
import importlib.metadata
import inspect
import json
import runpy
import socket
import textwrap
from functools import lru_cache
from pathlib import Path
from typing import Any, get_args, get_origin, get_type_hints

import httpx
import pytest
from foundry_sdk import PalantirRPCException, ReadTimeout
from foundry_sdk.v1.ontologies import models as v1
from foundry_sdk.v2.ontologies import models as v2
from pydantic import TypeAdapter

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.agents/skills/pal-found-dev/examples/rest/077/v1/ontologies'
ORACLE = json.loads((ROOT / 'tests/fixtures/offline/rest-acceptance/source-oracle.json').read_text())
CASES = [(path.parent.name, path.stem) for path in sorted(BASE.glob('*/*.py'))]


@pytest.fixture(autouse=True)
def deny_network(monkeypatch, offline_event_loop):
    def denied(*args, **kwargs):
        raise AssertionError('REST077 external network denied')

    for name in ('connect', 'connect_ex'):
        monkeypatch.setattr(socket.socket, name, denied)
    for name in ('create_connection', 'getaddrinfo', 'gethostbyname', 'gethostbyname_ex'):
        monkeypatch.setattr(socket, name, denied)
    monkeypatch.setattr(httpx.HTTPTransport, 'handle_request', denied)
    monkeypatch.setattr(httpx.AsyncHTTPTransport, 'handle_async_request', denied)


@pytest.fixture(scope='module')
def offline_event_loop():
    # Windows needs its local socket pair before network denial starts.
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


def example(resource, operation):
    return runpy.run_path(str(BASE / resource / (operation + '.py')))['verify'].__globals__


@pytest.mark.parametrize('resource,operation', CASES)
def test_each_example_uses_frozen_sdk_without_network(resource, operation):
    assert importlib.metadata.version('foundry-platform-sdk') == '1.101.0'
    identity = f'v1.ontologies.{resource}.{operation}'
    oracle = ORACLE['operations'][identity]
    source = importlib.import_module(oracle['module'])
    assert hashlib.sha256(Path(source.__file__).read_bytes()).hexdigest() == oracle['source_sha256']
    example(resource, operation)['verify']()


def test_schema_supports_search_aggregation_and_link_targets():
    schemas = example('ObjectType', 'list')['SUCCESS']['data']
    by_name = {schema['apiName']: v1.ObjectType.model_validate(schema) for schema in schemas}
    asset = by_name['Asset']
    assert asset.primary_key == ['assetId']
    assert asset.properties['status'].base_type == 'String'
    assert asset.properties['inspectionDate'].base_type == 'LocalDate'
    target = example('ObjectType', 'get_outgoing_link_type')['SUCCESS']
    facility = by_name[target['objectTypeApiName']]
    assert target['apiName'] == 'facility' and target['cardinality'] == 'ONE'
    assert facility.primary_key == ['facilityId']
    direct = example('OntologyObject', 'get')['SUCCESS']
    linked = example('OntologyObject', 'get_linked_object')['SUCCESS']
    assert direct['rid'] != linked['rid']
    assert linked['properties'][facility.primary_key[0]] == 'F-1'


def test_search_result_satisfies_source_defined_prefix_on_declared_property():
    assert 'starts with' in inspect.getdoc(v1.PrefixQuery)
    case = example('OntologyObject', 'search')
    schema = example('ObjectType', 'get')['SUCCESS']
    query = case['EXPECTED_BODY']['query']
    prefix, property_name = query['field'].split('.', 1)
    assert prefix == 'properties'
    assert schema['properties'][property_name]['baseType'] == 'String'
    for item in case['SUCCESS']['data']:
        assert item['properties'][property_name].startswith(query['value'])
        assert all(key in item['properties'] for key in schema['primaryKey'])


def test_duration_grouping_uses_date_and_numeric_named_metric():
    assert 'only on date types' in inspect.getdoc(v1.AggregationDurationGrouping)
    source = Path(v1.__file__).read_text()
    assert 'An ISO 8601 formatted duration' in source
    assert 'properties.{propertyApiName}' in source
    case = example('OntologyObject', 'aggregate')
    group = case['EXPECTED_BODY']['groupBy'][0]
    schema = example('ObjectType', 'get')['SUCCESS']
    assert schema['properties'][group['field'].removeprefix('properties.')]['baseType'] == 'LocalDate'
    assert group['duration'] == 'P1D'
    metric = case['EXPECTED_BODY']['aggregation'][0]
    bucket = case['SUCCESS']['data'][0]
    # This exact label/date pair belongs to the synthetic response fixture only.
    assert bucket['group'] == {'properties.inspectionDate': '2026-10-01'}
    assert bucket['metrics'][0] == {'name': metric['name'], 'value': 1.0}


@pytest.mark.parametrize('returned_group', [
    {'inspectionDate': '2026-10-01'},
    {'opaque-label': 17},
    {'opaque-label': None},
    {'opaque-label': {'synthetic': ['uninterpreted', 1]}},
    {'label-one': 'first', 'label-two': False},
    {},
])
def test_group_labels_and_values_roundtrip_without_request_field_mapping(monkeypatch, returned_group):
    group_type = get_type_hints(v1.AggregateObjectsResponseItem)['group']
    assert get_origin(group_type) is dict
    assert get_args(group_type) == (str, Any)
    case = example('OntologyObject', 'aggregate')
    fixture = copy.deepcopy(case['SUCCESS'])
    fixture['data'][0]['group'] = returned_group
    decoded = v1.AggregateObjectsResponse.model_validate(fixture).model_dump(
        mode='json', by_alias=True, exclude_none=True)
    actual_group = decoded['data'][0]['group']
    assert list(actual_group.items()) == list(returned_group.items())
    request_field = case['EXPECTED_BODY']['groupBy'][0]['field']
    assert request_field not in actual_group
    for confirmed_label, expected_value in returned_group.items():
        assert confirmed_label in actual_group
        assert actual_group[confirmed_label] == expected_value
    # Exercise the real SDK HTTP decoder and exact fixture comparison as well.
    monkeypatch.setitem(case, 'SUCCESS', fixture)
    case['verify']()


def test_query_metadata_matches_execution_inputs_and_result():
    query = example('QueryType', 'get')['SUCCESS']
    execution = example('Query', 'execute')
    assert query['apiName'] == execution['EXPECTED_PATH'].split('/')[-2]
    assert query['version'] == '1.2.3'
    assert set(execution['EXPECTED_BODY']['parameters']) == set(query['parameters'])
    assert set(execution['SUCCESS']['value']) == {field['name'] for field in query['output']['fields']}


def test_attachment_metadata_agrees_with_bytes_and_frozen_header_defect(monkeypatch):
    from foundry_sdk.v1.ontologies import attachment

    upload = example('Attachment', 'upload')
    requests = []
    original = upload['check_request']

    def capture(request):
        requests.append(request)
        original(request)

    monkeypatch.setitem(upload, 'check_request', capture)
    upload['verify']()
    request = requests[0]
    assert request.headers['Content-Type'] == '*/*'
    assert request.headers['Content-Length'] == str(len(request.content))
    metadata = upload['SUCCESS']
    assert metadata['filename'] == request.url.params['filename'] == 'inspection.txt'
    assert int(metadata['sizeBytes']) == len(request.content)
    assert metadata['mediaType'] == 'text/plain'
    assert request.content == example('Attachment', 'read')['SUCCESS']
    assert metadata == example('Attachment', 'get')['SUCCESS']
    tree = ast.parse(Path(attachment.__file__).read_text())
    duplicates = [node for node in ast.walk(tree) if isinstance(node, ast.Dict)
                  and sum(isinstance(key, ast.Constant) and key.value == 'Content-Type'
                          for key in node.keys) == 2]
    assert len(duplicates) == 2
    for headers in duplicates:
        values = [value for key, value in zip(headers.keys, headers.values)
                  if isinstance(key, ast.Constant) and key.value == 'Content-Type']
        assert isinstance(values[0], ast.Name) and values[0].id == 'content_type'
        assert ast.literal_eval(values[-1]) == '*/*'


def test_api_version_comparison_matches_source_models():
    from foundry_sdk.v1.ontologies.action import ActionClient as ActionV1
    from foundry_sdk.v2.ontologies.action import ActionClient as ActionV2

    assert 'title_property' not in v1.ObjectType.model_fields
    assert v2.ObjectTypeV2.model_fields['title_property'].alias == 'titleProperty'
    assert v2.ObjectTypeV2.model_fields['title_property'].is_required()
    primary_key_type = v1.ObjectType.model_fields['primary_key'].annotation
    assert get_origin(primary_key_type) is list and get_args(primary_key_type) == (str,)
    assert get_type_hints(v2.ObjectTypeV2)['primary_key'] is str
    assert 'ontology_rid' in inspect.signature(ActionV1.apply).parameters
    assert 'ontology' in inspect.signature(ActionV2.apply).parameters
    assert 'options' in inspect.signature(ActionV2.apply).parameters
    assert hasattr(ActionV1, 'validate') and not hasattr(ActionV2, 'validate')
    assert 'Object Storage V1' in inspect.getdoc(ActionV1.apply)
    assert 'Object Storage V2' in inspect.getdoc(ActionV1.apply)


MUTATIONS = [
    ('Attachment', 'get', ('mediaType',), 'synthetic-value'),
    ('Attachment', 'get', ('rid',), 'ri.synthetic.main.resource.00000000-0000-0000-0000-000000000099'),
    ('Attachment', 'upload', ('filename',), 'different.txt'),
    ('Attachment', 'upload', ('sizeBytes',), '1'),
    ('Attachment', 'upload', ('mediaType',), 'synthetic-value'),
    ('ObjectType', 'get', ('apiName',), 'WrongType'),
    ('ObjectType', 'get', ('primaryKey',), ['undefinedKey']),
    ('ObjectType', 'list', ('data', 0, 'properties', 'inspectionDate', 'baseType'), 'String'),
    ('OntologyObject', 'get', ('properties', 'assetId'), 'A-2'),
    ('OntologyObject', 'list', ('data', 0, 'properties', 'assetId'), 'A-2'),
    ('OntologyObject', 'get_linked_object', ('properties', 'facilityId'), 'F-2'),
    ('OntologyObject', 'list_linked_objects', ('data', 0, 'properties', 'facilityId'), 'F-2'),
    ('OntologyObject', 'search', ('data', 0, 'properties', 'status'), 'broken'),
    ('OntologyObject', 'aggregate', ('data', 0, 'metrics', 0, 'name'), 'wrongMetric'),
    ('OntologyObject', 'aggregate', ('data', 0, 'metrics', 0, 'value'), -1),
    ('QueryType', 'get', ('version',), 'synthetic-value'),
    ('QueryType', 'list', ('data', 0, 'version'), '1.2'),
]


@pytest.mark.parametrize('resource,operation,path,value', MUTATIONS)
def test_semantically_invalid_decodable_response_is_rejected(monkeypatch, resource, operation, path, value):
    case = example(resource, operation)
    result = copy.deepcopy(case['SUCCESS'])
    nested = result
    for key in path[:-1]:
        nested = nested[key]
    nested[path[-1]] = value
    monkeypatch.setitem(case, 'SUCCESS', result)
    with pytest.raises(AssertionError):
        case['verify']()


@pytest.mark.parametrize('operation,section,key,value', [
    ('aggregate', 'groupBy', 'field', 'properties.status'),
    ('aggregate', 'groupBy', 'duration', 'synthetic-value'),
    ('aggregate', 'aggregation', 'field', 'assetId'),
    ('search', 'query', 'field', 'status'),
])
def test_semantic_checker_rejects_invalid_request_even_if_mirrored(operation, section, key, value):
    case = example('OntologyObject', operation)
    body = copy.deepcopy(case['EXPECTED_BODY'])
    target = body[section][0] if isinstance(body[section], list) else body[section]
    target[key] = value
    request = httpx.Request('POST', 'https://offline.example.invalid', json=body)
    with pytest.raises(AssertionError):
        case['check_result'](case['SUCCESS'], request)


def operation_arguments(namespace):
    """Read adaptable example inputs; installed SDK remains the response oracle."""
    class Arguments:
        @property
        def with_raw_response(self):
            return self

        def __getattr__(self, name):
            return lambda **arguments: arguments

    return copy.deepcopy(namespace["invoke"](Arguments()))


def async_client(source):
    module = importlib.import_module(source["client"].__module__)
    return getattr(module, "Async" + source["client"].__name__)


def synthetic_response(payload):
    if isinstance(payload, bytes):
        return httpx.Response(200, content=payload)
    return httpx.Response(204) if payload is None else httpx.Response(200, json=payload)


@lru_cache
def contract(resource, operation):
    frozen = ORACLE['operations'][f'v1.ontologies.{resource}.{operation}']
    module = importlib.import_module(frozen['module'])
    assert hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest() == frozen['source_sha256']
    client = getattr(module, resource + 'Client')
    tree = ast.parse(textwrap.dedent(inspect.getsource(getattr(client, operation))))
    calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
             and isinstance(node.func, ast.Attribute) and node.func.attr == 'RequestInfo']
    assert len(calls) == 1
    fields = {kw.arg: kw.value for kw in calls[0].keywords}

    def value(node, arguments=None):
        return eval(compile(ast.Expression(node), '<installed SDK contract>', 'eval'),
                    vars(module), arguments or {})

    arguments = operation_arguments(example(resource, operation))
    return {
        'client': client,
        'method': value(fields['method']),
        'path': value(fields['resource_path']).format(**value(fields['path_params'], arguments)),
        'response': value(fields['response_type']),
        'errors': value(fields['throwable_errors']),
        'iterator': any(isinstance(node, ast.Constant) and node.value == 'ITERATOR'
                        for node in ast.walk(fields['response_mode'])),
    }


def normalized(value):
    if hasattr(value, 'model_dump'):
        return value.model_dump(mode='json', by_alias=True, exclude_none=True)
    if isinstance(value, (list, tuple)):
        return [normalized(item) for item in value]
    return value


def check_wire(source, request):
    assert request.method == source['method']
    assert request.url.path == '/api' + source['path']
    assert request.headers['Authorization'] == 'Bearer offline-fixture-token'
    assert request.extensions['timeout']['read'] == 30


async def consume_async(client, operation, arguments, mode, iterator):
    if mode == 'stream':
        async with getattr(client.with_streaming_response, operation)(**arguments) as response:
            return b''.join([chunk async for chunk in response.aiter_bytes()])
    target = client.with_raw_response if mode == 'raw' else client
    pending = getattr(target, operation)(**arguments)
    if mode == 'native' and iterator:
        assert hasattr(pending, '__aiter__') and not inspect.isawaitable(pending)
        return [normalized(row) async for row in pending]
    assert inspect.isawaitable(pending)
    result = await pending
    if mode == 'raw':
        try:
            assert not inspect.iscoroutinefunction(result.decode)
            return normalized(result.decode())
        finally:
            await result.aclose()
    return normalized(result)


def consume_sync(client, operation, arguments, mode, iterator):
    if mode == 'stream':
        with getattr(client.with_streaming_response, operation)(**arguments) as response:
            return b''.join(response.iter_bytes())
    target = client.with_raw_response if mode == 'raw' else client
    result = getattr(target, operation)(**arguments)
    if mode == 'native' and iterator:
        assert hasattr(result, '__next__')
        return [normalized(row) for row in result]
    if mode == 'raw':
        try:
            return normalized(result.decode())
        finally:
            result.close()
    return normalized(result)


def exercise_mode(resource, operation, mode, asynchronous, handler, loop):
    namespace = example(resource, operation)
    source = contract(resource, operation)
    arguments = operation_arguments(namespace)
    if asynchronous:
        async def run():
            mock_async = importlib.import_module('mock_transport').mock_async_resource
            async with mock_async(async_client(source), handler) as client:
                return await consume_async(client, operation, arguments, mode, source['iterator'])
        return loop.run_until_complete(run())
    with namespace['mock_resource'](source['client'], handler) as client:
        return consume_sync(client, operation, arguments, mode, source['iterator'])


@pytest.mark.parametrize('resource,operation', CASES)
@pytest.mark.parametrize('mode', ('native', 'raw', 'stream'))
@pytest.mark.parametrize('asynchronous', (False, True))
def test_every_source_mode_decodes_and_releases_response(
        resource, operation, mode, asynchronous, offline_event_loop):
    namespace = example(resource, operation)
    source = contract(resource, operation)
    responses = []

    def handler(request):
        check_wire(source, request)
        namespace['check_request'](request)
        response = synthetic_response(namespace['SUCCESS'])
        responses.append(response)
        return response

    result = exercise_mode(resource, operation, mode, asynchronous, handler, offline_event_loop)
    expected = normalized(TypeAdapter(source['response']).validate_python(namespace['SUCCESS']))
    if mode == 'stream':
        result = result if isinstance(expected, bytes) else json.loads(result)
    elif mode == 'native' and source['iterator']:
        expected = expected['data']
    assert result == expected
    assert len(responses) == 1 and responses[0].is_closed


@pytest.mark.parametrize('resource,operation', CASES)
@pytest.mark.parametrize('mode', ('native', 'raw', 'stream'))
@pytest.mark.parametrize('asynchronous', (False, True))
def test_declared_errors_and_generic_denial_stop_before_mock_effect(
        resource, operation, mode, asynchronous, offline_event_loop):
    namespace = example(resource, operation)
    source = contract(resource, operation)
    fixtures = {case['name']: case for case in namespace['ERRORS']}
    assert fixtures.keys() == source['errors'].keys()
    cases = [(case, source['errors'][name]) for name, case in fixtures.items()]
    cases.append(({'status': 403, 'code': 'PERMISSION_DENIED',
                   'name': 'PermissionDenied', 'parameters': {}}, PalantirRPCException))
    for case, error_type in cases:
        responses, effects = [], []

        def denied(request):
            check_wire(source, request)
            namespace['check_request'](request)
            response = httpx.Response(case['status'], json={
                'errorName': case['name'], 'errorCode': case['code'],
                'parameters': case['parameters'],
                'errorInstanceId': '00000000-0000-0000-0000-000000000004',
            })
            responses.append(response)
            if response.is_success:
                effects.append(request)
            return response

        with pytest.raises(error_type) as raised:
            exercise_mode(resource, operation, mode, asynchronous, denied, offline_event_loop)
        assert raised.value.name == case['name']
        assert normalized(raised.value.parameters) == case['parameters']
        assert raised.value.error_instance_id == '00000000-0000-0000-0000-000000000004'
        if case['name'] in source['errors']:
            assert type(raised.value) is error_type
        assert len(responses) == 1 and responses[0].is_closed and not effects


@pytest.mark.parametrize('resource,operation', CASES)
@pytest.mark.parametrize('mode', ('native', 'raw', 'stream'))
@pytest.mark.parametrize('asynchronous', (False, True))
def test_timeout_keeps_cause_without_repeating_uncertain_request(
        resource, operation, mode, asynchronous, offline_event_loop):
    calls = []

    def stalled(request):
        check_wire(contract(resource, operation), request)
        calls.append(request)
        raise httpx.ReadTimeout('Synthetic request deadline', request=request)

    with pytest.raises(ReadTimeout, match='Synthetic request deadline') as raised:
        exercise_mode(resource, operation, mode, asynchronous, stalled, offline_event_loop)
    assert isinstance(raised.value.__cause__, httpx.ReadTimeout)
    assert len(calls) == 1



STREAM_CASES = [case for case in CASES if contract(*case)["response"] is not None]
PAGED_CASES = [case for case in CASES
               if "page_token" in inspect.signature(getattr(contract(*case)["client"], case[1])).parameters]


class TrackedSyncStream(httpx.SyncByteStream):
    def __init__(self):
        self.chunks_read = 0
        self.closed = False

    def __iter__(self):
        for chunk in (b"part", b"two!", b"unread"):
            self.chunks_read += 1
            yield chunk

    def close(self):
        self.closed = True


class TrackedAsyncStream(httpx.AsyncByteStream):
    def __init__(self):
        self.chunks_read = 0
        self.closed = False

    async def __aiter__(self):
        for chunk in (b"part", b"two!", b"unread"):
            self.chunks_read += 1
            yield chunk

    async def aclose(self):
        self.closed = True


@pytest.mark.parametrize("resource,operation", STREAM_CASES)
@pytest.mark.parametrize("asynchronous", (False, True))
def test_stream_context_releases_response_when_caller_byte_budget_interrupts(
        resource, operation, asynchronous, offline_event_loop):
    namespace = example(resource, operation)
    source = contract(resource, operation)
    responses = []
    body = TrackedAsyncStream() if asynchronous else TrackedSyncStream()

    def handler(request):
        check_wire(source, request)
        assert request.extensions["timeout"]["read"] == 30
        response = httpx.Response(200, stream=body)
        assert not response.is_closed and not body.closed
        responses.append(response)
        return response

    arguments = operation_arguments(namespace)
    if asynchronous:
        async def exercise():
            mock_async = importlib.import_module("mock_transport").mock_async_resource
            async with mock_async(async_client(source), handler) as client:
                with pytest.raises(RuntimeError, match="Caller byte budget exhausted"):
                    async with getattr(client.with_streaming_response, operation)(**arguments) as response:
                        count = 0
                        async for chunk in response.aiter_bytes(chunk_size=4):
                            count += len(chunk)
                            if count > 4:
                                raise RuntimeError("Caller byte budget exhausted")
        offline_event_loop.run_until_complete(exercise())
    else:
        with namespace["mock_resource"](source["client"], handler) as client:
            with pytest.raises(RuntimeError, match="Caller byte budget exhausted"):
                with getattr(client.with_streaming_response, operation)(**arguments) as response:
                    count = 0
                    for chunk in response.iter_bytes(chunk_size=4):
                        count += len(chunk)
                        if count > 4:
                            raise RuntimeError("Caller byte budget exhausted")
    assert len(responses) == 1 and responses[0].is_closed
    assert body.closed and body.chunks_read == 2


@pytest.mark.parametrize('resource,operation', STREAM_CASES)
def test_async_cancellation_closes_stream_with_unread_bytes(
        resource, operation, offline_event_loop):
    namespace = example(resource, operation)
    source = contract(resource, operation)
    body = TrackedAsyncStream()
    responses = []

    def handler(request):
        check_wire(source, request)
        response = httpx.Response(200, stream=body)
        responses.append(response)
        return response

    async def exercise():
        mock_async = importlib.import_module('mock_transport').mock_async_resource
        started = asyncio.Event()
        hold_open = asyncio.Event()

        async def reader(client):
            async with getattr(client.with_streaming_response, operation)(
                    **operation_arguments(namespace)) as response:
                async for chunk in response.aiter_bytes(chunk_size=4):
                    assert chunk == b'part'
                    started.set()
                    await hold_open.wait()

        async with mock_async(async_client(source), handler) as client:
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

    offline_event_loop.run_until_complete(exercise())
    assert len(responses) == 1 and responses[0].is_closed
    assert body.closed and body.chunks_read == 1


@pytest.mark.parametrize("resource,operation", PAGED_CASES)
@pytest.mark.parametrize("asynchronous", (False, True))
def test_native_iterator_or_manual_response_pagination_stops_after_finite_final_page(
        resource, operation, asynchronous, offline_event_loop):
    namespace = example(resource, operation)
    source = contract(resource, operation)
    arguments = operation_arguments(namespace)
    calls, responses = [], []

    def handler(request):
        check_wire(source, request)
        body = json.loads(request.content) if request.content else {}
        token = request.url.params.get("pageToken", body.get("pageToken"))
        calls.append(token)
        assert calls == ([None] if len(calls) == 1 else [None, "next-fixture"])
        assert len(calls) <= 2, "Pagination must stop after the finite final page"
        assert request.extensions["timeout"]["read"] == 30
        payload = copy.deepcopy(namespace["SUCCESS"])
        if len(calls) == 1:
            payload["nextPageToken"] = "next-fixture"
        else:
            payload["data"] = []
            payload.pop("nextPageToken", None)
        response = httpx.Response(200, json=payload)
        responses.append(response)
        return response

    expected_rows = normalized(TypeAdapter(source["response"]).validate_python(namespace["SUCCESS"]))["data"]
    if asynchronous:
        async def exercise():
            mock_async = importlib.import_module("mock_transport").mock_async_resource
            async with mock_async(async_client(source), handler) as client:
                pending = getattr(client, operation)(**arguments)
                if hasattr(pending, "__aiter__"):
                    assert not inspect.isawaitable(pending)
                    return [normalized(row) async for row in pending]
                assert inspect.isawaitable(pending)
                first = await pending
                assert first.next_page_token == "next-fixture"
                second = await getattr(client, operation)(**dict(arguments, page_token=first.next_page_token))
                assert second.next_page_token is None
                return normalized(first.data + second.data)
        actual = offline_event_loop.run_until_complete(exercise())
    else:
        with namespace["mock_resource"](source["client"], handler) as client:
            first = getattr(client, operation)(**arguments)
            if hasattr(first, "__next__"):
                actual = [normalized(row) for row in first]
            else:
                assert first.next_page_token == "next-fixture"
                second = getattr(client, operation)(**dict(arguments, page_token=first.next_page_token))
                assert second.next_page_token is None
                actual = normalized(first.data + second.data)
    assert actual == expected_rows
    assert calls == [None, "next-fixture"] and all(response.is_closed for response in responses)


