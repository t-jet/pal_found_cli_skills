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
