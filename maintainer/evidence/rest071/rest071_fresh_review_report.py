"""Record fresh independent source, model and case review without client calls."""
import ast
import hashlib
import importlib
import json
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parent
CASE = BASE / 'rest071_formal_cases.json'
HARNESS = BASE / 'rest071_formal_execute.py'

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

manifest = json.loads(CASE.read_text())
static = json.loads((BASE / 'rest071_fresh_static_review.json').read_text())
assert static['manifest']['sha256'] == sha(CASE)
oracle_path = BASE / 'feature015_integration/tests/fixtures/offline/rest-acceptance/source-oracle.json'
oracle = json.loads(oracle_path.read_text())
findings = []
rows = []
for case in manifest['operations']:
    op = case['operation']
    checks = {'source_static_model_checks': next(row['checks'] for row in static['operations'] if row['operation'] == op)}
    checks['actual_source_matches_frozen_oracle'] = sha(case['source']['path']) == case['source']['sha256'] == oracle['operations'][op]['source_sha256']
    checks['oracle_file_hash_matches_manifest'] = sha(oracle_path) == case['source']['oracle_sha256']
    tree = ast.parse(Path(case['source']['path']).read_text())
    name, method = op.split('.')[-2:]
    source_text = Path(case['source']['path']).read_text()
    for prefix, field in (('', 'method_source_sha256'), ('Async', 'async_method_source_sha256')):
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == prefix + name + 'Client')
        fn = next(n for n in cls.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == method)
        checks[field] = hashlib.sha256(ast.get_source_segment(source_text, fn).encode()).hexdigest() == case['source'][field]
    for error in case['errors']:
        assert error['envelope']['errorName'] == error['expected']['name'] == error['name']
        assert error['envelope']['parameters'] == error['expected']['parameters'] == error['parameters']
        assert error['envelope']['errorCode'] == error['errorCode']
        assert error['envelope']['errorInstanceId'] == error['expected']['error_instance_id']
    for key, passed in checks.items():
        if passed is False:
            findings.append({'operation': op, 'severity': 'FAIL', 'finding': 'Provenance mismatch: ' + key})
    if op.endswith('.search'):
        is_group = '.Group.' in op
        fields = ['name'] if is_group else ['username', 'givenName', 'familyName']
        for extra in case['additional_cases']:
            if 'requests' not in extra:
                continue
            for index, (request, response) in enumerate(zip(extra['requests'], extra['responses'])):
                prefix = request['where']['value'].casefold()
                matches = all(any(str(item.get(field, '')).casefold().startswith(prefix) for field in fields) for item in response['data'])
                checks['search_prefix_page_' + str(index + 1)] = matches
                if not matches:
                    findings.append({'operation': op, 'severity': 'FAIL', 'finding': 'Finite continuation result does not match the requested prefix search.',
                                     'page': index + 1, 'request_prefix': prefix, 'returned_values': [{field: item.get(field) for field in fields} for item in response['data']],
                                     'source_basis': case['source']['docstring'].split(':param')[0].strip()})
    if op == 'v2.admin.Group.replace':
        pre = case['precondition']['existing_group']['attributes']
        error = next(e for e in case['errors'] if e['name'] == 'AttributesNotEditable')
        invalid = any(error['request']['attributes'].get(name) != pre.get(name) for name in error['parameters']['attributeNames'])
        checks['reserved_attribute_error_changes_reserved_value'] = invalid
        if not invalid:
            findings.append({'operation': op, 'severity': 'FAIL', 'finding': 'AttributesNotEditable adverse request preserves the named reserved attribute exactly as the stated prior GET; it does not exercise the documented forbidden edit.',
                             'source_basis': case['source']['docstring'].split(':param')[0].strip()})
    if 'content_hex' not in case['success']:
        assertion = case['success']['assertions'][0]
        checks['normalization_procedure_matches_python_mode_harness'] = 'mode="json"' not in assertion
        if not checks['normalization_procedure_matches_python_mode_harness']:
            findings.append({'operation': op, 'severity': 'FAIL', 'finding': 'Case prose prescribes model_dump JSON mode while the approved Python mode harness preserves SDK Long values; policy result literals are integers and JSON mode yields strings.', 'assertion': assertion})
    rows.append({'case_id': case['case_id'], 'operation': op, 'checks': checks})

report = {'story': 'DEV-STORY-071', 'reviewer_identity': '/root/rest071_finish_20261027/independent071_review',
          'reviewed_at_utc': datetime.now(timezone.utc).isoformat(), 'verdict': 'FAIL' if findings or static['failures'] else 'APPROVED',
          'execution': 'NOT_RUN', 'manifest': {'path': str(CASE), 'sha256': sha(CASE)},
          'harness': {'path': str(HARNESS), 'sha256': sha(HARNESS)},
          'method': 'Fresh independent manual SDK semantics and harness inspection, plus a separately executed adapted prior AST/schema checker. No SDK operation clients constructed or invoked.',
          'review_history': {'previous_manifest_sha256': '78c548179aa0020215ca471c4ebd031460584035933a3e85fce4dafa4706fb50',
                             'findings_reported_to_case_author': ['Both search continuation fixtures violated the requested prefix.', 'AttributesNotEditable request did not change a reserved attribute from the stated prior GET.', 'Case instructions prescribed JSON-mode normalization despite Python-mode Long expectations.'],
                             'correction_review': 'Current author corrections preserve the search prefix, alter the named reserved attribute only in its adverse request, use qualified DELETED-vs-active error context, and align the normalization procedure with the harness. The harness checks prefix and ACTIVE user search results in preflight and executed page paths.'},
          'static_check_provenance': {'script': 'rest071_fresh_static_review.py', 'sha256': sha(BASE / 'rest071_fresh_static_review.py'),
                                      'adapted_from': 'rest071_review_independent.py', 'report_sha256': sha(BASE / 'rest071_fresh_static_review.json'), 'failures': static['failures']},
          'counts': {'operations': len(rows), 'declared_errors': sum(len(c['errors']) for c in manifest['operations']),
                     'additional_cases': sum(len(c['additional_cases']) for c in manifest['operations']), 'findings': len(findings)},
          'harness_inspection': {'supported_sync_async_raw_streaming_success_paths': True, 'ordinary_sync_async_iterator_paths': True,
                                 'named_errors_use_each_error_request_and_wire': True, 'typed_error_identity_parameters_checked': True,
                                 'required_omission_and_schema_rejections_before_http': True, 'socket_and_dns_traps_with_denial_probes': True,
                                 'raw_streaming_transport_cleanup': True, 'timeout_no_retry_and_malformed_json_cases': True,
                                 'literal_wire_path_query_headers_body_auth_timeout_checks': True, 'source_asset_error_hash_preflight': True,
                                 'model_normalization_uses_python_mode_and_canonical_dates': True,
                                 'scope_limit': 'All modes are success paths; each declared service error is exercised through synchronous decoded mode. Synthetic responses establish transport/model behavior, not live server effects or grants.'},
          'operations': rows, 'findings': findings}
(BASE / 'rest071_case_approval.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({'verdict': report['verdict'], 'counts': report['counts'], 'manifest_sha256': sha(CASE), 'report_sha256': sha(BASE / 'rest071_case_approval.json')}))
