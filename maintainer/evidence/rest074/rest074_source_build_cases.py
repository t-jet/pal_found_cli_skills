"""Prepare independent source-derived cases; do not invoke operation clients or examples."""
import ast,copy,hashlib,importlib,inspect,json,subprocess,typing
from pathlib import Path
import pydantic
BASE=Path('.ept/tmp/feature015_integration'); SKILL=BASE/'.agents/skills/pal-found-dev'; OUT=Path('.ept/tmp/rest074_formal_cases.json')
IDENTITY='/root/formal074_prepare/source_cases'
UUID='00000000-0000-0000-0000-000000000074'
DATASET='ri.foundry.main.dataset.independent074'
TX='ri.foundry.main.transaction.independent074'
VIEW='ri.foundry.main.dataset.view074'
BACK='ri.foundry.main.dataset.backing074'
SURVIVOR='ri.foundry.main.dataset.survivor074'
FOLDER='ri.folder.main.folder.independent074'
BINARY='inspection_id,status\n074,independent\n'
SCHEMA={'fieldSchemaList':[{'type':'STRING','name':'inspection_id','nullable':False},{'type':'STRING','name':'status','nullable':False}]}
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def schema(t):return pydantic.TypeAdapter(t).json_schema()
def sample(s,root=None,depth=0):
 root=s if root is None else root
 if depth>8:return None
 if '$ref' in s:return sample(root['$defs'][s['$ref'].split('/')[-1]],root,depth+1)
 if 'const' in s:return s['const']
 if 'enum' in s:return s['enum'][0]
 for u in ('anyOf','oneOf'):
  if u in s:
   choice=next((x for x in s[u] if x.get('type')!='null'),s[u][0]);return sample(choice,root,depth+1)
 t=s.get('type')
 if t=='object':
  if s.get('properties'):return {k:sample(v,root,depth+1) for k,v in s['properties'].items() if k in s.get('required',[]) or 'const' in v}
  if s.get('patternProperties'):return {DATASET:sample(next(iter(s['patternProperties'].values())),root,depth+1)}
  return {'independent074':sample(s['additionalProperties'],root,depth+1)} if isinstance(s.get('additionalProperties'),dict) else {}
 if t=='array':return [sample(s.get('items',{}),root,depth+1)] if depth<6 else []
 if t=='integer':return max(2,s.get('minimum',2))
 if t=='number':return 2.5
 if t=='boolean':return True
 if t=='null':return None
 if s.get('format')=='date-time':return '2026-10-21T08:00:00Z'
 if s.get('format')=='date':return '2026-10-21'
 if s.get('format')=='uuid' or '0-9a-fA-F' in s.get('pattern',''):return UUID
 if s.get('pattern','').startswith('^ri'):return DATASET
 return 'independent074' if t=='string' else {}
def encode(v):
 if isinstance(v,bytes):return {'__bytes_hex__':v.hex()}
 if isinstance(v,pydantic.BaseModel):return v.model_dump(mode='json',by_alias=True,exclude_none=True)
 return v
def wire_for(expr,mod,kw):
 env=dict(mod.__dict__,**kw);result={k:encode(eval(expr[k],env)) for k in ('method','resource_path','query_params','path_params','header_params','body')};result['query_params']={k:v for k,v in result['query_params'].items() if v is not None};return result
ops=json.loads(Path('.ept/tmp/feature015_rest074_current_semantic_review.json').read_text())['operations']
oracle=json.loads((BASE/'tests/fixtures/offline/rest-acceptance/source-oracle.json').read_text());rows=[];gaps=[]
for index,asset in enumerate(ops,1):
 op=asset['id'];r,fn=op.split('.')[-2:];modname='foundry_sdk.'+'.'.join(op.split('.')[:2])+'.'+Path(asset['source_module']).stem;mod=importlib.import_module(modname);mp=Path(mod.__file__);src=mp.read_text();tree=ast.parse(src);cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name==r+'Client');f=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name==fn);req=next(n for n in ast.walk(f) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='RequestInfo');expr={k.arg:ast.unparse(k.value) for k in req.keywords};doc=ast.get_docstring(f);arg_schema={};kw={}
 assert h(mp)==oracle['operations'][op]['source_sha256'],op+' frozen module hash'
 for a in [*f.args.args,*f.args.kwonlyargs]:
  if a.arg in ('self','_sdk_internal','request_timeout'):continue
  typ=eval(ast.unparse(a.annotation),mod.__dict__);arg_schema[a.arg]=schema(typ);kw[a.arg]=sample(arg_schema[a.arg])
  if typ is bytes:kw[a.arg]=BINARY.encode()
 for k in kw:
  if k in ('dataset_rid','view_dataset_rid'):kw[k]=DATASET if k=='dataset_rid' else VIEW
  elif k=='parent_folder_rid':kw[k]=FOLDER
  elif k.endswith('transaction_rid'):kw[k]=TX if k!='start_transaction_rid' else 'ri.foundry.main.transaction.start074'
  elif k in ('branch_id','branch_name','branch'):kw[k]='master'
  elif k=='file_path':kw[k]='inspections-independent/status.csv'
  elif k in ('name','view_name'):kw[k]='Inspections independent 074' if r!='Branch' else 'master'
  elif k=='preview':kw[k]=True
  elif k=='path_prefix':kw[k]='inspections-independent/'
  elif k=='page_size':kw[k]=2
  elif k=='page_token':kw[k]='independent-next074'
  elif k=='row_limit':kw[k]=2
  elif k=='columns':kw[k]=['inspection_id','status']
  elif k=='format':kw[k]='CSV'
  elif k=='schema':kw[k]=copy.deepcopy(SCHEMA)
  elif k=='dataframe_reader':kw[k]=None
  elif k=='where':kw[k]={'type':'timeFilter','field':'SUBMITTED_TIME','comparisonType':'GTE','value':'2026-10-21T08:00:00Z'}
  elif k=='primary_key':kw[k]={'columns':['inspection_id'],'resolution':{'type':'unique'}}
  elif k=='backing_datasets':kw[k]=[{'datasetRid':BACK,'branch':'master','stopPropagatingMarkingIds':[]}]
 if op=='v1.datasets.Dataset.replace_schema':kw['body']=copy.deepcopy(SCHEMA)
 if fn=='get_schema_batch':kw['body']=[{'datasetRid':DATASET,'branchName':'master'},{'datasetRid':SURVIVOR,'branchName':'master'}]
 wire=wire_for(expr,mod,kw);ret=eval(expr['response_type'],mod.__dict__);rs=schema(ret);reply=sample(rs)
 if ret is None or ret is type(None):reply=None
 if r=='Branch' and fn!='transactions' and isinstance(reply,dict) and 'data' not in reply:
  reply.update({'branchId' if op.startswith('v1') else 'name':'master','transactionRid':kw.get('transaction_rid',TX)})
 if r=='Dataset' and fn in ('get','create'):reply.update(rid=kw.get('dataset_rid',DATASET),name=kw.get('name','Inspections independent 074'),parentFolderRid=kw.get('parent_folder_rid',FOLDER))
 if r=='File' and fn in ('get','upload'):
  reply.update(path=kw['file_path'],transactionRid=kw.get('transaction_rid',kw.get('end_transaction_rid',TX)),sizeBytes=len(BINARY.encode()))
 if r=='Transaction' and isinstance(reply,dict):
  reply.update(rid=kw.get('transaction_rid',TX),status={'abort':'ABORTED','commit':'COMMITTED'}.get(fn,'OPEN'),transactionType=kw.get('transaction_type','APPEND'))
  if fn in ('abort','commit'):reply['closedTime']='2026-10-21T08:01:00Z'
 if r=='View':
  reply.update(viewName=kw.get('view_name','Inspections independent 074'),datasetRid=kw.get('view_dataset_rid',VIEW),parentFolderRid=kw.get('parent_folder_rid',FOLDER),branch=kw.get('branch','master'),backingDatasets=copy.deepcopy(kw.get('backing_datasets',[{'datasetRid':BACK,'branch':'master','stopPropagatingMarkingIds':[]}])) )
  if fn=='remove_backing_datasets':reply['backingDatasets']=[{'datasetRid':SURVIVOR,'branch':'master','stopPropagatingMarkingIds':[]}]
  if fn=='add_primary_key':reply['primaryKey']=copy.deepcopy(kw['primary_key'])
  elif fn=='create' and kw.get('primary_key') is not None:reply['primaryKey']=copy.deepcopy(kw['primary_key'])
  else:reply.pop('primaryKey',None)
 if op=='v1.datasets.Dataset.get_schema':reply=copy.deepcopy(SCHEMA)
 if fn in ('get_schema','put_schema') and op.startswith('v2'):
  reply.update(branchName=kw.get('branch_name','master'),endTransactionRid=kw.get('end_transaction_rid',TX),schema=copy.deepcopy(kw.get('schema',SCHEMA)),versionId=kw.get('version_id',UUID))
 if fn=='get_schema_batch':reply={'data':{q['datasetRid']:{'branchName':q['branchName'],'endTransactionRid':TX,'schema':copy.deepcopy(SCHEMA),'versionId':UUID} for q in kw['body']}}
 if op=='v2.datasets.Dataset.get_health_check_reports':
  reply={'data':{'ri.health.main.check.independent074':{'rid':'ri.health.main.report.independent074','check':{'rid':'ri.health.main.check.independent074','groups':[],'config':{'type':'buildStatus','subject':{'datasetRid':DATASET,'branchId':'master'},'statusCheckConfig':{'severity':'CRITICAL'}}},'result':{'status':'PASSED'},'createdTime':'2026-10-21T08:00:00Z'}}}
 if op=='v2.datasets.Dataset.get_health_checks':reply={'data':['ri.health.main.check.independent074']}
 if op=='v2.datasets.Dataset.get_schedules':reply={'data':['ri.scheduler.main.schedule.independent074']}
 if op=='v2.datasets.Dataset.jobs':reply={'data':[{'jobRid':'ri.foundry.main.job.independent074'}]}
 if op=='v2.datasets.Transaction.build':reply='ri.foundry.main.build.independent074'
 if op=='v2.datasets.Transaction.job':reply='ri.foundry.main.job.independent074'
 if fn=='transactions':
  reply={'data':[{'rid':TX,'transactionType':'APPEND','status':'COMMITTED','createdTime':'2026-10-21T08:00:00Z','closedTime':'2026-10-21T08:01:00Z'}]}
 if r=='File' and fn=='list':reply={'data':[{'path':'inspections-independent/status.csv','transactionRid':TX,'updatedTime':'2026-10-21T08:00:00Z','sizeBytes':len(BINARY.encode())}]}
 success={'http_status':204 if ret is None else 200,'json':reply,'result_type':expr['response_type'],'schema':rs,'assertions':['Assert ordinary typed result against literal response with model_dump(mode="json", by_alias=True, exclude_none=True).','Do not call to_dict on model fields that shadow Python names; inspect aliases and exact schema fields.','Assert raw wrapper decoding and closure; streaming wrapper closes after consumption.']}
 if ret is bytes:success.update(json=None,content_hex=BINARY.encode().hex(),expected_bytes_hex=BINARY.encode().hex());success['assertions']=['Assert ordinary result equals bytes.fromhex(content_hex).','Assert raw and streaming responses yield exact bytes and close after consumption.']
 errors=[]
 for name,ec in eval(expr['throwable_errors'],mod.__dict__).items():
  es=schema(typing.get_type_hints(ec)['parameters']);params=sample(es)
  if isinstance(params,dict):params.update({k:v for k,v in wire['path_params'].items() if k in params})
  mapping={'BadRequestError':(400,'INVALID_ARGUMENT'),'InternalServerError':(500,'INTERNAL'),'UnauthorizedError':(401,'UNAUTHORIZED'),'UnprocessableEntityError':(422,'INVALID_ARGUMENT'),'NotFoundError':(404,'NOT_FOUND'),'PermissionDeniedError':(403,'PERMISSION_DENIED'),'InvalidArgumentError':(400,'INVALID_ARGUMENT'),'ConflictError':(409,'CONFLICT'),'InternalError':(500,'INTERNAL'),'FailedPreconditionError':(400,'FAILED_PRECONDITION'),'RequestEntityTooLargeError':(413,'REQUEST_ENTITY_TOO_LARGE'),'TimeoutError':(500,'TIMEOUT'),'CustomClientError':(400,'CUSTOM_CLIENT'),'CustomServerError':(500,'CUSTOM_SERVER')}
  base=next((c.__name__ for c in ec.__mro__[1:] if c.__name__ in mapping),None)
  if base is None:raise ValueError((op,name,[c.__name__ for c in ec.__mro__]))
  status,code=mapping[base];envelope={'errorName':name,'errorCode':code,'parameters':params,'errorInstanceId':UUID}
  target=dict(wire['query_params'],**wire['path_params'])
  if isinstance(wire['body'],dict):target.update(wire['body'])
  if isinstance(params,dict):params.update({k:v for k,v in target.items() if k in params})
  envelope['parameters']=copy.deepcopy(params)
  errors.append({'request':{k:encode(v) for k,v in kw.items()},'expected_wire':copy.deepcopy(wire),'source_condition':['Synthetic service rejection for this exact request. SDK declares this error; tenant conditions are unproven.'],'name':name,'status':status,'errorCode':code,'parameters':params,'parameter_schema':es,'error_source':inspect.getfile(ec),'error_source_sha256':h(inspect.getfile(ec)),'error_base':base,'envelope':envelope,'expected':{'exception_class':ec.__module__+'.'+name,'name':name,'parameters':copy.deepcopy(params),'error_instance_id':UUID},'assertions':['Assert exact SDK exception class, name, parameters and error_instance_id.','Assert one HTTP request and no successful result.']})
 assets={k:{'path':asset[k+'_path'],'sha256':h(SKILL/asset[k+'_path'])} for k in ('contract','behavior','example')}
 row={'case_id':f'F074-{index:02d}','operation':op,'source':{'module':modname,'path':str(mp),'sha256':h(mp),'method_source_sha256':hashlib.sha256(ast.get_source_segment(src,f).encode()).hexdigest(),'line':f.lineno,'docstring':doc,'request_expressions':expr,'oracle_sha256':h(BASE/'tests/fixtures/offline/rest-acceptance/source-oracle.json')},'assets':assets,'request':{'kwargs':{k:encode(v) for k,v in kw.items()},'argument_schemas':arg_schema,'expected_wire':wire,'path_prefix':'/api','timeout':7,'authorization':'Bearer independent-qa-074'},'success':success,'errors':errors,'semantic_expectation':doc.split(':param')[0].strip(),'source_silence':['SDK source does not establish tenant grants, live mutation effects, universal idempotency or a retry policy.','Mock responses verify transport and decoding; server validation and resource lifecycle effects require an authorized tenant.'],'additional_cases':[],'review':{'example_fixture_executed':False}}
 extras=row['additional_cases']
 optional=[a.arg for a,default in zip(f.args.kwonlyargs,f.args.kw_defaults) if default is not None and a.arg in kw]
 omit=copy.deepcopy(kw);omit.update({k:None for k in optional if k!='preview'})
 extras.append({'name':'optional omission','request':{k:encode(v) for k,v in omit.items()},'expected_wire':wire_for(expr,mod,omit),'response':copy.deepcopy(reply) if ret is not bytes else None,'response_status':success['http_status'],**({'content_hex':BINARY.encode().hex()} if ret is bytes else {})})
 if ret is bytes:extras[-1]['success']={'http_status':200,'content_hex':BINARY.encode().hex(),'expected_bytes_hex':BINARY.encode().hex()}
 if fn=='create' and r=='Branch':extras[-1]['response'].pop('transactionRid',None)
 if fn=='create' and r=='View':extras[-1]['response'].pop('primaryKey',None)
 required=[a.arg for a in f.args.args[:len(f.args.args)-len(f.args.defaults)] if a.arg!='self']+[a.arg for a,default in zip(f.args.kwonlyargs,f.args.kw_defaults) if default is None]
 if required:
  missing=copy.deepcopy(row['request']['kwargs']);missing.pop(required[0]);extras.append({'name':'required argument omitted','request':missing,'omitted_parameter':required[0],'expected_exception':'pydantic.ValidationError','expected_request_count':0})
 if 'pageToken' in wire['query_params']:
  first=copy.deepcopy(kw);first['page_token']=None;second=copy.deepcopy(kw);second['page_token']='independent-next074';a=copy.deepcopy(reply);b=copy.deepcopy(reply);a['nextPageToken']='independent-next074';b.pop('nextPageToken',None)
  for page,suffix in ((a,'A'),(b,'B')):
   if isinstance(page.get('data'),list) and page['data']:
    item=page['data'][0]
    if isinstance(item,dict):
     field=next((k for k in ('branchId','name','path','rid','jobRid') if k in item),None)
     if field:item[field]=('ri.foundry.main.'+('job' if field=='jobRid' else 'transaction')+'.page'+suffix+'074') if field in ('rid','jobRid') else ('inspections-independent/page'+suffix+'.csv' if field=='path' else 'independent-page'+suffix+'074')
    else:page['data']=['ri.scheduler.main.schedule.page'+suffix+'074']
  extras.append({'name':'finite continuation','requests':[first,second],'expected_wires':[wire_for(expr,mod,first),wire_for(expr,mod,second)],'responses':[a,b],'response_status':200,'expected_request_count':2,'expected_terminal_token':None,'steps':['Return two nonempty pages with distinct identities.','Carry returned token into second request; preserve scope and filters.','Stop when terminal response omits nextPageToken. Requested page size does not prove service page count.']})
 if fn=='get_schema_batch':
  for length in (0,1001):
   bad=copy.deepcopy(kw);bad['body']=[{'datasetRid':DATASET}]*length;extras.append({'name':f'batch length {length} rejected locally','request':bad,'expected_exception':'pydantic.ValidationError','expected_request_count':0,'provenance':'Annotated Len(min_length=1,max_length=1000) on SDK request body.'})
 if r=='View' and fn=='remove_backing_datasets':row['precondition']={'backingDatasets':[{'datasetRid':BACK,'branch':'master','stopPropagatingMarkingIds':[]},{'datasetRid':SURVIVOR,'branch':'master','stopPropagatingMarkingIds':[]}]}
 row['gherkin']={'feature':op,'scenarios':[{'name':row['case_id']+' literal request and typed success','given':['Pinned SDK source hashes match manifest.','Network sockets denied; fresh MockTransport returns success literals.'],'when':['Call '+op+' using request.kwargs and timeout 7.'],'then':['Compare exact method, substituted path, complete query, headers and body with request.expected_wire.','Compare normalized result with success.json or exact success.expected_bytes_hex.','Close raw and streaming wrappers after consuming result.']},{'name':row['case_id']+' each declared error','given':['For each errors entry, transport returns exact status and envelope literals.'],'when':['Call operation using same request.'],'then':['Exact exception class, parameters, name and error_instance_id match errors.expected.','One request; no successful result.']}]}
 row['case_sha256']=hashlib.sha256(json.dumps(row,sort_keys=True,separators=(',',':')).encode()).hexdigest();rows.append(row)
manifest={'story':'DEV-STORY-074','testcase':'TESTCASE-076','author_identity':IDENTITY,'sdk_release':'1.101.0','source_commit':oracle['source_commit'],'reviewed_candidate_sha':subprocess.check_output(['git','-C',str(BASE),'rev-parse','HEAD'],text=True).strip(),'generation_method':'Pinned installed SDK AST, annotations, request models, response and error JSON schemas. Semantic-review input supplies only operation IDs and asset paths. No author example constants, invoke or verify are read or run.','approval':'DESIGN_COMPLETE_PENDING_INDEPENDENT_REVIEW','execution':'NOT_RUN','binary_literal_encoding':'Objects with __bytes_hex__ encode request bytes; content_hex and expected_bytes_hex encode response bytes. Executor must decode these literals before SDK invocation.','network_policy':{'required':'Deny socket.connect, socket.connect_ex, socket.create_connection and DNS for entire execution. Use fresh httpx.MockTransport per scenario.','fixture_independence':'Do not import author examples or invoke/verify/EXPECTED/SUCCESS/ERRORS. Compare responses with stored literals.'},'operations':rows,'review_gaps':gaps}
OUT.write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps({'operations':len(rows),'errors':sum(len(x['errors']) for x in rows),'sha256':h(OUT)}))

