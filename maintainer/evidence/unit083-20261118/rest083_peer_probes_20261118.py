import ast
import asyncio
import hashlib
import importlib
import inspect
import json
from pathlib import Path
import runpy
import subprocess
from contextlib import contextmanager
from unittest.mock import patch

import httpx
import pytest
from foundry_sdk import Config, UserTokenAuth, PermissionDeniedError, ReadTimeout
from foundry_sdk.v2.ontologies.attachment import AttachmentClient, AsyncAttachmentClient
from foundry_sdk.v2.ontologies.geotemporal_series_property import GeotemporalSeriesPropertyClient
from foundry_sdk.v2.ontologies.time_series_property_v2 import TimeSeriesPropertyV2Client
from pydantic import ValidationError

ROOT = Path(__file__).resolve().parents[2]
PEER = ROOT / '.ept/tmp/feature015_rest083_peer_20261118'
AUTHOR = ROOT / '.ept/tmp/feature015_rest083_unit_modes_20261118'
SDK = ROOT / '.ept/docs/customer_input/foundry-platform-python'
PIN = '168d51910570b6966afa2320333ab36f6a3f7ccf'
BASE = 'ff70c30c99410b3b0784bcad934625b88d5e6e5c'

@pytest.fixture(autouse=True)
def deny_external_transport(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError('Peer external transport denied')
    monkeypatch.setattr(httpx.HTTPTransport, 'handle_request', denied)
    monkeypatch.setattr(httpx.AsyncHTTPTransport, 'handle_async_request', denied)

@contextmanager
def client(kind, handler):
    with httpx.Client(transport=httpx.MockTransport(handler)) as transport:
        with patch('foundry_sdk._core.api_client.HttpClient', return_value=transport):
            yield kind(auth=UserTokenAuth(token='peer-083'), hostname='peer.invalid',
                       config=Config(max_retries=1))

def test_source_and_baseline_binding():
    candidate = PEER / 'tests/test_offline_rest_083.py'
    data = candidate.read_bytes()
    assert data == (AUTHOR / 'tests/test_offline_rest_083.py').read_bytes()
    baseline = subprocess.check_output(['git', '-C', str(PEER), 'show', BASE + ':tests/test_offline_rest_083.py'])
    assert len(baseline) == 9743 and data.startswith(baseline)
    module = runpy.run_path(str(candidate))
    resources = {}
    operations = []
    for resource, stem in module['NATIVE_RESOURCES'].items():
        rel = 'foundry_sdk/v2/ontologies/' + stem + '.py'
        frozen = subprocess.check_output(['git', '-C', str(SDK), 'show', PIN + ':' + rel])
        runtime = importlib.import_module('foundry_sdk.v2.ontologies.' + stem)
        assert frozen == Path(runtime.__file__).read_bytes()
        assert hashlib.sha256(frozen).hexdigest() == module['NATIVE_SOURCE_HASHES'][resource]
        tree = ast.parse(frozen)
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == resource + 'Client')
        methods = [n for n in cls.body if isinstance(n, ast.FunctionDef) and not n.name.startswith('_')]
        ids = []
        for method in methods:
            calls = [n for n in ast.walk(method) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == 'RequestInfo']
            if not calls:
                continue
            fields = {n.arg: n.value for n in calls[0].keywords}
            assert ast.literal_eval(fields['throwable_errors']) == {}
            assert not (isinstance(fields['response_type'], ast.Constant) and fields['response_type'].value is None)
            ids.append(method.name)
            operations.append('v2.ontologies.' + resource + '.' + method.name)
        resources[resource] = {'sha256': hashlib.sha256(frozen).hexdigest(), 'operations': ids}
    assert len(operations) == 25
    assert hashlib.sha256('\n'.join(sorted(operations)).encode()).hexdigest() == '710719af53721cbf4c1f37db6a3723ba5b5af3e405c99b572941599cd5ca2f80'
    proof = {'candidate_sha256': hashlib.sha256(data).hexdigest(), 'base_commit': BASE,
             'baseline_bytes': len(baseline), 'prefix_preserved': True, 'source_commit': PIN,
             'source_resources': resources, 'operations': operations}
    (ROOT / '.ept/tmp/rest083_peer_source_binding_20261118.json').write_text(json.dumps(proof, indent=2))

@pytest.mark.parametrize('mode', ['ordinary', 'raw', 'streaming'])
@pytest.mark.parametrize('body', [b'', b'null'])
def test_nullable_boundary(mode, body):
    replies = []
    def handler(request):
        assert request.method == 'GET'
        assert request.url.path == '/api/v2/ontologies/peer-ontology/objects/Truck/unit-9/timeseries/temperature/firstPoint'
        reply = httpx.Response(200, content=body)
        replies.append(reply)
        return reply
    with client(TimeSeriesPropertyV2Client, handler) as resource:
        args = dict(ontology='peer-ontology', object_type='Truck', primary_key='unit-9', property='temperature')
        if mode == 'streaming':
            with resource.with_streaming_response.get_first_point(**args) as result:
                assert b''.join(result.iter_bytes()) == body
        elif body == b'null':
            with pytest.raises(ValidationError):
                if mode == 'raw':
                    raw = resource.with_raw_response.get_first_point(**args)
                    try:
                        raw.decode()
                    finally:
                        raw.close()
                else:
                    resource.get_first_point(**args)
        elif mode == 'raw':
            raw = resource.with_raw_response.get_first_point(**args)
            try:
                assert raw.decode() is None
            finally:
                raw.close()
        else:
            assert resource.get_first_point(**args) is None
    assert len(replies) == 1 and replies[0].is_closed

def test_manual_continuation_empty_first_page():
    tokens = []
    def handler(request):
        body = json.loads(request.content)
        tokens.append(body.get('pageToken'))
        assert request.method == 'POST'
        assert request.url.path.endswith('/geotemporalSeries/route/loadEntries')
        return httpx.Response(200, json={'data': [], **({'nextPageToken': 'peer /token'} if len(tokens) == 1 else {})})
    with client(GeotemporalSeriesPropertyClient, handler) as resource:
        args = dict(ontology='peer', object_type='Truck', primary_key='unit-9', property='route',
                    additional_properties=[], range={'type': 'absolute'}, page_size=1)
        first = resource.load_geotemporal_series_entries(**args)
        assert first.data == [] and first.next_page_token == 'peer /token'
        assert tokens == [None]
        final = resource.load_geotemporal_series_entries(**args, page_token=first.next_page_token)
        assert final.next_page_token is None and tokens == [None, 'peer /token']

@pytest.mark.parametrize('failure', [None, 'permission', 'timeout'])
def test_upload_binary_and_failure(failure):
    payload = b'\xff\x00peer-upload\xfe'
    requests = []
    def handler(request):
        requests.append(request)
        assert request.method == 'POST' and request.url.path == '/api/v2/ontologies/attachments/upload'
        assert request.content == payload
        assert request.headers['Content-Type'] == '*/*'
        assert request.headers['Content-Length'] == str(len(payload))
        assert request.headers['Authorization'] == 'Bearer peer-083'
        assert request.url.params['filename'] == 'peer report.bin'
        if failure == 'timeout':
            raise httpx.ReadTimeout('peer timeout', request=request)
        if failure == 'permission':
            return httpx.Response(403, json={'errorName': 'PermissionDenied', 'errorCode': 'PERMISSION_DENIED', 'parameters': {'peer': '083'}, 'errorInstanceId': '00000000-0000-0000-0000-000000000083'})
        return httpx.Response(200, json={'rid': 'ri.peer.main.attachment.unit9', 'filename': 'peer report.bin', 'sizeBytes': str(len(payload)), 'mediaType': 'application/octet-stream'})
    with client(AttachmentClient, handler) as resource:
        args = dict(body=payload, content_length=len(payload), content_type='text/plain', filename='peer report.bin')
        if failure:
            with pytest.raises(PermissionDeniedError if failure == 'permission' else ReadTimeout):
                resource.upload(**args)
        else:
            assert int(resource.upload(**args).size_bytes) == len(payload)
    assert len(requests) == 1

def test_async_cancel_unconsumed_transport():
    class Stream(httpx.AsyncByteStream):
        reads = 0
        closed = False
        async def __aiter__(self):
            for chunk in [b'\xffpeer-first', b'second']:
                self.reads += 1
                yield chunk
        async def aclose(self):
            self.closed = True
    body = Stream()
    async def run():
        async with httpx.AsyncClient(transport=httpx.MockTransport(lambda request: httpx.Response(200, stream=body))) as transport:
            with patch('foundry_sdk._core.api_client.AsyncHttpClient', return_value=transport):
                resource = AsyncAttachmentClient(auth=UserTokenAuth(token='peer-083'), hostname='peer.invalid')
            async with resource.with_streaming_response.read(attachment_rid='ri.peer.main.attachment.unit9') as reply:
                assert body.reads == 0 and not body.closed
                async for chunk in reply.aiter_bytes():
                    assert chunk == b'\xffpeer-first'
                    asyncio.current_task().cancel()
                    await asyncio.sleep(0)
    with pytest.raises(asyncio.CancelledError):
        asyncio.run(run())
    assert body.reads == 1 and body.closed

@pytest.mark.parametrize('mutant', ['async-close', 'page-token', 'binary-body'])
def test_candidate_fault_sensitivity(mutant):
    module = runpy.run_path(str(PEER / 'tests/test_offline_rest_083.py'))
    loop = asyncio.new_event_loop()
    try:
        if mutant == 'async-close':
            async def skip_close(self):
                pass
            with patch.object(module['NativeAsyncStream'], 'aclose', skip_close):
                with pytest.raises(AssertionError):
                    module['test_native_unfinished_stream_closes_on_interrupt_or_cancel']('Attachment', 'read', True, loop)
        elif mutant == 'page-token':
            from foundry_sdk._core.api_client import BaseApiClient
            original = BaseApiClient._serialize
            def remove_token(self, value):
                data = original(self, value)
                if data is not None:
                    parsed = json.loads(data)
                    if isinstance(parsed, dict):
                        parsed.pop('pageToken', None)
                        return json.dumps(parsed).encode()
                return data
            with patch.object(BaseApiClient, '_serialize', remove_token):
                with pytest.raises(Exception) as error:
                    module['test_native_geotemporal_continuation_is_explicit_and_finite'](False, 'ordinary', loop)
                cause = error.value
                while cause.__cause__ is not None:
                    cause = cause.__cause__
                assert isinstance(cause, AssertionError)
        else:
            from foundry_sdk._core.api_client import BaseApiClient
            original = BaseApiClient._serialize
            def corrupt_bytes(self, value):
                return b'corrupted payload' if isinstance(value, bytes) else original(self, value)
            with patch.object(BaseApiClient, '_serialize', corrupt_bytes):
                with pytest.raises(Exception) as error:
                    module['test_native_upload_is_raw_binary_not_multipart']('Attachment', 'upload', False, 'raw', loop)
                cause = error.value
                while cause.__cause__ is not None:
                    cause = cause.__cause__
                assert isinstance(cause, AssertionError)
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
