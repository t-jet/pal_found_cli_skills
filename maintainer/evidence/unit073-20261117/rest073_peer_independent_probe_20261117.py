"""Independent native-SDK wire controls and fault tests for UNITTEST-067."""
import ast
import asyncio
import datetime
import hashlib
import importlib.util
import json
import re
import socket
import subprocess
from collections import Counter
from pathlib import Path
from unittest.mock import patch
from urllib.parse import quote

import httpx
from foundry_sdk import PalantirRPCException

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / '.ept/tmp/feature015_rest073_unit_modes_20261117'
TEST = WORK / 'tests/test_offline_rest_073.py'
EXPECTED_SHA = 'd61e7750211d7ef7bb688c46579e75ed732a340e5ccbe71cfe13a9894feece17'
TAG = '168d51910570b6966afa2320333ab36f6a3f7ccf'
SDK = ROOT / '.ept/docs/customer_input/foundry-platform-python'
REPORT = ROOT / '.ept/tmp/rest073_peer_independent_probe_20261117.json'

# Literal route expectations transcribed from frozen SDK resource source.
ROUTES = {
    'v2.audit.LogFile': ('/audit/organizations/{organization_rid}/logFiles', {
        'content': ('GET', '/{log_file_id}/content'), 'list': ('GET', '')}),
    'v2.filesystem.Folder': ('/filesystem/folders', {
        'children': ('GET', '/{folder_rid}/children'), 'create': ('POST', ''),
        'get': ('GET', '/{folder_rid}'), 'get_batch': ('POST', '/getBatch'),
        'replace': ('PUT', '/{folder_rid}')}),
    'v2.filesystem.Project': ('/filesystem/projects', {
        'add_organizations': ('POST', '/{project_rid}/addOrganizations'),
        'create': ('POST', '/create'), 'create_from_template': ('POST', '/createFromTemplate'),
        'get': ('GET', '/{project_rid}'), 'organizations': ('GET', '/{project_rid}/organizations'),
        'remove_organizations': ('POST', '/{project_rid}/removeOrganizations'),
        'replace': ('PUT', '/{project_rid}')}),
    'v2.filesystem.ProjectResourceReference': ('/filesystem/projects/{project_rid}/references', {
        'add': ('POST', '/add'), 'list': ('GET', ''), 'remove': ('POST', '/remove')}),
    'v2.filesystem.Resource': ('/filesystem/resources', {
        'add_markings': ('POST', '/{resource_rid}/addMarkings'), 'delete': ('DELETE', '/{resource_rid}'),
        'get': ('GET', '/{resource_rid}'), 'get_access_requirements': ('GET', '/{resource_rid}/getAccessRequirements'),
        'get_batch': ('POST', '/getBatch'), 'get_by_path': ('GET', '/getByPath'),
        'get_by_path_batch': ('POST', '/getByPathBatch'), 'markings': ('GET', '/{resource_rid}/markings'),
        'permanently_delete': ('POST', '/{resource_rid}/permanentlyDelete'),
        'remove_markings': ('POST', '/{resource_rid}/removeMarkings'), 'restore': ('POST', '/{resource_rid}/restore')}),
    'v2.filesystem.ResourceRole': ('/filesystem/resources/{resource_rid}/roles', {
        'add': ('POST', '/add'), 'list': ('GET', ''), 'remove': ('POST', '/remove')}),
    'v2.filesystem.ResourceTag': ('/filesystem/resources/{resource_rid}/tags', {
        'add': ('POST', '/add'), 'list': ('GET', ''), 'remove': ('POST', '/remove')}),
    'v2.filesystem.Space': ('/filesystem/spaces', {
        'create': ('POST', ''), 'delete': ('DELETE', '/{space_rid}'), 'get': ('GET', '/{space_rid}'),
        'list': ('GET', ''), 'replace': ('PUT', '/{space_rid}')}),
    'v2.third_party_applications.ThirdPartyApplication': ('/thirdPartyApplications/{third_party_application_rid}', {
        'get': ('GET', '')}),
    'v2.third_party_applications.Version': ('/thirdPartyApplications/{third_party_application_rid}/website/versions', {
        'delete': ('DELETE', '/{version_version}'), 'get': ('GET', '/{version_version}'),
        'list': ('GET', ''), 'upload': ('POST', '/upload'), 'upload_snapshot': ('POST', '/uploadSnapshot')}),
    'v2.third_party_applications.Website': ('/thirdPartyApplications/{third_party_application_rid}/website', {
        'deploy': ('POST', '/deploy'), 'get': ('GET', ''), 'undeploy': ('POST', '/undeploy')}),
}
BODY_FIELDS = {
    'Folder.create': 'parent_folder_rid display_name',
    'Folder.replace': 'parent_folder_rid display_name',
    'Project.add_organizations': 'organization_rids',
    'Project.create': 'display_name description space_rid role_grants default_roles organization_rids resource_level_role_grants_allowed',
    'Project.create_from_template': 'template_rid variable_values default_roles organization_rids project_description',
    'Project.remove_organizations': 'organization_rids', 'Project.replace': 'display_name description',
    'ProjectResourceReference.add': 'resources', 'ProjectResourceReference.remove': 'resources',
    'Resource.add_markings': 'marking_ids', 'Resource.remove_markings': 'marking_ids',
    'ResourceRole.add': 'roles', 'ResourceRole.remove': 'roles',
    'ResourceTag.add': 'tag_rids', 'ResourceTag.remove': 'tag_rids',
    'Space.create': 'enrollment_rid usage_account_rid file_system_id display_name organizations description deletion_policy_organizations default_role_set_id',
    'Space.replace': 'usage_account_rid display_name description default_role_set_id',
    'Website.deploy': 'version',
}
PAGERS = {'LogFile.list', 'Folder.children', 'Project.organizations', 'ProjectResourceReference.list',
          'Resource.markings', 'ResourceRole.list', 'Space.list', 'Version.list'}
PREVIEW = {'Folder.replace', 'Project.replace', 'ResourceTag.add', 'ResourceTag.list', 'ResourceTag.remove',
           'Space.create', 'Space.delete', 'Space.get', 'Space.replace', 'ThirdPartyApplication.get',
           'Version.upload_snapshot'}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, check=True).stdout


def norm(value):
    if hasattr(value, 'model_dump'):
        return norm(value.model_dump(mode='json', by_alias=True, exclude_none=True))
    if isinstance(value, dict):
        return {key: norm(child) for key, child in value.items() if child is not None}
    if isinstance(value, (list, tuple)):
        return [norm(item) for item in value]
    if isinstance(value, (datetime.datetime, datetime.date)):
        return value.isoformat()
    return value


def camel(value):
    first, *rest = value.split('_')
    return first + ''.join(item.title() for item in rest)


def independent_wire(key, args, request, void):
    owner, method = key.rsplit('.', 1)
    prefix, operations = ROUTES[owner]
    verb, suffix = operations[method]
    path = '/api/v2' + prefix + suffix
    path = re.sub(r'\{([^}]+)\}', lambda match: quote(str(args[match[1]]), safe=''), path)
    assert request.method == verb, key
    assert request.url.raw_path.split(b'?')[0] == path.encode(), key
    assert request.url.host == 'offline.example.invalid', key
    assert request.headers['Authorization'] == 'Bearer offline-fixture-token', key
    assert request.extensions['timeout'] == dict.fromkeys(('connect', 'read', 'write', 'pool'), 30), key
    short = owner.rsplit('.', 1)[1] + '.' + method
    queries = {}
    if short in PAGERS:
        queries.update(page_size=args.get('page_size'), page_token=args.get('page_token'))
    if short in PREVIEW:
        queries['preview'] = args.get('preview')
    for operation, names in {
        'LogFile.list': ('start_date', 'end_date'),
        'ProjectResourceReference.list': ('reference_type',), 'ResourceRole.list': ('include_inherited',),
        'Resource.get_by_path': ('path',), 'Version.upload': ('version',),
        'Version.upload_snapshot': ('version', 'snapshot_identifier'),
    }.items():
        if short == operation:
            queries.update({name: args.get(name) for name in names})
    wanted = httpx.QueryParams({camel(name): value for name, value in queries.items() if value is not None})
    assert sorted(request.url.params.multi_items()) == sorted(wanted.multi_items()), key
    if short in BODY_FIELDS:
        expected_body = {camel(name): norm(args[name]) for name in BODY_FIELDS[short].split()
                         if args.get(name) is not None}
        assert json.loads(request.content) == expected_body, (key, request.content, expected_body)
        assert request.headers['Content-Type'] == 'application/json', key
    elif 'body' in args:
        body = args['body']
        if isinstance(body, bytes):
            assert request.content == body, key
            assert request.headers['Content-Type'] == 'application/octet-stream', key
        else:
            assert json.loads(request.content) == norm(body), key
            assert request.headers['Content-Type'] == 'application/json', key
    else:
        assert request.content == b'', key
    if key not in void:
        assert request.headers['Accept'] == ('application/octet-stream' if short == 'LogFile.content' else 'application/json'), key


def main():
    report = {'reviewer': '/root/rest073_formal_readiness_20261117', 'kind': 'independent unit peer controls; not formal QA',
              'candidate_sha256': digest(TEST), 'failures': [], 'counts': {}}
    assert report['candidate_sha256'] == EXPECTED_SHA
    spec = importlib.util.spec_from_file_location('rest073_candidate', TEST)
    candidate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(candidate)
    inventory, void, pagers, streaming, errors, hashes = set(), set(), set(), set(), {}, {}
    for owner in ROUTES:
        version, service, resource = owner.split('.')
        snake = re.sub(r'(?<!^)(?=[A-Z])', '_', resource).lower()
        relative = f'foundry_sdk/{version}/{service}/{snake}.py'
        frozen = git('-C', str(SDK), 'show', TAG + ':' + relative)
        tree = ast.parse(frozen)
        module = __import__(f'foundry_sdk.{version}.{service}.{snake}', fromlist=['x'])
        assert Path(module.__file__).read_bytes() == frozen
        hashes[relative] = hashlib.sha256(frozen).hexdigest()
        ordinary = next(item for item in tree.body if isinstance(item, ast.ClassDef) and item.name == resource + 'Client')
        for method in ordinary.body:
            if not isinstance(method, ast.FunctionDef) or method.name.startswith('_'):
                continue
            request = [item for item in ast.walk(method) if isinstance(item, ast.Call)
                       and isinstance(item.func, ast.Attribute) and item.func.attr == 'RequestInfo']
            if not request:
                continue
            key = owner + '.' + method.name
            inventory.add(key)
            fields = {item.arg: item.value for item in request[0].keywords}
            errors[key] = {ast.literal_eval(name) for name in fields['throwable_errors'].keys}
            if isinstance(method.returns, ast.Constant) and method.returns.value is None:
                void.add(key)
            if 'ResourceIterator' in ast.unparse(method.returns):
                pagers.add(key)
        wrapper = next(item for item in tree.body if isinstance(item, ast.ClassDef) and item.name == '_' + resource + 'ClientStreaming')
        for item in ast.walk(wrapper):
            if isinstance(item, ast.Attribute) and isinstance(item.ctx, ast.Store) and isinstance(item.value, ast.Name) and item.value.id == 'self':
                streaming.add(owner + '.' + item.attr)
    assert inventory == set(candidate.CASES) == {owner + '.' + method for owner, (_, methods) in ROUTES.items() for method in methods}
    forms = {(key, mode, asynchronous) for key in inventory for asynchronous in (False, True)
             for mode in ('ordinary', 'raw', 'stream') if mode != 'stream' or key in streaming}
    assert forms == set(candidate.FORMS)
    assert len(forms) == 258 and len(void) == 15 and len(streaming) == 33 and len(pagers) == 8
    assert inventory - streaming == void
    assert sum(map(len, errors.values())) == 165
    for key in inventory:
        assert {row['name'] for row in candidate.example(key)['ERRORS']} == errors[key]
    report['sdk_modules'] = hashes
    report['counts'].update(operations=len(inventory), forms=len(forms), void=len(void), pagers=len(pagers),
                            stream_operations=len(streaming), named_error_entries=sum(map(len, errors.values())))
    loop = asyncio.new_event_loop()
    counts = Counter()

    def denied(*args, **kwargs):
        raise AssertionError('Independent peer network denial')

    original_wire = candidate.check_wire

    def expect_assertion(callback, label):
        try:
            callback()
        except Exception as error:
            # Native SDK wraps assertions raised inside transport callbacks.
            while error.__cause__ is not None:
                error = error.__cause__
            if not isinstance(error, AssertionError):
                raise
            counts[label] += 1
        else:
            raise AssertionError('Fault escaped peer control: ' + label)

    try:
        with patch.object(socket, 'getaddrinfo', denied), patch.object(socket, 'create_connection', denied), \
             patch.object(socket.socket, 'connect', denied), patch.object(socket.socket, 'connect_ex', denied), \
             patch.object(httpx.HTTPTransport, 'handle_request', denied), \
             patch.object(httpx.AsyncHTTPTransport, 'handle_async_request', denied):
            for key, mode, asynchronous in sorted(forms):
                args = candidate.inputs(key)
                payload = candidate.example(key)['SUCCESS']
                requests = []

                def handler(request):
                    independent_wire(key, args, request, void)
                    requests.append(request)
                    return candidate.response_for(payload)

                candidate.exercise(key, mode, asynchronous, handler, loop, args)
                assert len(requests) == 1
                counts['independent_literal_wire_pass'] += 1

                def broken_wire(source, request, **kwargs):
                    damaged = httpx.Request(request.method, request.url.copy_with(path='/api/v2/peer-wrong-route'),
                                            headers=request.headers, content=request.content, extensions=request.extensions)
                    return original_wire(source, damaged, **kwargs)

                with patch.object(candidate, 'check_wire', broken_wire):
                    expect_assertion(lambda: candidate.test_native_modes_serialize_and_decode(key, mode, asynchronous, loop),
                                     'native_path_faults_detected')

                def generic_error(request):
                    independent_wire(key, args, request, void)
                    return httpx.Response(403, json={'errorName': 'IndependentUnmappedDenied', 'errorCode': 'PERMISSION_DENIED',
                                                   'parameters': {}, 'errorInstanceId': '00000000-0000-0000-0000-000000000099'})

                try:
                    candidate.exercise(key, mode, asynchronous, generic_error, loop, args)
                except PalantirRPCException as error:
                    assert error.name == 'IndependentUnmappedDenied'
                    counts['independent_generic_403_pass'] += 1
                else:
                    raise AssertionError('Unmapped error did not propagate: ' + key)
            for key in sorted(streaming):
                with patch.object(httpx.Response, 'close', lambda self: None):
                    expect_assertion(lambda: candidate.test_byte_budget_closes_unfinished_native_stream(key, False, loop),
                                     'sync_omitted_close_detected')

                async def omitted_close(self):
                    return None

                with patch.object(httpx.Response, 'aclose', omitted_close):
                    expect_assertion(lambda: candidate.test_byte_budget_closes_unfinished_native_stream(key, True, loop),
                                     'async_omitted_close_detected')
                    expect_assertion(lambda: candidate.test_async_cancellation_closes_with_unread_bytes(key, loop),
                                     'cancel_omitted_close_detected')
            body = candidate.TrackedSyncStream()
            response = httpx.Response(200, stream=body)
            response.read()
            expect_assertion(lambda: candidate.require_unfinished(response, body), 'prebuffered_unfinished_guard_detected')
    finally:
        loop.close()
    report['counts'].update(counts)
    report['candidate_sha256_after'] = digest(TEST)
    assert report['candidate_sha256_after'] == EXPECTED_SHA
    baseline = ROOT / '.ept/tmp/feature015_integration'
    preserved = {}
    for relative in git('-C', str(WORK), 'ls-files', '-z', '.agents', 'tests/fixtures',
                        'tests/test_offline_rest_073_semantics.py', 'tests/test_offline_rest_073_restore.py').decode().split('\0'):
        if not relative:
            continue
        assert digest(WORK / relative) == digest(baseline / relative), relative
        preserved[relative] = digest(WORK / relative)
    report['preserved_baseline_file_count'] = len(preserved)
    report['preserved_baseline_manifest_sha256'] = hashlib.sha256(json.dumps(preserved, sort_keys=True).encode()).hexdigest()
    report['git_status'] = git('-C', str(WORK), 'status', '--short').decode().strip()
    assert report['git_status'] == '?? tests/test_offline_rest_073.py'
    report['verdict'] = 'PASS'
    REPORT.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
