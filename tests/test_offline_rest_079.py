"""REST-079 SDK transport and cross-field semantic regression checks."""

import copy
import hashlib
import importlib
import json
import runpy
import socket
from pathlib import Path

import pytest


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


@pytest.fixture(autouse=True)
def deny_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError('Public socket/DNS access denied in REST-079 tests')

    for name in ('connect', 'connect_ex'):
        monkeypatch.setattr(socket.socket, name, denied)
    for name in ('create_connection', 'getaddrinfo', 'gethostbyname', 'gethostbyname_ex'):
        monkeypatch.setattr(socket, name, denied)


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
