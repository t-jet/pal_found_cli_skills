"""Declared synthetic schema for REST-079 fixtures; no tenant schema is implied.

Asset implements Trackable through shared properties. The checks below cover
relationships that SDK model decoding alone does not validate.
"""

from copy import deepcopy


ASSET = {
    'apiName': 'Asset', 'displayName': 'Asset', 'pluralDisplayName': 'Assets',
    'status': 'ACTIVE', 'rid': 'ri.ontology.main.object-type.asset',
    'icon': {'type': 'blueprint', 'name': 'cube', 'color': '#336699'},
    'primaryKey': 'assetId', 'titleProperty': 'name',
    'properties': {
        key: {'dataType': {'type': kind}, 'rid': 'ri.ontology.main.property.' + key}
        for key, kind in [('assetId', 'string'), ('name', 'string'), ('observedAt', 'timestamp')]
    },
}
SHARED_PROPERTIES = {
    key: {
        'rid': 'ri.ontology.main.shared-property.' + key,
        'apiName': key, 'displayName': key, 'dataType': deepcopy(prop['dataType']),
        'required': True, 'type': 'interfaceSharedPropertyType',
    }
    for key, prop in ASSET['properties'].items()
}
PEERS = {
    'rid': 'ri.ontology.main.interface-link-type.peers',
    'apiName': 'peers', 'displayName': 'Peer assets',
    'linkedEntityApiName': {'type': 'interfaceTypeApiName', 'apiName': 'Trackable'},
    'cardinality': 'MANY', 'required': True,
}
TRACKABLE = {
    'rid': 'ri.ontology.main.interface-type.trackable',
    'apiName': 'Trackable', 'displayName': 'Trackable',
    'properties': deepcopy(SHARED_PROPERTIES), 'allProperties': deepcopy(SHARED_PROPERTIES),
    'propertiesV2': deepcopy(SHARED_PROPERTIES),
    'allPropertiesV2': {
        key: {**{k: deepcopy(v) for k, v in prop.items() if k not in ('required', 'type')},
              'requireImplementation': True}
        for key, prop in SHARED_PROPERTIES.items()
    },
    'extendsInterfaces': [], 'allExtendsInterfaces': [],
    'implementedByObjectTypes': ['Asset'],
    'links': {'peers': deepcopy(PEERS)}, 'allLinks': {'peers': deepcopy(PEERS)},
}
ASSET_FULL = {
    'objectType': deepcopy(ASSET),
    'linkTypes': [{
        'apiName': 'relatedAssets', 'displayName': 'Related assets', 'status': 'ACTIVE',
        'objectTypeApiName': 'Asset', 'cardinality': 'MANY',
        'linkTypeRid': 'ri.ontology.main.link-type.related-assets',
    }],
    'implementsInterfaces': ['Trackable'],
    'implementsInterfaces2': {'Trackable': {
        'apiName': 'Trackable', 'rid': TRACKABLE['rid'],
        'properties': {key: key for key in SHARED_PROPERTIES},
        'propertiesV2': {key: {'type': 'localPropertyImplementation', 'propertyApiName': key}
                         for key in SHARED_PROPERTIES},
        'links': {'peers': ['relatedAssets']},
    }},
    'sharedPropertyTypeMapping': {key: key for key in SHARED_PROPERTIES},
}
RENAME_ACTION = {
    'actionType': {
        'apiName': 'rename-trackable', 'status': 'ACTIVE',
        'rid': 'ri.ontology.main.action-type.rename-trackable',
        'parameters': {
            'target': {'displayName': 'Target', 'required': True,
                       'dataType': {'type': 'interfaceObject', 'interfaceTypeApiName': 'Trackable'}},
            'newName': {'displayName': 'New name', 'required': True, 'dataType': {'type': 'string'}},
        },
        'operations': [{'type': 'modifyInterfaceObject', 'interfaceTypeApiName': 'Trackable'}],
    },
    'fullLogicRules': [{
        'type': 'modifyInterface', 'interfaceObjectToModify': 'target',
        'sharedPropertyArguments': {'name': {'type': 'parameterId', 'parameterId': 'newName'}},
        'structPropertyArguments': {},
    }],
}
OBSERVATION_DATE = {
    'apiName': 'ObservationDate', 'displayName': 'Observation date',
    'rid': 'ri.ontology.main.value-type.observation-date',
    'fieldType': {'type': 'date'}, 'version': '1', 'constraints': [],
}


def asset_object(key):
    return {'__apiName': 'Asset', '__primaryKey': key,
            '__rid': 'ri.phonograph2-objects.main.object.' + key,
            'assetId': key, 'name': 'Pump ' + key,
            'observedAt': '2026-10-07T00:00:00Z'}


def check_asset(value):
    assert value['apiName'] == 'Asset', 'Returned object type differs from requested Asset'
    for selector in ('primaryKey', 'titleProperty'):
        name = value[selector]
        assert name in value['properties'], 'Object identity property missing from schema'
        assert value['properties'][name]['dataType']['type'] == 'string'


def check_asset_full(value):
    check_asset(value['objectType'])
    assert set(value['implementsInterfaces']) == set(value['implementsInterfaces2']) == {'Trackable'}
    mapping = value['implementsInterfaces2']['Trackable']
    for shared, definition in TRACKABLE['properties'].items():
        local = mapping['properties'][shared]
        assert local in value['objectType']['properties'], 'Interface mapping has no backing property'
        assert value['sharedPropertyTypeMapping'][shared] == local
        assert mapping['propertiesV2'][shared]['propertyApiName'] == local
        assert value['objectType']['properties'][local]['dataType'] == definition['dataType']
    assert mapping['links']['peers'] == ['relatedAssets']
    assert any(link['apiName'] == 'relatedAssets' and link['objectTypeApiName'] == 'Asset'
               for link in value['linkTypes'])


def check_action(value):
    summary = value['actionType']
    assert summary['apiName'] == 'rename-trackable'
    rule, = value['fullLogicRules']
    operation, = summary['operations']
    # Summary and full rule use different discriminator names in SDK 1.101.0.
    assert operation['type'] == 'modifyInterfaceObject' and rule['type'] == 'modifyInterface', 'Action summary/full rule mismatch'
    parameter = summary['parameters'][rule['interfaceObjectToModify']]
    assert parameter['required'] and parameter['dataType'] == {
        'type': 'interfaceObject', 'interfaceTypeApiName': operation['interfaceTypeApiName']}
    assert operation['interfaceTypeApiName'] == TRACKABLE['apiName']
    for property_name, argument in rule['sharedPropertyArguments'].items():
        assert property_name in TRACKABLE['properties']
        assert argument['type'] == 'parameterId'
        assert summary['parameters'][argument['parameterId']]['dataType'] == TRACKABLE['properties'][property_name]['dataType']
    assert rule['sharedPropertyArguments'], 'Rename rule must change a declared property'


def check_interface(value):
    assert value['apiName'] == 'Trackable'
    assert value['apiName'] not in value['allExtendsInterfaces'], 'Interface cannot inherit itself'
    assert value['apiName'] not in value['extendsInterfaces'], 'Interface cannot inherit itself'
    assert value['extendsInterfaces'] == value['allExtendsInterfaces'] == []
    assert value['properties'] == value['allProperties'] == SHARED_PROPERTIES
    assert set(value['propertiesV2']) == set(value['allPropertiesV2']) == set(SHARED_PROPERTIES)
    assert value['implementedByObjectTypes'] == ['Asset']


def check_objects(value, linked=False):
    assert value['data'], 'Fixture must demonstrate an identified object'
    for obj in value['data']:
        assert obj.get('__apiName') in TRACKABLE['implementedByObjectTypes'], 'Missing or wrong object type'
        assert obj.get('__primaryKey') and obj['__primaryKey'] == obj.get(ASSET['primaryKey']), 'Missing or inconsistent primary key'
        assert obj.get(ASSET['titleProperty']), 'Selected title property missing'
        assert obj.get('observedAt'), 'Selected timestamp missing'
        if linked:
            assert obj['__primaryKey'] != 'A-1', 'Peer fixture must identify linked target A-2'


def check_aggregate(body, value):
    for item in body['aggregation'] + body['groupBy']:
        assert ('field' in item) != ('propertyIdentifier' in item), 'Supply exactly one field/propertyIdentifier'
        field = item.get('field') or item['propertyIdentifier']['apiName']
        assert field in TRACKABLE['properties'], 'Aggregation field absent from interface'
        if item['type'] == 'duration':
            assert TRACKABLE['properties'][field]['dataType']['type'] in ('date', 'timestamp'), 'Duration requires date/timestamp'
            if item['unit'] in ('YEARS', 'QUARTERS', 'MONTHS', 'WEEKS'):
                assert item['value'] == 1
    metric, = value['data'][0]['metrics']
    assert metric['name'] == body['aggregation'][0]['name'], 'Metric name differs from request'
    assert metric['value'] == 1
    assert set(value['data'][0]['group']) == {'observedAt'}


def check_value_type(value):
    assert value['apiName'] == 'ObservationDate'
    assert value['fieldType']['type'] == 'date'
    assert value['constraints'] == [], 'Date fixture has no struct constraint'


def check_history(value):
    assert value['data'], 'Fixture must identify a created object'
    for entry in value['data']:
        assert entry['timestamp'] == '2026-10-07T00:00:00+00:00', 'History timestamp differs from fixture event'
        assert set(entry['objectPrimaryKey']) == {ASSET['primaryKey']}, 'History must identify Asset key'
        assert entry['edit']['type'] == 'createEdit'
        for key, primary in entry['objectPrimaryKey'].items():
            assert primary['type'] == ASSET['properties'][key]['dataType']['type'] + 'Value'
            assert primary['value'] and entry['edit']['properties'][key] == primary['value'], 'Created properties/key mismatch'
        assert entry['edit']['properties'][ASSET['titleProperty']]
