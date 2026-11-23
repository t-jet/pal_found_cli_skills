"""Independent REST091 source, semantic and transport review; no service access."""
import ast, base64, hashlib, importlib, inspect, json, re, runpy, socket, subprocess, textwrap
from collections import Counter
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import patch
import httpx
from foundry_sdk import PalantirRPCException

TMP=Path(__file__).resolve().parent
REPO=TMP/'feature015_integration'
DEV=REPO/'.agents/skills/pal-found-dev'
OUT=TMP/'feature015_rest091_semantic_review_20261029.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
rows=[r for r in json.loads((REPO/'maintainer/rest-domain-authoring-register.json').read_bytes())['operations'] if r['story']=='DEV-STORY-091']
head=lambda:subprocess.check_output(['git','-C',str(REPO),'rev-parse','HEAD'],text=True).strip()
before_head=head()
assets={}
def bind(p):
    p=p.resolve(); assets[str(p)]=sha(p); return str(p)
for p in (DEV/'examples/rest/091').rglob('*.py'):bind(p)
for service in ('media_sets','widgets'):
    for p in (DEV/'references/rest/v2'/service).glob('*.md'):bind(p)
for r in rows:bind(DEV/('references/rest/contracts/'+r['id'].replace('.','/')+'.md'))
bind(DEV/'examples/rest/common/mock_transport.py')
original_assets=dict(assets)
denied=[]; events=[]
def deny(*a,**k):
    denied.append(str(a[:1])); raise AssertionError('Offline review denies DNS, sockets and native HTTP transport')
original_send=httpx.Client.send
def send(self,request,*a,**k):
    events.append({'method':request.method,'url':str(request.url),'headers':dict(request.headers),'body_base64':base64.b64encode(request.content).decode()})
    return original_send(self,request,*a,**k)

R='ri.mio.main.media-item.00000000-0000-0000-0000-000000000002'
S='ri.mio.main.media-set.00000000-0000-0000-0000-000000000001'
V='ri.mio.main.view.00000000-0000-0000-0000-000000000003'
W='ri.widgets.main.widget-set.00000000-0000-0000-0000-000000000004'
P='ri.widgets.main.repository.00000000-0000-0000-0000-000000000005'
release={'widgetSetRid':W,'version':'1.2.3','locator':{'repositoryRid':P,'repositoryVersion':'build-123'}}
ref={'mimeType':'text/plain','reference':{'type':'mediaSetViewItem','mediaSetViewItem':{'mediaSetRid':S,'mediaSetViewRid':V,'mediaItemRid':R}}}
responses={
'abort':None,'calculate':{'type':'pending'},'clear':None,'commit':None,'create':'00000000-0000-0000-0000-000000000006',
'get_result':b'Subject: independent completed email text\n','get_rid_by_path':{'mediaItemRid':R},'get_status':{'jobId':'independent-job','status':'SUCCESSFUL'},
'info':{'viewRid':V,'logicalTimestamp':'123'},'metadata':{'type':'document','format':'PDF','sizeBytes':128},
'read':b'independent media bytes\n','read_original':b'independent original bytes\n','reference':ref,
'register':{'mediaItemRid':R,'mediaType':'text/plain'},'transform':{'jobId':'independent-job','status':'PENDING'},
'upload':{'mediaItemRid':R,'mediaSetViewRid':V},'upload_media':ref,
}
reasons={
'abort':'Open-transaction abort returns None; source and behavior state deletion of staged uploads.',
'calculate':'Pending thumbnail acknowledgment remains distinct from successful thumbnail retrieval.',
'clear':'Path soft-deletion includes older items; branch exclusivity and deferred transactional visibility documented.',
'commit':'Commit None acknowledgment and staged-item visibility documented; uncertain writes require reconciliation.',
'create':'Returned transaction ID belongs to existing media set; no new-set claim.',
'get':'Supplemental SDK fixture inspects imagery schema, batch policy, required paths and bounded PNG read.',
'get_result':'Binary result and completed-success prerequisite documented; synthetic text is valid transformed bytes.',
'get_rid_by_path':'FAIL: success fixture is {}; optional missing RID is legal but no found identity or explicit missing-path handling is demonstrated.',
'get_status':'Pending status and retained job ID correctly modeled; finite polling boundary documented.',
'info':'View RID and logical timestamp preserve item/view identity separation.',
'metadata':'Document discriminator, PDF format and byte-size fields decode; type-specific metadata guidance local.',
'read':'Bytes remain binary; supplemental stream example enforces budget and closes response.',
'read_original':'Original bytes distinguished from transformed representation; response lifetime closed.',
'reference':'FAIL: mimeType=synthetic-value is not a MIME type despite local MediaType meaning; identities otherwise serialize.',
'register':'FAIL: mediaType=synthetic-value is not MIME type; physical item/schema relationship is not demonstrated. Federated-only prerequisite documented.',
'retrieve':'WebP RIFF fixture encodes 200px width, matching source thumbnail contract.',
'transform':'Discriminated emailToText/getEmailBody TEXT request and pending job acknowledgment are coherent; read scope/token restrictions documented.',
'upload':'FAIL: observed Content-Type */* conflicts with SDK doc required application/octet-stream; reader gives no source-discrepancy adaptation. Binary has no declared media format or set policy.',
'upload_media':'FAIL: Content-Type */* conflicts with SDK doc, filename synthetic-value lacks format and returned MIME synthetic-value invalid. One-hour lifetime documented.',
}
special={
'v2.widgets.DevModeSettings.enable':'User-scoped ENABLED settings result, declared permission error and Private Beta boundary documented.',
'v2.widgets.DevModeSettings.set_widget_set_by_id':'FAIL: baseHref synthetic-value and empty widgetSettings configure no usable widget; returned empty widgetSetSettings cannot verify selected target. Request uses WidgetId, response map uses WidgetRid. Recovery asks retrieve current settings but supplies no read-only supported route.',
'v2.widgets.DevModeSettingsV2.enable':'User-scoped ENABLED result; optional absent snapshot legal, no publication claim.',
'v2.widgets.DevModeSettingsV2.set_widget_set_manifest':'FAIL: manifest is string synthetic-value; source requires JSON object manifestVersion and devSettings containing baseHref/widgets/inputSpec. Returned status-only result cannot verify target as prose directs.',
'v2.widgets.Release.delete':'Exact set/version identity, None result, host-impact review and uncertain-delete read reconciliation documented.',
'v2.widgets.Release.get':'Release tuple and repository locator coherent; missing version handled via bounded discovery.',
'v2.widgets.Release.list':'Release collection and nextPageToken rules, sync/async iterator distinction and finite-page guidance local.',
'v2.widgets.Repository.get':'Repository RID metadata read is appropriately distinct from publication.',
'v2.widgets.Repository.publish':'ZIP manifest path and assets tested; build-generated dist adaptation and locator identity check present. Synthetic empty manifest explicitly limited to transport test.',
'v2.widgets.WidgetSet.get':'Set RID metadata read, access/availability and absent-resource boundary explicit.',
}
result=[]
with ExitStack() as stack:
    for name in ('connect','connect_ex'):stack.enter_context(patch.object(socket.socket,name,deny))
    for name in ('create_connection','getaddrinfo','gethostbyname','gethostbyname_ex'):stack.enter_context(patch.object(socket,name,deny))
    stack.enter_context(patch.object(httpx.HTTPTransport,'handle_request',deny))
    stack.enter_context(patch.object(httpx.AsyncHTTPTransport,'handle_async_request',deny))
    stack.enter_context(patch.object(httpx.Client,'send',send))
    for row in rows:
        op=row['id'];version,service,resource,method=op.split('.')
        canonical=DEV/'examples/rest/091'/version/service/resource/('invoke_'+method+'.py')
        m=runpy.run_path(str(canonical)); cls=m[resource+'Client']; fn=getattr(cls,method)
        source=Path(inspect.getfile(cls));bind(source)
        node=ast.parse(textwrap.dedent(inspect.getsource(fn))).body[0]
        req=next(n for n in ast.walk(node) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='RequestInfo')
        wire={k.arg:ast.unparse(k.value) for k in req.keywords}
        contract=DEV/('references/rest/contracts/'+op.replace('.','/')+'.md');ct=contract.read_text(encoding='utf-8')
        mismatches=[key for key,value in wire.items() if key not in ('extra_request_params',) and value not in ct]
        start=len(events)
        try:m['verify']();fixture={'status':'PASS','requests':events[start:]}
        except Exception as e:fixture={'status':'FAIL','error':repr(e),'requests':events[start:]}
        value=responses.get(method)
        if method=='retrieve':value=base64.b64decode('UklGRjgAAABXRUJQVlA4ICwAAABwAwCdASrIAAEAPm02mEkkIyKhIogAgA2JaQAAE+6fQmzy4AAA/vshgAAAAA==')
        if method=='get':value=({'rid':S,'mediaSchema':'DOCUMENT','defaultBranchName':'master','transactionPolicy':{'type':'batchTransactions'},'pathsRequired':True} if service=='media_sets' else release if resource=='Release' else {'rid':P if resource=='Repository' else W})
        if service=='widgets' and method=='list':value={'data':[release],'nextPageToken':'independent-page-2'}
        if service=='widgets' and method=='publish':value=release
        if service=='widgets' and method in ('enable','set_widget_set_by_id','set_widget_set_manifest'):value={'status':'ENABLED',**({'widgetSetSettings':{}} if resource=='DevModeSettings' else {})}
        own=[]
        for fail in (False,True):
            def handler(request):
                if fail:return httpx.Response(403,json={'errorName':'IndependentDenied','errorCode':'PERMISSION_DENIED','parameters':{},'errorInstanceId':'00000000-0000-0000-0000-000000000009'})
                if isinstance(value,bytes):return httpx.Response(200,content=value)
                return httpx.Response(204) if value is None else httpx.Response(200,json=value)
            try:
                with m['mock_resource'](cls,handler) as client:
                    raw=m['invoke'](client)
                    try:decoded=m['normalized'](raw.decode())
                    finally:raw.close()
                assert not fail and decoded==value
                own.append({'case':'independent response','status':'PASS','expected':value})
            except PalantirRPCException as error:
                own.append({'case':'independent generic denial','status':'PASS' if fail and error.name=='IndependentDenied' else 'FAIL','error':str(error)})
            except Exception as e:own.append({'case':'independent response' if not fail else 'independent denial','status':'FAIL','error':repr(e)})
        reason=special[op] if service=='widgets' else reasons[method]
        status='FAIL' if reason.startswith('FAIL:') or mismatches or fixture['status']=='FAIL' or any(x['status']=='FAIL' for x in own) else 'PASS'
        result.append({'id':op,'status':status,'reason':reason,'source':str(source),'source_sha256':sha(source),'source_doc':ast.get_docstring(node),'source_wire':wire,'contract':str(contract),'behavior':str(DEV/row['behavior']),'example':str(canonical),'contract_wire_mismatches':mismatches,'author_fixture_execution':fixture,'independent_cases':own})
    supplementary=runpy.run_path(str(DEV/'examples/rest/091/media_identity.py'))
    supplementary['verify']()

# Walk only qualified model/error links reachable from owned contracts.
todo=[]
for r in result:
    p=Path(r['contract'])
    todo.extend((p.parent/link.split('#')[0]).resolve() for link in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')) if 'models/' in link)
seen=set();model_checks=[]
ledger=json.loads((REPO/'tests/fixtures/offline/rest-acceptance/model-source-oracle.json').read_bytes())['symbols']
while todo:
    p=todo.pop()
    if p in seen:continue
    seen.add(p)
    if not p.is_file():model_checks.append({'asset':str(p),'status':'FAIL','reason':'missing local definition'});continue
    bind(p);txt=p.read_text(encoding='utf-8');title=txt.splitlines()[0].removeprefix('# ').strip()
    for link in re.findall(r'\]\(([^)]+)\)',txt):
        if link.startswith(('http:','https:','#')):continue
        target=(p.parent/link.split('#')[0]).resolve()
        if '/references/rest/models/' in target.as_posix():todo.append(target)
    if title not in ledger:continue
    info=ledger[title];module=importlib.import_module(info['module']);src=Path(module.__file__);bind(src)
    name=title.rsplit('.',1)[1];tree=ast.parse(src.read_text(encoding='utf-8'))
    definition=next(n for n in tree.body if (isinstance(n,ast.ClassDef) and n.name==name) or (isinstance(n,ast.AnnAssign) and isinstance(n.target,ast.Name) and n.target.id==name) or (isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets)))
    actual=ast.dump(definition,include_attributes=False)
    blocks=re.findall(r'```python\s*\n(.*?)\n```',txt,re.S)
    match=any(any(ast.dump(n,include_attributes=False)==actual for n in ast.parse(block).body) for block in blocks)
    model_checks.append({'symbol':title,'asset':str(p),'source':str(src),'source_sha256':sha(src),'definition_ast_matches':match,'status':'PASS' if match else 'FAIL','dependencies':info['dependencies']})
after_head=head();changed=[p for p,h in original_assets.items() if sha(p)!=h]
report={'story':'DEV-STORY-091','reviewer_agent':'/root/rest091_semantic_review_20261029','candidate':str(REPO),'candidate_head_before':before_head,'candidate_head_after':after_head,'candidate_asset_stability':{'changed':changed,'stable':not changed},'scope':'Independent all29 source and semantic review; SDK1.101.0 MockTransport execution only. No formal promotion, blind-reader or live Foundry claim.','counts':dict(Counter(r['status'] for r in result)),'operations':result,'model_checks':model_checks,'model_counts':dict(Counter(r['status'] for r in model_checks)),'model_dependency_closure_missing':sorted({d for r in model_checks for d in r.get('dependencies',[])}-{r.get('symbol') for r in model_checks}),'network':{'socket_DNS_native_HTTP':'DENIED','attempts':denied,'sdk_requests':len(events)},'raw_requests':events,'asset_sha256':assets,'boundaries':['Synthetic IDs and mock server acknowledgments do not establish tenant authorization, valid resources, transaction effects, transformation execution or publication.','No numeric widget count/entrypoint limits invented where frozen source is silent.','PASS requires source/behavior/model/meaning review; author fixture PASS alone never establishes semantic acceptance.']}
OUT.write_text(json.dumps(report,indent=2,default=lambda v:{'base64':base64.b64encode(v).decode()} if isinstance(v,bytes) else str(v)),encoding='utf-8')
print(json.dumps({'report':str(OUT),'counts':report['counts'],'models':report['model_counts'],'missing':report['model_dependency_closure_missing'],'changed':changed,'requests':len(events)}))

