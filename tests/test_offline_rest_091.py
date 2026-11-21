"""Media/widget examples use real SDK transport and source-derived semantics."""

import copy
import inspect
import runpy
import socket
import struct
import zlib
from pathlib import Path
from urllib.parse import urlparse

import pytest
import httpx
from foundry_sdk import PalantirRPCException
from foundry_sdk.v2.media_sets.media_set import MediaSetClient
from foundry_sdk.v2.media_sets import models as media
from foundry_sdk.v2.widgets import models as widgets
from foundry_sdk.v2.widgets.dev_mode_settings_v2 import DevModeSettingsV2Client

DEV = Path(__file__).parents[1] / '.agents/skills/pal-found-dev'
EXAMPLES = DEV / 'examples/rest/091/v2'
FILES = sorted(EXAMPLES.rglob('invoke_*.py'))


@pytest.fixture(autouse=True)
def deny_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError('Network forbidden in offline REST091 tests')
    for name in ('connect', 'connect_ex'):
        monkeypatch.setattr(socket.socket, name, denied)
    for name in ('create_connection', 'getaddrinfo', 'gethostbyname', 'gethostbyname_ex'):
        monkeypatch.setattr(socket, name, denied)


def load(service, resource, method):
    return runpy.run_path(str(EXAMPLES / service / resource / f'invoke_{method}.py'))


@pytest.mark.parametrize('path', FILES, ids=lambda p: str(p.relative_to(EXAMPLES)))
def test_all_operations_actual_sdk_mock_http(path):
    runpy.run_path(str(path))['verify']()


@pytest.mark.parametrize('path', FILES, ids=lambda p: str(p.relative_to(EXAMPLES)))
def test_generic_denial_stops_each_operation_without_replay(path):
    example = runpy.run_path(str(path))
    resource_type = next(value for name, value in example.items()
                         if name.endswith('Client') and isinstance(value, type))
    calls = []
    def denied(request):
        example['check_request'](request)
        if isinstance(example['EXPECTED_BODY'], bytes):
            assert int(request.headers['Content-Length']) == len(example['EXPECTED_BODY'])
        calls.append(request)
        return httpx.Response(403, json={
            'errorCode': 'PERMISSION_DENIED', 'errorName': 'OfflineDenied',
            'errorInstanceId': '00000000-0000-0000-0000-000000000009', 'parameters': {},
        })
    with example['mock_resource'](resource_type, denied) as client:
        with pytest.raises(PalantirRPCException) as caught:
            example['invoke'](client)
    assert caught.value.name == 'OfflineDenied'
    assert len(calls) == 1


def assert_widget_manifest(manifest):
    assert isinstance(manifest, dict)
    assert manifest['manifestVersion'] == '1.0.0'
    settings = manifest['devSettings']
    assert urlparse(settings['baseHref']).hostname == 'localhost'
    assert settings['widgets']
    for key, widget in settings['widgets'].items():
        assert widget['id'] == key and widget['name']
        assert widget['type'] == 'workshopWidgetV1'
        assert widget['entrypointJs']
        for asset in widget['entrypointJs'] + widget.get('entrypointCss', []):
            assert urlparse(asset['path']).hostname == 'localhost'
            assert urlparse(asset['path']).path.endswith(('.js', '.css'))
        assert isinstance(widget['parameters'], dict)
        assert isinstance(widget['events'], dict)
    assert isinstance(settings['inputSpec']['discovered']['sdks'], list)


def test_manifest_has_meaningful_widget_and_rejects_original_and_bad_assets():
    example = load('widgets', 'DevModeSettingsV2', 'set_widget_set_manifest')
    manifest = example['EXPECTED_BODY']['manifest']
    assert_widget_manifest(manifest)
    with pytest.raises(AssertionError):
        assert_widget_manifest('synthetic-value')
    broken = copy.deepcopy(manifest)
    next(iter(broken['devSettings']['widgets'].values()))['entrypointJs'][0]['path'] = 'synthetic-value'
    with pytest.raises(AssertionError):
        assert_widget_manifest(broken)
    doc = inspect.getdoc(DevModeSettingsV2Client.set_widget_set_manifest)
    assert all(key in doc for key in ('manifestVersion', 'devSettings', 'baseHref', 'widgets', 'inputSpec'))
    assert widgets.DevModeSettingsV2.model_validate(example['SUCCESS']).snapshot is None


def test_widget_ids_and_returned_rids_are_distinct_and_settings_are_useful():
    example = load('widgets', 'DevModeSettings', 'set_widget_set_by_id')
    request = example['EXPECTED_BODY']
    settings = widgets.WidgetSetDevModeSettingsById.model_validate(request['settings'])
    assert urlparse(settings.base_href).hostname == 'localhost'
    assert settings.widget_settings
    response = widgets.DevModeSettings.model_validate(example['SUCCESS'])
    returned = response.widget_set_settings[request['widgetSetRid']]
    assert set(settings.widget_settings).isdisjoint(returned.widget_settings)
    assert returned.base_href == settings.base_href
    for widget in settings.widget_settings.values():
        assert widget.script_entrypoints and widget.stylesheet_entrypoints
        assert widget.script_entrypoints[0].file_path.endswith('.js')
        assert widget.stylesheet_entrypoints[0].file_path.endswith('.css')
    assert 'WidgetId' in inspect.getsource(widgets.WidgetSetDevModeSettingsById)
    assert 'WidgetRid' in inspect.getsource(widgets.WidgetSetDevModeSettings)


def test_path_lookup_requires_found_identity_and_handles_absence():
    example = load('media_sets', 'MediaSet', 'get_rid_by_path')
    require = example['require_item_rid']
    assert require(media.GetMediaItemRidByPathResponse.model_validate(example['SUCCESS']))
    for empty in ({}, {'mediaItemRid': None}):
        with pytest.raises(LookupError, match='No media item'):
            require(media.GetMediaItemRidByPathResponse.model_validate(empty))


@pytest.mark.parametrize('method', ['upload', 'upload_media'])
def test_binary_png_and_sdk_upload_discrepancy_have_explicit_preflight(method):
    example = load('media_sets', 'MediaSet', method)
    assert_png_image(example['EXPECTED_BODY'])
    assert example['EXPECTED_HEADERS']['Content-Type'] == '*/*'
    assert 'application/octet-stream' in inspect.getdoc(getattr(MediaSetClient, method))
    assert '"Content-Type": "*/*"' in inspect.getsource(getattr(MediaSetClient, method))
    with pytest.raises(RuntimeError, match='authorized transport verification'):
        example['require_verified_upload']()
    example['require_verified_upload'](authorized_transport_verified=True)
    if method == 'upload_media':
        assert example['EXPECTED_QUERY']['filename'].endswith('.png')
        assert example['SUCCESS']['mimeType'] == 'image/png'


def assert_png_image(payload):
    """Validate this fixture's noninterlaced, 8-bit RGB PNG through scanlines."""
    assert payload[:8] == b'\x89PNG\r\n\x1a\n'
    offset = 8
    chunks = []
    while offset < len(payload):
        assert offset + 12 <= len(payload), 'truncated PNG chunk'
        size = struct.unpack('>I', payload[offset:offset + 4])[0]
        end = offset + 12 + size
        assert end <= len(payload), 'chunk length exceeds payload'
        kind = payload[offset + 4:offset + 8]
        data = payload[offset + 8:end - 4]
        crc = struct.unpack('>I', payload[end - 4:end])[0]
        assert crc == zlib.crc32(kind + data), 'PNG chunk CRC mismatch'
        chunks.append((kind, data))
        offset = end
    assert [kind for kind, _ in chunks] == [b'IHDR', b'IDAT', b'IEND']
    assert len(chunks[0][1]) == 13 and chunks[-1][1] == b''
    width, height, depth, color, compression, filtering, interlace = struct.unpack('>IIBBBBB', chunks[0][1])
    assert width > 0 and height > 0
    assert (depth, color, compression, filtering, interlace) == (8, 2, 0, 0, 0)
    decoder = zlib.decompressobj()
    pixels = decoder.decompress(chunks[1][1]) + decoder.flush()
    assert decoder.eof and not decoder.unused_data and not decoder.unconsumed_tail
    row_size = 1 + width * 3
    assert len(pixels) == height * row_size, 'PNG scanline length mismatch'
    for row in range(height):
        assert pixels[row * row_size] in range(5), 'invalid PNG filter'


def test_png_validation_rejects_crc_corruption_truncation_and_wrong_scanlines():
    payload = load('media_sets', 'MediaSet', 'upload')['EXPECTED_BODY']
    corrupted = bytearray(payload)
    corrupted[-1] ^= 1
    with pytest.raises(AssertionError, match='CRC'):
        assert_png_image(bytes(corrupted))
    with pytest.raises(AssertionError, match='chunk'):
        assert_png_image(payload[:-1])
    # Preserve valid chunk CRC while changing IHDR width: scanline validation
    # must catch the inconsistent decompressed pixel length independently.
    wrong = bytearray(payload)
    wrong[16:20] = struct.pack('>I', 2)
    wrong[29:33] = struct.pack('>I', zlib.crc32(wrong[12:29]))
    with pytest.raises(AssertionError, match='scanline length'):
        assert_png_image(bytes(wrong))


def test_media_mime_values_match_declared_imagery_content():
    reference = load('media_sets', 'MediaSet', 'reference')
    registration = load('media_sets', 'MediaSet', 'register')
    assert reference['SUCCESS']['mimeType'] == 'image/png'
    assert registration['SUCCESS']['mediaType'] == 'image/png'
    assert registration['EXPECTED_BODY']['physicalItemName'].endswith('.png')
    assert not registration['EXPECTED_BODY']['physicalItemName'].startswith(('/', 'http:'))
    assert 'federated media sets' in inspect.getdoc(MediaSetClient.register)


def test_status_uses_actual_successful_literal_and_rejects_reviewer_typo():
    result = dict(load('media_sets', 'MediaSet', 'get_status')['SUCCESS'], status='SUCCESSFUL')
    media.GetTransformationJobStatusResponse.model_validate(result)
    with pytest.raises(ValueError):
        media.GetTransformationJobStatusResponse.model_validate(dict(result, status='SUCCEEDED'))


# Native SDK modes are exercised independently of the reader's raw-only invoke().
import asyncio  # noqa: E402
import json  # noqa: E402
from contextlib import asynccontextmanager, contextmanager  # noqa: E402
from unittest.mock import patch  # noqa: E402

from foundry_sdk import Config, UserTokenAuth  # noqa: E402
from foundry_sdk.v2.media_sets.media_set import AsyncMediaSetClient  # noqa: E402
from foundry_sdk.v2.widgets.release import AsyncReleaseClient, ReleaseClient  # noqa: E402


NATIVE_RID = 'ri.widgets.main.widget-set.00000000-0000-0000-0000-000000000091'
NATIVE_MEDIA_RID = 'ri.mio.main.media-set.00000000-0000-0000-0000-000000000091'
NATIVE_ITEM_RID = 'ri.mio.main.media-item.00000000-0000-0000-0000-000000000092'
NATIVE_GET = {
    'rid': NATIVE_MEDIA_RID, 'mediaSchema': 'AUDIO', 'defaultBranchName': 'main',
    'transactionPolicy': {'type': 'batchTransactions'}, 'pathsRequired': True,
}
NATIVE_RELEASE = {
    'widgetSetRid': NATIVE_RID, 'version': '1.2.3',
    'locator': {'repositoryRid': NATIVE_RID, 'repositoryVersion': 'build-17'},
}
NATIVE_PILOTS = [
    ('MediaSet.get', MediaSetClient, AsyncMediaSetClient,
     {'media_set_rid': NATIVE_MEDIA_RID}, '/api/v2/mediasets/' + NATIVE_MEDIA_RID,
     NATIVE_GET),
    ('MediaSet.read', MediaSetClient, AsyncMediaSetClient,
     {'media_set_rid': NATIVE_MEDIA_RID, 'media_item_rid': NATIVE_ITEM_RID},
     '/api/v2/mediasets/' + NATIVE_MEDIA_RID + '/items/' + NATIVE_ITEM_RID + '/content',
     b'\x00\xffmedia\x00payload'),
    ('Release.list', ReleaseClient, AsyncReleaseClient,
     {'widget_set_rid': NATIVE_RID},
     '/api/v2/widgets/widgetSets/' + NATIVE_RID + '/releases',
     {'data': [NATIVE_RELEASE]}),
]


class NativeSyncBody(httpx.SyncByteStream):
    def __init__(self, payload):
        self.payload = payload
        self.reads = 0
        self.closed = False

    def __iter__(self):
        self.reads += 1
        yield self.payload[:3]
        yield self.payload[3:]

    def close(self):
        self.closed = True


class NativeAsyncBody(httpx.AsyncByteStream):
    def __init__(self, payload):
        self.payload = payload
        self.reads = 0
        self.closed = False

    async def __aiter__(self):
        self.reads += 1
        yield self.payload[:3]
        yield self.payload[3:]

    async def aclose(self):
        self.closed = True


@contextmanager
def native_sync_resource(resource_type, handler):
    with httpx.Client(transport=httpx.MockTransport(handler), timeout=11) as transport:
        with patch('foundry_sdk._core.api_client.HttpClient', return_value=transport):
            client = resource_type(UserTokenAuth(token='native-secret-token'),
                                   'offline.example.invalid',
                                   Config(timeout=11, max_retries=1,
                                          propagate_qos='PROPAGATE_429_AND_503_TO_CALLER'))
        yield client


@asynccontextmanager
async def native_async_resource(resource_type, handler):
    async with httpx.AsyncClient(transport=httpx.MockTransport(handler), timeout=11) as transport:
        with patch('foundry_sdk._core.api_client.AsyncHttpClient', return_value=transport):
            client = resource_type(UserTokenAuth(token='native-secret-token'),
                                   'offline.example.invalid',
                                   Config(timeout=11, max_retries=1,
                                          propagate_qos='PROPAGATE_429_AND_503_TO_CALLER'))
        yield client


def native_normalized(value):
    if hasattr(value, 'model_dump'):
        return value.model_dump(mode='json', by_alias=True, exclude_none=True)
    return value


@pytest.fixture(scope='session')
def native_event_loop():
    # Windows creates a local wakeup socket when the event loop is constructed.
    # Construct it before the function-scoped network guard, which stays active
    # throughout every SDK request and coroutine.
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


def native_pilot_handler(case, asynchronous):
    name, _, _, _, path, success = case
    payload = success if isinstance(success, bytes) else json.dumps(success).encode()
    body = (NativeAsyncBody if asynchronous else NativeSyncBody)(payload)
    calls = []

    def handler(request):
        assert request.method == 'GET'
        assert request.url.path == path
        assert request.url.params == httpx.QueryParams({'preview': 'true'})
        assert request.headers['Authorization'] == 'Bearer native-secret-token'
        assert request.headers['Accept'] == ('*/*' if name == 'MediaSet.read' else 'application/json')
        assert request.content == b''
        assert set(request.extensions['timeout'].values()) == {11}
        calls.append(request)
        return httpx.Response(200, stream=body)

    return handler, body, calls, payload


@pytest.mark.parametrize('case', NATIVE_PILOTS, ids=lambda case: case[0])
@pytest.mark.parametrize('mode', ['ordinary', 'raw', 'stream'])
def test_native_pilot_sync_modes(case, mode):
    name, sync_type, _, arguments, _, success = case
    handler, body, calls, payload = native_pilot_handler(case, False)
    with native_sync_resource(sync_type, handler) as client:
        target = client if mode == 'ordinary' else getattr(
            client, 'with_raw_response' if mode == 'raw' else 'with_streaming_response')
        result = getattr(target, name.split('.')[1])(**arguments, preview=True, request_timeout=11)
        if mode == 'stream':
            assert body.reads == 0
            with result as response:
                assert b''.join(response.iter_bytes()) == payload
            assert body.closed
        elif mode == 'raw':
            try:
                assert native_normalized(result.decode()) == success
            finally:
                result.close()
            assert body.closed
        elif name == 'Release.list':
            assert len(calls) == 1  # Synchronous PageIterator fetches its first page eagerly.
            assert [native_normalized(item) for item in result] == success['data']
        else:
            assert native_normalized(result) == success
    assert len(calls) == 1


@pytest.mark.parametrize('case', NATIVE_PILOTS, ids=lambda case: case[0])
@pytest.mark.parametrize('mode', ['ordinary', 'raw', 'stream'])
def test_native_pilot_async_modes(case, mode, native_event_loop):
    async def exercise():
        name, _, async_type, arguments, _, success = case
        handler, body, calls, payload = native_pilot_handler(case, True)
        async with native_async_resource(async_type, handler) as client:
            target = client if mode == 'ordinary' else getattr(
                client, 'with_raw_response' if mode == 'raw' else 'with_streaming_response')
            result = getattr(target, name.split('.')[1])(**arguments, preview=True, request_timeout=11)
            if mode == 'stream':
                assert not inspect.isawaitable(result)
                async with result as response:
                    assert body.reads == 0
                    assert b''.join([chunk async for chunk in response.aiter_bytes()]) == payload
                assert body.closed
            elif mode == 'ordinary' and name == 'Release.list':
                assert not inspect.isawaitable(result)
                assert calls == []
                assert [native_normalized(item) async for item in result] == success['data']
            else:
                assert inspect.isawaitable(result)
                result = await result
                if mode == 'raw':
                    try:
                        assert native_normalized(result.decode()) == success
                    finally:
                        await result.aclose()
                    assert body.closed
                else:
                    assert native_normalized(result) == success
        assert len(calls) == 1

    native_event_loop.run_until_complete(exercise())


import importlib  # noqa: E402
from types import SimpleNamespace  # noqa: E402
from urllib.parse import quote  # noqa: E402

from pydantic import TypeAdapter, ValidationError  # noqa: E402
from foundry_sdk.v2.core import models as core_models  # noqa: E402
from foundry_sdk.v2.widgets import errors as widget_errors  # noqa: E402


# Literal HTTP/result ledger transcribed from frozen SDK 1.101.0 resource files.
# Paths retain wire aliases, so a Python-name or route mutation cannot agree by accident.
NATIVE_CONTRACTS = {
    'media_sets.MediaSet.abort': ('POST', '/mediasets/{mediaSetRid}/transactions/{transactionId}/abort', None),
    'media_sets.MediaSet.calculate': ('GET', '/mediasets/{mediaSetRid}/items/{mediaItemRid}/transform/imagery/thumbnail/calculate', media.TrackedTransformationResponse),
    'media_sets.MediaSet.clear': ('DELETE', '/mediasets/{mediaSetRid}/items/clearAtPath', None),
    'media_sets.MediaSet.commit': ('POST', '/mediasets/{mediaSetRid}/transactions/{transactionId}/commit', None),
    'media_sets.MediaSet.create': ('POST', '/mediasets/{mediaSetRid}/transactions', media.TransactionId),
    'media_sets.MediaSet.get': ('GET', '/mediasets/{mediaSetRid}', media.GetMediaSetResponse),
    'media_sets.MediaSet.get_result': ('GET', '/mediasets/{mediaSetRid}/items/{mediaItemRid}/transformationJobs/{transformationJobId}/result', bytes),
    'media_sets.MediaSet.get_rid_by_path': ('GET', '/mediasets/{mediaSetRid}/items/getRidByPath', media.GetMediaItemRidByPathResponse),
    'media_sets.MediaSet.get_status': ('GET', '/mediasets/{mediaSetRid}/items/{mediaItemRid}/transformationJobs/{transformationJobId}', media.GetTransformationJobStatusResponse),
    'media_sets.MediaSet.info': ('GET', '/mediasets/{mediaSetRid}/items/{mediaItemRid}', media.GetMediaItemInfoResponse),
    'media_sets.MediaSet.metadata': ('GET', '/mediasets/{mediaSetRid}/items/{mediaItemRid}/metadata', media.MediaItemMetadata),
    'media_sets.MediaSet.read': ('GET', '/mediasets/{mediaSetRid}/items/{mediaItemRid}/content', bytes),
    'media_sets.MediaSet.read_original': ('GET', '/mediasets/{mediaSetRid}/items/{mediaItemRid}/original', bytes),
    'media_sets.MediaSet.reference': ('GET', '/mediasets/{mediaSetRid}/items/{mediaItemRid}/reference', core_models.MediaReference),
    'media_sets.MediaSet.register': ('POST', '/mediasets/{mediaSetRid}/items/register', media.RegisterMediaItemResponse),
    'media_sets.MediaSet.retrieve': ('GET', '/mediasets/{mediaSetRid}/items/{mediaItemRid}/transform/imagery/thumbnail/retrieve', bytes),
    'media_sets.MediaSet.transform': ('POST', '/mediasets/{mediaSetRid}/items/{mediaItemRid}/transform', media.TransformMediaItemResponse),
    'media_sets.MediaSet.upload': ('POST', '/mediasets/{mediaSetRid}/items', media.PutMediaItemResponse),
    'media_sets.MediaSet.upload_media': ('PUT', '/mediasets/media/upload', core_models.MediaReference),
    'widgets.DevModeSettings.enable': ('POST', '/widgets/devModeSettings/enable', widgets.DevModeSettings),
    'widgets.DevModeSettings.set_widget_set_by_id': ('POST', '/widgets/devModeSettings/setWidgetSetById', widgets.DevModeSettings),
    'widgets.DevModeSettingsV2.enable': ('POST', '/widgets/devModeSettingsV2/enable', widgets.DevModeSettingsV2),
    'widgets.DevModeSettingsV2.set_widget_set_manifest': ('POST', '/widgets/devModeSettingsV2/setWidgetSetManifest', widgets.DevModeSettingsV2),
    'widgets.Release.delete': ('DELETE', '/widgets/widgetSets/{widgetSetRid}/releases/{releaseVersion}', None),
    'widgets.Release.get': ('GET', '/widgets/widgetSets/{widgetSetRid}/releases/{releaseVersion}', widgets.Release),
    'widgets.Release.list': ('GET', '/widgets/widgetSets/{widgetSetRid}/releases', widgets.ListReleasesResponse),
    'widgets.Repository.get': ('GET', '/widgets/repositories/{repositoryRid}', widgets.Repository),
    'widgets.Repository.publish': ('POST', '/widgets/repositories/{repositoryRid}/publish', widgets.Release),
    'widgets.WidgetSet.get': ('GET', '/widgets/widgetSets/{widgetSetRid}', widgets.WidgetSet),
}
NATIVE_MODULES = {
    'MediaSet': 'media_set', 'DevModeSettings': 'dev_mode_settings',
    'DevModeSettingsV2': 'dev_mode_settings_v2', 'Release': 'release',
    'Repository': 'repository', 'WidgetSet': 'widget_set',
}
NATIVE_PATH_ALIASES = {
    'mediaSetRid': 'media_set_rid', 'mediaItemRid': 'media_item_rid',
    'transactionId': 'transaction_id', 'transformationJobId': 'transformation_job_id',
    'widgetSetRid': 'widget_set_rid', 'releaseVersion': 'release_version',
    'repositoryRid': 'repository_rid',
}


def native_operation(key):
    service, resource, method = key.split('.')
    example = load(service, resource, method)
    captured = {}

    def capture(**kwargs):
        captured.update(kwargs)

    # Reader input data stays immutable; this adapter selects each native mode.
    example['invoke'](SimpleNamespace(with_raw_response=SimpleNamespace(**{method: capture})))
    module = importlib.import_module(f'foundry_sdk.v2.{service}.{NATIVE_MODULES[resource]}')
    sync_type = getattr(module, resource + 'Client')
    async_type = getattr(module, 'Async' + resource + 'Client')
    return example, captured, sync_type, async_type, method


def native_validate_result(key, result, expected, pager=False):
    expected = native_success(key)
    expected_type = NATIVE_CONTRACTS[key][2]
    if pager:
        assert all(isinstance(item, widgets.Release) for item in result)
        assert [native_normalized(item) for item in result] == expected['data']
    elif expected_type is None:
        assert result is None and expected is None
    else:
        typed = TypeAdapter(expected_type).validate_python(expected)
        assert type(result) is type(typed)
        assert native_normalized(result) == native_normalized(typed)


def native_matrix_handler(key, example, arguments, asynchronous, status=200, error=None):
    method, template, _ = NATIVE_CONTRACTS[key]
    path = '/api/v2' + template
    for alias, argument in NATIVE_PATH_ALIASES.items():
        if '{' + alias + '}' in path:
            path = path.replace('{' + alias + '}', quote(arguments[argument], safe=''))
    expected_query = dict(NATIVE_QUERY.get(key, {}))
    if 'preview' in arguments:
        expected_query['preview'] = True
    success = native_success(key)
    payload = (success if isinstance(success, bytes) else b'' if success is None
               else json.dumps(success).encode()) if error is None else json.dumps(error).encode()
    body = (NativeAsyncBody if asynchronous else NativeSyncBody)(payload)
    calls = []

    def handler(request):
        assert request.method == method
        assert request.url.raw_path.split(b'?')[0].decode() == path
        assert request.url.params == httpx.QueryParams(expected_query)
        assert request.headers['Authorization'] == 'Bearer native-secret-token'
        headers = {'Accept': '*/*' if NATIVE_CONTRACTS[key][2] is bytes else 'application/json'}
        if NATIVE_CONTRACTS[key][2] is None:
            headers = {}
        if key in NATIVE_JSON_BODIES:
            headers['Content-Type'] = 'application/json'
        if key.endswith(('.upload', '.upload_media')):
            headers['Content-Type'] = '*/*'
        if key == 'widgets.Repository.publish':
            headers['Content-Type'] = 'application/octet-stream'
        for header, value in headers.items():
            assert request.headers[header] == value
        for header in ('ReadToken', 'Token', 'Attribution'):
            assert header not in request.headers
        expected_body = NATIVE_JSON_BODIES.get(key)
        if key.endswith(('.upload', '.upload_media')):
            import hashlib
            assert hashlib.sha256(request.content).hexdigest() == 'b1ff9c8ea3a780bad09b346c423d2d0e46815926879b18e841d928376a946640'
            assert int(request.headers['Content-Length']) == 69
        elif key == 'widgets.Repository.publish':
            from io import BytesIO
            from zipfile import ZipFile
            with ZipFile(BytesIO(request.content)) as archive:
                assert archive.namelist() == ['.palantir/widgets.config.json', 'counter.html', 'summary.html']
                assert json.loads(archive.read('.palantir/widgets.config.json')) == {'widgets': []}
                assert archive.read('counter.html') == b'<!doctype html><title>Counter fixture</title>'
                assert archive.read('summary.html') == b'<!doctype html><title>Summary fixture</title>'
            assert int(request.headers['Content-Length']) == len(request.content)
        elif expected_body is None:
            assert request.content == b''
        else:
            assert json.loads(request.content) == expected_body
        assert set(request.extensions['timeout'].values()) == {11}
        calls.append(request)
        return httpx.Response(204 if success is None and status == 200 else status, stream=body)

    return handler, body, calls, payload


NATIVE_MODES = [
    (key, asynchronous, mode)
    for key, (_, _, result_type) in NATIVE_CONTRACTS.items()
    for asynchronous in (False, True)
    for mode in (('ordinary', 'raw') if result_type is None else ('ordinary', 'raw', 'stream'))
]


@pytest.mark.parametrize('key,asynchronous,mode', NATIVE_MODES,
                         ids=[f'v2.{k}-{a}-{m}' for k, a, m in NATIVE_MODES])
def test_native_all_owned_operation_modes(key, asynchronous, mode, native_event_loop):
    example, arguments, sync_type, async_type, method = native_operation(key)
    arguments['request_timeout'] = 11
    if 'preview' in inspect.signature(getattr(sync_type, method)).parameters:
        arguments['preview'] = True
    handler, body, calls, payload = native_matrix_handler(key, example, arguments, asynchronous)

    def target(client):
        assert hasattr(client.with_raw_response, method)
        assert hasattr(client.with_streaming_response, method) == (NATIVE_CONTRACTS[key][2] is not None)
        assert not hasattr(client, 'with_sse_response')
        return client if mode == 'ordinary' else getattr(
            client, 'with_raw_response' if mode == 'raw' else 'with_streaming_response')

    async def exercise_async():
        async with native_async_resource(async_type, handler) as client:
            result = getattr(target(client), method)(**arguments)
            if mode == 'stream':
                assert not inspect.isawaitable(result)
                async with result as response:
                    assert body.reads == 0
                    assert b''.join([chunk async for chunk in response.aiter_bytes()]) == payload
            elif mode == 'ordinary' and key == 'widgets.Release.list':
                assert not inspect.isawaitable(result)
                native_validate_result(key, [item async for item in result], example['SUCCESS'], pager=True)
            else:
                assert inspect.isawaitable(result)
                result = await result
                if mode == 'raw':
                    try:
                        native_validate_result(key, result.decode(), example['SUCCESS'])
                    finally:
                        await result.aclose()
                else:
                    native_validate_result(key, result, example['SUCCESS'])

    if asynchronous:
        native_event_loop.run_until_complete(exercise_async())
    else:
        with native_sync_resource(sync_type, handler) as client:
            result = getattr(target(client), method)(**arguments)
            if mode == 'stream':
                assert body.reads == 0
                with result as response:
                    assert b''.join(response.iter_bytes()) == payload
            elif mode == 'raw':
                try:
                    native_validate_result(key, result.decode(), example['SUCCESS'])
                finally:
                    result.close()
            elif key == 'widgets.Release.list':
                native_validate_result(key, list(result), example['SUCCESS'], pager=True)
            else:
                native_validate_result(key, result, example['SUCCESS'])
    assert len(calls) == 1
    assert body.closed


# These wire fixtures belong to this test, independently of reader EXPECTED_* data.
NATIVE_SYNTHETIC = 'ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001'
NATIVE_WIDGET = 'ri.widgets.main.widget-set.00000000-0000-0000-0000-000000000001'
NATIVE_WIDGET_ID = 'ri.widgets.main.widget.00000000-0000-0000-0000-000000000002'
NATIVE_SCRIPT = {'filePath': 'assets/inspection.js', 'scriptType': 'MODULE'}
NATIVE_STYLE = {'filePath': 'assets/inspection.css'}
NATIVE_SETTINGS = {
    'baseHref': 'http://localhost:5173/',
    'widgetSettings': {'inspection-summary': {
        'scriptEntrypoints': [NATIVE_SCRIPT], 'stylesheetEntrypoints': [NATIVE_STYLE]}},
}
NATIVE_MANIFEST = {
    'manifestVersion': '1.0.0', 'devSettings': {
        'baseHref': 'http://localhost:5173/', 'widgets': {'inspection-summary': {
            'id': 'inspection-summary', 'name': 'Inspection summary', 'type': 'workshopWidgetV1',
            'entrypointJs': [{'path': 'http://localhost:5173/assets/inspection.js', 'type': 'module'}],
            'entrypointCss': [{'path': 'http://localhost:5173/assets/inspection.css'}],
            'parameters': {}, 'events': {}}}, 'inputSpec': {'discovered': {'sdks': []}}},
}
NATIVE_JSON_BODIES = {
    'media_sets.MediaSet.register': {'physicalItemName': 'inspections/pixel.png'},
    'media_sets.MediaSet.transform': {'transformation': {
        'operation': {'outputFormat': 'TEXT', 'type': 'getEmailBody'}, 'type': 'emailToText'}},
    'widgets.DevModeSettings.set_widget_set_by_id': {
        'widgetSetRid': NATIVE_WIDGET, 'settings': NATIVE_SETTINGS},
    'widgets.DevModeSettingsV2.set_widget_set_manifest': {
        'widgetSetRid': NATIVE_WIDGET, 'manifest': NATIVE_MANIFEST},
}
NATIVE_QUERY = {
    'media_sets.MediaSet.clear': {'mediaItemPath': 'synthetic-value'},
    'media_sets.MediaSet.get_rid_by_path': {'mediaItemPath': 'inspections/pixel.png'},
    'media_sets.MediaSet.upload_media': {'filename': 'pixel.png'},
    'widgets.Repository.publish': {'repositoryVersion': 'synthetic-value'},
}


def native_success(key):
    method = key.split('.')[-1]
    if NATIVE_CONTRACTS[key][2] is None:
        return None
    if NATIVE_CONTRACTS[key][2] is bytes:
        return b'\x00\xff\x80native-media\x00'
    if key.startswith('media_sets.'):
        reference = {'mimeType': 'image/png', 'reference': {'type': 'mediaSetViewItem',
                     'mediaSetViewItem': {'mediaSetRid': NATIVE_SYNTHETIC,
                                          'mediaSetViewRid': NATIVE_SYNTHETIC,
                                          'mediaItemRid': NATIVE_SYNTHETIC}}}
        return {
            'calculate': {'type': 'pending'},
            'create': '00000000-0000-0000-0000-000000000001',
            'get': {'rid': NATIVE_SYNTHETIC, 'mediaSchema': 'AUDIO',
                    'defaultBranchName': 'synthetic-value',
                    'transactionPolicy': {'type': 'batchTransactions'}, 'pathsRequired': True},
            'get_rid_by_path': {'mediaItemRid': NATIVE_ITEM_RID},
            'get_status': {'status': 'PENDING', 'jobId': 'synthetic-value'},
            'info': {'viewRid': NATIVE_SYNTHETIC, 'logicalTimestamp': '1'},
            'metadata': {'format': 'PDF', 'sizeBytes': 1, 'type': 'document'},
            'reference': reference, 'upload_media': reference,
            'register': {'mediaItemRid': NATIVE_SYNTHETIC, 'mediaType': 'image/png'},
            'transform': {'status': 'PENDING', 'jobId': 'synthetic-value'},
            'upload': {'mediaItemRid': NATIVE_SYNTHETIC, 'mediaSetViewRid': NATIVE_SYNTHETIC},
        }[method]
    release = {'widgetSetRid': NATIVE_SYNTHETIC, 'version': 'synthetic-value',
               'locator': {'repositoryRid': NATIVE_SYNTHETIC, 'repositoryVersion': 'synthetic-value'}}
    if key == 'widgets.Release.list':
        return {'data': [release]}
    if key.startswith('widgets.Release.') or method == 'publish':
        return release
    if '.Repository.' in key or '.WidgetSet.' in key:
        return {'rid': NATIVE_SYNTHETIC}
    if '.DevModeSettingsV2.' in key:
        return {'status': 'ENABLED'}
    settings = {} if method == 'enable' else {NATIVE_WIDGET: {
        'baseHref': 'http://localhost:5173/', 'widgetSettings': {NATIVE_WIDGET_ID: {
            'scriptEntrypoints': [NATIVE_SCRIPT], 'stylesheetEntrypoints': [NATIVE_STYLE]}}}}
    return {'status': 'ENABLED', 'widgetSetSettings': settings}


NATIVE_NAMED_ERRORS = [
    ('widgets.DevModeSettings.enable', 'EnableDevModeSettingsPermissionDenied', 403, {}),
    ('widgets.DevModeSettings.set_widget_set_by_id', 'SetWidgetSetDevModeSettingsByIdPermissionDenied', 403, {}),
    ('widgets.DevModeSettingsV2.enable', 'EnableDevModeSettingsV2PermissionDenied', 403, {}),
    *[('widgets.DevModeSettingsV2.set_widget_set_manifest', name, 400, parameters)
      for name, parameters in [
          ('InvalidDevModeBaseHref', {'baseHref': 'synthetic-value'}),
          ('InvalidDevModeEntrypointCssCount', {'reason': 'synthetic-value', 'entrypointCssCount': 1}),
          ('InvalidDevModeEntrypointJsCount', {'reason': 'synthetic-value', 'entrypointJsCount': 1}),
          ('InvalidDevModeFilePath', {'reason': 'synthetic-value', 'filePath': 'synthetic-value'}),
          ('InvalidDevModeWidgetSettingsCount', {'reason': 'synthetic-value', 'widgetSettingsCount': 1}),
          ('InvalidManifest', {'reason': 'synthetic-value'}),
      ]],
    ('widgets.DevModeSettingsV2.set_widget_set_manifest', 'SetWidgetSetManifestDevModeSettingsV2PermissionDenied', 403, {}),
    ('widgets.DevModeSettingsV2.set_widget_set_manifest', 'WidgetIdNotFound', 404,
     {'widgetSetRid': NATIVE_WIDGET, 'widgetId': 'synthetic-value'}),
    ('widgets.Release.delete', 'DeleteReleasePermissionDenied', 403,
     {'widgetSetRid': NATIVE_SYNTHETIC, 'releaseVersion': 'synthetic-value'}),
    ('widgets.Release.get', 'ReleaseNotFound', 404,
     {'widgetSetRid': NATIVE_SYNTHETIC, 'releaseVersion': 'synthetic-value'}),
    ('widgets.Repository.get', 'RepositoryNotFound', 404, {'repositoryRid': NATIVE_SYNTHETIC}),
    ('widgets.Repository.publish', 'PublishReleasePermissionDenied', 403, {'repositoryRid': NATIVE_SYNTHETIC}),
    ('widgets.WidgetSet.get', 'WidgetSetNotFound', 404, {'widgetSetRid': NATIVE_SYNTHETIC}),
]
NATIVE_ERROR_MODES = [
    (key, name, status, parameters, asynchronous, mode)
    for key, name, status, parameters in NATIVE_NAMED_ERRORS
    for operation, asynchronous, mode in NATIVE_MODES if operation == key
]


def native_error_exercise(key, asynchronous, mode, status, error, loop):
    example, arguments, sync_type, async_type, method = native_operation(key)
    arguments.update(preview=True, request_timeout=11)
    handler, body, calls, _ = native_matrix_handler(key, example, arguments, asynchronous, status, error)

    def target(client):
        return client if mode == 'ordinary' else getattr(
            client, 'with_raw_response' if mode == 'raw' else 'with_streaming_response')

    async def exercise():
        async with native_async_resource(async_type, handler) as client:
            result = getattr(target(client), method)(**arguments)
            if mode == 'stream':
                async with result:
                    raise AssertionError('HTTP error must stop context entry')
            elif mode == 'ordinary' and key == 'widgets.Release.list':
                await result.__anext__()
            else:
                await result

    from foundry_sdk._errors.palantir_qos_exception import RateLimitError
    with pytest.raises(RateLimitError if status == 429 else PalantirRPCException) as caught:
        if asynchronous:
            loop.run_until_complete(exercise())
        else:
            with native_sync_resource(sync_type, handler) as client:
                result = getattr(target(client), method)(**arguments)
                if mode == 'stream':
                    with result:
                        raise AssertionError('HTTP error must stop context entry')
                elif mode == 'ordinary' and key == 'widgets.Release.list':
                    next(result)
    assert len(calls) == 1  # Config propagates 429/503; max_retries=1 is the actual SDK policy.
    assert body.closed
    if status == 429:
        assert type(caught.value) is RateLimitError
        assert caught.value.reason == 'client-qos-response'
    else:
        assert caught.value.name == error['errorName']
        assert native_normalized(caught.value.parameters) == error['parameters']
        assert caught.value.error_instance_id == error['errorInstanceId']
    return caught.value


@pytest.mark.parametrize('key,name,status,parameters,asynchronous,mode', NATIVE_ERROR_MODES)
def test_native_declared_error_modes(key, name, status, parameters, asynchronous, mode, native_event_loop):
    error = {'errorName': name, 'errorCode': {400: 'INVALID_ARGUMENT', 403: 'PERMISSION_DENIED', 404: 'NOT_FOUND'}[status],
             'parameters': parameters, 'errorInstanceId': '00000000-0000-0000-0000-000000000004'}
    result = native_error_exercise(key, asynchronous, mode, status, error, native_event_loop)
    assert type(result) is getattr(widget_errors, name)


@pytest.mark.parametrize('key,asynchronous,mode', NATIVE_MODES)
@pytest.mark.parametrize('status,code', [(401, 'UNAUTHORIZED'), (403, 'PERMISSION_DENIED'), (429, 'CUSTOM_CLIENT')])
def test_native_generic_denial_modes(key, asynchronous, mode, status, code, native_event_loop):
    result = native_error_exercise(key, asynchronous, mode, status, {
        'errorName': 'NativeOfflineDenied', 'errorCode': code, 'parameters': {},
        'errorInstanceId': '00000000-0000-0000-0000-000000000005'}, native_event_loop)
    from foundry_sdk._errors.palantir_rpc_exception import PermissionDeniedError, UnauthorizedError
    if status != 429:
        assert type(result) is (UnauthorizedError if status == 401 else PermissionDeniedError)


NATIVE_UNIONS = [
    *[('calculate', {'type': tag}, 'TrackedTransformation' + name + 'Response')
      for tag, name in [('pending', 'Pending'), ('failed', 'Failed'), ('successful', 'Successful')]],
    ('metadata', {'type': 'document', 'format': 'PDF', 'sizeBytes': 17}, 'DocumentMediaItemMetadata'),
    ('metadata', {'type': 'imagery', 'format': 'PNG', 'sizeBytes': 69,
                  'dimensions': {'width': 1, 'height': 1}, 'bands': [], 'attributes': {}}, 'ImageryMediaItemMetadata'),
    ('metadata', {'type': 'spreadsheet', 'format': 'XLSX', 'sizeBytes': 1, 'sheetNames': ['Sheet1']}, 'SpreadsheetMediaItemMetadata'),
    ('metadata', {'type': 'untyped', 'sizeBytes': 1}, 'UntypedMediaItemMetadata'),
    ('metadata', {'type': 'audio', 'format': 'WAV', 'sizeBytes': 1,
                  'specification': {'bitRate': 128000, 'durationSeconds': 1.25}}, 'AudioMediaItemMetadata'),
    ('metadata', {'type': 'video', 'format': 'MP4', 'sizeBytes': 1,
                  'specification': {'bitRate': 128000, 'durationSeconds': 1.25}}, 'VideoMediaItemMetadata'),
    ('metadata', {'type': 'model3d', 'format': 'OBJ', 'modelType': 'MESH', 'sizeBytes': 1}, 'Model3dMediaItemMetadata'),
    ('metadata', {'type': 'dicom', 'sizeBytes': 1, 'mediaType': 'IMAGE', 'metaInformation': {
        'type': 'v1', 'mediaStorageSop': '1.2.840.10008.5.1.4.1.1.2',
        'mediaStorageSopInstance': '1.2.3', 'transferSyntax': '1.2.840.10008.1.2'},
        'commonDataElements': {}, 'otherDataElements': {}}, 'DicomMediaItemMetadata'),
    ('metadata', {'type': 'email', 'format': 'EML', 'sizeBytes': 1, 'sender': [],
                  'date': '2026-11-19T00:00:00+00:00', 'attachmentCount': 0,
                  'to': [], 'cc': [], 'attachments': []}, 'EmailMediaItemMetadata'),
    ('info', {'viewRid': NATIVE_SYNTHETIC, 'logicalTimestamp': '9'}, 'GetMediaItemInfoResponse'),
    ('info', {'viewRid': NATIVE_SYNTHETIC, 'logicalTimestamp': '9', 'path': None}, 'GetMediaItemInfoResponse'),
    ('get_rid_by_path', {}, 'GetMediaItemRidByPathResponse'),
    ('get_rid_by_path', {'mediaItemRid': None}, 'GetMediaItemRidByPathResponse'),
]


@pytest.mark.parametrize('method,payload,class_name', NATIVE_UNIONS)
@pytest.mark.parametrize('asynchronous', [False, True])
@pytest.mark.parametrize('raw', [False, True])
def test_native_union_and_nullable_decoding(method, payload, class_name, asynchronous, raw, native_event_loop):
    _, arguments, sync_type, async_type, _ = native_operation('media_sets.MediaSet.' + method)
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(200, json=payload)

    async def exercise():
        async with native_async_resource(async_type, handler) as client:
            result = await getattr(client.with_raw_response if raw else client, method)(**arguments)
            if raw:
                try:
                    return result.decode()
                finally:
                    await result.aclose()
            return result

    if asynchronous:
        result = native_event_loop.run_until_complete(exercise())
    else:
        with native_sync_resource(sync_type, handler) as client:
            result = getattr(client.with_raw_response if raw else client, method)(**arguments)
            if raw:
                response = result
                try:
                    result = response.decode()
                finally:
                    response.close()
    assert len(calls) == 1
    assert type(result) is getattr(media, class_name)
    assert native_normalized(result) == {k: v for k, v in payload.items() if v is not None}
    if method == 'info':
        assert result.path is None
    if method == 'get_rid_by_path':
        assert result.media_item_rid is None


@pytest.mark.parametrize('union', [media.TrackedTransformationResponse, media.MediaItemMetadata])
def test_native_union_rejects_unknown_discriminator(union):
    with pytest.raises(ValidationError, match='union_tag_invalid'):
        TypeAdapter(union).validate_python({'type': 'invented'})


@pytest.mark.parametrize('asynchronous', [False, True])
@pytest.mark.parametrize('preview', [None, False, True])
def test_native_preview_is_serialized_without_invented_client_access_guard(asynchronous, preview, native_event_loop):
    calls = []

    def handler(request):
        assert request.url.params == httpx.QueryParams({} if preview is None else {'preview': preview})
        calls.append(request)
        return httpx.Response(200, json=NATIVE_GET)

    async def exercise():
        async with native_async_resource(AsyncMediaSetClient, handler) as client:
            return await client.get(NATIVE_MEDIA_RID, preview=preview)

    if asynchronous:
        result = native_event_loop.run_until_complete(exercise())
    else:
        with native_sync_resource(MediaSetClient, handler) as client:
            result = client.get(NATIVE_MEDIA_RID, preview=preview)
    assert native_normalized(result) == NATIVE_GET
    assert len(calls) == 1


@pytest.mark.parametrize('asynchronous', [False, True])
def test_native_ordinary_pager_crosses_empty_intermediate_page(asynchronous, native_event_loop):
    tokens = []
    pages = [
        {'data': [dict(NATIVE_RELEASE, version='1.0.0')], 'nextPageToken': 'page-2'},
        {'data': [], 'nextPageToken': 'page-3'},
        {'data': [dict(NATIVE_RELEASE, version='3.0.0')]},
    ]

    def handler(request):
        assert len(tokens) < 3, 'finite fixture has only three pages'
        tokens.append(request.url.params.get('pageToken'))
        assert request.url.params['pageSize'] == '2'
        return httpx.Response(200, json=pages[len(tokens) - 1])

    async def exercise():
        async with native_async_resource(AsyncReleaseClient, handler) as client:
            iterator = client.list(NATIVE_RID, page_size=2)
            assert not inspect.isawaitable(iterator) and tokens == []
            return [item.version async for item in iterator]

    if asynchronous:
        result = native_event_loop.run_until_complete(exercise())
    else:
        with native_sync_resource(ReleaseClient, handler) as client:
            iterator = client.list(NATIVE_RID, page_size=2)
            assert tokens == [None]
            result = [item.version for item in iterator]
    assert result == ['1.0.0', '3.0.0']
    assert tokens == [None, 'page-2', 'page-3']


@pytest.mark.parametrize('asynchronous', [False, True])
@pytest.mark.parametrize('scenario', ['repeat', 'empty'])
def test_native_raw_pager_caller_bounds_requests(asynchronous, scenario, native_event_loop):
    calls = []

    def handler(request):
        assert len(calls) < 3, 'caller budget must stop before fourth request'
        calls.append(request.url.params.get('pageToken'))
        token = 'repeat-token' if scenario == 'repeat' else f'empty-{len(calls)}'
        return httpx.Response(200, json={'data': [], 'nextPageToken': token})

    async def exercise():
        token, seen = None, set()
        async with native_async_resource(AsyncReleaseClient, handler) as client:
            for _ in range(3):
                response = await client.with_raw_response.list(NATIVE_RID, page_token=token)
                try:
                    page = response.decode()
                finally:
                    await response.aclose()
                assert page.data == []
                token = page.next_page_token
                if token is None or token in seen:
                    break
                seen.add(token)

    if asynchronous:
        native_event_loop.run_until_complete(exercise())
    else:
        token, seen = None, set()
        with native_sync_resource(ReleaseClient, handler) as client:
            for _ in range(3):
                response = client.with_raw_response.list(NATIVE_RID, page_token=token)
                try:
                    page = response.decode()
                finally:
                    response.close()
                assert page.data == []
                token = page.next_page_token
                if token is None or token in seen:
                    break
                seen.add(token)
    assert calls == ([None, 'repeat-token'] if scenario == 'repeat' else [None, 'empty-1', 'empty-2'])


def test_native_sync_context_abort_closes_unread_body():
    handler, body, calls, _ = native_pilot_handler(NATIVE_PILOTS[1], False)
    with native_sync_resource(MediaSetClient, handler) as client:
        with pytest.raises(RuntimeError, match='caller abort'):
            with client.with_streaming_response.read(NATIVE_MEDIA_RID, NATIVE_ITEM_RID, preview=True, request_timeout=11):
                assert body.reads == 0
                raise RuntimeError('caller abort')
    assert len(calls) == 1 and body.closed and body.reads == 0


def test_native_async_task_cancellation_closes_stream(native_event_loop):
    async def exercise():
        entered = asyncio.Event()

        class WaitingBody(NativeAsyncBody):
            async def __aiter__(self):
                self.reads += 1
                entered.set()
                await asyncio.Future()
                yield self.payload

        body = WaitingBody(b'\xff\x00')
        calls = []

        def handler(request):
            calls.append(request)
            return httpx.Response(200, stream=body)

        async with native_async_resource(AsyncMediaSetClient, handler) as client:
            async def consume():
                async with client.with_streaming_response.read(NATIVE_MEDIA_RID, NATIVE_ITEM_RID) as response:
                    assert body.reads == 0
                    async for _ in response.aiter_bytes():
                        raise AssertionError('waiting stream must not yield')

            task = asyncio.create_task(consume())
            await asyncio.wait_for(entered.wait(), timeout=1)
            task.cancel()
            with pytest.raises(asyncio.CancelledError):
                await task
            assert task.cancelled()
        assert len(calls) == 1 and body.closed and body.reads == 1

    native_event_loop.run_until_complete(exercise())


def test_native_declared_error_ledger_equals_actual_sdk_maps():
    import ast
    import textwrap

    for key in NATIVE_CONTRACTS:
        _, _, sync_type, _, method = native_operation(key)
        tree = ast.parse(textwrap.dedent(inspect.getsource(getattr(sync_type, method))))
        maps = [keyword.value for node in ast.walk(tree) if isinstance(node, ast.Call)
                for keyword in node.keywords if keyword.arg == 'throwable_errors']
        assert len(maps) == 1
        actual = {value.value for value in maps[0].keys}
        assert actual == {name for operation, name, _, _ in NATIVE_NAMED_ERRORS if operation == key}


@pytest.mark.parametrize('fault', ['route', 'body', 'credential', 'prebuffer', 'async_close', 'async_iterator', 'upload_guard'])
def test_native_fault_controls_detect_contract_regressions(fault, monkeypatch, native_event_loop):
    from foundry_sdk._core.api_client import ApiClient
    from foundry_sdk._errors.sdk_internal_error import SDKInternalError

    with monkeypatch.context() as mutation:
        if fault == 'route':
            original = ApiClient._create_url
            mutation.setattr(ApiClient, '_create_url', lambda self, request: original(self, request) + '/wrong')
        elif fault == 'body':
            original = ApiClient._serialize
            mutation.setattr(ApiClient, '_serialize', lambda self, body: b'{"wrong":true}' if body is not None else original(self, body))
        elif fault == 'credential':
            original = ApiClient._create_headers

            def headers(self, request, token):
                result = original(self, request, token)
                result['Authorization'] = 'Bearer wrong-token'
                return result

            mutation.setattr(ApiClient, '_create_headers', headers)
        elif fault == 'prebuffer':
            original = NativeSyncBody.__init__

            def prebuffer(self, payload):
                original(self, payload)
                b''.join(self)

            mutation.setattr(NativeSyncBody, '__init__', prebuffer)
        elif fault == 'async_close':
            async def no_close(self):
                pass

            mutation.setattr(NativeAsyncBody, 'aclose', no_close)
        elif fault == 'async_iterator':
            original = AsyncReleaseClient.list

            async def awaited_iterator(self, *args, **kwargs):
                return original(self, *args, **kwargs)

            # Close the deliberately wrong coroutine immediately to avoid warning leakage.
            def wrong_form(self, *args, **kwargs):
                result = awaited_iterator(self, *args, **kwargs)
                result.close()
                return result

            mutation.setattr(AsyncReleaseClient, 'list', wrong_form)
        elif fault == 'upload_guard':
            original_load = load

            def no_guard(*args):
                example = original_load(*args)
                example['require_verified_upload'] = lambda **kwargs: None
                return example

            mutation.setitem(globals(), 'load', no_guard)

        with pytest.raises((AssertionError, pytest.fail.Exception, SDKInternalError)) as detected:
            if fault == 'async_close':
                test_native_pilot_async_modes(NATIVE_PILOTS[1], 'stream', native_event_loop)
            elif fault == 'async_iterator':
                test_native_pilot_async_modes(NATIVE_PILOTS[2], 'ordinary', native_event_loop)
            elif fault == 'upload_guard':
                test_binary_png_and_sdk_upload_discrepancy_have_explicit_preflight('upload')
            else:
                key = 'media_sets.MediaSet.register' if fault == 'body' else 'media_sets.MediaSet.read'
                test_native_all_owned_operation_modes(key, False, 'stream' if fault == 'prebuffer' else 'ordinary', native_event_loop)
        if isinstance(detected.value, SDKInternalError):
            assert isinstance(detected.value.__cause__, AssertionError)
