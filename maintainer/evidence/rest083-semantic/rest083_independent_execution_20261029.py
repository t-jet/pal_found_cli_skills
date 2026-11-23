"""Independent SDK 1.101.0 probes. Run from repository root with prepared QA Python."""
import ast, contextlib, hashlib, http.client, inspect, json, re, socket, sys, urllib.request
from pathlib import Path
from unittest.mock import patch
import httpx
import foundry_sdk
from foundry_sdk import Config, UserTokenAuth, PalantirRPCException

BASE=Path(__file__).resolve().parent
ROOT=BASE/'feature015_rest083_review_20261029'
SKILL=ROOT/'.agents/skills/pal-found-dev'
REVIEWER='/root/rest083_semantic_review_20261029'
RID='ri.attachments.main.attachment.00000000-0000-0000-0000-000000000001'
STAMP='2026-10-29T00:00:00Z'
POINT={'time':STAMP,'value':21.5}
CONTENT=b'QA attachment\n'
META={'rid':RID,'filename':'qa.txt','sizeBytes':str(len(CONTENT)),'mediaType':'text/plain','type':'single'}
EDITS={'type':'edits','edits':[],'addedObjectCount':0,'modifiedObjectsCount':1,'deletedObjectsCount':0,'addedLinksCount':0,'deletedLinksCount':0}
OVERRIDES={'uniqueIdentifierLinkIdValues':{'00000000-0000-0000-0000-000000000001':'00000000-0000-0000-0000-000000000002'},'actionExecutionTime':STAMP}
WINDOW={'type':'absolute','startTime':STAMP,'endTime':'2026-10-29T00:01:00Z'}

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def deny(*args,**kwargs): raise AssertionError('QA denies public network, DNS and native HTTP')
@contextlib.contextmanager
def client_for(cls,handler):
 with httpx.Client(transport=httpx.MockTransport(handler)) as transport:
  with patch('foundry_sdk._core.api_client.HttpClient',return_value=transport):
   client=cls(auth=UserTokenAuth(token='qa-independent-token'),hostname='qa.example.invalid',config=Config(max_retries=1,propagate_qos='PROPAGATE_429_AND_503_TO_CALLER'))
  yield client

def case(resource,op):
 key=dict(ontology='qa-ontology',object_type='Sensor',primary_key='S-17',property='temperature')
 if resource=='Action':
  args=dict(ontology='qa-ontology',action='setTemperature')
  params={'sensor':'S-17','temperature':21.5}
  if op=='apply': args.update(parameters=params,options={'mode':'VALIDATE_AND_EXECUTE','returnEdits':'ALL'})
  elif op=='apply_with_overrides': args.update(request={'parameters':params},overrides=OVERRIDES)
  elif op=='apply_batch': args.update(requests=[{'parameters':params}])
  else: args.update(requests=[{'parameters':params,'overrides':OVERRIDES}])
  response={'edits':EDITS} if 'batch' in op else {'validation':{'result':'VALID','submissionCriteria':[],'parameters':{}},'edits':EDITS}
  return args,response
 if resource=='Attachment':
  args={'attachment_rid':RID} if op in ('get','read','upload_with_rid') else {}
  if op.startswith('upload'): args.update(body=CONTENT,content_length=len(CONTENT),content_type='text/plain',filename='qa.txt')
  return args,CONTENT if op=='read' else META
 if resource=='AttachmentProperty':
  key['property']='inspectionEvidence'
  if op.endswith('by_rid'): key['attachment_rid']=RID
  return key,CONTENT if op.startswith('read') else META
 if resource=='CipherTextProperty':
  key['property']='secret'
  if op!='decrypt': key['plaintext']='QA synthetic secret'
  if op=='encrypt_with_default_channel': key.pop('primary_key')
  if op=='encrypt': key['cipher_channel_strategy']='PREFER_EXISTING'
  if op!='decrypt': key['preview']=True
  return key,{'plaintext':'QA synthetic secret'} if op=='decrypt' else {'ciphertext':'qa-encrypted-value'}
 if resource=='GeotemporalSeriesProperty':
  key.update(additional_properties=['temperature'],range=WINDOW,page_size=2,preview=True)
  return key,{'data':[{'temperature':21.5,'time':STAMP}],'nextPageToken':'qa-page-2'}
 if resource=='MediaReferenceProperty':
  key['property']='inspectionPhoto'; key['preview']=True
  if op=='upload':
   key.pop('primary_key'); key.update(body=CONTENT,media_item_path='qa/inspection.txt')
   return key,{'mimeType':'text/plain','reference':{'type':'mediaSetViewItem','mediaSetViewItem':{'mediaSetRid':'ri.mio.main.media-set.00000000-0000-0000-0000-000000000001','mediaSetViewRid':'ri.mio.main.view.00000000-0000-0000-0000-000000000002','mediaItemRid':'ri.mio.main.media-item.00000000-0000-0000-0000-000000000003'}}}
  return key,CONTENT if op=='get_media_content' else {'sizeBytes':str(len(CONTENT)),'mediaType':'text/plain'}
 if resource=='Query': return dict(ontology='qa-ontology',query_api_name='sensorReading',parameters={'sensor':'S-17'},version='1.2.3'),{'value':{'temperature':21.5,'unit':'C'}}
 if resource=='TimeSeriesValueBankProperty':
  if op=='get_latest_value': key['property_name']=key.pop('property'); key['branch']='master'; return key,POINT
  key.update(branch='master',range=WINDOW)
  return key,json.dumps([POINT]).encode()
 if op.startswith('get_'): return key,POINT
 key.update(format='JSON',range=WINDOW)
 return key,json.dumps([POINT]).encode()

def normalized(value):
 if hasattr(value,'model_dump'): return value.model_dump(mode='json',by_alias=True,exclude_none=True)
 return value

rows=[r for r in json.loads((ROOT/'maintainer/rest-domain-authoring-register.json').read_text())['operations'] if r['story']=='DEV-STORY-083']
results=[]
with contextlib.ExitStack() as stack:
 for obj,name in [(socket.socket,'connect'),(socket.socket,'connect_ex'),(socket,'create_connection'),(socket,'getaddrinfo'),(socket,'gethostbyname'),(http.client.HTTPConnection,'connect'),(http.client.HTTPSConnection,'connect'),(urllib.request,'urlopen')]: stack.enter_context(patch.object(obj,name,deny))
 for row in rows:
  _,_,resource,op=row['id'].split('.')
  ex=SKILL/row['example']; ns={'__file__':str(ex),'__name__':'qa083_'+resource+'_'+op}; exec(compile(ex.read_text(),str(ex),'exec'),ns)
  cls=next(v for k,v in ns.items() if k.endswith('Client') and isinstance(v,type))
  args,payload=case(resource,op); requests=[]; checks=[]
  def handler(request):
   assert request.headers['authorization']=='Bearer qa-independent-token'
   requests.append({'method':request.method,'path':request.url.path,'query':str(request.url.query),'body':request.content.decode(errors='replace'),'headers':dict(request.headers)})
   return httpx.Response(200,content=payload) if isinstance(payload,bytes) else httpx.Response(200,json=payload)
  try:
   with client_for(cls,handler) as client:
    raw=getattr(client.with_raw_response,op)(**args,request_timeout=30)
    try:
     decoded=normalized(raw.decode()); assert decoded is not None
     if isinstance(payload,bytes): assert decoded==payload
     elif resource=='Action' and 'batch' not in op: assert decoded['validation']['result']=='VALID'
     elif resource=='Attachment' and op.startswith('upload'): assert int(decoded['sizeBytes'])==len(CONTENT)
     elif resource=='Query': assert decoded['value']['temperature']==21.5
     elif resource.startswith('TimeSeries') and not op.startswith('stream'): assert decoded['value']==21.5
    finally: raw.close()
   checks.append({'name':'independent_meaningful_success','verdict':'PASS','decoded':decoded})
  except Exception as error: checks.append({'name':'independent_meaningful_success','verdict':'FAIL','error':repr(error)})
  def forbidden(request): return httpx.Response(403,json={'errorCode':'PERMISSION_DENIED','errorName':'QAAccessDenied','errorInstanceId':'00000000-0000-0000-0000-000000000001','parameters':{}})
  try:
   with client_for(cls,forbidden) as client:
    try: getattr(client.with_raw_response,op)(**args,request_timeout=30)
    except PalantirRPCException as error: assert error.name=='QAAccessDenied'; checks.append({'name':'generic_permission_denial','verdict':'PASS','type':type(error).__name__})
    else: raise AssertionError('403 treated as success')
  except Exception as error: checks.append({'name':'generic_permission_denial','verdict':'FAIL','error':repr(error)})
  def timeout(request): raise httpx.ReadTimeout('QA response timeout',request=request)
  try:
   with client_for(cls,timeout) as client:
    try: getattr(client.with_raw_response,op)(**args,request_timeout=30)
    except Exception as error:
     assert type(error).__name__=='ReadTimeout', repr(error)
     checks.append({'name':'timeout_propagates_no_business_success_claim','verdict':'PASS','exception_module':type(error).__module__})
    else: raise AssertionError('timeout treated as success')
  except Exception as error: checks.append({'name':'timeout_propagates_no_business_success_claim','verdict':'FAIL','error':repr(error)})
  results.append({'id':row['id'],'inputs':args,'payload':payload,'requests':requests,'checks':checks})

matrix=json.loads((ROOT/'maintainer/rest-model-semantic-matrix.json').read_text())['symbols']
sdkroot=Path(foundry_sdk.__file__).parent.parent
model_evidence=[]
ids={r['id'] for r in rows}
for symbol in matrix:
 consumers=sorted(ids.intersection(symbol['consumer_operation_ids']))
 if not consumers: continue
 source=sdkroot/symbol['source']
 pages=[{'path':p,'sha256':sha(SKILL/p),'matches_prior_matrix':sha(SKILL/p)==expected} for p,expected in zip(symbol['local_pages'],symbol['local_page_sha256'])]
 model_evidence.append({'id':symbol['id'],'source':str(source),'source_sha256':sha(source),'source_matches_frozen':sha(source)==symbol['source_file_sha256'],'pages':pages,'consumers':consumers,'dependencies':symbol['dependencies'],'prior_local_meaning_review':symbol['local_meaning_review']})
output={'reviewer':REVIEWER,'candidate':'6df64cce16bf0619bee124f831e1e8686c08cccf','operations':results,'models':model_evidence,'guard':'socket connect/connect_ex/create_connection, DNS, HTTP(S)Connection.connect, urllib.urlopen denied; actual SDK with httpx.MockTransport','limits':'Independent fake HTTP payloads demonstrate client handling. Server permissions, side effects, ordering and supported tenant schemas require authorized enrollment validation.'}
(BASE/'rest083_independent_execution_20261029.json').write_text(json.dumps(output,indent=2,default=str))
for row in results: print(row['id'],[(c['name'],c['verdict'],c.get('error')) for c in row['checks']])
print('Model symbols',len(model_evidence),'source/page continuity failures',sum(not m['source_matches_frozen'] or any(not p['matches_prior_matrix'] for p in m['pages']) for m in model_evidence))
