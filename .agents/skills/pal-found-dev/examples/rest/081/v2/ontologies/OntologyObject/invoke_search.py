"""v2.ontologies.OntologyObject.search: SDK request, decoded result and declared error fixtures.

Identifiers and records follow Palantir's illustrative API examples.
Source: https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-objects/search-objects
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

EXPECTED_METHOD = 'POST'
EXPECTED_PATH = '/api/v2/ontologies/palantir/objects/employee/search'
EXPECTED_BODY = {'select': ['employeeId', 'lastName', 'firstName', 'age'], 'where': {'type': 'eq', 'field': 'age', 'value': 21}}
EXPECTED_QUERY = {'branch': None, 'executeInMemoryOnly': None, 'sdkPackageRid': None, 'sdkVersion': None}
EXPECTED_HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json'}
SUCCESS = {'data': [{'__rid': 'ri.phonograph2-objects.main.object.5b5dbc28-7f05-4e83-a33a-1e5b851ababb', '__primaryKey': 1000, '__apiName': 'Employee', 'employeeId': 1000, 'lastName': 'smith', 'firstName': 'john', 'age': 21}], 'totalCount': '1'}
ERRORS = [{'status': 400, 'name': 'PropertiesNotSearchable', 'code': 'INVALID_ARGUMENT', 'parameters': {'properties': ['age']}}]

def invoke(client):
    return client.with_raw_response.search(ontology='palantir', object_type='employee', select=['employeeId', 'lastName', 'firstName', 'age'], where={'type': 'eq', 'field': 'age', 'value': 21}, request_timeout=30)

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
            decoded = normalized(raw.decode())
            assert decoded == SUCCESS
        finally:
            raw.close()
    assert len(calls) == 1
    assert decoded['data'][0]['__primaryKey'] == 1000
    assert decoded['data'][0]['__apiName'] == 'Employee'
    assert decoded['data'][0]['age'] == EXPECTED_BODY['where']['value']
    assert decoded['totalCount'] == '1' and 'nextPageToken' not in decoded
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
    print('v2.ontologies.OntologyObject.search' + ': serialized request, decoded result and ' + str(len(ERRORS)) + ' named errors passed')
