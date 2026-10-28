"""Review case literals against SDK source without invoking SDK operations."""
import ast
import hashlib
import importlib
import inspect
import json
import typing
from datetime import datetime
from pathlib import Path

import pydantic
from foundry_sdk._core.api_client import ApiClient

BASE = Path(__file__).resolve().parent
MANIFEST = BASE / 'rest071_formal_cases.json'
SKILL = BASE / 'feature015_integration/.agents/skills/pal-found-dev'
rows = []
failures = []


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check(ok, label):
    if not ok:
        failures.append(label)
    return bool(ok)


def materialize(value):
    if isinstance(value, dict):
        if set(value) == {'__bytes_hex__'}:
            return bytes.fromhex(value['__bytes_hex__'])
        return {k: materialize(v) for k, v in value.items()}
    if isinstance(value, list):
        return [materialize(v) for v in value]
    return value


def wire(exprs, namespace, hints, signature, kwargs):
    values = {key: parameter.default for key, parameter in signature.parameters.items()
              if parameter.default is not inspect.Parameter.empty}
    values.update({k: pydantic.TypeAdapter(hints[k]).validate_python(materialize(v)) for k, v in kwargs.items()})
    answer = {}
    for field in ('method', 'resource_path', 'query_params', 'path_params', 'header_params', 'body'):
        value = eval(compile(ast.Expression(exprs[field]), '<source request>', 'eval'), namespace, values)
        if field == 'body' and value is not None and not isinstance(value, bytes):
            value = json.loads(json.dumps(value, cls=ApiClient._BaseModelJSONEncoder))
        if field == 'query_params':
            value = {k: v for k, v in value.items() if v is not None}
        answer[field] = value
    return answer


def expected_wire(value):
    value = materialize(value)
    value['query_params'] = {k: v for k, v in value['query_params'].items() if v is not None}
    return value


manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
for case in manifest['operations']:
    cid = case['case_id']
    module = importlib.import_module(case['source']['module'])
    resource, method = case['operation'].split('.')[-2:]
    source_text = Path(module.__file__).read_text(encoding='utf-8')
    tree = ast.parse(source_text)
    sync_class = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == resource + 'Client')
    method_ast = next(n for n in sync_class.body if isinstance(n, ast.FunctionDef) and n.name == method)
    request_ast = next(n for n in ast.walk(method_ast) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == 'RequestInfo')
    exprs = {k.arg: k.value for k in request_ast.keywords}
    fn = getattr(getattr(module, resource + 'Client'), method)
    hints = typing.get_type_hints(fn, include_extras=True)
    signature = inspect.signature(fn)
    checks = {}
    checks['source_hash'] = check(sha(module.__file__) == case['source']['sha256'], cid + ': source hash')
    checks['actual_ast_expressions'] = check(all(ast.unparse(exprs[k]) == v for k, v in case['source']['request_expressions'].items()), cid + ': expressions')
    checks['asset_hashes'] = check(all(sha(SKILL / a['path']) == a['sha256'] for a in case['assets'].values()), cid + ': assets')
    checks['wire_literal'] = check(wire(exprs, vars(module), hints, signature, case['request']['kwargs']) == expected_wire(case['request']['expected_wire']), cid + ': wire')
    response_type = eval(compile(ast.Expression(exprs['response_type']), '<response>', 'eval'), vars(module))
    response_adapter = pydantic.TypeAdapter(response_type)
    checks['response_schema'] = check(response_adapter.json_schema() == case['success']['schema'], cid + ': response schema')
    reply = case['success']
    response_adapter.validate_python(bytes.fromhex(reply['content_hex']) if 'content_hex' in reply else reply['json'])
    checks['response_valid'] = True
    errors = eval(compile(ast.Expression(exprs['throwable_errors']), '<errors>', 'eval'), vars(module))
    checks['exact_declared_errors'] = check(set(errors) == {e['name'] for e in case['errors']}, cid + ': errors')
    for e in case['errors']:
        error_type = errors[e['name']]
        adapter = pydantic.TypeAdapter(typing.get_type_hints(error_type)['parameters'])
        check(adapter.json_schema() == e['parameter_schema'], cid + ': error schema ' + e['name'])
        adapter.validate_python(e['parameters'])
        check(error_type.__module__ + '.' + error_type.__name__ == e['expected']['exception_class'], cid + ': error class ' + e['name'])
        check(sha(e['error_source']) == e['error_source_sha256'], cid + ': error hash ' + e['name'])
        check(wire(exprs, vars(module), hints, signature, e['request']) == expected_wire(e['expected_wire']), cid + ': error wire ' + e['name'])
    for extra in case['additional_cases']:
        label = cid + ': extra ' + extra['name']
        if 'expected_exception' in extra:
            invalid = False
            try:
                bound = signature.bind(None, **materialize(extra['request']))
                for key, value in extra['request'].items():
                    pydantic.TypeAdapter(hints[key]).validate_python(materialize(value))
            except (TypeError, pydantic.ValidationError):
                invalid = True
            check(invalid, label + ' invalid request')
            continue
        for kwargs, expected in zip(extra.get('requests', [extra['request']] if 'request' in extra else []), extra.get('expected_wires', [extra['expected_wire']] if 'expected_wire' in extra else [])):
            check(wire(exprs, vars(module), hints, signature, kwargs) == expected_wire(expected), label + ' wire')
        for reply in extra.get('responses', [extra['response']] if 'response' in extra else []):
            response_adapter.validate_python(reply)
        if 'success' in extra:
            reply = extra['success']
            response_adapter.validate_python(bytes.fromhex(reply['content_hex']) if 'content_hex' in reply else reply['json'])
        if 'requests' in extra:
            check(extra['expected_request_count'] == len(extra['requests']) == len(extra['responses']), label + ' finite count')
            check(extra['responses'][-1].get('nextPageToken') is None, label + ' terminal token')
            for index, kwargs in enumerate(extra['requests']):
                token = None if index == 0 else extra['responses'][index - 1]['nextPageToken']
                check(kwargs['page_token'] == token, label + ' token propagation')
    checks['all_additional_reviewed'] = len(case['additional_cases'])
    rows.append({'case_id': cid, 'operation': case['operation'], 'checks': checks})

evidence = {'reviewer': '/root/rest071_finish_20261027/independent071_review', 'execution': 'NOT_RUN',
            'method': 'Independent SDK AST, schema and model-only checks; no client construction or SDK operation invocation.',
            'manifest': {'path': str(MANIFEST), 'sha256': sha(MANIFEST)},
            'operations': rows, 'failures': failures}
(BASE / 'rest071_fresh_static_review.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'operations': len(rows), 'additional_cases': sum(len(c['additional_cases']) for c in manifest['operations']), 'errors': sum(len(c['errors']) for c in manifest['operations']), 'failures': failures}))
