"""Independently bind REST-074 assets to original SDK source without executing fixtures."""
import ast
import hashlib
import importlib
import inspect
import json
import typing
from pathlib import Path

import pydantic

ROOT = Path('.ept/tmp/feature015_integration')
DEV = ROOT / '.agents/skills/pal-found-dev'
ORACLE = ROOT / 'tests/fixtures/offline/rest-acceptance/source-oracle.json'
oracle = json.loads(ORACLE.read_text())
authors = {r['id']: r for r in json.loads((ROOT/'maintainer/rest-domain-authoring-register.json').read_text())['operations']}
contracts = {r['id']: r for r in json.loads((ROOT/'maintainer/rest-contract-register.json').read_text())['operations']}
prior = {r['id']: r for r in json.loads((ROOT/'maintainer/rest-qa-074.json').read_text())['operations']}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def norm(value):
    if hasattr(value, 'model_dump'):
        return value.model_dump(mode='json', by_alias=True, exclude_none=True)
    return value

rows = []
for oid, entry in oracle['operations'].items():
    version, domain, resource, method = oid.split('.')
    if domain != 'datasets':
        continue
    author = authors[oid]
    contract = contracts[oid]
    mod = importlib.import_module(entry['module'])
    source = Path(mod.__file__)
    text = source.read_text()
    tree = ast.parse(text)
    cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == resource+'Client')
    fn = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == method)
    call = next(n for n in ast.walk(fn) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == 'RequestInfo')
    wire = {k.arg: ast.unparse(k.value) for k in call.keywords}
    fixture = DEV/author['example']
    ft = ast.parse(fixture.read_text())
    literal = {n.targets[0].id: ast.literal_eval(n.value) for n in ft.body if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) and n.targets[0].id in ('SUCCESS', 'ERRORS', 'EXPECTED_METHOD', 'EXPECTED_PATH', 'EXPECTED_BODY', 'EXPECTED_QUERY', 'EXPECTED_HEADERS')}
    invoke = next(n for n in ft.body if isinstance(n, ast.FunctionDef) and n.name == 'invoke')
    invocation = next(n for n in ast.walk(invoke) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == method)
    arguments = {k.arg: eval(compile(ast.Expression(k.value), '<fixture argument>', 'eval'), {'__builtins__': {}}, literal) for k in invocation.keywords}
    signature = inspect.signature(getattr(getattr(mod, resource+'Client'), method))
    args = {k: p.default for k,p in signature.parameters.items() if p.default is not inspect.Parameter.empty}
    args.update(arguments)
    env = dict(mod.__dict__, **args)
    evaluated = {k: eval(v, env) for k,v in wire.items() if k != 'response_mode'}
    declared = evaluated['throwable_errors']
    rt = evaluated['response_type']
    checks = {
        'source_hash_oracle_author_contract': sha(source) == entry['source_sha256'] == author['source_sha256'] == contract['source_sha256'],
        'signature_original_ast': ast.unparse(fn.args) == entry['ordinary']['signature'],
        'wire_original_ast': wire == entry['wire'],
        'behavior_hash_author': sha(DEV/author['behavior']) == author['behavior_sha256'],
        'example_hash_author': sha(fixture) == author['example_sha256'],
        'contract_hash_prior_review': sha(DEV/contract['contract']) == prior[oid]['contract_sha256'],
        'request_method': evaluated['method'] == literal['EXPECTED_METHOD'],
        'request_path': '/api'+evaluated['resource_path'].format(**evaluated['path_params']) == literal['EXPECTED_PATH'],
        'request_query': evaluated['query_params'] == literal['EXPECTED_QUERY'],
        'request_headers': evaluated['header_params'] == literal['EXPECTED_HEADERS'],
        'request_body_model': norm(evaluated['body']) == literal['EXPECTED_BODY'],
        'error_names': set(declared) == {e['name'] for e in literal['ERRORS']},
    }
    result = pydantic.TypeAdapter(rt).validate_python(literal['SUCCESS'])
    checks['result_model_valid'] = True
    errors = []
    for error in literal['ERRORS']:
        et = declared[error['name']]
        params_type = typing.get_type_hints(et)['parameters']
        pydantic.TypeAdapter(params_type).validate_python(error['parameters'])
        base = et.__mro__[1].__name__
        status = {'BadRequestError':400, 'PermissionDeniedError':403, 'NotFoundError':404, 'ConflictError':409, 'UnprocessableEntityError':422, 'InternalServerError':500}.get(base)
        code = {'BadRequestError':'INVALID_ARGUMENT', 'PermissionDeniedError':'PERMISSION_DENIED', 'NotFoundError':'NOT_FOUND', 'ConflictError':'CONFLICT', 'UnprocessableEntityError':'FAILED_PRECONDITION', 'InternalServerError':'INTERNAL'}.get(base)
        errors.append({'name': error['name'], 'class': et.__module__+'.'+et.__name__, 'parameters_schema_valid': True, 'status_match': status == error['status'], 'code_match': code == error['code'], 'base': base})
    checks['errors_source_class_status_code_schema'] = all(e['status_match'] and e['code_match'] for e in errors)
    ct = (DEV/contract['contract']).read_text()
    bt = (DEV/author['behavior']).read_text()
    checks['contract_source_signature'] = entry['ordinary']['signature'] in ct
    checks['contract_wire_expressions'] = all(expression in ct for expression in wire.values())
    checks['behavior_operation_and_errors'] = '### '+method in bt and all('| '+name+' |' in bt for name in declared)
    rows.append({'id':oid,'checks':checks,'source':str(source),'source_sha256':sha(source),'example':str(fixture),'example_sha256':sha(fixture),'behavior':str(DEV/author['behavior']),'behavior_sha256':sha(DEV/author['behavior']),'contract':str(DEV/contract['contract']),'contract_sha256':sha(DEV/contract['contract']),'request_arguments':{k:v if not isinstance(v,bytes) else {'bytes':v.decode()} for k,v in arguments.items()},'success':literal['SUCCESS'] if not isinstance(literal['SUCCESS'],bytes) else {'bytes':literal['SUCCESS'].decode()},'errors':errors,'source_description':ast.get_docstring(fn)})

report = {'reviewer':'/root/formal074_prepare/independent_review','kind':'Independent static review; no fixture or formal harness execution','source_oracle_sha256':sha(ORACLE),'operations':rows,'count':len(rows),'failed_checks':{r['id']:[k for k,v in r['checks'].items() if not v] for r in rows if not all(r['checks'].values())}}
Path('.ept/tmp/rest074_review_static.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'count':len(rows),'failed_checks':report['failed_checks']}))
