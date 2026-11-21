import ast
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / '.ept/tmp/feature015_rest073_restore_fixes'
AUTHOR = ROOT / '.ept/tmp/feature015_rest073_restore_author_manifest_20261116.json'
OUTPUT = ROOT / '.ept/tmp/feature015_rest073_restore_combined_manifest_20261116.json'
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
author = json.loads(AUTHOR.read_text())
assert digest(AUTHOR) == 'bd91a2d1ccad859349a07f393094e7b3bcd222510e0d4994b91e3d7a15bf7eef'
frozen = {path: digest(WORK / path) for path in author['candidate_files']}
assert frozen == author['candidate_files']
core = ['scripts/offline_rest_catalog.py',
        '.agents/skills/pal-found-dev/references/rest/contracts/v2/filesystem/Resource/restore.md',
        'tests/test_offline_rest_catalog_restore.py']
dirty = subprocess.check_output(['git', '-C', str(WORK), 'status', '--porcelain', '--untracked-files=all'], text=True)
paths = [line[3:] for line in dirty.splitlines()]
assert set(paths) == set(core) | frozen.keys(), paths
for path in core:
    if path.endswith('.py'):
        compile((WORK / path).read_text(encoding='utf-8'), path, 'exec')
contract = WORK / core[1]
prose = contract.read_text(encoding='utf-8')
links = re.findall(r'\[[^\]]+\]\(([^)]+)\)', prose)
for link in links:
    assert not re.match(r'https?://', link), link
    target, _, anchor = link.partition('#')
    resolved = (contract.parent / target).resolve()
    assert resolved.is_relative_to((WORK / '.agents/skills/pal-found-dev').resolve()), link
    assert resolved.is_file(), link
    if anchor:
        assert re.search(r'(?m)^#{1,6} ' + re.escape(anchor) + r'\s*$', resolved.read_text(encoding='utf-8')), link
source = {path: digest(Path(path)) for path in author['source_bindings']}
assert source == author['source_bindings']
proof_paths = ['feature015_restore_core_regeneration_20261116.json',
               'feature015_restore_core_baseline_comparison_20261116.json',
               'feature015_restore_core_tests_20261116.xml']
proofs = {name: digest(ROOT / '.ept/tmp' / name) for name in proof_paths}
comparison = json.loads((ROOT / '.ept/tmp' / proof_paths[1]).read_text())
assert comparison['patch_only_generated_delta'] == [core[1]]
report = {'scope': 'Core source-conflict qualifier plus frozen REST073 author correction; independent QA pending',
          'worktree': str(WORK), 'base_sha': author['base_sha'],
          'core_files': {path: digest(WORK / path) for path in core},
          'frozen_author_files_unchanged': frozen,
          'combined_dirty_manifest': {path: digest(WORK / path) for path in sorted(paths)},
          'source_bindings': source, 'restore_method_sha256': author['restore_method_sha256'],
          'sdk_release': '1.101.0', 'source_commit': comparison['source_commit'],
          'proofs': proofs, 'core_compile': 'PASS in memory', 'contract_local_links_verified': len(links),
          'test_proof': {'command': 'prepared QA Python -m pytest tests/test_offline_rest_catalog_restore.py tests/test_offline_rest_073_restore.py -q',
                         'passed': 33, 'exit_code': 0, 'network': 'DNS/connect/connect_ex denied'},
          'regeneration': {'full_frozen_output_idempotent': True,
                           'baseline_to_patch_delta': comparison['patch_only_generated_delta'],
                           'preexisting_full_tree_drift': comparison['preexisting_full_render_drift'],
                           'claim': 'Patch reproduces only restore qualifier; full current tree has seven preexisting regeneration differences, left unchanged.'},
          'boundaries': {'tracker_writes': 0, 'live_calls': 0, 'commits': 0, 'pushes': 0,
                         'review_register_changes': 0, 'semantic_promotion': False, 'server_policy': 'unverified'}}
OUTPUT.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({'manifest': str(OUTPUT), 'sha256': digest(OUTPUT), 'core_files': report['core_files'],
                  'combined_dirty_file_count': len(paths), 'local_links': len(links)}, indent=2))
