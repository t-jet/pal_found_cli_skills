"""Check frozen independent case literals against original SDK without client calls."""
import ast
import hashlib
import importlib
import inspect
import json
import typing
from pathlib import Path
import pydantic

MP = Path('.ept/tmp/rest074_formal_cases.json')
m = json.loads(MP.read_text())
oracle = json.loads(Path('.ept/tmp/feature015_integration/tests/fixtures/offline/rest-acceptance/source-oracle.json').read_text())
dev = Path('.ept/tmp/feature015_integration/.agents/skills/pal-found-dev')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def decode(v):
    if isinstance(v,dict):
        return bytes.fromhex(v['__bytes_hex__']) if set(v)=={'__bytes_hex__'} else {k:decode(x) for k,x in v.items()}
    return [decode(x) for x in v] if isinstance(v,list) else v
def encode(v):
    if isinstance(v,bytes): return {'__bytes_hex__':v.hex()}
    if isinstance(v,pydantic.BaseModel): return v.model_dump(mode='json',by_alias=True,exclude_none=True)
    return v
rows=[]
for r in m['operations']:
    oid=r['operation'];version,domain,resource,method=oid.split('.')
    mod=importlib.import_module(r['source']['module']);text=Path(mod.__file__).read_text();tree=ast.parse(text)
    cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name==resource+'Client')
    fn=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name==method)
    req=next(n for n in ast.walk(fn) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='RequestInfo')
    expr={k.arg:ast.unparse(k.value) for k in req.keywords}
    checks={'source_hash':sha(Path(mod.__file__))==r['source']['sha256']==oracle['operations'][oid]['source_sha256'],'method_hash':hashlib.sha256(ast.get_source_segment(text,fn).encode()).hexdigest()==r['source']['method_source_sha256'],'wire_ast':expr==r['source']['request_expressions']==oracle['operations'][oid]['wire'],'assets':all(sha(dev/a['path'])==a['sha256'] for a in r['assets'].values())}
    signature=inspect.signature(getattr(getattr(mod,resource+'Client'),method))
    def wire(kw):
        args={k:p.default for k,p in signature.parameters.items() if p.default is not inspect.Parameter.empty};args.update(decode(kw));env=dict(mod.__dict__,**args)
        out={k:encode(eval(expr[k],env)) for k in ('method','resource_path','query_params','path_params','header_params','body')}
        out['query_params']={k:v for k,v in out['query_params'].items() if v is not None}
        return out
    checks['request_literal_wire']=wire(r['request']['kwargs'])==r['request']['expected_wire']
    for k,v in decode(r['request']['kwargs']).items():
        ann=signature.parameters[k].annotation
        if isinstance(ann,str):ann=eval(ann,mod.__dict__)
        ta=pydantic.TypeAdapter(ann);ta.validate_python(v)
        assert ta.json_schema()==r['request']['argument_schemas'][k],(oid,k)
    checks['request_argument_schemas']=True
    rt=eval(expr['response_type'],mod.__dict__);adapter=pydantic.TypeAdapter(rt)
    checks['success_schema']=adapter.json_schema()==r['success']['schema']
    body=bytes.fromhex(r['success']['content_hex']) if rt is bytes else r['success']['json'];adapter.validate_python(body)
    checks['success_literal_model']=True
    declared=eval(expr['throwable_errors'],mod.__dict__)
    checks['error_names']=set(declared)=={e['name'] for e in r['errors']}
    for e in r['errors']:
        et=declared[e['name']];pt=typing.get_type_hints(et)['parameters'];ta=pydantic.TypeAdapter(pt);ta.validate_python(e['parameters'])
        assert ta.json_schema()==e['parameter_schema'],(oid,e['name'],'schema')
        assert sha(Path(inspect.getfile(et)))==e['error_source_sha256']
        assert e['expected']['exception_class']==et.__module__+'.'+et.__name__
        assert e['expected']['parameters']==e['parameters']==e['envelope']['parameters']
        base=et.__mro__[1].__name__
        mapping={'BadRequestError':(400,'INVALID_ARGUMENT'),'PermissionDeniedError':(403,'PERMISSION_DENIED'),'NotFoundError':(404,'NOT_FOUND'),'ConflictError':(409,'CONFLICT'),'InternalServerError':(500,'INTERNAL')}
        assert mapping[base]==(e['status'],e['errorCode']),(oid,e['name'])
    checks['error_classes_hashes_schemas_envelopes_status_codes']=True
    for extra in r['additional_cases']:
        if 'expected_wire' in extra:
            assert wire(extra['request'])==extra['expected_wire'],(oid,extra['name'])
        if extra['name']=='finite continuation':
            assert len(extra['requests'])==len(extra['responses'])==2
            for kwargs,expected,response in zip(extra['requests'],extra['expected_wires'],extra['responses']):
                assert wire(kwargs)==expected
                adapter.validate_python(response)
                prefix=kwargs.get('path_prefix')
                if resource=='File' and prefix:assert all(x['path'].startswith(prefix) for x in response['data']),(oid,'prefix')
            assert extra['responses'][0]['nextPageToken']==extra['requests'][1]['page_token']
            assert 'nextPageToken' not in extra['responses'][1]
    checks['additional_request_wires_paging_schemas']=True
    if method in ('read','read_table') and resource=='Dataset':
        assert body.decode().splitlines()[0].split(',')==r['request']['kwargs']['columns']
        assert len(body.decode().splitlines())-1<=r['request']['kwargs']['row_limit']
    rows.append({'id':oid,'checks':checks,'case_sha256':r['case_sha256']})
report={'reviewer':'/root/formal074_prepare/independent_review','manifest_sha256':sha(MP),'operations':rows,'failed_checks':{r['id']:[k for k,v in r['checks'].items() if not v] for r in rows if not all(r['checks'].values())},'operation_count':len(rows),'error_count':sum(len(r['errors']) for r in m['operations']),'additional_case_count':sum(len(r['additional_cases']) for r in m['operations']),'execution':'No client calls or formal test execution.'}
Path('.ept/tmp/rest074_review_cases.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='operations'}))
