"""Fresh reviewer checks against frozen REST083 candidate; no candidate writes."""
import ast, copy, contextlib, datetime, hashlib, http.client, inspect, json, re, runpy, socket, subprocess, sys, time, urllib.request
from pathlib import Path
from unittest.mock import patch
import httpx
from types import SimpleNamespace
from foundry_sdk import PermissionDeniedError, TimeoutError as SDKTimeoutError
from foundry_sdk.v2.ontologies import models

BASE=Path(__file__).resolve().parent
ROOT=BASE/'feature015_rest083_fixes'
SKILL=ROOT/'.agents/skills/pal-found-dev'
REVIEWER='/root/rest083_fresh_qa_20261116'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
freeze_path=BASE/'feature015_rest083_author_freeze_20261116.json'
old_path=BASE/'feature015_rest083_semantic_review_20261029.json'
freeze=json.loads(freeze_path.read_text()); old=json.loads(old_path.read_text())
assert sha(freeze_path)=='20e4e657f908165eec22600d09e42f0a624370c52a856df5caae7f1ec42f421f'
assert sha(old_path)=='2f0db7991c430205a5b9a4d52ab56965b496f58852b4ff6cec9265305182d1ca'
paths={str(ROOT/f['path']) for f in freeze['files']}
for row in freeze['operations']:
 paths.update([str(ROOT/row['example']),str(SKILL/row['behavior']),row['source_path']])
for m in old['full_transitive_models']:
 paths.add(m['source']); paths.update(str(SKILL/p['path']) for p in m['pages'])
paths.update([str(freeze_path),str(old_path),freeze['source_model_file']['path']])
before={p:sha(Path(p)) for p in sorted(paths)}
assert all(sha(ROOT/f['path'])==f['sha256'] for f in freeze['files'])
def deny(*a,**k): raise AssertionError('Fresh QA denies socket, DNS, native HTTP, real httpx transport')
guards=[(socket.socket,'connect'),(socket.socket,'connect_ex'),(socket,'create_connection'),(socket,'getaddrinfo'),(socket,'gethostbyname'),(socket,'gethostbyname_ex'),(http.client.HTTPConnection,'connect'),(http.client.HTTPSConnection,'connect'),(urllib.request,'urlopen'),(httpx.HTTPTransport,'handle_request'),(httpx.AsyncHTTPTransport,'handle_async_request')]
checks=[]
def check(name,fn,oid=None):
 start=time.monotonic()
 try: result=fn(); item={'name':name,'id':oid,'verdict':'PASS','evidence':result}
 except Exception as exc: item={'name':name,'id':oid,'verdict':'FAIL','error':repr(exc)}
 item['seconds']=round(time.monotonic()-start,6); checks.append(item); return item
def expect_error(fn,types=(AssertionError,ValueError)):
 try: fn()
 except types as e: return type(e).__name__+': '+str(e)
 raise AssertionError('Mutation escaped required rejection')

# Re-run independently authored SDK payloads from original review, changing only
# root/output names and the corrected geotemporal source-required position.
prior=(BASE/'rest083_independent_execution_20261029.py').read_text()
prior=prior.replace("ROOT=BASE/'feature015_rest083_review_20261029'","ROOT=BASE/'feature015_rest083_fixes'")
prior=prior.replace("REVIEWER='/root/rest083_semantic_review_20261029'",'REVIEWER='+repr(REVIEWER))
prior=prior.replace('rest083_independent_execution_20261029.json','rest083_fresh_sdk_execution_20261116.json')
prior=prior.replace("{'temperature':21.5,'time':STAMP}","{'temperature':21.5,'time':STAMP,'position':{'type':'Point','coordinates':[23.3,42.7]}}")
with contextlib.ExitStack() as stack:
 for obj,name in guards: stack.enter_context(patch.object(obj,name,deny))
 for obj,name in guards:
  check('network_negative_control:'+obj.__name__+'.'+name,lambda obj=obj,name=name: expect_error(lambda:getattr(obj,name)('https://example.invalid')))
 exec(compile(prior,str(BASE/'rest083_independent_execution_20261029.py'),'exec'),{'__file__':str(BASE/'rest083_independent_execution_20261029.py'),'__name__':'fresh_sdk'})
 modules={}
 for row in freeze['operations']:
  oid=row['id']; resource,op=oid.split('.')[-2:]
  ns=runpy.run_path(str(ROOT/row['example'])); ns=ns['invoke'].__globals__; modules[oid]=ns
  check('reader_fixture',ns['verify'],oid)
  def continuity(row=row):
   assert sha(Path(row['source_path']))==row['source_sha256']
   assert sha(ROOT/row['example'])==row['example_sha256']
   assert sha(SKILL/row['behavior'])==row['behavior_sha256']
   if row['preserved_baseline_bytes']:
    baseline=BASE/'feature015_rest083_review_20261029'/row['example']
    assert (ROOT/row['example']).read_bytes()==baseline.read_bytes()
   source=ast.parse(Path(row['source_path']).read_text())
   cls=next(n for n in source.body if isinstance(n,ast.ClassDef) and n.name==resource+'Client')
   fn=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name==op)
   contract=SKILL/'references/rest/contracts/v2/ontologies'/resource/(op+'.md')
   text=contract.read_text()
   assert op in text and resource in text
   return {'source_function':ast.unparse(fn),'contract_sha256':sha(contract),'preserved_baseline':row['preserved_baseline_bytes']}
  check('source_contract_binding_continuity',continuity,oid)
  if resource=='Action':
   def action_checks(ns=ns,op=op):
    cls=next(v for k,v in ns.items() if k.endswith('Client') and isinstance(v,type))
    good=copy.deepcopy(ns['SUCCESS'])
    bad=[{},dict(good,edits=None)]
    wrong=copy.deepcopy(good); wrong['edits']['edits'][0]['primaryKey']='WRONG'; bad.append(wrong)
    wrong=copy.deepcopy(good); wrong['edits']['modifiedObjectsCount']=0; bad.append(wrong)
    if 'batch' not in op:
     wrong=copy.deepcopy(good); wrong['validation']['result']='INVALID'; bad.append(wrong)
    results=[]
    for payload in bad:
     replies=[]
     def handler(req):
      body=json.loads(req.content)
      assert (body['request'] if op=='apply_with_overrides' else body)['options']['returnEdits']=='ALL'
      item=body['requests'][0] if 'batch' in op else body
      if 'overrides' in op:
       assert len(item['overrides']['uniqueIdentifierLinkIdValues'])==1
       assert datetime.datetime.fromisoformat(item['overrides']['actionExecutionTime']).tzinfo
      res=httpx.Response(200,json=payload); replies.append(res); return res
     with ns['mock_resource'](cls,handler) as client:
      raw=ns['invoke'](client)
      try: decoded=raw.decode(); results.append(expect_error(lambda:ns['check_outcome'](decoded)))
      finally: raw.close()
     assert all(r.is_closed for r in replies)
    return results
   check('action_mutations_and_real_wire_overrides',action_checks,oid)
  if resource=='Attachment' and op.startswith('upload'):
   def attachment_mutations(ns=ns):
    evidence=[]
    for field,value in [('sizeBytes','1'),('filename','wrong.txt'),('mediaType','wrong/type')]:
     saved=copy.deepcopy(ns['SUCCESS']); ns['SUCCESS'][field]=value
     try: evidence.append(expect_error(ns['verify']))
     finally: ns['SUCCESS']=saved
    return evidence
   check('attachment_metadata_mutations',attachment_mutations,oid)
  if op.startswith('stream_'):
   def stream_mutations(ns=ns,op=op):
    stamp='2026-01-01T00:00:30Z'
    good=json.dumps([{'time':stamp,'value':24.75,'label':'\u00b0C'}],ensure_ascii=False).encode()
    assert ns['parse_records']([good[i:i+1] for i in range(len(good))])[0]['value']==24.75
    bad=[(b'[{',json.JSONDecodeError),(b'[{}]',ValueError),(b'{}',ValueError),(b'[{"time":"2026-01-01T00:02:00Z","value":1}]',ValueError)]
    cls=next(v for k,v in ns.items() if k.endswith('Client') and isinstance(v,type))
    evidence=[]
    for payload,error in bad+[(b'x'*30,ValueError)]:
     replies=[]
     def handler(req):
      res=httpx.Response(200,content=payload); replies.append(res); return res
     with ns['mock_resource'](cls,handler) as client:
      def consume():
       kw=dict(ontology='qa',object_type='Sensor',primary_key='S1',property='temperature',range={'type':'absolute','startTime':'2026-01-01T00:00:00Z','endTime':'2026-01-01T00:02:00Z'},request_timeout=30)
       if op=='stream_points': kw['format']='JSON'
       with getattr(client.with_streaming_response,op)(**kw) as response:
        return ns['parse_records'](response.iter_bytes(chunk_size=1),byte_budget=8 if payload==b'x'*30 else 4096)
      evidence.append(expect_error(consume,(error,)))
     assert replies and all(r.is_closed for r in replies)
    return evidence
   check('fragmented_utf8_records_mutations_budget_cleanup',stream_mutations,oid)
  if resource=='GeotemporalSeriesProperty':
   def geo(ns=ns):
    cls=next(v for k,v in ns.items() if k.endswith('Client') and isinstance(v,type))
    evidence=[]
    for mode in ['empty_continuation','repeated','budget','missing_position']:
     requests=[]; replies=[]
     def handler(req):
      body=json.loads(req.content); requests.append(body)
      assert body['range']['startTime']=='2026-01-01T00:00:00+00:00'
      assert body['range']['endTime']=='2026-01-01T00:02:00+00:00'
      if mode=='missing_position': payload={'data':[{'time':'2026-01-01T00:00:30Z'}]}
      elif mode=='empty_continuation' and len(requests)==2:
       assert body['pageToken']=='qa-next'; payload={'data':[{'time':'2026-01-01T00:00:30Z','position':{'type':'Point','coordinates':[1,2]},'speed':9}]}
      else: payload={'data':[],'nextPageToken':str(len(requests)) if mode=='budget' else 'qa-next'}
      response=httpx.Response(200,json=payload); replies.append(response); return response
     with ns['mock_resource'](cls,handler) as client:
      if mode=='empty_continuation': assert ns['load_entries'](client,page_budget=2)[0]['speed']==9
      else: evidence.append(expect_error(lambda:ns['load_entries'](client,page_budget=2)))
     assert len(requests)<=2 and all(r.is_closed for r in replies)
    assert models.AbsoluteTimeRange.model_validate({'type':'absolute'}).start_time is None
    return evidence
   check('finite_paging_mutations_empty_continuation_cleanup',geo,oid)

def action_poll_timing():
 text=(SKILL/'references/rest/v2/ontologies/Action.md').read_text()
 code=text.split('from time import monotonic, sleep',1)[1].split('```',1)[0]
 evidence=[]
 for succeed in (True,False):
  now=[0.0]; calls=[]
  def get(**kw):
   calls.append(kw['request_timeout'])
   return {'priority':'P0' if succeed and len(calls)==3 else 'P1'}
  ns={'monotonic':lambda:now[0],'sleep':lambda secs:now.__setitem__(0,now[0]+secs),'ontology':'qa','client':SimpleNamespace(ontologies=SimpleNamespace(OntologyObject=SimpleNamespace(get=get)))}
  try: exec(compile(code,'Action.md bounded polling','exec'),ns)
  except TimeoutError:
   assert not succeed and now[0]==30
  else: assert succeed and len(calls)==3 and now[0]==2
  assert all(isinstance(v,int) and 1<=v<=5 for v in calls)
  evidence.append({'success_case':succeed,'seconds':now[0],'requests':len(calls),'request_timeouts':calls})
 return evidence
check('documented_action_poll_timing_success_and_timeout',action_poll_timing,'v2.ontologies.Action.apply')

model_results=[]
for m in old['full_transitive_models']:
 symbol=m['id'].rsplit('.',1)[-1]; source_text=Path(m['source']).read_text()
 def matches(n):
  if isinstance(n,(ast.ClassDef,ast.FunctionDef,ast.AsyncFunctionDef)): return n.name==symbol
  if isinstance(n,ast.AnnAssign): return isinstance(n.target,ast.Name) and n.target.id==symbol
  return isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==symbol for t in n.targets)
 definitions=[n for n in ast.parse(source_text).body if matches(n)]
 local=[]
 for p in m['pages']:
  for block in re.findall(r'```python\s*\n(.*?)```',(SKILL/p['path']).read_text(),re.S):
   try: local.extend(ast.parse(block).body)
   except SyntaxError: pass
 dumps=[ast.dump(n,include_attributes=False) for n in local]
 gaps=[d for d in m['dependencies'] if d not in {x['id'] for x in old['full_transitive_models']}]
 ok=bool(definitions) and all(ast.dump(n,include_attributes=False) in dumps for n in definitions)
 pages_ok=all(sha(SKILL/p['path'])==p['sha256'] for p in m['pages'])
 model_results.append({'id':m['id'],'source_sha256':sha(Path(m['source'])),'source_matches_frozen':sha(Path(m['source']))==m['source_sha256'],'definition_ast_equal':ok,'pages_unchanged':pages_ok,'dependency_gaps':gaps,'consumers':m['consumers']})

result=subprocess.run([sys.executable,'-B','-m','pytest','tests/test_offline_rest_083.py','-q','-p','no:cacheprovider'],cwd=ROOT,capture_output=True,text=True)
pytest_path=BASE/'rest083_fresh_author_tests_20261116.txt'; pytest_path.write_text(result.stdout+result.stderr)
execution=json.loads((BASE/'rest083_fresh_sdk_execution_20261116.json').read_text())
after={p:sha(Path(p)) for p in sorted(paths)}
assert before==after, 'Frozen content changed during QA'
operations=[]
meaning={
 'Action':'Single apply requires VALID validation; all four examples request and verify concrete Asset edit evidence. Batch has no invented per-item validation. Override UUID map and aware CurrentTime reach actual SDK wire. Missing/invalid/incorrect edits rejected. Object polling tested with controlled clock; downstream effects require enrollment reconciliation.',
 'Attachment':'Metadata/content reads separated. Upload length derives from bytes; returned filename/size/media type checked. Actual SDK duplicate Content-Type produces */*; guide discloses limitation and synthetic response media type. Upload requires later Action binding before one-hour expiry; uncertain effects reconciled before retry.',
 'AttachmentProperty':'Object/property route and RID-specific membership distinguished. Metadata and content decoded through actual SDK; standalone RID does not establish membership. Authorization/timeout propagate; content lifetime and bounds supplied through common guide.',
 'CipherTextProperty':'Decrypt, existing-object channel strategy, and default-channel encryption distinguished. Default channel prerequisite explicit. Encryption response does not write property; authorized Action/storage and separate decrypt grant required. Synthetic plaintext/ciphertext fixtures are bounded client examples.',
 'GeotemporalSeriesProperty':'Time/position and meaningful speed records over finite two-minute window. Optional SDK bounds acknowledged. Empty-page continuation, repeated token and page budget checked; raw responses close. Guide removes universal ordering claim and states unsupported archive-only integration.',
 'MediaReferenceProperty':'Metadata, bytes and upload separated. Upload requires single backing Media Set/branch and returns reference without binding object. Beta availability differs by operation. Fixture payload is opaque synthetic bytes, with no PNG/image validity claim.',
 'Query':'Typed parameters, QueryType discovery and matching pinned version adaptation explained. Latest means most recently published and may be prerelease. Actual SDK returns meaningful temperature result; empty business result distinguished from API error.',
 'TimeSeriesPropertyV2':'First/last optional points and byte streaming distinguished. Explicit JSON selection matches frozen source, without universal JSON-array envelope claim. Fragmented UTF-8 assembled, timestamps/values inspected; interval, byte budget, malformed records and response cleanup checked.',
 'TimeSeriesValueBankProperty':'property_name latest endpoint differs from property stream endpoint. Same property/branch required; live integration precedence and optional latest value explained. JSON-array framing explicitly synthetic because SDK declares bytes without wire default; finite interval, byte cap, parsing and cleanup checked.'}
for row in freeze['operations']:
 oid=row['id']; independent=next(r for r in execution['operations'] if r['id']==oid)
 own=[c for c in checks if c['id']==oid]
 issues=[c for c in own+independent['checks'] if c['verdict']!='PASS']
 operations.append({'id':oid,'verdict':'FAIL' if issues else 'PASS','initial_verdict':next(r['verdict'] for r in old['operations'] if r['id']==oid),'reader_semantic_review':meaning[oid.split('.')[-2]],'checks':own,'independent_actual_sdk_checks':independent['checks'],'source_path':row['source_path'],'source_sha256':row['source_sha256'],'example':row['example'],'example_sha256':row['example_sha256'],'behavior':row['behavior'],'behavior_sha256':row['behavior_sha256'],'model_ids':[m['id'] for m in model_results if oid in m['consumers']],'findings':issues})
report={'story':'DEV-STORY-083','reviewer':REVIEWER,'candidate':freeze['base_commit'],'status':'PASS' if all(r['verdict']=='PASS' for r in operations) and result.returncode==0 and all(m['definition_ast_equal'] and m['pages_unchanged'] and m['source_matches_frozen'] and not m['dependency_gaps'] for m in model_results) else 'FAIL','summary':{'operations':25,'PASS':sum(r['verdict']=='PASS' for r in operations),'FAIL':sum(r['verdict']=='FAIL' for r in operations),'initial_PASS':16,'initial_FAIL':9,'source_models':len(model_results),'fresh_checks':len(checks),'independent_actual_sdk_checks':sum(len(r['checks']) for r in execution['operations']),'author_pytest_exit':result.returncode,'author_pytest_output':result.stdout.strip(),'frozen_before_after_equal':before==after},'freeze':{'path':str(freeze_path),'sha256':sha(freeze_path)},'initial_fail_history_preserved':{'path':str(old_path),'sha256':sha(old_path)},'network_negative_controls':[c for c in checks if c['id'] is None],'operations':operations,'models':model_results,'continuity_before':before,'continuity_after':after,'limits':['Process-level guards exercised; no OS firewall claim.','No live Foundry, tenant permissions, server side effects, ordering, media framing or integration schema claims.','ValueBank JSON is synthetic. TimeSeriesPropertyV2 JSON selection does not establish array envelope.','SDK upload duplicate Content-Type serializes */*; synthetic response mediaType needs tenant verification.','Full model definitions and dependencies checked; shared semantic annotations preserved, no new manual interpretation claim.','No author/register changes, tracker writes, commit, push, formal promotion or acceptance.'],'reproduction':'.ept/tmp/feature015_shared_cli_qa_env/Scripts/python.exe -B .ept/tmp/rest083_fresh_retest_20261116.py'}
report['probe_provenance']={'historical_independent_sdk_harness':str(BASE/'rest083_independent_execution_20261029.py'),'historical_harness_sha256':sha(BASE/'rest083_independent_execution_20261029.py'),'reuse':'75 prior independently authored client probes rerun against corrected candidate. Fresh reviewer added mutation/cleanup/paging/UTF8/timing/source-continuity checks and reviewed guides/source contracts.','reviewer_harness_correction':'Initial own mutation probe assumed single override options at top level. SDK request actually nests options under request. Corrected test after source inspection; no candidate defect.'}
destination=BASE/'feature015_rest083_semantic_retest_20261116.json'; destination.write_text(json.dumps(report,indent=2,default=str))
manifest=BASE/'feature015_rest083_semantic_retest_manifest_20261116.json'
proofs=[Path(__file__),destination,pytest_path,BASE/'rest083_fresh_sdk_execution_20261116.json']
manifest.write_text(json.dumps({'reviewer':REVIEWER,'files':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in proofs]},indent=2))
print(json.dumps(report['summary'],indent=2)); print('STATUS',report['status']); print('REPORT_SHA256',sha(destination)); print('MANIFEST_SHA256',sha(manifest))
