"""v2.admin.UserProviderInfo.get: SDK request, decoded result and declared error fixtures.

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
from foundry_sdk.v2.admin.user_provider_info import UserProviderInfoClient

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'common'))
from mock_transport import mock_resource

EXPECTED_METHOD = 'GET'
EXPECTED_PATH = '/api/v2/admin/users/00000000-0000-0000-0000-000000000001/providerInfo'
EXPECTED_BODY = None
EXPECTED_QUERY = {}
EXPECTED_HEADERS = {'Accept': 'application/json'}
SUCCESS = {'providerId': 'synthetic-value'}
ERRORS = [{'name': 'GetUserProviderInfoPermissionDenied',
  'status': 403,
  'code': 'PERMISSION_DENIED',
  'parameters': {'userId': '00000000-0000-0000-0000-000000000001'}},
 {'name': 'UserDeleted',
  'status': 400,
  'code': 'INVALID_ARGUMENT',
  'parameters': {'principalId': '00000000-0000-0000-0000-000000000001'}},
 {'name': 'UserNotFound',
  'status': 404,
  'code': 'NOT_FOUND',
  'parameters': {'userId': '00000000-0000-0000-0000-000000000001'}},
 {'name': 'UserProviderInfoNotFound',
  'status': 404,
  'code': 'NOT_FOUND',
  'parameters': {'userId': '00000000-0000-0000-0000-000000000001'}}]

def invoke(client):
    return client.with_raw_response.get(user_id='00000000-0000-0000-0000-000000000001', request_timeout=30)

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
    with mock_resource(UserProviderInfoClient, success) as client:
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
        with mock_resource(UserProviderInfoClient, failure) as client:
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
    print('v2.admin.UserProviderInfo.get' + ': serialized request, decoded result and ' + str(len(ERRORS)) + ' named errors passed')
