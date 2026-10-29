"""Check physical, committed REST074 assets and run its isolated unit suite."""
import ast
import hashlib
import importlib.metadata
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

TMP = Path(__file__).resolve().parent
REPO = TMP / 'feature015_integration'
SKILL = REPO / '.agents/skills/pal-found-dev'
START = datetime.now(timezone.utc)
CLOCK = time.monotonic()

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args], text=True).strip()

review_path = REPO / 'maintainer/rest-domain-independent-review-074-current.json'
review = json.loads(review_path.read_text(encoding='utf-8'))
assert len(review['operations']) == 52
assert importlib.metadata.version('foundry-platform-sdk') == '1.101.0'
rows = []
for operation in review['operations']:
    source = Path(operation['source_module'])
    assert sha(source) == operation['source_module_sha256']
    source_text = source.read_text(encoding='utf-8')
    resource, method = operation['id'].split('.')[-2:]
    cls = next(n for n in ast.parse(source_text).body if isinstance(n, ast.ClassDef) and n.name == resource + 'Client')
    function = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == method)
    assert hashlib.sha256(ast.get_source_segment(source_text, function).encode()).hexdigest() == operation['source_method_sha256']
    assets = {}
    for kind in ('contract', 'behavior', 'example'):
        path = SKILL / operation[kind + '_path']
        assert path.is_file()
        assert sha(path) == operation[kind + '_sha256'], str(path)
        git('ls-files', '--error-unmatch', path.relative_to(REPO).as_posix())
        if kind == 'example':
            compile(path.read_text(encoding='utf-8'), str(path), 'exec')
        assets[kind] = {'path': path.relative_to(REPO).as_posix(), 'sha256': sha(path)}
    rows.append({'operation': operation['id'], 'source_sha256': sha(source), 'assets': assets})

test = REPO / 'tests/test_offline_rest_074_semantics.py'
assert test.is_file()
git('ls-files', '--error-unmatch', test.relative_to(REPO).as_posix())
run = subprocess.run([sys.executable, '-m', 'pytest', str(test), '-q', '--basetemp', str(TMP / 'rest074_unit_pytest'), '-p', 'no:cacheprovider'], capture_output=True, text=True)
(TMP / 'rest074_unit_stdout.log').write_text(run.stdout, encoding='utf-8')
(TMP / 'rest074_unit_stderr.log').write_text(run.stderr, encoding='utf-8')
report = {'reviewer': '/root/formal074_prepare', 'activity': 'Fresh current file existence, tracked-file, pinned SDK/module/method/hash checks, compilation and isolated real unit run. Excludes historical author effort.', 'story': 'DEV-STORY-074', 'candidate_commit': git('rev-parse', 'HEAD'), 'started_at': START.isoformat(), 'finished_at': datetime.now(timezone.utc).isoformat(), 'elapsed_seconds': time.monotonic() - CLOCK, 'sdk_release': importlib.metadata.version('foundry-platform-sdk'), 'semantic_review': {'path': review_path.relative_to(REPO).as_posix(), 'sha256': sha(review_path)}, 'operations': rows, 'compiled_examples': 52, 'unit_test_path': test.relative_to(REPO).as_posix(), 'unit_test_sha256': sha(test), 'unit_exit_code': run.returncode, 'unit_stdout': run.stdout, 'unit_stderr': run.stderr, 'path_correction': 'Root PM explicitly authorized actual committed tests/test_offline_rest_074_semantics.py as meaningful 52-example plus21-guard suite; historical nominal _074.py does not exist. Indexed handoff/ticket wording correction belongs to root.', 'result': 'PASS' if run.returncode == 0 else 'FAIL'}
(TMP / 'rest074_readiness.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: report[k] for k in ('candidate_commit', 'compiled_examples', 'unit_stdout', 'unit_exit_code', 'elapsed_seconds', 'result')}))
raise SystemExit(run.returncode)
