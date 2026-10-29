import json,ast,importlib,pydantic
from pathlib import Path
ops=json.loads(Path('.ept/tmp/feature015_rest074_current_semantic_review.json').read_text())['operations']
for o in ops:
 m=importlib.import_module('foundry_sdk.'+'.'.join(o['id'].split('.')[:2])+'.'+Path(o['source_module']).stem); r,fn=o['id'].split('.')[-2:];t=ast.parse(Path(m.__file__).read_text());c=next(n for n in t.body if isinstance(n,ast.ClassDef) and n.name==r+'Client');f=next(n for n in c.body if isinstance(n,ast.FunctionDef) and n.name==fn);req=next(n for n in ast.walk(f) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='RequestInfo');e={k.arg:ast.unparse(k.value) for k in req.keywords}
 print(o['id'],ast.unparse(f.args), 'RETURN',e['response_type'])
 if r=='View' or fn in ('read_table','upload','read'):
  typ=eval(e['response_type'],m.__dict__)
  try: print(json.dumps(pydantic.TypeAdapter(typ).json_schema()))
  except Exception as ex:print(type(ex).__name__)
