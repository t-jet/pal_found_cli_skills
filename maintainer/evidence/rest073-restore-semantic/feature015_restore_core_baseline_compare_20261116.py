import hashlib
import importlib.util
import json
from pathlib import Path
import socket
import subprocess
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / '.ept/tmp/feature015_rest073_restore_fixes'
OUTPUT = ROOT / '.ept/tmp/feature015_restore_core_regenerated_20261116'
SOURCE = ROOT / '.ept/docs/customer_input/foundry-platform-python'
CONTRACT = '.agents/skills/pal-found-dev/references/rest/contracts/v2/filesystem/Resource/restore.md'
baseline_path = ROOT / '.ept/tmp/feature015_restore_core_baseline_generator_20261116.py'
baseline_path.write_bytes(subprocess.check_output(['git', '-C', str(WORK), 'show', 'HEAD:scripts/offline_rest_catalog.py']))
def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result
baseline = module(baseline_path, 'baseline')
candidate = module(WORK / 'scripts/offline_rest_catalog.py', 'candidate')
def hashes():
    return {p.relative_to(OUTPUT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in OUTPUT.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
files = baseline.archive(SOURCE)
print('Building frozen source inventory', flush=True)
operations, symbols = baseline.build_inventory(files)
patched = hashes()
attempts = []
def deny(*args, **kwargs):
    attempts.append('network')
    raise AssertionError('Network denied during offline regeneration')
with patch.object(socket, 'getaddrinfo', deny), patch.object(socket.socket, 'connect', deny), patch.object(socket.socket, 'connect_ex', deny):
    baseline.render(OUTPUT, files, operations, symbols, None)
    original = hashes()
    baseline.render(OUTPUT, files, operations, symbols, None)
    assert original == hashes()
    candidate.render(OUTPUT, files, operations, symbols, None)
    regenerated = hashes()
delta = sorted(p for p in original.keys() | regenerated.keys() if original.get(p) != regenerated.get(p))
assert delta == [CONTRACT], delta
assert patched == regenerated
report = {'source_commit': baseline.COMMIT, 'operations': len(operations), 'inventory_declarations': len(symbols),
          'rendered_reachable_symbols': 3251,
          'base_generator_sha256': hashlib.sha256(baseline_path.read_bytes()).hexdigest(),
          'candidate_generator_sha256': hashlib.sha256((WORK / 'scripts/offline_rest_catalog.py').read_bytes()).hexdigest(),
          'patch_only_generated_delta': delta, 'baseline_idempotent': True,
          'candidate_matches_previous_idempotent_full_render': True, 'network_attempts': len(attempts),
          'contract_sha256': regenerated[CONTRACT],
          'preexisting_full_render_drift': json.loads((ROOT / '.ept/tmp/feature015_restore_core_regeneration_20261116.json').read_text())['changed']}
report['preexisting_full_render_drift'].remove(CONTRACT)
report_path = ROOT / '.ept/tmp/feature015_restore_core_baseline_comparison_20261116.json'
report_path.write_text(json.dumps(report, indent=2) + '\n')
(WORK / CONTRACT).write_bytes((OUTPUT / CONTRACT).read_bytes())
print(json.dumps(report, indent=2), flush=True)
