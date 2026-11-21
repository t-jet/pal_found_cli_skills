import ast, hashlib, inspect, json, socket, sys, http.client, urllib.request
from pathlib import Path
from unittest.mock import patch
from contextlib import ExitStack

BASE=Path('E:/learn/GenAI_Foundations_DA/git/foundry_cli/.ept/tmp')
ROOT=BASE/'feature015_rest083_review_20261029'
SKILL=ROOT/'.agents/skills/pal-found-dev'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def deny(*a,**k): raise AssertionError('Independent QA: network/DNS/native HTTP denied')
rows=[r for r in json.loads((ROOT/'maintainer/rest-domain-authoring-register.json').read_text())['operations'] if r['story']=='DEV-STORY-083']
out=[]
with ExitStack() as stack:
 for obj,name in [(socket.socket,'connect'),(socket.socket,'connect_ex'),(socket,'create_connection'),(socket,'getaddrinfo'),(socket,'gethostbyname'),(http.client.HTTPConnection,'connect'),(http.client.HTTPSConnection,'connect'),(urllib.request,'urlopen')]: stack.enter_context(patch.object(obj,name,deny))
 for r in rows:
  id=r['id']; _,_,res,op=id.split('.')
  ex=SKILL/r['example']; ns={'__file__':str(ex),'__name__':'qa083_'+res+'_'+op}
  exec(compile(ex.read_text(),str(ex),'exec'),ns)
  try: ns['verify'](); verdict='PASS'; error=None
  except Exception as e: verdict='FAIL'; error=repr(e)
  cls=next(v for k,v in ns.items() if k.endswith('Client') and isinstance(v,type))
  src=Path(inspect.getfile(cls)); tree=ast.parse(src.read_text()); c=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name==cls.__name__)
  fn=next(n for n in c.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)) and n.name==op)
  contract=SKILL/'references/rest/contracts/v2/ontologies'/res/(op+'.md')
  models=sorted(set(__import__('re').findall(r'\[[^\]]*\]\(([^)]+)\)',contract.read_text())))
  out.append(dict(id=id,source_path=str(src),source_sha256=sha(src),source_matches_register=sha(src)==r['source_sha256'],source_function=ast.unparse(fn),source_doc=ast.get_docstring(fn),contract_path=str(contract),contract_sha256=sha(contract),behavior=r['behavior'],behavior_sha256=sha(SKILL/r['behavior']),example=r['example'],example_sha256=sha(ex),fixture_verdict=verdict,fixture_error=error,fixture_success=ns.get('SUCCESS'),fixture_body=ns.get('EXPECTED_BODY'),fixture_path=ns.get('EXPECTED_PATH'),fixture_method=ns.get('EXPECTED_METHOD'),fixture_query=ns.get('EXPECTED_QUERY'),fixture_errors=ns.get('ERRORS'),invoke=next(ast.unparse(n) for n in ast.parse(ex.read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='invoke'),links=models))
(BASE/'rest083_semantic_probe_20261029.json').write_text(json.dumps(out,indent=2,default=str))
for r in out:
 print(r['id'],r['fixture_verdict'],r['fixture_error'],'source_match',r['source_matches_register'])
 print('INVOKE',r['invoke']); print('SUCCESS',r['fixture_success']); print('DOC',r['source_doc'].split(':param')[0])
