import asyncio, contextlib, hashlib, importlib.metadata, inspect, io, json, os, re, shlex, socket, subprocess, sys, traceback
from pathlib import Path
from unittest.mock import patch
import httpx
from foundry_sdk import AsyncFoundryClient, UserTokenAuth
from foundry_sdk._core.config import Config
from foundry_sdk.v2.connectivity import models as cm
from foundry_sdk.v2.orchestration import models as om

ROOT=Path.cwd(); TMP=ROOT/'.ept/tmp'; PAGES=TMP/'feature015_connectivity_fixes/.agents/skills/pal-found-connectivity'
TOOL=TMP/'feature015_shared_cli_fixes'
sys.path.insert(0,str(TOOL/'src'))
from pal_found_cli.connectivity.scripts import pal_found_connectivity_cli as cc
from pal_found_cli.orchestration.scripts import pal_found_orchestration_cli as oc
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
prior_path=TMP/'feature015_connectivity_pages_review_20261028.json'
prior=json.loads(prior_path.read_text())
report={'owner':'DEV-STORY-061','reviewer':'/root/connectivity_retest_20261029','date':'2026-10-29','initial_review':{'path':str(prior_path),'sha256':sha(prior_path),'verdict':prior['overall_verdict'],'findings':prior['findings']},'harness_failures':[],'new_probes':[]}
previous=TMP/'feature015_connectivity_pages_retest_20261029.json'
if previous.exists():
 old_run=json.loads(previous.read_text())
 report['previous_harness_runs']=old_run.get('previous_harness_runs',[])+[{'overall_verdict':old_run['overall_verdict'],'harness_failures':old_run['harness_failures'],'new_probes':old_run['new_probes']}]
R='ri.magritte.main.source.synthetic'; B='ri.foundry.main.build.synthetic'; J='ri.foundry.main.job.synthetic'; D='ri.foundry.main.dataset.synthetic'; I='ri.magritte.main.file-import.synthetic'
build={'rid':B,'branchName':'master','createdTime':'2026-10-29T00:00:00Z','createdBy':'00000000-0000-0000-0000-000000000001','fallbackBranches':[],'jobRids':[J],'retryCount':0,'retryBackoffDuration':{'value':1,'unit':'SECONDS'},'abortOnFailure':False,'status':'RUNNING'}
job={'rid':J,'buildRid':B,'startedTime':'2026-10-29T00:00:00Z','jobStatus':'SUCCEEDED','outputs':[{'type':'datasetJobOutput','datasetRid':D,'outputTransactionRid':'ri.foundry.main.transaction.synthetic'}]}
fi={'rid':I,'connectionRid':R,'datasetRid':D,'branchName':'master','displayName':'Orders','fileImportFilters':[],'importMode':'SNAPSHOT'}
ti=dict(fi,rid='ri.magritte.main.table-import.synthetic',config={'type':'jdbcImportConfig','query':'SELECT * FROM table'},allowSchemaChanges=False); ti.pop('fileImportFilters')
env={'FOUNDRY_AGENTIC_CLI_ENV_FILE':str(TMP/'feature015_connectivity_finish_probe/probe.env'),'FOUNDRY_TOKEN':'offline-fixture','FOUNDRY_HOSTNAME':'https://offline.invalid','FOUNDRY_AGENTIC_CLI_ENABLED':'true','FOUNDRY_AGENTIC_CLI_READONLY':'false','FOUNDRY_AGENTIC_CLI_METADATA_ONLY':'false','FOUNDRY_AGENTIC_CLI_DEFAULT_FORMAT':'json','FOUNDRY_AGENTIC_CLI_LOG_LEVEL':'CRITICAL'}
async def probe(name,cli,argv,bodies,path,code=0,status=200):
 requests=[]
 def reply(req):
  requests.append({'method':req.method,'path':req.url.path,'query':req.url.query.decode(),'body':req.content.decode()})
  assert req.url.path==path
  body=bodies[min(len(requests)-1,len(bodies)-1)]
  return httpx.Response(status,json=body)
 out,err=io.StringIO(),io.StringIO()
 async with httpx.AsyncClient(transport=httpx.MockTransport(reply)) as transport:
  with patch('foundry_sdk._core.api_client.AsyncHttpClient',return_value=transport):
   sdk=AsyncFoundryClient(auth=UserTokenAuth('offline-fixture'),hostname='https://offline.invalid',config=Config(max_retries=0),preview=True)
   class Factory:
    def invocation_scope(self,*a,**kw): return contextlib.nullcontext()
    def create(self,*a,**kw): return sdk
   with patch.object(cli,'AsyncClientFactory',Factory),patch.object(sys,'argv',['probe',*argv]),patch.dict(os.environ,env),contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
    actual=await cli.main()
 row={'name':name,'argv':argv,'exit_code':actual,'stdout':out.getvalue(),'stderr':err.getvalue(),'requests':requests,'status':'PASS' if actual==code else 'FAIL'}
 report['new_probes'].append(row)
 assert actual==code,row
 return row

async def main():
 om.Build.model_validate(build); om.Job.model_validate(job)
 for state in om.BuildStatus.__args__:
  row=await probe('build state '+state,oc,['build','get',B,'--format','json','--timeout','30'],[dict(build,status=state)],'/api/v2/orchestration/builds/'+B)
  assert json.loads(row['stdout'])['status']==state
 for state in om.JobStatus.__args__:
  row=await probe('job state '+state,oc,['build','jobs',B,'--format','json','--max-pages','2','--timeout','30'],[{'data':[dict(job,jobStatus=state)]}],'/api/v2/orchestration/builds/'+B+'/jobs')
  assert json.loads(row['stdout'])[0]['jobStatus']==state
 for outputs in ([],[{'type':'datasetJobOutput','datasetRid':D}]):
  row=await probe('missing publication evidence '+str(outputs),oc,['build','jobs',B,'--format','json','--max-pages','2','--timeout','30'],[{'data':[dict(job,outputs=outputs)]}],'/api/v2/orchestration/builds/'+B+'/jobs')
  value=json.loads(row['stdout'])[0]['outputs']; assert not value or not value[0].get('outputTransactionRid')
 where={'type':'eq','field':'BRANCH_NAME','value':'master'}
 for resume in (False,True):
  argv=['build','search','--where-json',json.dumps(where),'--format','json','--max-pages','2','--timeout','30']+(['--page-token','resume-token'] if resume else [])
  row=await probe('lost execute branch search'+str(resume),oc,argv,[{'data':[],'nextPageToken':'next-page'},{'data':[build],'nextPageToken':'remaining'}],'/api/v2/orchestration/builds/search')
  assert len(row['requests'])==2 and json.loads(row['requests'][0]['body'])['where']==where
  assert json.loads(row['requests'][1]['body'])['pageToken']=='next-page' and 'remaining' in row['stderr']
  if resume: assert json.loads(row['requests'][0]['body'])['pageToken']=='resume-token'
 row=await probe('jobs empty cursor and bounded continuation',oc,['build','jobs',B,'--format','json','--max-pages','2','--page-token','resume-token','--timeout','30'],[{'data':[],'nextPageToken':'next-page'},{'data':[job],'nextPageToken':'remaining'}],'/api/v2/orchestration/builds/'+B+'/jobs')
 assert len(row['requests'])==2 and 'pageToken=resume-token' in row['requests'][0]['query'] and 'remaining' in row['stderr']
 for resource,value,modes in [('file-import',fi,cm.FileImportMode.__args__),('table-import',ti,cm.TableImportMode.__args__)]:
  endpoint='/api/v2/connectivity/connections/'+R+'/'+('fileImports' if resource=='file-import' else 'tableImports')
  for mode in modes:
   argv=[resource,'replace',R,value['rid'],'--display-name','Orders','--import-mode',mode]+(['--filters-json','[]'] if resource=='file-import' else ['--config-json',json.dumps(value['config'])])
   row=await probe(resource+' mode '+mode,cc,argv,[dict(value,importMode=mode)],endpoint+'/'+value['rid'])
   assert json.loads(row['requests'][0]['body'])['importMode']==mode
  row=await probe(resource+' uncertain create list recovery',cc,[resource,'list',R,'--max-pages','2','--page-token','resume-token'],[{'data':[],'nextPageToken':'next-page'},{'data':[value],'nextPageToken':'remaining'}],endpoint)
  assert len(row['requests'])==2 and 'remaining' in row['stderr']
  await probe(resource+' known RID read recovery',cc,[resource,'get',R,value['rid']],[value],endpoint+'/'+value['rid'])
  for status,code in ((403,3),(404,4)):
   await probe(resource+' inaccessible/missing read '+str(status),cc,[resource,'get',R,value['rid']],[{'errorCode':'PERMISSION_DENIED' if status==403 else 'NOT_FOUND','errorName':'PermissionDenied' if status==403 else 'NotFound','errorInstanceId':'00000000-0000-0000-0000-000000000001','parameters':{}}],endpoint+'/'+value['rid'],code,status)
 for status,code in ((401,2),(403,3)):
  await probe('build access stop '+str(status),oc,['build','get',B,'--format','json','--timeout','30'],[{'errorCode':'UNAUTHORIZED' if status==401 else 'PERMISSION_DENIED','errorName':'Unauthorized' if status==401 else 'PermissionDenied','errorInstanceId':'00000000-0000-0000-0000-000000000001','parameters':{}}],'/api/v2/orchestration/builds/'+B,code,status)

loop=asyncio.new_event_loop()
def deny(*a,**kw): raise AssertionError('NETWORK DENIED')
socket.socket.connect=socket.socket.connect_ex=socket.create_connection=socket.getaddrinfo=deny
try: loop.run_until_complete(main())
except BaseException: report['harness_failures'].append(traceback.format_exc())
finally: loop.close()
pattern=r'\*\*Example:\*\* `(pal-found-connectivity [^`]+)`'
report['pages']=[]
for old in prior['pages']:
 p=PAGES/old['page']; examples=re.findall(pattern,p.read_text(encoding='utf-8')); old_examples=[r['example'] for r in prior['full_command_evidence'] if r['page'].replace('\\','/')==old['page']]
 assert examples==old_examples
 report['pages'].append({'page':old['page'],'sha256':sha(p),'prior_sha256':old['sha256'],'prior_verdict':old['verdict'],'verdict':'PASS' if not report['harness_failures'] else 'UNCERTAIN','example_continuity':True,'unchanged_original_examples':len(examples)})
report['cli_commit']=subprocess.check_output(['git','-C',str(TOOL),'rev-parse','HEAD'],text=True).strip()
report['sdk_version']=importlib.metadata.version('foundry-platform-sdk')
report['source_continuity']={p:{'expected_sha256':s,'actual_sha256':sha(p),'matches':sha(p)==s} for p,s in prior['source_hashes'].items() if Path(p).exists()}
report['new_source_hashes']={str(p):sha(p) for p in [Path(cc.__file__),Path(oc.__file__),Path(inspect.getfile(cm)),Path(inspect.getfile(om))]}
report['harness_sha256']=sha(Path(__file__))
report['harness_command']='.ept/tmp/feature015_shared_cli_qa_env/Scripts/python.exe .ept/tmp/feature015_connectivity_pages_retest_20261029.py'
report['harness_failure_resolution']='First run used an absent explicit env file; corrected to existing isolated fixture env. Second run incorrectly expected POST build search pageToken in query; source and captured HTTP confirm JSON-body pagination, so assertion corrected. Both original runs retained in previous_harness_runs. Neither failure identifies a candidate defect.'
report['prior_HTTP_evidence_reused']={'examples':20,'extras':4,'basis':'All original examples identical. Previously reviewed source hashes checked below; corrected imports adds local knowledge and follow-up commands only.'}
report['semantic_review']={'CNT-PAGE-01':'PASS: Local build get/jobs commands, exact four build and six job states, branch/output/transaction evidence, bounded polling/paging, access stop and unresolved outcomes present. Orchestration installation/auth prerequisite explicit; no sibling skill required.','CNT-PAGE-02':'PASS: File SNAPSHOT/APPEND/UPDATE and Table SNAPSHOT/APPEND match SDK literal aliases and adjacent mode docstrings; UPDATE matches file names, not row keys.','CNT-PAGE-03':'PASS: Uncertain write warns accepted writes may precede client failure; known RID observation, branch search candidates without false request attribution, finite list/get recovery and explicit no-replay/owner resolution guidance cover create/replace/delete/execute. Virtual create lookup limitation explicit.','finite_budgets':'PASS: Observation 12 reads/5min with 10sec spacing, 4 job pages; uncertain execute 5min/2search pages/10candidates/2job pages each; create 4pages/5min; replace/delete 3reads/2min with 10sec spacing. Repeated cursor stops; partial/absent/ambiguous evidence unresolved.','full_page':'All three complete pages reviewed; unchanged operation contracts retain previous reviewed evidence. No invented Connectivity status command, unconditional retry advice or live tenant claim found.'}
report['limits']='Actual CLI main, installed SDK1.101.0 and MockTransport prove command parsing, typed responses, serialization, state/field exposure and recovery reads. Manual source-backed prose review proves stated budgets and decisions; no automated workflow/poll implementation claimed. No live permissions, source reachability, real import completion or dataset content validated. Initial FAIL retained; source/ledger/tracker untouched.'
report['overall_verdict']='PASS' if not report['harness_failures'] and all(x['matches'] for x in report['source_continuity'].values()) else 'UNCERTAIN'
out=TMP/'feature015_connectivity_pages_retest_20261029.json'; out.write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'report':str(out),'verdict':report['overall_verdict'],'probes':len(report['new_probes']),'failures':report['harness_failures'],'pages':report['pages']},indent=2))
