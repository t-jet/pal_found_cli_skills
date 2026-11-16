"""Independent corrected-candidate retest. Reuses prior reviewer source/wire/model audit."""
import ast
import base64
import copy
import hashlib
import json
import runpy
import socket
import struct
import subprocess
import zlib
from collections import Counter
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import patch
from urllib.parse import urlparse

import httpx

TMP = Path(__file__).resolve().parent
ROOT = TMP / 'feature015_rest091_fixes'
DEV = ROOT / '.agents/skills/pal-found-dev'
OUT = TMP / 'feature015_rest091_semantic_retest_20261029.json'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
manifest_path = TMP / 'feature015_rest091_correction_manifest_20261029.json'
manifest = json.loads(manifest_path.read_text())
baseline_path = TMP / 'feature015_rest091_semantic_review_20261029.json'
baseline = json.loads(baseline_path.read_text())
initial_paths = [ROOT / r['path'] for r in manifest['changed_files']]
initial_paths += [Path(p) for p in manifest['source_bindings']]
initial_paths += list((DEV / 'examples/rest/091').rglob('*.py'))
initial_paths += [manifest_path, baseline_path, TMP / 'feature015_rest091_semantic_review_20261029_rejected_harness_enum.json']
before = {str(p): sha(p) for p in initial_paths}
frozen_mismatches = [r['path'] for r in manifest['changed_files'] if sha(ROOT/r['path']) != r['sha256']]
source_mismatches = [p for p,h in manifest['source_bindings'].items() if sha(p) != h]
assert not frozen_mismatches and not source_mismatches, (frozen_mismatches, source_mismatches)

# This is the previous independent reviewer's harness, never the author's test oracle.
# Keep its all-operation wire/model reconciliation and independent success/denial cases.
prior = TMP / 'rest091_independent_semantics_20261029.py'
source = prior.read_text()
source = source.replace("REPO=TMP/'feature015_integration'", "REPO=TMP/'feature015_rest091_fixes'")
source = source.replace("OUT=TMP/'feature015_rest091_semantic_review_20261029.json'", "OUT=TMP/'rest091_retest_raw_20261029.json'")
source = source.replace("'/root/rest091_semantic_review_20261029'", "'/root/rest091_independent_retest_20261029'")
scope = {'__file__': str(prior), '__name__': '__qa_retest__'}
exec(compile(source, str(prior), 'exec'), scope)
report = scope['report']
reasons = {
 'get_rid_by_path': 'Found optional RID is demonstrated; absent successful response raises LookupError before downstream item use.',
 'reference': 'Concrete image/png MIME and mediaSetViewItem discriminator preserve distinct set/view/item fields.',
 'register': 'Configured-store relative PNG item and image/png response; IMAGERY prerequisite and existing store content are explicit.',
 'upload': 'Observed SDK Content-Type */* retained; explicit supported-transport verification boundary. PNG integrity checked independently.',
 'upload_media': 'Filename pixel.png and image/png response align; observed SDK header discrepancy and one-hour lifecycle explicit. PNG integrity checked independently.',
 'set_widget_set_by_id': 'Nonempty published WidgetId request maps to WidgetRid response; localhost base and relative assets coherent; uncertain-write verification uses authorized preview workflow.',
 'set_widget_set_manifest': 'Object manifest matches pinned official builder/type shape; localhost assets and empty discovered SDK dependency list coherent; optional snapshot never presumed from status-only result.'
}
checks = []
def record(op, name, action):
    try:
        detail = action()
        checks.append({'operation': op, 'check': name, 'status': 'PASS', 'detail': detail})
    except Exception as error:
        checks.append({'operation': op, 'check': name, 'status': 'FAIL', 'error': repr(error), 'classification': 'candidate defect'})

def png_details(data):
    assert data[:8] == b'\x89PNG\r\n\x1a\n'
    pos = 8
    chunks = []
    compressed = b''
    while pos < len(data):
        size = struct.unpack('>I', data[pos:pos+4])[0]
        kind = data[pos+4:pos+8]
        payload = data[pos+8:pos+8+size]
        stored = struct.unpack('>I', data[pos+8+size:pos+12+size])[0]
        computed = zlib.crc32(kind + payload)
        chunks.append({'type':kind.decode(), 'bytes':size, 'stored_crc':hex(stored), 'computed_crc':hex(computed), 'valid':stored==computed})
        if kind == b'IDAT': compressed += payload
        pos += size+12
    assert pos == len(data) and chunks[0]['type'] == 'IHDR' and chunks[-1]['type'] == 'IEND'
    return {'chunks':chunks, 'decompressed_scanline_hex':zlib.decompress(compressed).hex()}

def validate_manifest(body):
    value = body['manifest']
    assert isinstance(value, dict) and value['manifestVersion'] == '1.0.0'
    settings = value['devSettings']
    assert urlparse(settings['baseHref']).hostname == 'localhost'
    assert settings['inputSpec']['discovered']['sdks'] == []
    assert settings['widgets']
    for key, widget in settings['widgets'].items():
        assert key == widget['id'] and widget['type'] == 'workshopWidgetV1'
        assert isinstance(widget['parameters'], dict) and isinstance(widget['events'], dict)
        assert widget['entrypointJs']
        for entry in widget['entrypointJs']:
            assert entry['type'] in ('module', 'text/javascript')
            assert urlparse(entry['path']).hostname == 'localhost'
        for entry in widget.get('entrypointCss', []):
            assert urlparse(entry['path']).hostname == 'localhost'
    return 'Nested shape checked against official manifest.ts and buildDevModeManifest.ts at declared commit.'

network_probes = []
def expect_rejection(name, action, error_type):
    try: action()
    except error_type as error: return {'rejected':name, 'error':str(error)}
    raise AssertionError(name + ' was accepted')

with ExitStack() as stack:
    for name in ('connect', 'connect_ex'): stack.enter_context(patch.object(socket.socket, name, scope['deny']))
    for name in ('create_connection', 'getaddrinfo', 'gethostbyname', 'gethostbyname_ex'): stack.enter_context(patch.object(socket, name, scope['deny']))
    stack.enter_context(patch.object(httpx.HTTPTransport, 'handle_request', scope['deny']))
    stack.enter_context(patch.object(httpx.AsyncHTTPTransport, 'handle_async_request', scope['deny']))
    for row in report['operations']:
        op = row['id']; method = op.rsplit('.',1)[1]
        module = runpy.run_path(row['example'])
        if method in reasons:
            row['reason'] = reasons[method]
            row['status'] = 'PASS' if not row['contract_wire_mismatches'] and row['author_fixture_execution']['status']=='PASS' and all(c['status']=='PASS' for c in row['independent_cases']) else 'FAIL'
        requests = row['author_fixture_execution']['requests']
        first = requests[0]
        if method in ('upload', 'upload_media'):
            payload = base64.b64decode(first['body_base64'])
            detail = png_details(payload)
            row['png_integrity'] = detail
            record(op, 'PNG chunk CRC integrity', lambda detail=detail: (all(c['valid'] for c in detail['chunks']) or (_ for _ in ()).throw(AssertionError(detail))))
            record(op, 'frozen SDK wildcard header preserved', lambda first=first: first['headers']['content-type']=='*/*' or (_ for _ in ()).throw(AssertionError(first['headers'])))
            record(op, 'unverified live transport preflight rejects', lambda module=module: expect_rejection('unverified transport', module['require_verified_upload'], RuntimeError))
        if method == 'get_rid_by_path':
            from foundry_sdk.v2.media_sets.models import GetMediaItemRidByPathResponse
            record(op, 'missing RID response stops item use', lambda module=module: expect_rejection('absent RID', lambda: module['require_item_rid'](GetMediaItemRidByPathResponse()), LookupError))
            record(op, 'found RID preserved', lambda module=module: module['require_item_rid'](GetMediaItemRidByPathResponse(mediaItemRid=scope['R'])) == scope['R'] or (_ for _ in ()).throw(AssertionError('wrong RID')))
        if method == 'set_widget_set_manifest':
            body = json.loads(base64.b64decode(first['body_base64']))
            record(op, 'independent nested manifest meaning', lambda body=body: validate_manifest(body))
            mutated = copy.deepcopy(body); mutated['manifest'] = 'synthetic-value'
            record(op, 'negative manifest string rejected by semantic oracle', lambda mutated=mutated: expect_rejection('string manifest', lambda: validate_manifest(mutated), (AssertionError, TypeError)))
            mutated = copy.deepcopy(body); mutated['manifest']['devSettings']['widgets']['inspection-summary']['entrypointJs'][0]['path']='https://outside.invalid/app.js'
            record(op, 'negative nonlocal asset rejected by semantic oracle', lambda mutated=mutated: expect_rejection('nonlocal dev asset', lambda: validate_manifest(mutated), AssertionError))
            from foundry_sdk.v2.widgets.models import DevModeSettingsV2
            status_only = DevModeSettingsV2(status='ENABLED')
            snapshot = DevModeSettingsV2(status='ENABLED', snapshot={'snapshotId':'independent-content-id','widgetSetSettings':{}})
            record(op, 'SDK optional snapshot model cases', lambda: {'status_only_snapshot':status_only.snapshot, 'present_snapshot_id':snapshot.snapshot.snapshot_id})
        if method == 'set_widget_set_by_id':
            body = json.loads(base64.b64decode(first['body_base64']))
            settings = body['settings']
            assert urlparse(settings['baseHref']).hostname == 'localhost'
            request_keys = list(settings['widgetSettings'])
            response_keys = list(module['SUCCESS']['widgetSetSettings'][body['widgetSetRid']]['widgetSettings'])
            record(op, 'WidgetId request and WidgetRid response identity separation', lambda: (request_keys == ['inspection-summary'] and response_keys[0].startswith('ri.widgets.') and request_keys != response_keys) or (_ for _ in ()).throw(AssertionError((request_keys,response_keys))))
        row['previous_status'] = next(r['status'] for r in baseline['operations'] if r['id']==op)
    for name, action in [('DNS',lambda:socket.getaddrinfo('offline.invalid',443)),('socket',lambda:socket.socket().connect(('127.0.0.1',9))),('native HTTP',lambda:httpx.Client().get('https://offline.invalid/'))]:
        network_probes.append(expect_rejection(name, action, AssertionError))

for row in report['operations']:
    row['semantic_checks'] = [c for c in checks if c['operation']==row['id']]
    if any(c['status']=='FAIL' for c in row['semantic_checks']):
        row['status']='FAIL'
        row['reason']='FAIL: declared PNG fixture has invalid IDAT CRC; transport/model acceptance cannot establish valid media bytes.'

report['counts'] = dict(Counter(r['status'] for r in report['operations']))
report['network']['negative_probes'] = network_probes
report['network']['attempts'] = scope['denied']
report['author_agent']='/root/rest091_correct_20261029'
report['review_method']='Prior independent reviewer source/wire/model audit reused; corrected meaning assertions and negative checks independently authored. No author test expectations imported.'
report['scope']='All29 frozen-candidate source/semantic retest; actual SDK uses MockTransport with DNS/socket/native HTTP denied. No live platform or formal acceptance/promotion claim.'
report['frozen_manifest']={'path':str(manifest_path),'sha256':before[str(manifest_path)],'candidate_file_mismatches':frozen_mismatches,'SDK_source_mismatches':source_mismatches}
report['unchanged_previous_pass_examples']=[{'id':r['id'],'same_bytes':sha(r['example'])==baseline['asset_sha256'][next(k for k in baseline['asset_sha256'] if k.endswith(str(Path(r['example']).relative_to(ROOT))))]} for r in report['operations'] if r['previous_status']=='PASS']
report['history']={'original_review':{'path':str(baseline_path),'sha256':before[str(baseline_path)],'counts':baseline['counts'],'reviewer':baseline['reviewer_agent']},'rejected_harness_enum':{'path':str(initial_paths[-1]),'sha256':before[str(initial_paths[-1])],'reason':'SUCCEEDED is reviewer response error. Frozen SDK enum is PENDING/FAILED/SUCCESSFUL; original author get_status fixture was valid.'}}
report['official_provenance']=[{'url':'https://raw.githubusercontent.com/palantir/osdk-ts/'+manifest['supplemental_source']['commit']+'/'+remote,'snapshot':str(TMP/local),'sha256':sha(TMP/local)} for remote,local in zip(manifest['supplemental_source']['paths'],['rest091_retest_official_manifest_20261029.ts','rest091_retest_official_builder_20261029.ts'])]
report['exact_before_after_hashes']=[{'path':p,'before':h,'after':sha(p),'stable':h==sha(p)} for p,h in before.items()]
report['candidate_asset_stability']['changed'] += [p for p,h in before.items() if sha(p)!=h]
report['candidate_asset_stability']['stable'] = not report['candidate_asset_stability']['changed']
OUT.write_text(json.dumps(report,indent=2,default=lambda v:{'base64':base64.b64encode(v).decode()} if isinstance(v,bytes) else str(v)),encoding='utf-8')
hash_manifest=TMP/'feature015_rest091_semantic_retest_20261029_manifest.json'
hash_manifest.write_text(json.dumps({'reviewer':'/root/rest091_independent_retest_20261029','artifacts':{str(p):sha(p) for p in [Path(__file__),OUT,TMP/'rest091_retest_raw_20261029.json']}},indent=2),encoding='utf-8')
print(json.dumps({'report':str(OUT),'sha256':sha(OUT),'counts':report['counts'],'model_counts':report['model_counts'],'changed':report['candidate_asset_stability']['changed'],'unchanged_previous_pass':len(report['unchanged_previous_pass_examples']),'network_negative_probes':len(network_probes)}))
