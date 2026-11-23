"""Prepare independent source-derived cases; do not invoke operation clients or examples."""
import re,ast,copy,hashlib,importlib,inspect,json,subprocess,typing
from pathlib import Path
import pydantic
from datetime import datetime, timezone
BASE=Path('.ept/tmp/feature015_integration'); SKILL=BASE/'.agents/skills/pal-found-dev'; OUT=Path('.ept/tmp/rest071_formal_cases.json')
IDENTITY='/root/formal071_completion/source071'
UUID='00000000-0000-0000-0000-000000000071'
ORGANIZATION='ri.multipass..organization.independent071'
BINARY=bytes.fromhex('89504e470d0a1a0a0000000d4948445200000001000000010804000000b51c0c020000000b4944415478da6364f80f00010501012718e3660000000049454e44ae426082')

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
  if s.get('patternProperties'):return {ORGANIZATION:sample(next(iter(s['patternProperties'].values())),root,depth+1)}
  return {'independent071':sample(s['additionalProperties'],root,depth+1)} if isinstance(s.get('additionalProperties'),dict) else {}
 if t=='array':return [sample(s.get('items',{}),root,depth+1)] if depth<6 else []
 if t=='integer':return max(2,s.get('minimum',2))
 if t=='number':return 2.5
 if t=='boolean':return True
 if t=='null':return None
 if s.get('format')=='date-time':return '2026-10-21T08:00:00Z'
 if s.get('format')=='date':return '2026-10-21'
 if s.get('format')=='uuid' or '0-9a-fA-F' in s.get('pattern',''):return UUID
 if s.get('pattern','').startswith('^ri'):return ORGANIZATION
 return 'independent071' if t=='string' else {}
def encode(v):
 if isinstance(v,bytes):return {'__bytes_hex__':v.hex()}
 if isinstance(v,pydantic.BaseModel):return encode(v.model_dump(mode='python',by_alias=True,exclude_none=True))
 if isinstance(v,datetime):return (v if v.tzinfo else v.replace(tzinfo=timezone.utc)).astimezone(timezone.utc).isoformat()
 if isinstance(v,dict):return {k:encode(item) for k,item in v.items()}
 if isinstance(v,list):return [encode(item) for item in v]
 return v
def wire_for(expr,mod,kw):
 env=dict(mod.__dict__,**kw);result={k:encode(eval(expr[k],env)) for k in ('method','resource_path','query_params','path_params','header_params','body')};result['query_params']={k:v for k,v in result['query_params'].items() if v is not None};return result
ops=[dict(r,source_module=re.sub(r'(?<!^)(?=[A-Z])','_',r['id'].split('.')[-2]).lower()+'.py', **{k+'_path':r[k] for k in ('behavior','example')},contract_path='references/rest/contracts/'+r['id'].replace('.','/')+'.md') for r in json.loads((BASE/'maintainer/rest-domain-authoring-register.json').read_text())['operations'] if r['story']=='DEV-STORY-071']
oracle=json.loads((BASE/'tests/fixtures/offline/rest-acceptance/source-oracle.json').read_text());rows=[];gaps=[]
for index,asset in enumerate(ops,1):
 op=asset['id'];r,fn=op.split('.')[-2:];modname='foundry_sdk.'+'.'.join(op.split('.')[:2])+'.'+Path(asset['source_module']).stem;mod=importlib.import_module(modname);mp=Path(mod.__file__);src=mp.read_text();tree=ast.parse(src);cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name==r+'Client');f=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name==fn);req=next(n for n in ast.walk(f) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='RequestInfo');expr={k.arg:ast.unparse(k.value) for k in req.keywords};doc=ast.get_docstring(f);arg_schema={};kw={}
 assert h(mp)==oracle['operations'][op]['source_sha256'],op+' frozen module hash'
 for a in [*f.args.args,*f.args.kwonlyargs]:
  if a.arg in ('self','_sdk_internal','request_timeout'):continue
  typ=eval(ast.unparse(a.annotation),mod.__dict__);arg_schema[a.arg]=schema(typ);kw[a.arg]=sample(arg_schema[a.arg])
  if typ is bytes:kw[a.arg]=BINARY
 GROUP='00000000-0000-0000-0000-000000000071'
 USER='00000000-0000-0000-0000-000000000172'
 ORG='ri.multipass..organization.independent071'
 for k in kw:
  if k=='group_id':kw[k]=GROUP
  elif k=='user_id':kw[k]=USER
  elif k=='principal_ids':kw[k]=[USER]
  elif k=='organizations':kw[k]=[ORG]
  elif k=='attributes':kw[k]={'multipass:owner':['independent-owner071'],'team':['identity-audit071']}
  elif k=='name':kw[k]='Identity audit 071'
  elif k=='description':kw[k]='Independent identity review group'
  elif k=='provider_id':kw[k]='independent-provider071'
  elif k=='maximum_duration':kw[k]=7200
  elif k=='maximum_value':kw[k]='2026-10-24T08:00:00Z'
  elif k=='expiration':kw[k]='2026-10-23T08:00:00Z'
  elif k=='preview':kw[k]=True
  elif k=='include_expirations':kw[k]=True
  elif k=='transitive':kw[k]=False
  elif k=='page_size':kw[k]=2
  elif k=='page_token':kw[k]='independent-next071'
  elif k=='where':kw[k]={'type':'queryString','value':'Identity audit 071' if r=='Group' else 'identity.audit071'}
 if fn=='get_batch':kw['body']=[{'groupId' if r=='Group' else 'userId':GROUP if r=='Group' else USER}]
 wire=wire_for(expr,mod,kw);ret=eval(expr['response_type'],mod.__dict__);rs=schema(ret);reply=sample(rs)
 if ret is None or ret is type(None):reply=None
 def group():return {'id':GROUP,'realm':'independent-realm071','name':kw.get('name','Identity audit 071'),'attributes':copy.deepcopy(kw.get('attributes',{'team':['identity-audit071']})),'organizations':[ORG],**({'description':kw['description']} if kw.get('description') else {})}
 def user():return {'id':USER,'username':'identity.audit071','status':kw.get('status',kw.get('include','ACTIVE')),'givenName':'Alex','familyName':'Audit','email':'identity071@example.invalid','attributes':{'team':['identity-audit071']},'realm':'independent-realm071','organization':ORG}
 if r in ('Group','User'):
  item=group() if r=='Group' else user()
  if fn in ('get','get_current','create','replace'):reply=item
  elif fn=='get_batch':reply={'data':{item['id']:item}}
  elif fn in ('list','list_current','search'):reply={'data':[item]}
 if r=='GroupMember' and fn=='list':reply={'data':[{'principalId':USER,'principalType':'USER','expiration':'2026-10-23T08:00:00Z'}]}
 if r=='GroupMembership':reply={'data':[{'groupId':GROUP}]}
 if r=='GroupMembershipExpirationPolicy':reply={'maximumDuration':7200,'maximumValue':'2026-10-24T08:00:00Z'}
 if r in ('GroupProviderInfo','UserProviderInfo'):reply={'providerId':kw.get('provider_id','independent-provider071')}
 if fn=='get_markings':reply={'view':['independent-marking071']}
 success={'http_status':204 if ret is None else 200,'json':reply,'result_type':expr['response_type'],'schema':rs,'assertions':['Validate the response literal with the declared SDK response TypeAdapter, then compare the actual typed result using model_dump(mode="python", by_alias=True, exclude_unset=True) and recursive date canonicalization on both sides. Python mode preserves core.Long integers; JSON mode may serialize them as strings.','Do not call to_dict on model fields that shadow Python names; inspect aliases and exact schema fields.','Assert raw wrapper decoding and closure; streaming wrapper closes after consumption.']}
 if fn=='profile_picture':success.update(json=None,content_hex=BINARY.hex(),expected_bytes_hex=BINARY.hex());success['assertions']=['Assert ordinary result equals bytes.fromhex(content_hex).','Assert raw and streaming responses yield exact bytes and close after consumption.']
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
  error_kw=copy.deepcopy(kw)
  condition=['Synthetic service rejection; SDK declares this error. Tenant conditions remain unproven.']
  if name=='InvalidPageSize':
   error_kw['page_size']=0;params['pageSize']=0;condition=['Zero page size violates the explicit SDK endpoint docstring. MockTransport supplies the service rejection; SDK annotation does not enforce positivity.']
  if name=='InvalidGroupOrganizations':
   error_kw['organizations']=[];condition=['Empty organizations violates the explicit SDK requirement for at least one organization. Service rejection is synthetic.']
  if name=='ExpirationForTransitiveGroupMembersNotSupported':
   error_kw.update(include_expirations=True,transitive=True);condition=['Both flags true contradict the explicit SDK GroupMember.list restriction. Service rejection is synthetic.']
  if 'principalId' in params:
   params['principalId']=kw.get('user_id',kw.get('principal_ids',[kw.get('group_id',USER)])[0])
  if name=='GroupNameAlreadyExists':params['groupName']=kw['name']
  if name=='AttributesNotEditable':
   params['attributeNames']=['multipass:owner'];error_kw['attributes']['multipass:owner']=['changed-owner071'];condition=['Existing GET group preserves multipass:owner as independent-owner071; this adverse request changes it to changed-owner071, contrary to the explicit SDK preservation requirement. Service rejection is synthetic.']
  if name=='UserIsActive':
   error_kw['status']='DELETED';condition=['Synthetic existing user remains active while this request asks for DELETED status. The SDK declares UserIsActive but does not document a complete server status-selection policy.']
  if name=='InvalidGroupMembershipExpiration':
   params['earliestExpiration']='2026-10-24T08:00:00Z';condition=['Synthetic group requirement sets earliestExpiration to 2026-10-24T08:00:00Z; requested expiration 2026-10-23T08:00:00Z violates that requirement. No universal group policy is implied.']
  envelope['parameters']=copy.deepcopy(params)
  errors.append({'request':{k:encode(v) for k,v in error_kw.items()},'expected_wire':wire_for(expr,mod,error_kw),'source_condition':condition,'name':name,'status':status,'errorCode':code,'parameters':params,'parameter_schema':es,'error_source':inspect.getfile(ec),'error_source_sha256':h(inspect.getfile(ec)),'error_base':base,'envelope':envelope,'expected':{'exception_class':ec.__module__+'.'+name,'name':name,'parameters':copy.deepcopy(params),'error_instance_id':UUID},'assertions':['Assert exact SDK exception class, name, parameters and error_instance_id.','Assert one HTTP request and no successful result.']})
 assets={k:{'path':asset[k+'_path'],'sha256':h(SKILL/asset[k+'_path'])} for k in ('contract','behavior','example')}
 row={'case_id':f'F071-{index:02d}','operation':op,'source':{'module':modname,'path':str(mp),'sha256':h(mp),'method_source_sha256':hashlib.sha256(ast.get_source_segment(src,f).encode()).hexdigest(),'line':f.lineno,'docstring':doc,'request_expressions':expr,'oracle_sha256':h(BASE/'tests/fixtures/offline/rest-acceptance/source-oracle.json')},'assets':assets,'request':{'kwargs':{k:encode(v) for k,v in kw.items()},'argument_schemas':arg_schema,'expected_wire':wire,'path_prefix':'/api','timeout':7,'authorization':'Bearer independent-qa-071'},'success':success,'errors':errors,'semantic_expectation':doc.split(':param')[0].strip(),'source_silence':['SDK source does not establish tenant grants, live mutation effects, universal idempotency or a retry policy.','Mock responses verify transport and decoding; server validation and resource lifecycle effects require an authorized tenant.'],'additional_cases':[],'review':{'example_fixture_executed':False}}
 extras=row['additional_cases']
 optional=[a.arg for a,default in zip(f.args.kwonlyargs,f.args.kw_defaults) if default is not None and a.arg in kw]
 omit=copy.deepcopy(kw);omit.update({k:None for k in optional if k!='preview'})
 extras.append({'name':'optional omission','request':{k:encode(v) for k,v in omit.items()},'expected_wire':wire_for(expr,mod,omit),'response':copy.deepcopy(reply) if fn!='profile_picture' else None,'response_status':success['http_status'],**({'content_hex':BINARY.hex()} if fn=='profile_picture' else {})})
 if fn=='profile_picture':extras[-1]['success']={'http_status':200,'content_hex':BINARY.hex(),'expected_bytes_hex':BINARY.hex()}
 if fn=='create' and r=='Branch':extras[-1]['response'].pop('transactionRid',None)
 if fn=='create' and r=='View':extras[-1]['response'].pop('primaryKey',None)
 required=[a.arg for a in f.args.args[:len(f.args.args)-len(f.args.defaults)] if a.arg!='self']+[a.arg for a,default in zip(f.args.kwonlyargs,f.args.kw_defaults) if default is None]
 if required:
  missing=copy.deepcopy(row['request']['kwargs']);missing.pop(required[0]);extras.append({'name':'required argument omitted','request':missing,'omitted_parameter':required[0],'expected_exception':'pydantic.ValidationError','expected_request_count':0})
 if 'page_token' in kw:
  first=copy.deepcopy(kw);first['page_token']=None;second=copy.deepcopy(kw);second['page_token']='independent-next071';a=copy.deepcopy(reply);b=copy.deepcopy(reply);a['nextPageToken']='independent-next071';b.pop('nextPageToken',None)
  for page,suffix in ((a,'A'),(b,'B')):
   item=page['data'][0]
   for field in ('id','principalId','groupId'):
    if field in item:item[field]='00000000-0000-0000-0000-000000000'+('271' if suffix=='A' else '371')
   if 'name' in item:item['name']='Identity audit 071 page '+suffix
   if 'username' in item:item['username']='identity.audit071.page'+suffix
  extras.append({'name':'finite continuation','requests':[first,second],'expected_wires':[wire_for(expr,mod,first),wire_for(expr,mod,second)],'responses':[a,b],'response_status':200,'expected_request_count':2,'expected_terminal_token':None,'steps':['Return two nonempty pages with distinct identities.','Carry returned token into second request; preserve scope and filters.','Stop when terminal response omits nextPageToken. Requested page size does not prove service page count.']})
 if fn=='get_batch':
  for length in (0,501):
   bad=copy.deepcopy(kw);bad['body']=[copy.deepcopy(kw['body'][0])]*length;extras.append({'name':f'batch length {length} rejected locally','request':bad,'expected_exception':'pydantic.ValidationError','expected_request_count':0,'provenance':'SDK request body Annotated Len(min_length=1,max_length=500).'})
 if fn=='get_batch':
  boundary=copy.deepcopy(kw);boundary['body']=[copy.deepcopy(kw['body'][0]) for _ in range(500)]
  extras.append({'name':'batch upper bound accepted','request':boundary,'expected_wire':wire_for(expr,mod,boundary),'response':copy.deepcopy(reply),'response_status':200,'provenance':'SDK Annotated Len maximum 500; duplicate requests retained as 500 literal elements.'})
 for key in ('group_id','user_id'):
  if key in kw:
   invalid=copy.deepcopy(kw);invalid[key]='invalid-uuid071'
   extras.append({'name':key+' malformed UUID rejected locally','request':invalid,'expected_exception':'pydantic.ValidationError','expected_request_count':0,'provenance':arg_schema[key]})
 for key in ('status','include'):
  if key in kw:
   invalid=copy.deepcopy(kw);invalid[key]='UNSUPPORTED071'
   extras.append({'name':key+' unsupported enum rejected locally','request':invalid,'expected_exception':'pydantic.ValidationError','expected_request_count':0,'provenance':arg_schema[key]})
 if r=='Group' and fn=='replace':
  row['precondition']={'existing_group':{**group(),'attributes':{'multipass:owner':['independent-owner071'],'team':['prior-team071']}},'assertion':'Reserved multipass: attributes match prior GET exactly; editable team attribute changes.'}
 if r=='GroupMember' and fn in ('add','remove'):
  row['business_identity_assertion']='Destination group_id differs from each principal_ids entry; request mutates destination membership.'
 if r=='GroupMembershipExpirationPolicy':
  row['business_policy_assertion']='maximumDuration is 7200 seconds; maximumValue is explicit 2026-10-24T08:00:00Z cutoff. Source gives no tenant default for absent values.'
  if fn=='replace':
   for key,alias in (('maximum_duration','maximumDuration'),('maximum_value','maximumValue')):
    single=copy.deepcopy(kw);single['maximum_value' if key=='maximum_duration' else 'maximum_duration']=None
    extras.append({'name':key+' alone','request':single,'expected_wire':wire_for(expr,mod,single),'response':{alias:kw[key]},'response_status':200})
 for extra in extras:
  if extra['name']=='optional omission' and r=='GroupMembershipExpirationPolicy' and fn=='replace':extra['response']={}
 if fn=='profile_picture':extras.append({'name':'empty optional profile picture','request':copy.deepcopy(kw),'expected_wire':copy.deepcopy(wire),'response':None,'response_status':204,'success':{'http_status':204,'json':None}})
 row['gherkin']={'feature':op,'scenarios':[{'name':row['case_id']+' literal request and typed success','given':['Pinned SDK source hashes match manifest.','Network sockets denied; fresh MockTransport returns success literals.'],'when':['Call '+op+' using request.kwargs and timeout 7.'],'then':['Compare exact method, substituted path, complete query, headers and body with request.expected_wire.','Compare normalized result with success.json or exact success.expected_bytes_hex.','Close raw and streaming wrappers after consuming result.']},{'name':row['case_id']+' each declared error','given':['For each errors entry, transport returns exact status and envelope literals.'],'when':['Call operation using same request.'],'then':['Exact exception class, parameters, name and error_instance_id match errors.expected.','One request; no successful result.']}]}
 row['source']['modes']=copy.deepcopy(oracle['operations'][op].get('wrappers',{}))
 row['source']['async_signature']=copy.deepcopy(oracle['operations'][op].get('async',{}))
 row['source']['iterator']=copy.deepcopy(oracle['operations'][op].get('iterator',{}))
 async_cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='Async'+r+'Client')
 af=next(n for n in async_cls.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)) and n.name==fn)
 row['source']['async_method_source_sha256']=hashlib.sha256(ast.get_source_segment(src,af).encode()).hexdigest()
 for extra in extras:
  row['gherkin']['scenarios'].append({'name':row['case_id']+' '+extra['name'],'given':['Use immutable request/response literals in additional_cases named '+extra['name']+'.','Deny sockets and DNS; use fresh MockTransport.'],'when':['Invoke '+op+' in SDK modes supported by pinned source.'],'then':(['Raise '+extra['expected_exception']+' before transport; request count is 0.'] if 'expected_exception' in extra else ['Compare complete request with stored expected_wire or expected_wires.','Compare typed result with stored response or responses; honor expected_request_count.','Close response wrappers and transports.'])})
 row['gherkin']['scenarios'].append({'name':row['case_id']+' sync async and response modes','given':['Use pinned ordinary, async, raw and stream wrapper definitions in source module.'],'when':['Invoke each supported mode using same request and reply literals.'],'then':['Result payload and wire request agree across modes.','Raw and streaming wrappers close after consumption.','Iterator pages retain scope, carry continuation token, and stop at terminal token.']})
 row['case_sha256']=hashlib.sha256(json.dumps(row,sort_keys=True,separators=(',',':')).encode()).hexdigest();rows.append(row)
manifest={'story':'DEV-STORY-071','testcase':'TESTCASE-074','author_identity':'/root/formal071_completion/source071','sdk_release':'1.101.0','source_commit':oracle['source_commit'],'reviewed_candidate_sha':subprocess.check_output(['git','-C',str(BASE),'rev-parse','HEAD'],text=True).strip(),'generation_method':'Pinned installed SDK AST, annotations, request models, response and error JSON schemas. Authoring register supplies only operation IDs and asset paths. No author example constants, invoke or verify are read or run.','approval':'DESIGN_COMPLETE_PENDING_INDEPENDENT_REVIEW','execution':'NOT_RUN','binary_literal_encoding':'Objects with __bytes_hex__ encode request bytes; content_hex and expected_bytes_hex encode response bytes. Executor must decode these literals before SDK invocation.','network_policy':{'required':'Deny socket.connect, socket.connect_ex, socket.create_connection and DNS for entire execution. Use fresh httpx.MockTransport per scenario.','fixture_independence':'Do not import author examples or invoke/verify/EXPECTED/SUCCESS/ERRORS. Compare responses with stored literals.'},'operations':rows,'review_gaps':gaps}
manifest['correction_author_identity']='/root/rest071_finish_20261027'
manifest['correction_history']={'original_manifest_sha256':'25515d476f8e719d1c5cc0ccee18913dabfd99953e66404c5925672388f43262','reason':'Independent review found invalid success flags, missing search continuation, contradictory adverse literals, and SDK Python-mode Long serialization.'}
OUT.write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps({'operations':len(rows),'errors':sum(len(x['errors']) for x in rows),'sha256':h(OUT)}))

