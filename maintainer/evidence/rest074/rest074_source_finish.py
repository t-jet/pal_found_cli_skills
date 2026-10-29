from pathlib import Path
p=Path('.ept/tmp/rest074_source_build_cases.py');s=p.read_text().replace("'testcase':'TESTCASE-077'","'testcase':'TESTCASE-076'")
s=s.replace("  errors.append({'name':name", "  target=dict(wire['query_params'],**wire['path_params'])\n  if isinstance(wire['body'],dict):target.update(wire['body'])\n  if isinstance(params,dict):params.update({k:v for k,v in target.items() if k in params})\n  envelope['parameters']=copy.deepcopy(params)\n  errors.append({'request':{k:encode(v) for k,v in kw.items()},'expected_wire':copy.deepcopy(wire),'source_condition':['Synthetic service rejection for this exact request. SDK declares this error; tenant conditions are unproven.'],'name':name")
s=s.replace(" extras.append({'name':'optional omission'", " extras.append({'name':'optional omission'")
s=s.replace(" required=[a.arg", " if ret is bytes:extras[-1]['success']={'http_status':200,'content_hex':BINARY.encode().hex(),'expected_bytes_hex':BINARY.encode().hex()}\n if fn=='create' and r=='Branch':extras[-1]['response'].pop('transactionRid',None)\n if fn=='create' and r=='View':extras[-1]['response'].pop('primaryKey',None)\n required=[a.arg")
p.write_text(s)
