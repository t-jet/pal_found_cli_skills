"""Independent frozen-candidate restore proof. All HTTP responses are synthetic."""
import os
import ast
import hashlib
import importlib
import inspect
import json
import re
import runpy
import socket
import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

import httpx
from foundry_sdk import Config, UserTokenAuth, PalantirRPCException, TimeoutError
from foundry_sdk.v2.filesystem.resource import ResourceClient
from foundry_sdk.v2.filesystem import errors

TMP = Path(__file__).resolve().parent
ROOT = TMP / 'feature015_rest073_restore_fixes'
SKILL = ROOT / '.agents/skills/pal-found-dev'
MANIFEST = TMP / 'feature015_rest073_restore_combined_manifest_20261116.json'
OUT = TMP / 'feature015_rest073_restore_semantic_retest_20261116.json'
SDKREPO = TMP.parents[1] / '.ept/docs/customer_input/foundry-platform-python'
RID = 'ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001'
PARENT = 'ri.synthetic.main.folder.00000000-0000-0000-0000-000000000002'
PATH = '/qa/approved/resource'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest = json.loads(MANIFEST.read_text())
assert sha(MANIFEST) == '659afb12a6877eed8ea3f26f2ba6cf6cef8ed6974851a8e1b5f02263cca81467'
bindings = {str(ROOT / p): h for p, h in manifest['combined_dirty_manifest'].items()}
bindings.update(manifest['source_bindings'])
bindings.update({str(TMP / p): h for p,h in manifest['proofs'].items()})
bindings[str(MANIFEST)] = sha(MANIFEST)
assert all(sha(Path(p)) == h for p,h in bindings.items())
assert subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD'], text=True).strip() == manifest['base_sha']
assert subprocess.check_output(['git','-C',str(SDKREPO),'rev-parse','1.101.0^{}'], text=True).strip() == manifest['source_commit']
for p in manifest['source_bindings']:
    relative = 'foundry_sdk/' + Path(p).as_posix().split('/foundry_sdk/',1)[1]
    frozen = subprocess.check_output(['git','-C',str(SDKREPO),'show',manifest['source_commit'] + ':' + relative])
    assert frozen.replace(b'\r\n',b'\n') == Path(p).read_bytes().replace(b'\r\n',b'\n')

contract = SKILL / 'references/rest/contracts/v2/filesystem/Resource/restore.md'
behavior = SKILL / 'references/rest/v2/filesystem/Resource.md'
example = SKILL / 'examples/rest/073/v2/filesystem/Resource/restore.py'
source = Path(inspect.getfile(ResourceClient)).read_text(encoding='utf8')
client_ast = next(n for n in ast.parse(source).body if isinstance(n,ast.ClassDef) and n.name == 'ResourceClient')
restore_ast = next(n for n in client_ast.body if isinstance(n,ast.FunctionDef) and n.name == 'restore')
assert hashlib.sha256(ast.get_source_segment(source,restore_ast).encode()).hexdigest() == manifest['restore_method_sha256']
assert ast.get_docstring(restore_ast).split(':param')[0].strip() in contract.read_text()
assert '## SDK source disagreement' in contract.read_text()
assert '../../../../v2/filesystem/Resource.md#restore' in contract.read_text()
assert '### restore' in behavior.read_text()
bindings[str(Path(__file__).resolve())] = sha(Path(__file__).resolve())
classes = {n.name:n for n in ast.parse(source).body if isinstance(n,ast.ClassDef)}
async_restore = next(n for n in classes['AsyncResourceClient'].body if isinstance(n,ast.FunctionDef) and n.name == 'restore')
assert ast.unparse(async_restore.returns) == 'typing.Awaitable[None]'
assert '| async_ordinary | typing.Awaitable[None] |' in contract.read_text()
assert '| sync_raw | ApiResponse[None] |' in contract.read_text()
assert '| async_raw | Awaitable[AsyncApiResponse[None]] |' in contract.read_text()
for cls in ('_ResourceClientStreaming','_AsyncResourceClientStreaming'):
    assert not any(isinstance(n,ast.Attribute) and n.attr=='restore' for n in ast.walk(classes[cls]))
for cls in ('_ResourceClientRaw','_AsyncResourceClientRaw'):
    assert any(isinstance(n,ast.Attribute) and n.attr=='restore' for n in ast.walk(classes[cls]))
request_info = next(n for n in ast.walk(restore_ast) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='RequestInfo')
for keyword in request_info.keywords:
    assert '**'+keyword.arg+'**\n\n```python\n'+ast.unparse(keyword.value)+'\n```' in contract.read_text()
for target in re.findall(r'\]\(([^)]+)\)',behavior.read_text()):
    if '://' not in target and not target.startswith('#'):
        assert (behavior.parent / target.split('#')[0]).resolve().is_file(), target

models = set()
pending = [contract, SKILL / 'references/rest/models/v2/filesystem/models/Resource.md']
links = []
while pending:
    page = pending.pop()
    bindings[str(page)] = sha(page)
    for target in re.findall(r'\]\(([^)]+)\)',page.read_text(encoding='utf8')):
        if '://' in target or target.startswith('#'):
            continue
        path = (page.parent / target.split('#')[0]).resolve()
        assert path.is_file(), (page,target)
        links.append({'from':str(page.relative_to(SKILL)), 'target':target})
        if '/references/rest/models/' in path.as_posix() and path not in models:
            models.add(path)
            pending.append(path)
model_source_checks = []
for page in sorted(models):
    content = page.read_text(encoding='utf8')
    symbol = content.splitlines()[0].removeprefix('# ')
    module_name, name = symbol.rsplit('.',1)
    module = importlib.import_module(module_name)
    module_path = Path(inspect.getfile(module))
    bindings[str(module_path)] = sha(module_path)
    nodes = ast.parse(module_path.read_text(encoding='utf8')).body
    definitions = [n for n in nodes if (isinstance(n,(ast.ClassDef,ast.FunctionDef)) and n.name == name) or (isinstance(n,ast.AnnAssign) and isinstance(n.target,ast.Name) and n.target.id == name) or (isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id == name for t in n.targets))]
    fences = re.findall(r'```python\n(.*?)\n```',content,re.S)
    assert definitions and fences, symbol
    assert any(ast.dump(ast.parse(fence).body[0],include_attributes=False) == ast.dump(definitions[0],include_attributes=False) for fence in fences), symbol
    model_source_checks.append({'symbol':symbol,'exact_definition':'PASS','page_sha256':sha(page),'source_sha256':sha(module_path)})

proof = []
attempts = []
def denied(*a,**kw):
    attempts.append(True)
    raise AssertionError('Independent QA denies native DNS/HTTP')
def payload(status, **changes):
    value = dict(rid=RID,displayName='QA resource',path=PATH,type='FOLDER',createdBy='00000000-0000-0000-0000-000000000001',updatedBy='00000000-0000-0000-0000-000000000001',createdTime='2026-11-16T00:00:00Z',updatedTime='2026-11-16T00:00:00Z',trashStatus=status,parentFolderRid=PARENT,projectRid='ri.synthetic.main.project.00000000-0000-0000-0000-000000000003',spaceRid='ri.synthetic.main.space.00000000-0000-0000-0000-000000000004')
    value.update(changes)
    return httpx.Response(200,json=value)
def error(name,status=400,code='INVALID_ARGUMENT'):
    return httpx.Response(status,json=dict(errorName=name,errorCode=code,parameters={'resourceRid':RID},errorInstanceId='00000000-0000-0000-0000-000000000004'))
def execute(name,responses,decision=None,exception=None,raw=False,ordinary=False):
    observed=[]
    def handler(request):
        assert len(observed)<len(responses), 'Unexpected replay/read'
        assert request.url.path == '/api/v2/filesystem/resources/' + RID + ('/restore' if request.method=='POST' else '')
        assert request.url.query == b'' and request.content == b''
        assert request.headers['authorization']=='Bearer qa-token'
        assert request.extensions['timeout']==dict.fromkeys(('connect','read','write','pool'),30)
        observed.append({'method':request.method,'path':request.url.path,'timeout':request.extensions['timeout']})
        response=responses[len(observed)-1]
        if isinstance(response,Exception): raise response
        return response
    with httpx.Client(transport=httpx.MockTransport(handler)) as transport:
        with patch('foundry_sdk._core.api_client.HttpClient',return_value=transport):
            resource=ResourceClient(auth=UserTokenAuth(token='qa-token'),hostname='offline.invalid',config=Config(timeout=30,max_retries=1))
        try:
            if raw:
                result=resource.with_raw_response.restore(RID,request_timeout=30)
                try:
                    assert result.status_code==204 and result.decode() is None
                finally: result.close()
                assert result._response.is_closed
                result='204/None/closed'
            elif ordinary:
                result=resource.restore(RID,request_timeout=30)
                assert result is None
            else:
                result=example_ns['restore_once'](resource,RID,expected_parent_rid=PARENT,expected_path=PATH)
                assert result==decision,(name,result,decision)
            assert exception is None
        except Exception as exc:
            assert exception is not None and isinstance(exc,exception),(name,type(exc))
            if hasattr(exc,'parameters'): assert exc.parameters=={'resourceRid':RID}
            result=type(exc).__name__
    assert len(observed)==len(responses)
    assert sum(r['method']=='POST' for r in observed)<=1
    proof.append({'case':name,'verdict':'PASS','requests':observed,'outcome':result})

with patch.object(socket,'getaddrinfo',denied),patch.object(socket.socket,'connect',denied),patch.object(socket.socket,'connect_ex',denied):
    example_ns=runpy.run_path(str(example))
    execute('ordinary success 204', [httpx.Response(204)],ordinary=True)
    execute('raw success closes response', [httpx.Response(204)],raw=True)
    for name,status,code in [('ResourceNotDirectlyTrashed',400,'INVALID_ARGUMENT'),('ResourceNotFound',404,'NOT_FOUND'),('RestoreResourcePermissionDenied',403,'PERMISSION_DENIED')]:
        execute('exact SDK error '+name,[error(name,status,code)],exception=getattr(errors,name),ordinary=True)
    execute('active preflight skips write',[payload('NOT_TRASHED')],decision='Desired state observed; no restore sent')
    ancestor='STOP: authorized owner must reconcile original folder restoration'
    execute('ancestor preflight stops',[payload('ANCESTOR_TRASHED')],decision=ancestor)
    for outcome in ('204','not-direct','timeout'):
        for state in ('NOT_TRASHED','ANCESTOR_TRASHED','DIRECTLY_TRASHED'):
            write={'204':httpx.Response(204),'not-direct':error('ResourceNotDirectlyTrashed'),'timeout':httpx.ReadTimeout('unknown write outcome')}[outcome]
            decision={'NOT_TRASHED':'Desired state observed after attempt; no replay','ANCESTOR_TRASHED':ancestor,'DIRECTLY_TRASHED':'STOP: still directly trashed; reconcile outcome/policy with authorized owner'}[state]
            execute(outcome+' readback '+state,[payload('DIRECTLY_TRASHED'),write,payload(state)],decision=decision)
    for field,new in [('rid',RID+'9'),('parentFolderRid',PARENT+'9'),('path',PATH+'-moved')]:
        for after in (False,True):
            responses=([payload('DIRECTLY_TRASHED'),httpx.Response(204)] if after else [])+[payload('NOT_TRASHED',**{field:new})]
            execute('mismatch '+field+' after='+str(after),responses,decision='STOP: reconcile RID, parent and path with authorized owner')
    for after in (False,True):
        for fault in ('denied','missing','timeout'):
            response,exc={'denied':(error('PermissionDenied',403,'PERMISSION_DENIED'),PalantirRPCException),'missing':(error('ResourceNotFound',404,'NOT_FOUND'),errors.ResourceNotFound),'timeout':(httpx.ReadTimeout('read unavailable'),TimeoutError)}[fault]
            execute('read '+fault+' after='+str(after),([payload('DIRECTLY_TRASHED'),httpx.Response(204)] if after else [])+[response],exception=exc)
    for name,status,code in [('ResourceNotFound',404,'NOT_FOUND'),('RestoreResourcePermissionDenied',403,'PERMISSION_DENIED')]:
        execute('restore stops '+name,[payload('DIRECTLY_TRASHED'),error(name,status,code)],exception=getattr(errors,name))
    runpy.run_path(str(example),run_name='__main__')
    os.chdir(ROOT)
    import pytest
    pytest_code=pytest.main(['-q','-p','no:cacheprovider','tests/test_offline_rest_073_restore.py','tests/test_offline_rest_catalog_restore.py','--basetemp='+str(TMP/'feature015_rest073restore_recover_pytest_20261116')])
    assert pytest_code==0
assert not attempts
assert all(sha(Path(p))==h for p,h in bindings.items())
prior=TMP/'feature015_rest073_restore_semantic_review_20261029.json'
assert json.loads(prior.read_text())['operations'][0]['verdict']=='FAIL'
report=dict(story='DEV-STORY-073',development='DEV-068',core_development='DEV-064',reviewer='/root/restore_last_qa_recover_20261116',candidate_sha=manifest['base_sha'],manifest_sha256=sha(MANIFEST),sdk_version='1.101.0',source_commit=manifest['source_commit'],operations=[dict(id='v2.filesystem.Resource.restore',verdict='PASS',runtime_contract_verdict='PASS',server_policy_verdict='UNCERTAIN',acceptance_assessment=dict(decision_and_prerequisites='PASS: exact identity, enrollment, owner-confirmed RID/parent/path and three TrashStatus states are explicit',expected_result_and_validation='PASS: None is separated from observed exact-RID state; ancestor state requires separate authorized reads',reconciliation='PASS: one write and at most two reads, bounded retries/timeouts, denial/missing/conflict stops, no blind replay',source_difference='PASS: original SDK purpose retained and paired with ResourceNotDirectlyTrashed; policy remains unverified',local_models_errors_modes='PASS: complete reachable definition closure checked against installed frozen SDK, wrappers and cleanup locally described'),source_conflict=dict(disposition='Explained bounded uncertainty; no server no-op or idempotency guarantee asserted',source_method_sha256=manifest['restore_method_sha256'],server_policy='UNCERTAIN',waiver=False))],raw_proof=proof,model_closure=dict(documents=len(models),unresolved=[],exact_source_checks=model_source_checks),local_links=links,bindings_before=bindings,bindings_after={p:sha(Path(p)) for p in bindings},all_bindings_unchanged=True,network=dict(native_DNS_connect_connect_ex_denied=True,attempts=0,live_calls=0),tests=dict(exit_code=int(pytest_code),passed=33),generator_evidence=dict(proofs=manifest['proofs'],patch_only_delta=manifest['regeneration']['baseline_to_patch_delta'],preexisting_drift=manifest['regeneration']['preexisting_full_tree_drift'],whole_tree_canonical_claim=False,review='Generator regression independently rerun; full-render and baseline comparison evidence hash-verified and reviewed'),prior_failure=dict(path=str(prior),sha256=sha(prior),preserved=True),boundaries=dict(formal_QA='pending',review_register_promotion=False,tracker_writes=0,author_changes=0,commits=0,pushes=0,live_claim=False))
OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(report=str(OUT),sha256=sha(OUT),verdict='PASS',cases=len(proof),model_documents=len(models))))
