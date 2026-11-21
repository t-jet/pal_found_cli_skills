"""Capture independent executor readiness without constructing SDK clients."""
import hashlib
import importlib.metadata
import json
from datetime import datetime, timezone
from pathlib import Path

TMP = Path(__file__).resolve().parent
IDENTITY = '/root/rest071_execute_20261027'
SKILL = TMP / 'feature015_integration/.agents/skills/pal-found-dev'

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

expected = {
    'rest071_formal_cases.json': 'eaa4126766a52b28eb99d7d26b392d2ec997c20479022f7e3eafeacfa38295e7',
    'rest071_formal_execute.py': 'd36df0fb9824d603944971a702cabf7694e0dada1a08c953797798db99fb7876',
    'rest071_case_approval.json': '8998fb2f9c816841dd7c7c3bcc1374d5349144f14f780848dcae1f1768aa7229',
}
for name, digest in expected.items():
    assert sha(TMP / name) == digest, name
cases = json.loads((TMP / 'rest071_formal_cases.json').read_bytes())
approval = json.loads((TMP / 'rest071_case_approval.json').read_bytes())
assert approval['verdict'] == 'APPROVED'
assert IDENTITY not in (cases['author_identity'], approval['reviewer_identity'])
assert importlib.metadata.version('foundry-platform-sdk') == cases['sdk_release'] == '1.101.0'
assert len(cases['operations']) == 27
assert sum(len(case['errors']) for case in cases['operations']) == 74
bindings = {}
for case in cases['operations']:
    for source in [case['source'], *case['assets'].values()]:
        path = Path(source['path']) if source is case['source'] else SKILL / source['path']
        assert sha(path) == source['sha256'], str(path)
        bindings[str(path)] = source['sha256']
    for error in case['errors']:
        path = Path(error['error_source'])
        assert sha(path) == error['error_source_sha256'], str(path)
        bindings[str(path)] = error['error_source_sha256']
report = {
    'executor_identity': IDENTITY,
    'observed_at_utc': datetime.now(timezone.utc).isoformat(),
    'sdk_release': cases['sdk_release'],
    'case_author_identity': cases['author_identity'],
    'case_reviewer_identity': approval['reviewer_identity'],
    'independence_checked': True,
    'approved_artifacts': expected,
    'operations': len(cases['operations']),
    'declared_errors': sum(len(case['errors']) for case in cases['operations']),
    'source_asset_error_bindings': bindings,
    'binding_count': len(bindings),
    'runner': {
        'path': str(TMP / 'rest071_executor_runner_20261027.py'),
        'sha256': sha(TMP / 'rest071_executor_runner_20261027.py'),
        'adaptation': 'Only executor identity and immutable output prefix changed from prior coordinator runner.',
        'original_sha256': sha(TMP / 'rest071_exec_runner.py'),
    },
    'execution': 'NOT_RUN',
    'workflow_prerequisites': 'Awaiting manager confirmation of actual TESTCASE Closed and TESTEXEC In Progress states.',
}
output = TMP / 'rest071_executor_preflight_20261027.json'
output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'execution': 'NOT_RUN', 'operations': 27, 'declared_errors': 74,
                  'binding_count': len(bindings), 'report': str(output), 'sha256': sha(output)}))
