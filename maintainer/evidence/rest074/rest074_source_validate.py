import json,importlib,pydantic
from pathlib import Path
p=Path('.ept/tmp/rest074_formal_cases.json');d=json.loads(p.read_text());fails=[]
for o in d['operations']:
 m=importlib.import_module(o['source']['module']);ret=eval(o['source']['request_expressions']['response_type'],m.__dict__)
 if ret is not bytes:
  try:pydantic.TypeAdapter(ret).validate_python(o['success']['json'])
  except Exception as e:fails.append((o['operation'],str(e)))
 print(o['operation'],json.dumps(o['request']['kwargs']),'=>',json.dumps(o['success'].get('json'))[:500])
print('FAILURES',json.dumps(fails))
