"""Synthetic ObjectType metadata; actual SDK decoding, no enrollment access."""

import sys
from pathlib import Path

import httpx
from foundry_sdk.v2.ontologies.object_type import ObjectTypeClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'common'))
from mock_transport import mock_resource

ASSET = {
    'apiName': 'Asset', 'displayName': 'Asset', 'pluralDisplayName': 'Assets',
    'status': 'ACTIVE', 'rid': 'ri.ontology.main.object-type.asset',
    'icon': {'type': 'blueprint', 'name': 'cube', 'color': '#336699'},
    'primaryKey': 'assetId', 'titleProperty': 'assetId',
    'properties': {
        'assetId': {'dataType': {'type': 'string'}, 'rid': 'ri.ontology.main.property.asset-id'},
        'status': {'dataType': {'type': 'string'}, 'rid': 'ri.ontology.main.property.asset-status'},
    },
}


def verify():
    def serve(request):
        assert request.method == 'GET'
        assert request.url.path == '/api/v2/ontologies/demo/objectTypes/Asset'
        assert request.url.params['branch'] == 'master'
        return httpx.Response(200, json=ASSET)

    with mock_resource(ObjectTypeClient, serve) as client:
        result = client.get('demo', 'Asset', branch='master', request_timeout=30)
        assert result.api_name == 'Asset'
        assert result.primary_key == 'assetId'
        assert result.primary_key in result.properties
        assert result.properties['assetId'].data_type.type == 'string'
        assert result.title_property in result.properties


if __name__ == '__main__':
    verify()
    print('Asset identity/key/property metadata decoded through SDK; no live schema checked.')
