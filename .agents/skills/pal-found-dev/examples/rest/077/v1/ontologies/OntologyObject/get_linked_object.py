"""v1.ontologies.OntologyObject.get_linked_object: SDK request, decoded result and declared error fixtures.

Synthetic identifiers do not name tenant resources. Prepared SDK 1.101.0/httpx
required. No network connections or live mutations occur.
"""
import json
import sys
import urllib.parse
import datetime
from pathlib import Path

import httpx
from foundry_sdk import PalantirRPCException
from foundry_sdk.v1.ontologies.ontology_object import OntologyObjectClient

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'common'))
from mock_transport import mock_resource

EXPECTED_METHOD = 'GET'
EXPECTED_PATH = '/api/v1/ontologies/ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001/objects/Asset/A-1/links/synthetic-value/synthetic-value'
EXPECTED_BODY = None
EXPECTED_QUERY = {'properties': None}
EXPECTED_HEADERS = {'Accept': 'application/json'}
SUCCESS = {'properties': {'assetId': 'A-1', 'status': 'ready'},
 'rid': 'ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001'}
ERRORS = []

def invoke(client):
    return client.with_raw_response.get_linked_object(ontology_rid='ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001', object_type='Asset', primary_key='A-1', link_type='synthetic-value', linked_object_primary_key='synthetic-value', request_timeout=30)

def check_request(request):
    assert request.method == EXPECTED_METHOD
    assert urllib.parse.unquote(request.url.path) == EXPECTED_PATH
    assert request.headers['Authorization'] == 'Bearer offline-fixture-token'
    for key, value in EXPECTED_HEADERS.items():
        if value is None:
            assert key not in request.headers
        else:
            assert request.headers[key] == str(value)
    expected = httpx.QueryParams({key: value for key,value in EXPECTED_QUERY.items() if value is not None})
    assert sorted(request.url.params.multi_items()) == sorted(expected.multi_items())
    if isinstance(EXPECTED_BODY, bytes):
        assert request.content == EXPECTED_BODY
    elif EXPECTED_BODY is not None:
        assert json.loads(request.content) == EXPECTED_BODY

def normalized(value):
    if isinstance(value, dict):
        return {key: normalized(child) for key,child in value.items()}
    if isinstance(value, (list, tuple)):
        return [normalized(child) for child in value]
    if isinstance(value, (datetime.datetime, datetime.date)):
        return value.isoformat()
    if isinstance(value, bytes):
        return bytes(value)
    if hasattr(value, 'model_dump'):
        return value.model_dump(mode='json', by_alias=True, exclude_none=True)
    return value

def verify():
    calls = []
    def success(request):
        check_request(request)
        calls.append(True)
        if isinstance(SUCCESS, bytes):
            return httpx.Response(200, content=SUCCESS)
        if SUCCESS is None:
            return httpx.Response(204)
        return httpx.Response(200, json=SUCCESS)
    with mock_resource(OntologyObjectClient, success) as client:
        raw = invoke(client)
        try:
            assert normalized(raw.decode()) == SUCCESS
        finally:
            raw.close()
    assert len(calls) == 1
    for error_case in ERRORS:
        def failure(request):
            check_request(request)
            return httpx.Response(error_case['status'], json={
                'errorName':error_case['name'], 'errorCode':error_case['code'],
                'parameters':error_case['parameters'],
                'errorInstanceId':'00000000-0000-0000-0000-000000000004',
            })
        with mock_resource(OntologyObjectClient, failure) as client:
            try:
                raw = invoke(client)
                raw.close()
            except PalantirRPCException as error:
                assert error.name == error_case['name']
                assert type(error).__name__ == error_case['name']
                assert normalized(error.parameters) == error_case['parameters']
            else:
                raise AssertionError('Expected ' + error_case['name'])

if __name__ == '__main__':
    verify()
    print('v1.ontologies.OntologyObject.get_linked_object' + ': serialized request, decoded result and ' + str(len(ERRORS)) + ' named errors passed')
