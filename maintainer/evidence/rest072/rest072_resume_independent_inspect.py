"""Validate REST072 review inputs against primary SDK source without requests."""
import ast
import hashlib
import importlib
import importlib.metadata
import inspect
import json
import textwrap
from datetime import datetime, timezone
from pathlib import Path

import pydantic

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'feature015_integration/.agents/skills/pal-found-dev'
MANIFEST = ROOT / 'rest072_formal_cases.json'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def plain(value):
    if isinstance(value, pydantic.BaseModel):
        return plain(value.model_dump(mode='json', by_alias=True, exclude_none=True))
    if isinstance(value, dict):
        return {k: plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [plain(v) for v in value]
    return value


def main():
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    assert importlib.metadata.version('foundry-platform-sdk') == manifest['sdk_release']
    results = []
    for case in manifest['operations']:
        module = importlib.import_module(case['source']['module'])
        resource, method = case['operation'].split('.')[-2:]
        function = getattr(getattr(module, resource + 'Client'), method)
        tree = ast.parse(textwrap.dedent(inspect.getsource(function)))
        request = next(node for node in ast.walk(tree) if isinstance(node, ast.Call)
                       and isinstance(node.func, ast.Attribute) and node.func.attr == 'RequestInfo')
        expressions = {kw.arg: ast.unparse(kw.value) for kw in request.keywords}
        assert expressions == case['source']['request_expressions'], case['operation']
        assert sha(case['source']['path']) == case['source']['sha256']
        for asset in case['assets'].values():
            assert sha(ASSETS / asset['path']) == asset['sha256'], asset
            (ASSETS / asset['path']).read_text(encoding='utf-8')
        hints = inspect.get_annotations(function, eval_str=True)
        defaults = {k: v.default for k, v in inspect.signature(function).parameters.items()
                    if v.default is not inspect.Parameter.empty}
        errors = eval(expressions['throwable_errors'], vars(module))
        assert set(errors) == {err['name'] for err in case['errors']}
        checks = [(case['request']['kwargs'], case['request']['expected_wire'])]
        for error in case['errors']:
            assert sha(error['error_source']) == error['error_source_sha256']
            cls = errors[error['name']]
            assert cls.__module__ + '.' + cls.__name__ == error['expected']['exception_class']
            assert error['expected']['parameters'] == error['parameters']
            pydantic.TypeAdapter(inspect.get_annotations(cls, eval_str=True)['parameters']).validate_python(error['parameters'])
            checks.append((error.get('request', case['request']['kwargs']),
                           error.get('expected_wire', case['request']['expected_wire'])))
        response_type = eval(expressions['response_type'], vars(module))
        pydantic.TypeAdapter(response_type).validate_python(case['success']['json'])
        for extra in case.get('additional_cases', []):
            if 'request' in extra and 'expected_wire' in extra:
                checks.append((extra['request'], extra['expected_wire']))
            checks.extend(zip(extra.get('requests', []), extra.get('expected_wires', [])))
            if 'boundary_request' in extra:
                checks.append((extra['boundary_request'], extra['boundary_expected_wire']))
            replies = extra.get('responses', [])
            if 'response' in extra:
                replies = replies + [extra['response']]
            if 'boundary_response' in extra:
                replies = replies + [extra['boundary_response']]
            for reply in replies:
                pydantic.TypeAdapter(response_type).validate_python(reply)
        for kwargs, expected in checks:
            variables = dict(defaults)
            variables.update({key: pydantic.TypeAdapter(hints[key]).validate_python(value)
                              for key, value in kwargs.items()})
            actual = {key: plain(eval(expressions[key], vars(module), variables)) for key in expected}
            actual['query_params'] = {k: v for k, v in actual['query_params'].items() if v is not None}
            assert actual == expected, (case['operation'], actual, expected)
        results.append(dict(operation=case['operation'], source_wire_oracles=len(checks),
                            declared_errors=len(errors), verdict='PASS'))
    prior = json.loads((ROOT / 'rest072_independent_codereview.json').read_text())
    for case in prior['operations']:
        for asset in case['model_error_closure']:
            assert sha(ASSETS / asset['path']) == asset['sha256']
    dedicated = ROOT / 'feature015_integration/tests/test_offline_rest_072.py'
    assert sha(dedicated) == prior['dedicated_unit_review']['sha256']
    report = dict(reviewer_identity='/root/formal072_resume/independent072',
                  reviewed_at=datetime.now(timezone.utc).isoformat(),
                  candidate_sha='a8695c8356a5f42e2e8cf6945753bdaaeaae0071',
                  case_manifest_sha256=sha(MANIFEST), operations=results,
                  harness_sha256=sha(ROOT / 'rest072_formal_execute.py'),
                  verdict='PASS', formal_execution='NOT_RUN',
                  scope='Primary SDK RequestInfo AST evaluation; all baseline/error/additional wires; response types; asset and closure hashes; dedicated regression source inspection.')
    target = ROOT / 'rest072_resume_independent_inspection.json'
    target.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(dict(report=str(target), operations=len(results),
                         declared_errors=sum(row['declared_errors'] for row in results),
                         source_wire_oracles=sum(row['source_wire_oracles'] for row in results))))


if __name__ == '__main__':
    main()
