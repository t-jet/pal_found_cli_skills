import ast, hashlib, importlib.util, json, re, socket, sys
from pathlib import Path
from unittest.mock import patch
ROOT=Path('E:/learn/GenAI_Foundations_DA/git/foundry_cli/.ept/tmp/feature015_integration')
SKILL=ROOT/'.agents/skills/pal-found-dev'
rows=json.loads((ROOT/'maintainer/rest-domain-authoring-register.json').read_text())['operations']
rows=[r for r in rows if r['story']=='DEV-STORY-091']
oracle=json.loads((ROOT/'tests/fixtures/offline/rest-acceptance/source-oracle.json').read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def deny(*a,**k): raise AssertionError('Network/DNS denied by independent review')
out=[]
for r in rows:
 id=r['id']; _,_,resource,operation=id.split('.')
 ex=SKILL/r['example']; contract=SKILL/('references/rest/contracts/'+id.replace('.', '/')+'.md')
 spec=importlib.util.spec_from_file_location('review_'+resource+'_'+operation,ex); m=importlib.util.module_from_spec(spec)
 exec(compile(ex.read_text(),str(ex),'exec'),m.__dict__)
 with patch.object(socket.socket,'connect',deny),patch.object(socket.socket,'connect_ex',deny),patch.object(socket,'create_connection',deny),patch.object(socket,'getaddrinfo',deny),patch.object(socket,'gethostbyname',deny):
  try:m.verify(); result='PASS';error=None
  except Exception as e:result='FAIL';error=repr(e)
 cls=getattr(m,resource+'Client',None)
 if cls is None: cls=next(v for k,v in vars(m).items() if k.endswith('Client') and isinstance(v,type))
 import inspect
 src=Path(inspect.getfile(cls));tree=ast.parse(src.read_text()); c=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name==cls.__name__); fn=next(n for n in c.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)) and n.name==operation)
 doc=ast.get_docstring(fn) or '';text=contract.read_text();o=oracle['operations'][id]
 mismatches=[]
 if o['ordinary']['signature'] not in text:mismatches.append('signature')
 for k,v in o['wire'].items():
  if v not in text:mismatches.append('wire:'+k)
 out.append(dict(id=id,source_path=str(src),source_sha256=sha(src),registered_source_sha256=r.get('source_sha256'),contract_sha256=sha(contract),behavior_sha256=sha(SKILL/r['behavior']),example_sha256=sha(ex),fixture_verdict=result,fixture_error=error,contract_mismatches=mismatches,doc=doc,fixture_success=getattr(m,'SUCCESS',getattr(m,'ASSET',None)),fixture_body=getattr(m,'EXPECTED_BODY',None),fixture_query=getattr(m,'EXPECTED_QUERY',None),fixture_path=getattr(m,'EXPECTED_PATH',None),fixture_errors=getattr(m,'ERRORS',None),invoke=next((ast.unparse(n) for n in ast.parse(ex.read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='invoke'),ex.read_text()),oracle=o))
Path('E:/learn/GenAI_Foundations_DA/git/foundry_cli/.ept/tmp/rest091_review_probe_20261029.json').write_text(json.dumps(out,indent=2,default=str))
for r in out:
 print(r['id'],r['fixture_verdict'],'source_match',r['source_sha256']==r['registered_source_sha256'],'contract',r['contract_mismatches'])
 print('INVOKE',r['invoke']);print('SUCCESS',json.dumps(r['fixture_success'],default=str)); print('DOC',r['doc'].split(':param')[0])


