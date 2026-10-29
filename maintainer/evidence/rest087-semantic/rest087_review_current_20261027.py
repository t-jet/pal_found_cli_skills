"""Fresh independent retest of the complete REST087 source and semantic review."""
from pathlib import Path
import hashlib

prior = Path(__file__).with_name('rest087_independent_review.py')
code = prior.read_text(encoding='utf-8')
replacements = {
    "feature015_rest087_current_semantic_review.json": "feature015_rest087_current_semantic_review_20261027.json",
    "'/root/rest087_review_resume'": "'/root/rest087_semantic_qa_20261027'",
    "2026-10-22 Europe/Sofia": "2026-10-27 Europe/Sofia",
    "'initial_findings_artifact':": "'harness_dependency': {'path': str(prior), 'sha256': hashlib.sha256(prior.read_bytes()).hexdigest()},\n    'initial_findings_artifact':",
    "'manual_semantic_review': NOTES[short],": "'manual_semantic_review': NOTES[short], 'fresh_manual_review': FRESH_NOTES.get(short, 'Fresh reviewer checked the complete resource guide, installed source method/docstring, success/error model fields and fixture identities. No additional contradiction found within the stated synthetic boundary.'),",
}
for old, new in replacements.items():
    assert old in code, old
    code = code.replace(old, new)
FRESH_NOTES = {
    'OpenAiModel.embeddings': 'Response data is list[list[float]] with no index field. Check count and dimension; frozen source does not state an independent index/order mapping guarantee.',
    'Session.blocking_continue': 'SessionExchange response has userInput, contexts and result. Trace identity is result.session_trace_id; no exchange ID field is promised.',
    'Session.update_title': 'Operation returns None. Verify changed title through a subsequent Session.get and its metadata.title field.',
    'AgentVersion.get': 'Only string and numeric version details returned. Agent.get supplies parameter definitions for the selected version; no tool/application definitions claimed from AgentVersion response.',
    'Content.get': 'SessionExchange contains userInput, optional contexts and result, with sessionTraceId in result. No exchange/message ID field is exposed by this response.',
    'ModelFunction.create': 'Returned ModelFunction metadata has no input/output schema. Use ModelVersion.model_api and keep parent Model RID as request context.',
    'ModelFunction.get': 'Returned fields are functionRid, functionVersion, displayName, apiName and isRowWise; schema belongs to ModelVersion.model_api.',
    'ModelFunction.replace': 'Replacement returns metadata, not schemas. Read actual version model_api before compatibility decisions.',
    'Model.get': 'Model response contains RID only. Version and branch knowledge cannot be read from absent response fields; separate version reads required.',
    'ModelStudio.get': 'Studio response contains RID, folder RID and creation time. Configuration/trainer are separate resource reads.',
    'ModelStudioRun.list': 'Optional buildStatus can be absent; runId/buildRid/jobRid/configVersion remain actual fields. Run metadata alone does not establish completed training.',
    'ModelVersion.get': 'Parent Model RID is request context, not a returned field; returned version RID/API/dependencies/backing repositories support artifact checks.',
    'ExperimentArtifactTable.json': 'SDK bytes contain JSON row array, not table metadata. Page-size defaults and max limits from source; response interpretation and truncation remain caller checks.',
}
extra_checks = """
    if short == 'Session.update_title' and 'verify the returned title' in behavior_text.lower():
        findings.append({'code': 'GUIDE_ABSENT_RETURN_FIELDS', 'reason': 'Update title returns None; subsequent get is needed for metadata.title verification.'})
    if short == 'Session.blocking_continue' and 'Check returned exchange identity' in behavior_text:
        findings.append({'code': 'GUIDE_ABSENT_RETURN_FIELDS', 'reason': 'SessionExchange has no exchange ID field; result.sessionTraceId is the trace locator.'})
    if short == 'Content.get' and 'check exchange/message IDs' in behavior_text:
        findings.append({'code': 'GUIDE_ABSENT_RETURN_FIELDS', 'reason': 'SessionExchange has userInput, contexts and result; only sessionTraceId in result, no exchange/message ID fields.'})
    if short in ('ModelFunction.create', 'ModelFunction.replace') and (
        'returned definition and parameter schema' in behavior_text or 'returned schema' in behavior_text
    ):
        findings.append({'code': 'GUIDE_ABSENT_RETURN_FIELDS', 'reason': 'ModelFunction response contains callable metadata only; schemas require ModelVersion.model_api.'})
"""
code = code.replace('    checks = {\n', extra_checks + '\n    checks = {\n')
code = code.replace('rows = []\n', 'NOTES.update(FRESH_NOTES)\nrows = []\n')
code = code.replace("        'contract_exists': contract.is_file(),", """        'contract_exists': contract.is_file(),
        'contract_wire_matches_frozen_source': all(
            '**' + key + '**\\n\\n```python\\n' + value + '\\n```' in contract.read_text()
            for key, value in oracle['wire'].items()
        ),
        'contract_signature_matches_frozen_source': (
            'def ' + oid.split('.')[-1] + '(' + oracle['ordinary']['signature'] + ') -> ' + oracle['ordinary']['return'] + ': ...'
        ) in contract.read_text(),
        'contract_stage_matches_frozen_source': 'release stage: ' + oracle['documentation']['stage'] + '.' in contract.read_text(),""")
exec(compile(code, str(prior), 'exec'), globals())

# Final evidence is tied to asset bytes, including assets not changed by the author.
import importlib.metadata
import os
import sys
from datetime import datetime, timezone

assert importlib.metadata.version('foundry-platform-sdk') == '1.101.0'
for row in report['operations']:
    for kind in ('behavior', 'example', 'contract'):
        assert sha(BASE / row[kind + '_path']) == row[kind + '_sha256']
    error_map = ast.parse(ORACLE[row['id']]['wire']['throwable_errors'], mode='eval').body
    row['source_declared_error_names'] = [ast.literal_eval(key) for key in error_map.keys]
    row['source_declared_error_count'] = len(error_map.keys)

test_path = REPO / 'tests/test_offline_rest_087.py'
commands = [
    [sys.executable, '-m', 'pytest', str(test_path), '-q',
     '--basetemp=' + str(ROOT / '.ept/tmp/rest087_final_independent_basetemp_20261027'),
     '-o', 'cache_dir=' + str(ROOT / '.ept/tmp/rest087_final_independent_pytest_cache_20261027')],
    ['ruff', 'check', str(test_path)],
]
command_results = []
for command in commands:
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                            encoding='utf-8', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    command_results.append({'command': command, 'exit_code': result.returncode,
                            'stdout': result.stdout, 'stderr': result.stderr})
    assert result.returncode == 0, result.stdout + result.stderr

author_path = ROOT / '.ept/tmp/rest087_author_validation_20261027.json'
report.update({
    'completed_at_utc': datetime.now(timezone.utc).isoformat(),
    'review_harness': {'path': str(Path(__file__)), 'sha256': sha(Path(__file__))},
    'unit_suite': {'path': str(test_path), 'sha256': sha(test_path), 'test_count': 30,
                   'scope': 'Native integer-path bridge and ten corrected operation examples, including semantic mutation guards; this is not the complete formal TESTEXEC suite.'},
    'verification_commands': command_results,
    'author_correction_report': {'path': str(author_path), 'sha256': sha(author_path)},
    'asset_stability_checked_after_execution': True,
    'formal_qa_status': 'pending',
    'scope_limits': [
        'Semantic/source acceptance of all 47 current operation assets only. Formal independently authored cases and TESTEXEC approval are still required.',
        'Examples use real SDK request serialization and HTTP mock responses, not live tenant state transitions or model inference.',
        'Typed synthetic successes and errors do not establish server capability, authorization, resource scheduling, artifact validity or model executable dependencies.',
        'The SDK 1.101.0 integer-path defect remains documented and reproduced before HTTP; its separate bounded direct-REST adapter is reviewed without claiming a native SDK success.',
        'Streaming, paging and asynchronous source contracts are reviewed; this semantic review does not claim an exhaustive runtime matrix of every wrapper or every model alternative.',
    ],
    'source_error_count': sum(row['source_declared_error_count'] for row in report['operations']),
})
for row in report['operations']:
    for kind in ('behavior', 'example', 'contract'):
        assert sha(BASE / row[kind + '_path']) == row[kind + '_sha256']
OUT.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'final_report_sha256': sha(OUT), 'operations': len(rows),
                  'summary': report['summary'], 'source_errors': report['source_error_count']}))
