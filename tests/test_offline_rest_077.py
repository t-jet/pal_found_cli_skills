"""Legacy Ontology fixtures checked against SDK source and application schemas."""

import ast
import copy
import hashlib
import importlib
import importlib.metadata
import inspect
import json
import runpy
import socket
from pathlib import Path
from typing import Any, get_args, get_origin, get_type_hints

import httpx
import pytest
from foundry_sdk.v1.ontologies import models as v1
from foundry_sdk.v2.ontologies import models as v2

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.agents/skills/pal-found-dev/examples/rest/077/v1/ontologies'
ORACLE = json.loads((ROOT / 'tests/fixtures/offline/rest-acceptance/source-oracle.json').read_text())
CASES = [(path.parent.name, path.stem) for path in sorted(BASE.glob('*/*.py'))]


@pytest.fixture(autouse=True)
def deny_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError('REST077 external network denied')

    for name in ('connect', 'connect_ex'):
        monkeypatch.setattr(socket.socket, name, denied)
    for name in ('create_connection', 'getaddrinfo', 'gethostbyname', 'gethostbyname_ex'):
        monkeypatch.setattr(socket, name, denied)
    monkeypatch.setattr(httpx.HTTPTransport, 'handle_request', denied)
    monkeypatch.setattr(httpx.AsyncHTTPTransport, 'handle_async_request', denied)


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
