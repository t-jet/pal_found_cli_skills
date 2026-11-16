"""Restore decisions against SDK 1.101.0 with synthetic HTTP and no network."""

import copy
import importlib.metadata
import runpy
import socket
from pathlib import Path

import httpx
import pytest
from foundry_sdk import PalantirRPCException, TimeoutError as SDKTimeoutError
from foundry_sdk.v2.filesystem import errors


BASE = Path(__file__).parents[1] / '.agents/skills/pal-found-dev/examples/rest/073/v2/filesystem/Resource'
RID = 'ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001'
PARENT = 'ri.synthetic.main.folder.00000000-0000-0000-0000-000000000002'
PATH = '/synthetic-space/synthetic-project/synthetic-value'


@pytest.fixture(autouse=True)
def deny_network(monkeypatch):
    attempts = []

    def denied(*args, **kwargs):
        attempts.append(True)
        raise AssertionError('Network forbidden in offline restore tests')

    monkeypatch.setattr(socket, 'getaddrinfo', denied)
    monkeypatch.setattr(socket.socket, 'connect', denied)
    monkeypatch.setattr(socket.socket, 'connect_ex', denied)
    yield
    assert not attempts


@pytest.fixture
def example():
    assert importlib.metadata.version('foundry-platform-sdk') == '1.101.0'
    return runpy.run_path(str(BASE / 'restore.py'))


def state(status, **changes):
    payload = copy.deepcopy(runpy.run_path(str(BASE / 'get.py'))['SUCCESS'])
    payload.update(trashStatus=status, parentFolderRid=PARENT, path=PATH)
    payload.update(changes)
    return httpx.Response(200, json=payload)


def error_response(name, status=400, code='INVALID_ARGUMENT'):
    return httpx.Response(status, json={
        'errorName': name, 'errorCode': code, 'parameters': {'resourceRid': RID},
        'errorInstanceId': '00000000-0000-0000-0000-000000000004',
    })


def execute(example, responses):
    calls = []

    def handler(request):
        calls.append(request.method)
        suffix = '/restore' if request.method == 'POST' else ''
        assert request.url.path == '/api/v2/filesystem/resources/' + RID + suffix
        assert request.url.query == b''
        assert request.content == b''
        assert request.headers['Authorization'] == 'Bearer offline-fixture-token'
        assert request.extensions['timeout'] == dict.fromkeys(('connect', 'read', 'write', 'pool'), 30)
        response = responses[len(calls) - 1]
        if isinstance(response, Exception):
            raise response
        return response

    with example['mock_resource'](example['ResourceClient'], handler) as client:
        result = example['restore_once'](
            client, RID, expected_parent_rid=PARENT, expected_path=PATH)
    assert len(calls) == len(responses)
    return result, calls


def test_exact_wire_raw_204_close_and_all_declared_errors(example):
    example['verify']()


@pytest.mark.parametrize('status,message', [
    ('NOT_TRASHED', 'Desired state observed; no restore sent'),
    ('ANCESTOR_TRASHED', 'STOP: authorized owner must reconcile original folder restoration'),
])
def test_preflight_state_limits_mutation(example, status, message):
    result, calls = execute(example, [state(status)])
    assert result == message
    assert calls == ['GET']


@pytest.mark.parametrize('changes', [
    {'rid': RID + '9'}, {'parentFolderRid': PARENT + '9'}, {'path': PATH + '-moved'},
])
@pytest.mark.parametrize('after_write', [False, True])
def test_identity_parent_path_conflicts_stop_without_replay(example, changes, after_write):
    responses = [state('NOT_TRASHED', **changes)]
    if after_write:
        responses = [state('DIRECTLY_TRASHED'), httpx.Response(204)] + responses
    result, calls = execute(example, responses)
    assert result == 'STOP: reconcile RID, parent and path with authorized owner'
    assert calls.count('POST') == int(after_write)


@pytest.mark.parametrize('outcome', ['success', 'not_directly_trashed', 'read_timeout', 'write_timeout', 'connect_timeout'])
@pytest.mark.parametrize('after', ['NOT_TRASHED', 'ANCESTOR_TRASHED', 'DIRECTLY_TRASHED'])
def test_one_attempt_one_readback_with_no_inferred_server_policy(example, outcome, after):
    write_response = {
        'success': httpx.Response(204),
        'not_directly_trashed': error_response('ResourceNotDirectlyTrashed'),
        'read_timeout': httpx.ReadTimeout('Synthetic unknown write outcome'),
        'write_timeout': httpx.WriteTimeout('Synthetic unknown write outcome'),
        'connect_timeout': httpx.ConnectTimeout('Synthetic timeout'),
    }[outcome]
    result, calls = execute(example, [state('DIRECTLY_TRASHED'), write_response, state(after)])
    assert calls == ['GET', 'POST', 'GET']
    if after == 'NOT_TRASHED':
        assert result == 'Desired state observed after attempt; no replay'
    elif after == 'ANCESTOR_TRASHED':
        assert result == 'STOP: authorized owner must reconcile original folder restoration'
    else:
        assert result == 'STOP: still directly trashed; reconcile outcome/policy with authorized owner'


@pytest.mark.parametrize('name,status,code', [
    ('ResourceNotFound', 404, 'NOT_FOUND'),
    ('RestoreResourcePermissionDenied', 403, 'PERMISSION_DENIED'),
])
def test_restore_denial_or_missing_resource_propagates_exact_error_and_stops(example, name, status, code):
    with pytest.raises(getattr(errors, name)) as caught:
        execute(example, [state('DIRECTLY_TRASHED'), error_response(name, status, code)])
    assert caught.value.parameters == {'resourceRid': RID}


@pytest.mark.parametrize('after_write', [False, True])
@pytest.mark.parametrize('fault', ['missing', 'denied', 'timeout'])
def test_unavailable_or_denied_read_stops(example, after_write, fault):
    response, expected = {
        'missing': (error_response('ResourceNotFound', 404, 'NOT_FOUND'), errors.ResourceNotFound),
        'denied': (error_response('PermissionDenied', 403, 'PERMISSION_DENIED'), PalantirRPCException),
        'timeout': (httpx.ReadTimeout('Synthetic read unavailable'), SDKTimeoutError),
    }[fault]
    responses = [response]
    if after_write:
        responses = [state('DIRECTLY_TRASHED'), httpx.Response(204)] + responses
    with pytest.raises(expected):
        execute(example, responses)
