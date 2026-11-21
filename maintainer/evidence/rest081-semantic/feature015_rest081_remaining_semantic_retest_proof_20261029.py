"""Independent offline review of the eleven pending DEV-STORY-081 operations."""
import ast
import asyncio
import hashlib
import importlib
import importlib.metadata
import inspect
import json
import pathlib
import re
import socket
import sys
import traceback
import urllib.request
from unittest.mock import patch

sys.dont_write_bytecode = True
BASE = pathlib.Path(__file__).resolve().parent
ROOT = BASE / 'rest081_remaining_qa_20261029'
SKILL = ROOT / '.agents/skills/pal-found-dev'
OUT = BASE / 'feature015_rest081_remaining_semantic_retest_20261029.json'
REVIEWER = '/root/rest081_review_harness_recover_20261029'
import httpx
import foundry_sdk
from foundry_sdk import Config, UserTokenAuth, PalantirRPCException

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

domain = json.loads((ROOT/'maintainer/rest-domain-authoring-register.json').read_text())
contracts = {x['id']:x for x in json.loads((ROOT/'maintainer/rest-contract-register.json').read_text())['operations']}
models = {x['id']:x for x in json.loads((ROOT/'maintainer/rest-model-register.json').read_text())['symbols']}
owned = [x for x in domain['operations'] if x['story']=='DEV-STORY-081']
pending = [x for x in owned if x['semantic_review_status']!='accepted']
assert len(pending)==11 and len(owned)==22
sdkroot = pathlib.Path(foundry_sdk.__file__).resolve().parent.parent
manifest = {}

def bind(path):
    path=path.resolve()
    manifest[str(path)] = sha(path)

for name in ['rest-domain-authoring-register.json','rest-contract-register.json','rest-model-register.json']:
    bind(ROOT/'maintainer'/name)
bind(pathlib.Path(__file__))

# Separate values and results from the distributed author fixtures.
ontology='qa-dispatch'; scenario='ri.scenario.main.scenario.00000000-0000-0000-0000-000000000081'
rid='ri.object-set.main.temporary-object-set.00000000-0000-0000-0000-000000000081'
asset={'__primaryKey':'QA-42','__apiName':'Asset'}
site={'__primaryKey':'QA-SITE-8','__apiName':'Site'}
links={'sourceObject':asset,'linkedObjects':[{'targetObject':site,'linkType':'installedAt'}]}
ordered=[{'objectType':'Asset','primaryKey':'QA-42','properties':{'state':'Inspect'},'type':'modifyObject'},
         {'objectType':'Asset','primaryKey':'QA-42','properties':{'state':'Approved'},'type':'modifyObject'}]
CASES={
 'OntologyObject.count':('POST','/objects/Asset/count',{'object_type':'Asset'},None,{'count':17}),
 'OntologyObjectSet.get':('GET','/objectSets/'+rid,{'object_set_rid':rid},None,{'type':'base','objectType':'Asset'}),
 'OntologyObjectSet.load_links':('POST','/objectSets/loadLinks',{'links':['installedAt'],'object_set':{'type':'base','objectType':'Asset'}}, {'objectSet':{'type':'base','objectType':'Asset'},'links':['installedAt']},{'data':[links]}),
 'OntologyScenario.create_scenario':('POST','/scenarios/create',{}, {},{'scenarioRid':scenario}),
 'OntologyScenario.list_scenario_conflicting_objects':('GET',f'/scenarios/{scenario}/objects/Asset/conflicting',{'scenario_rid':scenario,'object_type':'Asset'},None,{'data':[{'objectTypeApiName':'Asset','primaryKeyValue':'QA-42'}]}),
 'OntologyScenario.list_scenario_edited_entity_types':('GET',f'/scenarios/{scenario}/editedEntityTypes',{'scenario_rid':scenario},None,{'objectTypes':['Asset'],'linkTypes':[{'objectTypeApiName':'Asset','linkTypes':['installedAt']}]}),
 'OntologyScenario.list_scenario_edited_link_types':('GET',f'/scenarios/{scenario}/objectTypes/Asset/outgoingLinkTypes/edited',{'scenario_rid':scenario,'object_type':'Asset'},None,{'data':['installedAt']}),
 'OntologyScenario.list_scenario_edited_links':('GET',f'/scenarios/{scenario}/objects/Asset/links/installedAt/edited',{'scenario_rid':scenario,'object_type':'Asset','link_type':'installedAt'},None,{'data':[links]}),
 'OntologyScenario.list_scenario_edited_object_types':('GET',f'/scenarios/{scenario}/objectTypes/edited',{'scenario_rid':scenario},None,{'data':['Asset']}),
 'OntologyScenario.list_scenario_edited_objects':('GET',f'/scenarios/{scenario}/objects/Asset/edited',{'scenario_rid':scenario,'object_type':'Asset'},None,{'data':[asset]}),
 'OntologyTransaction.post_edits':('POST','/transactions/qa-txn-81/edits',{'transaction_id':'qa-txn-81','edits':ordered},{'edits':ordered},{}),
}
NOTES={
 'OntologyObject.count':'Count is optional; absent count means unknown. Type count has no filter argument. Branch support is experimental.',
 'OntologyObjectSet.get':'Returns an ObjectSet definition union, not loaded objects or a permanent inventory. Temporary RID expiry comes from create_temporary source.',
 'OntologyObjectSet.load_links':'Locators only; repeat source entries allowed; links may be stale. 1,000 source objects per page, 100,000-link cap per group of 1,000 makes partial data possible. OSv1 and interface links/sets unsupported.',
 'OntologyScenario.create_scenario':'Returns scenarioRid; propagate identifier to inspections. Omitted base is accepted by SDK but source does not define server default base.',
 'OntologyScenario.list_scenario_conflicting_objects':'ObjectLocator uses objectTypeApiName/primaryKeyValue, unlike link object metadata. Permission-filtered; false positives possible; page_size bounds examined objects.',
 'OntologyScenario.list_scenario_edited_entity_types':'Object API names and outgoing many-to-many link API names grouped by source type; one-to-many changes surface as foreign-key-owner object edits.',
 'OntologyScenario.list_scenario_edited_link_types':'Only outgoing many-to-many link types; one-to-many changes surface as object edits.',
 'OntologyScenario.list_scenario_edited_links':'Links grouped by source object, many-to-many only; visibility required for both endpoints. Short page may still have continuation.',
 'OntologyScenario.list_scenario_edited_object_types':'Returns modified object API names; response is a model containing data, not an object iterator.',
 'OntologyScenario.list_scenario_edited_objects':'Iterator returns OntologyObjectV2 dictionaries, not ObjectLocator. Permission-filtered; empty visible results do not prove no edits.',
 'OntologyTransaction.post_edits':'Edits retain list order and discriminator aliases. Empty response model acknowledges transport only; no commit guarantee, retry/idempotency guarantee, or transaction creation route inferred.',
}

deny_events=[]
def deny(*args,**kwargs):
    deny_events.append('denied')
    raise RuntimeError('QA_PUBLIC_NETWORK_DENIED')

def normalized(x):
    if hasattr(x,'model_dump'):return x.model_dump(mode='json',by_alias=True,exclude_none=True)
    if isinstance(x,list):return [normalized(v) for v in x]
    return x

def resource(cls,transport,async_mode=False):
    seam='foundry_sdk._core.api_client.'+('AsyncHttpClient' if async_mode else 'HttpClient')
    with patch(seam,return_value=transport):
        return cls(auth=UserTokenAuth(token='qa-offline-token'),hostname='qa.invalid',config=Config(timeout=3,max_retries=1,propagate_qos='PROPAGATE_429_AND_503_TO_CALLER'))

def getmodule(res):
    return importlib.import_module('foundry_sdk.v2.ontologies.'+re.sub(r'(?<!^)(?=[A-Z])','_',res).lower())

def source_wire(fn):
    tree=ast.parse(inspect.getsource(fn).lstrip() if not inspect.getsource(fn).startswith(' ') else __import__('textwrap').dedent(inspect.getsource(fn)))
    calls=[n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='call_api']
    assert len(calls)==1
    return {k.arg:ast.unparse(k.value) for k in calls[0].keywords}

model_evidence={}
def review_model(symbol):
    if symbol in model_evidence:return
    row=models[symbol]; p=SKILL/row['local_definition'];bind(p)
    source=sdkroot/row['source'];bind(source)
    name=symbol.rsplit('.',1)[1]
    tree=ast.parse(source.read_text(encoding='utf-8'))
    candidates=[n for n in tree.body if (isinstance(n,ast.ClassDef) and n.name==name) or (isinstance(n,ast.AnnAssign) and isinstance(n.target,ast.Name) and n.target.id==name) or (isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets))]
    text=p.read_text(encoding='utf-8')
    # Split pages carry the remainder of long definitions.
    parts=sorted(p.parent.glob(p.stem+'.part*.md'))
    for part in parts:bind(part);text+='\n'+part.read_text(encoding='utf-8')
    snippets=[]
    for code in re.findall(r'```python\s*\n(.*?)```',text,re.S):
        try:snippets.extend(ast.parse(code).body)
        except SyntaxError:pass
    exact=bool(candidates and any(ast.dump(candidates[0],include_attributes=False)==ast.dump(n,include_attributes=False) for n in snippets))
    model_evidence[symbol]={'source':str(source),'source_sha256':sha(source),'registered_source_match':sha(source)==row['source_sha256'],'guide':str(p),'guide_sha256':sha(p),'exact_definition_ast_match':exact,'dependencies':row['dependencies']}
    for dep in row['dependencies']:review_model(dep)

operations=[]
loop = asyncio.new_event_loop()
with patch.object(socket,'getaddrinfo',deny),patch.object(socket,'create_connection',deny),patch.object(socket.socket,'connect',deny),patch.object(socket.socket,'connect_ex',deny),patch.object(httpx.HTTPTransport,'handle_request',deny),patch.object(httpx.AsyncHTTPTransport,'handle_async_request',deny),patch.object(urllib.request,'urlopen',deny):
    for probe in [lambda:socket.getaddrinfo('www.palantir.com',443),lambda:socket.create_connection(('www.palantir.com',443)),lambda:httpx.get('https://www.palantir.com',timeout=1),lambda:urllib.request.urlopen('https://www.palantir.com',timeout=1)]:
        try:probe();raise AssertionError('Network guard did not block')
        except RuntimeError as e:assert str(e)=='QA_PUBLIC_NETWORK_DENIED'
    for item in pending:
        oid=item['id'];_,_,res,method=oid.split('.');key=res+'.'+method
        contract=contracts[oid];module=getmodule(res);cls=getattr(module,res+'Client');fn=getattr(cls,method)
        source=pathlib.Path(module.__file__);bind(source)
        for p in [item['behavior'],item['example'],*contract['parts']]:bind(SKILL/p)
        for symbol in contract['symbols']:review_model(symbol)
        result={'id':oid,'semantic_verdict':'PASS','reviewer':REVIEWER,'finding':NOTES[key],'stage':contract['stage'],'source_path':str(source),'source_sha256':sha(source),'registered_source_match':sha(source)==item['source_sha256'],'sdk_signature':str(inspect.signature(fn)),'sdk_docstring':inspect.getdoc(fn),'source_wire':source_wire(fn),'contract':contract['contract'],'behavior':item['behavior'],'example':item['example'],'models':contract['symbols'],'mode_probes':[],'failures':[],'live_enrollment_status':'not exercised','permission_boundary':'Authorized identity and beta access required; source provides no complete permission policy or universal scopes.','availability_boundary':'Private Beta frozen source surface; passing preview does not prove enablement.'}
        try:
            assert result['registered_source_match']
            spec=importlib.util.spec_from_file_location('qa_'+method,SKILL/item['example']);example=importlib.util.module_from_spec(spec);spec.loader.exec_module(example);example.verify();result['distributed_fixture']='PASS'
            verb,suffix,kw,body,payload=CASES[key];params={'ontology':ontology,**kw,'preview':True,'request_timeout':3};requests=[]
            def handler(req):
                assert req.method==verb
                assert req.url.path=='/api/v2/ontologies/'+ontology+suffix
                assert req.url.params.get('preview')=='true'
                assert req.headers['authorization']=='Bearer qa-offline-token'
                assert (json.loads(req.content) if req.content else None)==body
                requests.append({'method':req.method,'path':req.url.path,'query':str(req.url.query),'body':body})
                return httpx.Response(200,json=payload)
            iterator='ResourceIterator' in str(inspect.signature(fn).return_annotation)
            with httpx.Client(transport=httpx.MockTransport(handler)) as http:
                client=resource(cls,http)
                ordinary=getattr(client,method)(**params)
                assert normalized(list(ordinary) if iterator else ordinary)==(payload['data'] if iterator else payload)
                result['mode_probes'].append('sync ordinary')
                raw=getattr(client.with_raw_response,method)(**params)
                try:assert normalized(raw.decode())==payload
                finally:raw.close()
                assert raw._response.is_closed
                result['mode_probes'].append('sync raw closed')
                with getattr(client.with_streaming_response,method)(**params) as stream:assert json.loads(b''.join(stream.iter_bytes()))==payload
                assert stream._response.is_closed
                result['mode_probes'].append('sync streaming closed')
            async def aprobe():
                acls=getattr(module,'Async'+res+'Client')
                async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as http:
                    client=resource(acls,http,True)
                    value=getattr(client,method)(**params)
                    value=[x async for x in value] if iterator else await value
                    assert normalized(value)==(payload['data'] if iterator else payload)
                    raw=await getattr(client.with_raw_response,method)(**params)
                    try:assert normalized(raw.decode())==payload
                    finally:await raw.aclose()
                    assert raw._response.is_closed
                    async with getattr(client.with_streaming_response,method)(**params) as stream:assert json.loads(b''.join([chunk async for chunk in stream.aiter_bytes()]))==payload
                    assert stream._response.is_closed
            loop.run_until_complete(aprobe());result['mode_probes']+=['async ordinary','async raw closed','async streaming closed']
            result['independent_requests']=requests
            def failure(req):return httpx.Response(403,json={'errorCode':'PERMISSION_DENIED','errorName':'QaAccessDenied','errorInstanceId':'00000000-0000-0000-0000-000000000081','parameters':{}})
            with httpx.Client(transport=httpx.MockTransport(failure)) as http:
                client=resource(cls,http)
                try:
                    raw=getattr(client.with_raw_response,method)(**params);raw.close();raise AssertionError('403 did not fail')
                except PalantirRPCException as e:assert e.name=='QaAccessDenied';result['generic_denial_probe']='PASS: synthetic generic 403, no invented named endpoint error'
        except Exception:
            result['semantic_verdict']='FAIL';result['failures'].append(traceback.format_exc())
        operations.append(result)

loop.close()
bad_models=[k for k,v in model_evidence.items() if not v['registered_source_match'] or not v['exact_definition_ast_match']]
for op in operations:
    bad=[m for m in op['models'] if m in bad_models]
    if bad:op['semantic_verdict']='UNCERTAIN' if not op['failures'] else 'FAIL';op['model_definition_review_gaps']=bad
stable=all(sha(pathlib.Path(p))==h for p,h in manifest.items())
report={'original_harness_disposition':'Harness failure; original FAIL results invalid as candidate defect evidence. Original artifacts unchanged.', 'provenance_file':str(BASE/'feature015_rest081_remaining_harness_provenance_20261029.json'),'story':'DEV-STORY-081','reviewer':REVIEWER,'reviewed_candidate_sha':'6df64cce16bf0619bee124f831e1e8686c08cccf','sdk_release':importlib.metadata.version('foundry-platform-sdk'),'sdk_source_commit':'168d51910570b6966afa2320333ab36f6a3f7ccf','scope':'11 previously pending private-beta operations; previous accepted11 retained unchanged','counts':{v:sum(x['semantic_verdict']==v for x in operations) for v in ['PASS','FAIL','UNCERTAIN']},'operations':operations,'model_review':model_evidence,'model_review_gaps':bad_models,'content_manifest':manifest,'hash_stability':stable,'network_guard_probes_denied':len(deny_events),'network_guard':'DNS/socket connect/create_connection, httpx native sync/async transports, urllib denied before importing fixtures; only MockTransport permitted','preserved_accepted_operation_ids':[x['id'] for x in owned if x['semantic_review_status']=='accepted'],'formal_qa_status':'not promoted; TESTEXEC prerequisites remain tracker-gated','live_foundry_claims':False}
OUT.write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'counts':report['counts'],'model_count':len(model_evidence),'model_gaps':len(bad_models),'hash_stability':stable,'report':str(OUT)}))
for op in operations:
    if op['failures']:print(op['id'],op['failures'][0])
if bad_models:print('MODEL GAPS',bad_models[:20])
