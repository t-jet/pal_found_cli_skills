"""v2.filesystem.Project.create_from_template: SDK request, decoded result and declared error fixtures.

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
from foundry_sdk.v2.filesystem.project import ProjectClient

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'common'))
from mock_transport import mock_resource

EXPECTED_METHOD = 'POST'
EXPECTED_PATH = '/api/v2/filesystem/projects/createFromTemplate'
EXPECTED_BODY = {'templateRid': 'ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001',
 'variableValues': {}}
EXPECTED_QUERY = {}
EXPECTED_HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json'}
SUCCESS = {'rid': 'ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001',
 'displayName': 'synthetic-value',
 'path': 'synthetic-value',
 'createdBy': '00000000-0000-0000-0000-000000000001',
 'updatedBy': '00000000-0000-0000-0000-000000000001',
 'createdTime': '2026-10-07T00:00:00+00:00',
 'updatedTime': '2026-10-07T00:00:00+00:00',
 'trashStatus': 'DIRECTLY_TRASHED',
 'spaceRid': 'ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001',
 'resourceLevelRoleGrantsAllowed': True}
ERRORS = [{'name': 'AddGroupToParentGroupPermissionDenied',
  'status': 403,
  'code': 'PERMISSION_DENIED',
  'parameters': {'parentGroupsWithoutPermission': ['ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001']}},
 {'name': 'CreateGroupPermissionDenied',
  'status': 403,
  'code': 'PERMISSION_DENIED',
  'parameters': {'organizationsWithoutPermission': ['ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001']}},
 {'name': 'CreateProjectFromTemplatePermissionDenied',
  'status': 403,
  'code': 'PERMISSION_DENIED',
  'parameters': {}},
 {'name': 'CreateProjectNoOwnerLikeRoleGrant',
  'status': 400,
  'code': 'INVALID_ARGUMENT',
  'parameters': {'grantedRoleIds': ['synthetic-value'],
                 'roleSetOwnerLikeRoleIds': ['synthetic-value']}},
 {'name': 'DefaultRolesNotInSpaceRoleSet',
  'status': 400,
  'code': 'INVALID_ARGUMENT',
  'parameters': {}},
 {'name': 'InvalidDefaultRoles', 'status': 400, 'code': 'INVALID_ARGUMENT', 'parameters': {}},
 {'name': 'InvalidDescription', 'status': 400, 'code': 'INVALID_ARGUMENT', 'parameters': {}},
 {'name': 'InvalidOrganizationHierarchy',
  'status': 400,
  'code': 'INVALID_ARGUMENT',
  'parameters': {'organizationRids': ['ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001']}},
 {'name': 'InvalidOrganizations', 'status': 400, 'code': 'INVALID_ARGUMENT', 'parameters': {}},
 {'name': 'InvalidPrincipalIdsForGroupTemplate',
  'status': 400,
  'code': 'INVALID_ARGUMENT',
  'parameters': {'invalidPrincipalIds': ['00000000-0000-0000-0000-000000000001']}},
 {'name': 'InvalidVariable',
  'status': 400,
  'code': 'INVALID_ARGUMENT',
  'parameters': {'templateVariableId': 'synthetic-value'}},
 {'name': 'InvalidVariableEnumOption',
  'status': 400,
  'code': 'INVALID_ARGUMENT',
  'parameters': {'variableId': 'synthetic-value',
                 'invalidOption': 'synthetic-value',
                 'validOptions': ['synthetic-value']}},
 {'name': 'MissingVariableValue',
  'status': 400,
  'code': 'INVALID_ARGUMENT',
  'parameters': {'templateVariableId': 'synthetic-value'}},
 {'name': 'NotAuthorizedToApplyOrganization',
  'status': 400,
  'code': 'INVALID_ARGUMENT',
  'parameters': {'organizationRids': ['ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001']}},
 {'name': 'OrganizationsNotFound',
  'status': 404,
  'code': 'NOT_FOUND',
  'parameters': {'organizationRids': ['ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001']}},
 {'name': 'ProjectNotFound',
  'status': 404,
  'code': 'NOT_FOUND',
  'parameters': {'projectRid': 'ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001'}},
 {'name': 'ProjectTemplateNotFound',
  'status': 404,
  'code': 'NOT_FOUND',
  'parameters': {'projectTemplateRid': 'ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001'}},
 {'name': 'TemplateGroupNameConflict',
  'status': 409,
  'code': 'CONFLICT',
  'parameters': {'conflictingGroupNames': ['synthetic-value']}},
 {'name': 'TemplateMarkingNameConflict',
  'status': 409,
  'code': 'CONFLICT',
  'parameters': {'conflictingMarkingNames': ['synthetic-value']}}]

def invoke(client):
    return client.with_raw_response.create_from_template(template_rid='ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001', variable_values={}, request_timeout=30)

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
    with mock_resource(ProjectClient, success) as client:
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
        with mock_resource(ProjectClient, failure) as client:
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
    print('v2.filesystem.Project.create_from_template' + ': serialized request, decoded result and ' + str(len(ERRORS)) + ' named errors passed')
