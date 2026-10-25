"""Verify local navigation and operation headings against approved asset hashes."""
import hashlib
import json
from pathlib import Path
import re
from datetime import datetime, timezone

TMP = Path(__file__).resolve().parent
SKILL = TMP / 'feature015_integration/.agents/skills/pal-found-dev'
MANIFEST = TMP / 'rest074_formal_cases.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def links(path):
    return [(label, (path.parent / target.split('#')[0]).resolve())
            for label, target in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', path.read_text(encoding='utf-8'))
            if not re.match(r'[a-z]+://', target) and target.split('#')[0]]


manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
catalog = SKILL / 'references/rest/catalog.md'
catalog_links = links(catalog)
rows, issues = [], []
for case in manifest['operations']:
    operation = case['operation']
    version, service, resource, method = operation.split('.')
    contract = SKILL / case['assets']['contract']['path']
    behavior = SKILL / case['assets']['behavior']['path']
    example = SKILL / case['assets']['example']['path']
    index = SKILL / f'references/rest/{version}/{service}/index.md'
    service_links = [pair for part in index.parent.glob('index*.md') for pair in links(part)]
    contract_links = links(contract)
    behavior_links = links(behavior)
    model_links = [(label, path) for label, path in contract_links if '/models/' in path.as_posix()]
    checks = {
        'catalog_service_link': (f'{version}.{service}', index.resolve()) in catalog_links,
        'index_exact_operation_contract': (operation, contract.resolve()) in service_links,
        'contract_operation_heading': f'# {operation}' in contract.read_text(encoding='utf-8').splitlines(),
        'contract_resource_guide_link': any(path == behavior.resolve() for _, path in contract_links),
        'behavior_method_heading': f'### {method}' in behavior.read_text(encoding='utf-8').splitlines(),
        'behavior_example_link': any(path == example.resolve() for _, path in behavior_links),
        'contract_model_definitions_resolve': bool(model_links) and all(path.is_file() for _, path in model_links),
        'all_contract_local_links_resolve': all(path.is_file() for _, path in contract_links),
        'bound_asset_hashes': all(sha(SKILL / asset['path']) == asset['sha256'] for asset in case['assets'].values()),
    }
    for check, passed in checks.items():
        if not passed:
            issues.append(dict(operation=operation, check=check))
    rows.append(dict(case_id=case['case_id'], operation=operation, checks=checks,
                     catalog=dict(path=str(catalog), sha256=sha(catalog)),
                     index=dict(path=str(index), sha256=sha(index)),
                     contract=dict(path=str(contract), sha256=sha(contract), heading=f'# {operation}'),
                     behavior=dict(path=str(behavior), sha256=sha(behavior), heading=f'### {method}'),
                     example=dict(path=str(example), sha256=sha(example)),
                     model_links=[dict(label=label, path=str(path), exists=path.is_file(),
                                       sha256=sha(path) if path.is_file() else None) for label, path in model_links]))
report = dict(executor_identity='/root/formal074_prepare/independent_execute',
              completed_at=datetime.now(timezone.utc).isoformat(), manifest_sha256=sha(MANIFEST),
              result='PASS' if not issues else 'FAIL', operations=rows, issues=issues,
              boundary='Local navigation and file assertions only; no tenant or integrated journey execution.')
(TMP / 'rest074_exec_discovery.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps(dict(result=report['result'], operations=len(rows), issues=issues)))
raise SystemExit(bool(issues))
