import asyncio
import hashlib
import json
from pathlib import Path
import runpy
import subprocess
from unittest.mock import patch

import httpx
import pytest
from foundry_sdk._core.api_client import BaseApiClient

root = Path.cwd()
worktree = root / '.ept/tmp/feature015_rest083_unit_modes_20261118'
test_file = worktree / 'tests/test_offline_rest_083.py'
module = runpy.run_path(str(test_file))
loop = asyncio.new_event_loop()
results = []


def success():
    module['test_native_all_forms_wire_and_typed_decode']('Action', 'apply', False, 'ordinary', loop)


def stream():
    module['test_native_unfinished_stream_closes_on_interrupt_or_cancel']('Attachment', 'read', False, loop)


original_url = BaseApiClient._create_url
original_headers = BaseApiClient._create_headers
original_serialize = BaseApiClient._serialize
original_send = httpx.Client.send
mutants = [
    ('wrong escaped resource path', BaseApiClient, '_create_url',
     lambda self, info: original_url(self, info) + '/wrong-resource', success),
    ('wrong bearer identity', BaseApiClient, '_create_headers',
     lambda self, info, token: {**original_headers(self, info, token), 'Authorization': 'Bearer wrong'}, success),
    ('discard serialized request body', BaseApiClient, '_serialize',
     lambda self, value: b'{}' if value is not None else original_serialize(self, value), success),
    ('ignore request timeout', BaseApiClient, '_get_timeout', lambda self, info: 99, success),
    ('skip response close', httpx.Response, 'close', lambda self: None, stream),
    ('prebuffer streaming body', httpx.Client, 'send',
     lambda self, *args, **kwargs: original_send(self, *args, **{**kwargs, 'stream': False}), stream),
]

try:
    with pytest.MonkeyPatch.context() as guard:
        module['deny_network'].__wrapped__(guard)
        success()
        stream()
        for name, target, attribute, replacement, check in mutants:
            try:
                with patch.object(target, attribute, replacement):
                    check()
            except Exception as error:
                cause = error
                while cause.__cause__ is not None:
                    cause = cause.__cause__
                assert isinstance(cause, AssertionError), repr(error)
                results.append({'mutation': name, 'killed': True, 'exception': type(error).__name__,
                                'root_exception': type(cause).__name__})
            else:
                results.append({'mutation': name, 'killed': False})
finally:
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()

baseline = subprocess.check_output(['git', '-C', str(worktree), 'show', 'HEAD:tests/test_offline_rest_083.py'])
proof = {
    'test_file': str(test_file),
    'sha256': hashlib.sha256(test_file.read_bytes()).hexdigest(),
    'base_commit': subprocess.check_output(['git', '-C', str(worktree), 'rev-parse', 'HEAD'], text=True).strip(),
    'baseline_prefix_bytes_preserved': test_file.read_bytes().startswith(baseline),
    'changed_files': subprocess.check_output(['git', '-C', str(worktree), 'diff', '--name-only'], text=True).splitlines(),
    'operation_count': len(module['NATIVE_IDS']),
    'available_form_count': len(module['NATIVE_FORMS']),
    'source_resource_hashes': module['NATIVE_SOURCE_HASHES'],
    'mutations': results,
}
destination = root / '.ept/tmp/rest083_unit_mutation_proof_20261118.json'
destination.write_text(json.dumps(proof, indent=2) + '\n')
print(json.dumps({'proof': str(destination), 'killed': sum(row['killed'] for row in results), 'total': len(results)}))
assert all(row['killed'] for row in results)
assert proof['baseline_prefix_bytes_preserved']
assert proof['changed_files'] == ['tests/test_offline_rest_083.py']
