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
OUT = TMP / 'feature015_rest091_semantic_final_retest_20261116.json'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
manifest_path = TMP / 'feature015_rest091_correction_manifest_second_20261029.json'
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
source = source.replace("OUT=TMP/'feature015_rest091_semantic_review_20261029.json'", "OUT=TMP/'rest091_final_retest_raw_20261116.json'")
source = source.replace("'/root/rest091_semantic_review_20261029'", "'/root/rest091_final_retest_20261116'")
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
    assert data[:8] == b'\x89PNG\r\n\x1a\n', 'PNG signature'
    pos = 8
    chunks = []
    compressed = b''
    dimensions = None
    while pos < len(data):
        assert pos + 12 <= len(data), 'truncated chunk header or CRC'
        size = struct.unpack('>I', data[pos:pos+4])[0]
        kind = data[pos+4:pos+8]
        assert pos + size + 12 <= len(data), 'truncated chunk data'
        payload = data[pos+8:pos+8+size]
        stored = struct.unpack('>I', data[pos+8+size:pos+12+size])[0]
        computed = zlib.crc32(kind + payload) & 0xffffffff
        assert stored == computed, ('CRC', kind, stored, computed)
        chunks.append({'type':kind.decode(), 'bytes':size, 'stored_crc':hex(stored), 'computed_crc':hex(computed), 'valid':True})
        if kind == b'IHDR':
            assert len(chunks) == 1 and size == 13, 'IHDR first, length 13'
            width,height,depth,color,compression,filter_method,interlace = struct.unpack('>IIBBBBB', payload)
            assert (width,height,depth,color,compression,filter_method,interlace) == (1,1,8,2,0,0,0), 'expected complete 1x1 RGB noninterlaced image'
            dimensions = (width,height)
        if kind == b'IDAT': compressed += payload
        if kind == b'IEND': assert size == 0 and pos + 12 == len(data), 'IEND must be final and empty'
        pos += size+12
    assert pos == len(data) and [c['type'] for c in chunks] == ['IHDR','IDAT','IEND'], 'chunk order'
    decoder = zlib.decompressobj()
    scanlines = decoder.decompress(compressed) + decoder.flush()
    assert decoder.eof and not decoder.unused_data and not decoder.unconsumed_tail, 'complete single zlib stream'
    width,height = dimensions
    row_bytes = 1 + width * 3
    assert len(scanlines) == row_bytes * height, 'scanline row length'
    assert all(scanlines[row * row_bytes] <= 4 for row in range(height)), 'scanline filter'
    return {'chunks':chunks, 'dimensions':dimensions, 'row_bytes':row_bytes, 'scanline_rows':height, 'zlib_complete':True, 'decompressed_scanline_hex':scanlines.hex(), 'payload_sha256':hashlib.sha256(data).hexdigest(), 'payload_bytes':len(data)}

def png_negative_controls(data):
    malformed = bytearray(data); malformed[45] ^= 1
    controls = []
    for name, payload in [('IDAT CRC corruption', bytes(malformed)), ('truncation', data[:-1])]:
        controls.append(expect_rejection(name, lambda payload=payload: png_details(payload), AssertionError))
    def chunk(kind, payload):
        return struct.pack('>I',len(payload)) + kind + payload + struct.pack('>I', zlib.crc32(kind+payload)&0xffffffff)
    header = data[:33]
    for name, raw in [('wrong row length', b'\x00\xff'), ('invalid row filter', b'\x05\xff\x00\x00')]:
        payload = header + chunk(b'IDAT', zlib.compress(raw)) + chunk(b'IEND', b'')
        controls.append(expect_rejection(name, lambda payload=payload: png_details(payload), AssertionError))
    return controls

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
            record(op, 'PNG negative controls', lambda payload=payload: png_negative_controls(payload))
            record(op, 'HTTP Content-Length equals complete PNG', lambda first=first,payload=payload: int(first['headers']['content-length']) == len(payload) or (_ for _ in ()).throw(AssertionError(first['headers'])))
            record(op, 'PNG chunk CRC integrity', lambda detail=detail: (all(c['valid'] for c in detail['chunks']) or (_ for _ in ()).throw(AssertionError(detail))))
            record(op, 'frozen SDK wildcard header preserved', lambda first=first: first['headers']['content-type']=='*/*' or (_ for _ in ()).throw(AssertionError(first['headers'])))
            record(op, 'unverified live transport preflight rejects', lambda module=module: expect_rejection('unverified transport', module['require_verified_upload'], RuntimeError))
        if method in ('reference','register','upload_media'):
            mime = module['SUCCESS']['mediaType' if method=='register' else 'mimeType']
            record(op, 'concrete MIME matches PNG imagery family', lambda mime=mime: mime == 'image/png' or (_ for _ in ()).throw(AssertionError(mime)))
        if method == 'register':
            physical = module['EXPECTED_BODY']['physicalItemName']
            record(op, 'configured-store relative PNG identity', lambda physical=physical: physical.endswith('.png') and not physical.startswith(('/', 'http:','https:')) or (_ for _ in ()).throw(AssertionError(physical)))
            record(op, 'federated registration constraint retained', lambda row=row: 'federated media sets' in row['source_doc'] or (_ for _ in ()).throw(AssertionError('source prerequisite missing')))
        if method in ('upload','upload_media'):
            record(op, 'SDK docs and observed wildcard discrepancy', lambda row=row: 'application/octet-stream' in row['source_doc'] and any('*/*' in value for value in row['source_wire'].values()) or (_ for _ in ()).throw(AssertionError(row['source_wire'])))
        if method == 'upload_media':
            record(op, 'temporary upload PNG filename', lambda module=module: module['EXPECTED_QUERY']['filename'].endswith('.png') or (_ for _ in ()).throw(AssertionError(module['EXPECTED_QUERY'])))
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

prior_retest_path = TMP / 'feature015_rest091_semantic_retest_20261029.json'
prior_retest = json.loads(prior_retest_path.read_text())
assert sha(prior_retest_path) == 'f7cac9387bba34f57e261a58b75aaa9fdfe1f0c24f4ad69de438fbcf37ce81d5'
assert sha(baseline_path) == '3e34be11f213e4aae7b8facd731b0c42989e2aaafe106662d82902a6a67d3712'
assert report['model_counts'] == {'PASS':157} and not report['model_dependency_closure_missing']
assert {r['id'] for r in report['operations']} == {r['id'] for r in baseline['operations']}
model_continuity = []
for old in prior_retest['model_checks']:
    new = next(r for r in report['model_checks'] if r['symbol']==old['symbol'])
    assert new['source_sha256']==old['source_sha256'] and sha(new['asset'])==prior_retest['asset_sha256'][old['asset']]
    model_continuity.append({'symbol':new['symbol'],'source_sha256':new['source_sha256'],'local_sha256':sha(new['asset']),'unchanged':True})
report['model_hash_continuity'] = model_continuity
report['prior_retest'] = {'path':str(prior_retest_path),'sha256':sha(prior_retest_path),'counts':prior_retest['counts']}
runtime_source_bindings = []
for path, expected in manifest['source_bindings'].items():
    suffix = path.replace('\\','/').split('/foundry_sdk/',1)[1]
    current = [p for p in report['asset_sha256'] if p.replace('\\','/').endswith('/foundry_sdk/'+suffix)]
    assert current and all(sha(p)==expected for p in current), (path,current)
    runtime_source_bindings.append({'frozen_path':path,'runtime_paths':current,'sha256':expected,'matches':True})
assert len(runtime_source_bindings)==8
report['runtime_source_bindings'] = runtime_source_bindings
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
for entry in manifest['supplemental_source']['local_snapshots']:
    assert sha(entry['path']) == entry['sha256']
assert [r['sha256'] for r in report['official_provenance']] == [r['sha256'] for r in reversed(manifest['supplemental_source']['local_snapshots'])]
assert all(r['same_bytes'] for r in report['unchanged_previous_pass_examples'])
assert len(report['unchanged_previous_pass_examples']) == 22
assert subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD'],text=True).strip() == manifest['base_head']
report['exact_before_after_hashes']=[{'path':p,'before':h,'after':sha(p),'stable':h==sha(p)} for p,h in before.items()]
report['candidate_asset_stability']['changed'] += [p for p,h in before.items() if sha(p)!=h]
report['candidate_asset_stability']['stable'] = not report['candidate_asset_stability']['changed']
OUT.write_text(json.dumps(report,indent=2,default=lambda v:{'base64':base64.b64encode(v).decode()} if isinstance(v,bytes) else str(v)),encoding='utf-8')
hash_manifest=TMP/'feature015_rest091_semantic_final_retest_20261116_manifest.json'
hash_manifest.write_text(json.dumps({'reviewer':'/root/rest091_final_retest_20261116','artifacts':{str(p):sha(p) for p in [Path(__file__),OUT,TMP/'rest091_final_retest_raw_20261116.json']}},indent=2),encoding='utf-8')
print(json.dumps({'report':str(OUT),'sha256':sha(OUT),'counts':report['counts'],'model_counts':report['model_counts'],'changed':report['candidate_asset_stability']['changed'],'unchanged_previous_pass':len(report['unchanged_previous_pass_examples']),'network_negative_probes':len(network_probes)}))
