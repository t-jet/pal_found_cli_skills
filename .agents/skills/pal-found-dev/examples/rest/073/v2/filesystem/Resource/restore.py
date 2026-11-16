"""v2.filesystem.Resource.restore: SDK request, decoded result and declared error fixtures.

Synthetic identifiers do not name tenant resources. Prepared SDK 1.101.0/httpx
required. No network connections or live mutations occur.
"""
import json
import sys
import urllib.parse
import datetime
from pathlib import Path

import httpx
from foundry_sdk import PalantirRPCException, TimeoutError as SDKTimeoutError
from foundry_sdk.v2.filesystem.resource import ResourceClient
from foundry_sdk.v2.filesystem.errors import ResourceNotDirectlyTrashed

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'common'))
from mock_transport import mock_resource

EXPECTED_METHOD = 'POST'
EXPECTED_PATH = '/api/v2/filesystem/resources/ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001/restore'
EXPECTED_BODY = None
EXPECTED_QUERY = {}
EXPECTED_HEADERS = {}
SUCCESS = None
ERRORS = [{'name': 'ResourceNotDirectlyTrashed',
  'status': 400,
  'code': 'INVALID_ARGUMENT',
  'parameters': {'resourceRid': 'ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001'}},
 {'name': 'ResourceNotFound',
  'status': 404,
  'code': 'NOT_FOUND',
  'parameters': {'resourceRid': 'ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001'}},
 {'name': 'RestoreResourcePermissionDenied',
  'status': 403,
  'code': 'PERMISSION_DENIED',
  'parameters': {'resourceRid': 'ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001'}}]

def invoke(client):
    return client.with_raw_response.restore(resource_rid='ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001', request_timeout=30)

def check_request(request):
    assert request.method == EXPECTED_METHOD
    assert urllib.parse.unquote(request.url.path) == EXPECTED_PATH
    assert request.headers['Authorization'] == 'Bearer offline-fixture-token'
    assert request.content == b''
    assert request.extensions['timeout'] == dict.fromkeys(('connect', 'read', 'write', 'pool'), 30)
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


def restore_once(client, resource_rid, *, expected_parent_rid, expected_path):
    """Use only with an authorized identity and owner-confirmed RID/parent/path.

    At most one restore and two reads. Read failures propagate: stop and ask an
    authorized owner to reconcile access/state. No path lookup or ancestor write
    is performed. The SDK's active-resource no-op prose conflicts with its
    ResourceNotDirectlyTrashed declaration; this example promises neither server
    policy nor idempotency. A timeout can leave the write outcome unknown.
    """
    def inspect_state():
        resource = client.get(resource_rid, request_timeout=30)
        if (resource.rid != resource_rid
                or resource.parent_folder_rid != expected_parent_rid
                or resource.path != expected_path):
            return 'STOP: reconcile RID, parent and path with authorized owner'
        return resource.trash_status

    before = inspect_state()
    if before == 'NOT_TRASHED':
        return 'Desired state observed; no restore sent'
    if before == 'ANCESTOR_TRASHED':
        return 'STOP: authorized owner must reconcile original folder restoration'
    if before != 'DIRECTLY_TRASHED':
        return before if before.startswith('STOP:') else 'STOP: unknown trash status'

    # Other SDK errors propagate and stop. In particular ResourceNotFound and
    # RestoreResourcePermissionDenied do not authorize a different RID or identity.
    try:
        result = client.restore(resource_rid, request_timeout=30)
        assert result is None  # 204 contains no restored Resource or hierarchy.
    except (ResourceNotDirectlyTrashed, SDKTimeoutError):
        pass  # Reconcile once; never replay this mutation automatically.

    after = inspect_state()
    if after == 'NOT_TRASHED':
        return 'Desired state observed after attempt; no replay'
    if after == 'ANCESTOR_TRASHED':
        return 'STOP: authorized owner must reconcile original folder restoration'
    if after == 'DIRECTLY_TRASHED':
        return 'STOP: still directly trashed; reconcile outcome/policy with authorized owner'
    return after if after.startswith('STOP:') else 'STOP: unknown trash status'

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
    with mock_resource(ResourceClient, success) as client:
        raw = invoke(client)
        try:
            assert raw.status_code == 204
            assert normalized(raw.decode()) == SUCCESS
        finally:
            raw.close()
        assert raw._response.is_closed
    assert len(calls) == 1
    for error_case in ERRORS:
        def failure(request):
            check_request(request)
            return httpx.Response(error_case['status'], json={
                'errorName':error_case['name'], 'errorCode':error_case['code'],
                'parameters':error_case['parameters'],
                'errorInstanceId':'00000000-0000-0000-0000-000000000004',
            })
        with mock_resource(ResourceClient, failure) as client:
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
    print('v2.filesystem.Resource.restore' + ': serialized request, decoded result and ' + str(len(ERRORS)) + ' named errors passed')
