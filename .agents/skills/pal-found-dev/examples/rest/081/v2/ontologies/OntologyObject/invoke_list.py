"""v2.ontologies.OntologyObject.list: SDK request, decoded result and declared error fixtures.

Identifiers and records follow Palantir's illustrative API examples.
Source: https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-objects/list-objects
Prepared SDK 1.101.0/httpx required. No network or live mutations occur.
"""
import json
import sys
import urllib.parse
import datetime
from pathlib import Path

import httpx
from foundry_sdk import BadRequestError, PalantirRPCException
from foundry_sdk.v2.ontologies.ontology_object import OntologyObjectClient

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'common'))
from mock_transport import mock_resource

EXPECTED_METHOD = 'GET'
EXPECTED_PATH = '/api/v2/ontologies/palantir/objects/employee'
EXPECTED_BODY = None
EXPECTED_QUERY = {'branch': None,
 'excludeRid': None,
 'orderBy': None,
 'pageSize': 100,
 'pageToken': None,
 'sdkPackageRid': None,
 'sdkVersion': None,
 'select': None,
 'snapshot': None}
EXPECTED_HEADERS = {'Accept': 'application/json'}
SUCCESS = {'data': [{'__rid': 'ri.phonograph2-objects.main.object.88a6fccb-f333-46d6-a07e-7725c5f18b61', '__primaryKey': 50030, '__apiName': 'Employee', 'id': 50030, 'firstName': 'John', 'lastName': 'Doe'}], 'nextPageToken': 'employee-page-2', 'totalCount': '2'}
PAGE_TWO = {'data': [{'__rid': 'ri.phonograph2-objects.main.object.dcd887d1-c757-4d7a-8619-71e6ec2c25ab', '__primaryKey': 20090, '__apiName': 'Employee', 'id': 20090, 'firstName': 'John', 'lastName': 'Haymore'}], 'totalCount': '2'}
ERRORS = [{'status': 400, 'name': 'ObjectsExceededLimit', 'code': 'INVALID_ARGUMENT', 'parameters': {}}]

def invoke(client, page_token=None):
    return client.with_raw_response.list(ontology='palantir', object_type='employee', page_size=100, page_token=page_token, request_timeout=30)

def check_request(request, page_token=None):
    assert request.method == EXPECTED_METHOD
    assert urllib.parse.unquote(request.url.path) == EXPECTED_PATH
    assert request.headers['Authorization'] == 'Bearer offline-fixture-token'
    for key, value in EXPECTED_HEADERS.items():
        if value is None:
            assert key not in request.headers
        else:
            assert request.headers[key] == str(value)
    expected_query = {**EXPECTED_QUERY, 'pageToken': page_token}
    expected = httpx.QueryParams({key: value for key,value in expected_query.items() if value is not None})
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
            decoded = normalized(raw.decode())
            assert decoded == SUCCESS
        finally:
            raw.close()
    assert len(calls) == 1
    assert decoded['data'][0]['__primaryKey'] == 50030
    assert decoded['data'][0]['__apiName'] == 'Employee'
    token = decoded['nextPageToken']
    def next_page(request):
        check_request(request, token)
        return httpx.Response(200, json=PAGE_TWO)
    with mock_resource(OntologyObjectClient, next_page) as client:
        raw = invoke(client, token)
        try:
            decoded_second_page = normalized(raw.decode())
            assert decoded_second_page == PAGE_TWO
        finally:
            raw.close()
    assert decoded_second_page['data'][0]['__primaryKey'] == 20090
    assert decoded_second_page['data'][0]['__apiName'] == 'Employee'
    assert 'nextPageToken' not in decoded_second_page
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
                assert type(error) is BadRequestError
                assert error.error_code == error_case['code']
                assert normalized(error.parameters) == error_case['parameters']
            else:
                raise AssertionError('Expected ' + error_case['name'])

if __name__ == '__main__':
    verify()
    print('v2.ontologies.OntologyObject.list' + ': serialized request, decoded result and ' + str(len(ERRORS)) + ' named errors passed')
