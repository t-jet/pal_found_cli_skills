import ast,hashlib,importlib,json,pydantic,typing
from pathlib import Path
p=Path('.ept/tmp/rest074_formal_cases.json');d=json.loads(p.read_text());issues=[];counts={'operations':0,'request_arguments':0,'success_payloads':0,'error_parameters':0,'asset_hashes':0}
def check(label,fn):
 try:fn()
 except Exception as ex:issues.append({'item':label,'error':str(ex)})
def decode(v):return bytes.fromhex(v['__bytes_hex__']) if isinstance(v,dict) and set(v)=={'__bytes_hex__'} else v
for o in d['operations']:
 counts['operations']+=1;m=importlib.import_module(o['source']['module']);r,f=o['operation'].split('.')[-2:];t=ast.parse(Path(m.__file__).read_text());cl=next(n for n in t.body if isinstance(n,ast.ClassDef) and n.name==r+'Client');func=next(n for n in cl.body if isinstance(n,ast.FunctionDef) and n.name==f)
 for a in [*func.args.args,*func.args.kwonlyargs]:
  if a.arg not in o['request']['kwargs']:continue
  typ=eval(ast.unparse(a.annotation),m.__dict__);counts['request_arguments']+=1;check(o['operation']+' argument '+a.arg,lambda:pydantic.TypeAdapter(typ).validate_python(decode(o['request']['kwargs'][a.arg])))
 ret=eval(o['source']['request_expressions']['response_type'],m.__dict__)
 if ret is not bytes:
  payloads=[o['success']['json']]
  for extra in o['additional_cases']:
   if 'response' in extra:payloads.append(extra['response'])
   payloads.extend(extra.get('responses',[]))
  for n,value in enumerate(payloads):counts['success_payloads']+=1;check(o['operation']+' payload '+str(n),lambda:pydantic.TypeAdapter(ret).validate_python(value))
 for e in o['errors']:
  em=importlib.import_module(e['expected']['exception_class'].rsplit('.',1)[0]);ec=getattr(em,e['name']);typ=typing.get_type_hints(ec)['parameters'];counts['error_parameters']+=1;check(o['operation']+' '+e['name'],lambda:pydantic.TypeAdapter(typ).validate_python(e['parameters']))
 for a in o['assets'].values():
  counts['asset_hashes']+=1;actual=hashlib.sha256((Path('.ept/tmp/feature015_integration/.agents/skills/pal-found-dev')/a['path']).read_bytes()).hexdigest()
  if actual!=a['sha256']:issues.append({'asset':a['path'],'error':'hash changed'})
out={'manifest_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'validation_kind':'Source schema preflight only; operation clients and examples were not invoked. This is not case approval or formal execution.','counts':counts,'issues':issues}
Path('.ept/tmp/rest074_source_validation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
