from pathlib import Path

tmp = Path(__file__).resolve().parent
source = (tmp / 'rest091_independent_retest_20261029.py').read_text()
source = source.replace('feature015_rest091_semantic_retest_20261029', 'feature015_rest091_semantic_final_retest_20261116')
source = source.replace('feature015_rest091_correction_manifest_20261029.json', 'feature015_rest091_correction_manifest_second_20261029.json')
source = source.replace('rest091_retest_raw_20261029.json', 'rest091_final_retest_raw_20261116.json')
source = source.replace('/root/rest091_independent_retest_20261029', '/root/rest091_final_retest_20261116')
start = source.index('def png_details(data):')
end = source.index('\ndef validate_manifest(body):', start)
source = source[:start] + '''def png_details(data):
    assert data[:8] == b'\\x89PNG\\r\\n\\x1a\\n', 'PNG signature'
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
    for name, raw in [('wrong row length', b'\\x00\\xff'), ('invalid row filter', b'\\x05\\xff\\x00\\x00')]:
        payload = header + chunk(b'IDAT', zlib.compress(raw)) + chunk(b'IEND', b'')
        controls.append(expect_rejection(name, lambda payload=payload: png_details(payload), AssertionError))
    return controls
''' + source[end:]
needle = "            row['png_integrity'] = detail"
source = source.replace(needle, needle + "\n            record(op, 'PNG negative controls', lambda payload=payload: png_negative_controls(payload))\n            record(op, 'HTTP Content-Length equals complete PNG', lambda first=first,payload=payload: int(first['headers']['content-length']) == len(payload) or (_ for _ in ()).throw(AssertionError(first['headers'])))")
needle = "        if method == 'get_rid_by_path':"
source = source.replace(needle, '''        if method in ('reference','register','upload_media'):
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
''' + needle)
needle = "report['counts'] = dict(Counter(r['status'] for r in report['operations']))"
source = source.replace(needle, '''prior_retest_path = TMP / 'feature015_rest091_semantic_retest_20261029.json'
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
    suffix = path.replace('\\\\','/').split('/foundry_sdk/',1)[1]
    current = [p for p in report['asset_sha256'] if p.replace('\\\\','/').endswith('/foundry_sdk/'+suffix)]
    assert current and all(sha(p)==expected for p in current), (path,current)
    runtime_source_bindings.append({'frozen_path':path,'runtime_paths':current,'sha256':expected,'matches':True})
assert len(runtime_source_bindings)==8
report['runtime_source_bindings'] = runtime_source_bindings
report['counts'] = dict(Counter(r['status'] for r in report['operations']))''')
needle = "report['official_provenance']="
source = source.replace(needle, "report['official_provenance']=")
needle = "report['exact_before_after_hashes']="
source = source.replace(needle, "for entry in manifest['supplemental_source']['local_snapshots']:\n    assert sha(entry['path']) == entry['sha256']\nassert [r['sha256'] for r in report['official_provenance']] == [r['sha256'] for r in reversed(manifest['supplemental_source']['local_snapshots'])]\nassert all(r['same_bytes'] for r in report['unchanged_previous_pass_examples'])\nassert len(report['unchanged_previous_pass_examples']) == 22\nassert subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD'],text=True).strip() == manifest['base_head']\n" + needle)
(tmp / 'rest091_independent_final_retest_20261116.py').write_text(source, encoding='utf-8')
