import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import socket
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / '.ept/tmp/feature015_rest073_restore_fixes'
OUTPUT = ROOT / '.ept/tmp/feature015_restore_core_regenerated_20261116'
SOURCE = ROOT / '.ept/docs/customer_input/foundry-platform-python'
CONTRACT = '.agents/skills/pal-found-dev/references/rest/contracts/v2/filesystem/Resource/restore.md'
assert not OUTPUT.exists(), OUTPUT
OUTPUT.mkdir()
shutil.copytree(WORK / '.agents', OUTPUT / '.agents')
shutil.copytree(WORK / 'maintainer', OUTPUT / 'maintainer')
def hashes():
    return {p.relative_to(OUTPUT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in OUTPUT.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
before = hashes()
spec = importlib.util.spec_from_file_location('catalog', WORK / 'scripts/offline_rest_catalog.py')
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)
files = catalog.archive(SOURCE)
operations, symbols = catalog.build_inventory(files)
attempts = []
def deny(*args, **kwargs):
    attempts.append('network')
    raise AssertionError('Network denied during offline regeneration')
with patch.object(socket, 'getaddrinfo', deny), patch.object(socket.socket, 'connect', deny), patch.object(socket.socket, 'connect_ex', deny):
    result = catalog.render(OUTPUT, files, operations, symbols, None)
after = hashes()
changed = sorted(p for p in before.keys() | after.keys() if before.get(p) != after.get(p))
with patch.object(socket, 'getaddrinfo', deny), patch.object(socket.socket, 'connect', deny), patch.object(socket.socket, 'connect_ex', deny):
    catalog.render(OUTPUT, files, operations, symbols, None)
second = hashes()
report = {'source_commit': catalog.COMMIT, 'result': result, 'changed': changed,
          'idempotent': after == second, 'network_attempts': len(attempts),
          'changes': {p: {'before': before.get(p), 'after': after.get(p)} for p in changed}}
report_path = ROOT / '.ept/tmp/feature015_restore_core_regeneration_20261116.json'
report_path.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
assert after == second
assert changed == [CONTRACT], 'Unexpected regeneration changes; do not promote extras'
shutil.copyfile(OUTPUT / CONTRACT, WORK / CONTRACT)
