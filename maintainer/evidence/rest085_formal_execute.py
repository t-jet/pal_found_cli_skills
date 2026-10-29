"""Independent F085 formal execution, using real pinned SDK and denied sockets."""
import asyncio
import hashlib
import importlib.util
import inspect
import json
import runpy
import socket
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import httpx
import pydantic
from foundry_sdk import PalantirRPCException
from foundry_sdk.v2.functions.execution import ExecutionClient
from foundry_sdk.v2.functions.query import QueryClient, AsyncQueryClient
from foundry_sdk.v2.functions.value_type import ValueTypeClient
from foundry_sdk.v2.functions.version_id import VersionIdClient

TMP = Path(__file__).resolve().parent
ROOT = TMP / 'feature015_integration'
SKILL = ROOT / '.agents/skills/pal-found-dev'
sys.path.insert(0, str(SKILL / 'examples/rest/common'))
sys.path.insert(0, str(SKILL / 'examples/rest/085/v2/functions/Query'))
from mock_transport import mock_resource, mock_async_resource
from sse_fixture import TrackingStream, framed, consume_sse

RID = 'ri.functions.main.function.00000000-0000-0000-0000-000000000001'
VT = 'ri.functions.main.value-type.00000000-0000-0000-0000-000000000002'
VID = '00000000-0000-0000-0000-000000000003'
NAME = 'scale'
QUERY = {'apiName': NAME, 'parameters': {}, 'output': {'type':'integer'}, 'rid': RID, 'version':'1.0.0'}
VALUE = {'rid': VT, 'version':'1.0.0','versionId':VID,'apiName':'ScaleValue','displayName':'Scale','constraints':[{'type':'struct','fields':{}}]}
DATA = {'type':'data','value':[6]}
ERROR = {'type':'error','errorCode':'INVALID_ARGUMENT','errorName':'QueryRuntimeError','errorInstanceId':VID,'errorDescription':'fixture failure','parameters':{}}
SPECS = [
 ('Execution','cancel',ExecutionClient, {'execution_id':'submitted-1'}, 'POST','/executions/submitted-1/cancel',None,{'id':'submitted-1'}),
 ('Execution','get_result',ExecutionClient, {'execution_id':'submitted-1','timeout':0}, 'POST','/executions/submitted-1/getResult',{'timeout':0},{'type':'running'}),
 ('Query','execute',QueryClient, {'query_api_name':NAME,'parameters':{'amount':2,'factor':3},'version':'1.0.0','branch':'master'}, 'POST','/queries/scale/execute',{'parameters':{'amount':2,'factor':3},'version':'1.0.0','branch':'master'},{'value':6}),
 ('Query','execute_async',QueryClient, {'query_api_name':NAME,'parameters':{'amount':2},'version':'1.0.0','branch':'master','ontology':'sample-ontology','transaction_id':'tx-1'}, 'POST','/queries/scale/executeAsync',{'parameters':{'amount':2},'version':'1.0.0','branch':'master','ontology':'sample-ontology'},{'type':'submitted','executionId':'submitted-1'}),
 ('Query','get',QueryClient, {'query_api_name':NAME,'version':'1.0.0'},'GET','/queries/scale',None,QUERY),
 ('Query','get_by_rid',QueryClient, {'rid':RID,'include_prerelease':True,'version':'1.0.0'},'GET','/queries/getByRid',None,QUERY),
 ('Query','get_by_rid_batch',QueryClient, {'body':[{'rid':RID,'includePrerelease':True,'version':'1.0.0'}]},'POST','/queries/getByRidBatch',[{'rid':RID,'includePrerelease':True,'version':'1.0.0'}],{'data':[QUERY]}),
 ('Query','streaming_execute',QueryClient, {'query_api_name':NAME,'parameters':{'amount':2},'version':'1.0.0','branch':'master','ontology':'sample-ontology','transaction_id':'tx-1'},'POST','/queries/scale/streamingExecute',{'parameters':{'amount':2},'version':'1.0.0','branch':'master','ontology':'sample-ontology'},None),
 ('Query','streaming_execute_events',QueryClient, {'query_api_name':NAME,'parameters':{'amount':2}},'POST','/queries/scale/streamingExecuteEvents',{'parameters':{'amount':2}},None),
 ('ValueType','get',ValueTypeClient, {'value_type_rid':VT},'GET','/valueTypes/'+VT,None,VALUE),
 ('VersionId','get',VersionIdClient, {'value_type_rid':VT,'version_id_version_id':VID},'GET','/valueTypes/'+VT+'/versionIds/'+VID,None,VALUE),
]
RESULTS=[]
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def log(case, check, detail):
    row={'case_id':case,'check':check,'result':'PASS','detail':detail,'at':datetime.now(timezone.utc).isoformat()}
    RESULTS.append(row)
    print(json.dumps(row),flush=True)
def denied(*args,**kwargs): raise AssertionError('PUBLIC_SOCKET_DENIED')
def invoke(client, method, kwargs):
    return getattr(client,method)(**kwargs,preview=True,request_timeout=5)
def consume(result, method):
    if method.startswith('streaming_'):
        assert type(result).__name__=='SseContextManager'
        with result as stream: return [event.data.model_dump(mode='json',by_alias=True,exclude_none=True) for event in stream.iter_sse()]
    return result.model_dump(mode='json',by_alias=True,exclude_none=True)

def execute():
    for i,(resource,method,cls,kwargs,http,path,body,reply) in enumerate(SPECS,1):
        case=f'F085-{i:02}'
        calls=[]
        def check(req):
            calls.append(req)
            assert req.method==http and req.url.path=='/api/v2/functions'+path
            expected={'preview':'true'}
            if kwargs.get('transaction_id'):expected['transactionId']=kwargs['transaction_id']
            if method in ('get','get_by_rid') and resource=='Query':expected['version']='1.0.0'
            if method=='get_by_rid':expected.update(rid=RID,includePrerelease='true')
            assert dict(req.url.params)==expected
            assert req.headers['Authorization']=='Bearer offline-fixture-token'
            if body is not None: assert json.loads(req.content)==body
            if method.startswith('streaming_'): assert req.headers['Accept']=='text/event-stream'
        def handler(req):
            check(req)
            if reply is None:return httpx.Response(200,headers={'content-type':'text/event-stream'},content=framed(DATA,ERROR))
            return httpx.Response(200,json=reply)
        with mock_resource(cls,handler) as client:
            result=consume(invoke(client,method,kwargs),method)
            assert result==([DATA,ERROR] if reply is None else reply)
            if method=='cancel': assert consume(invoke(client,method,kwargs),method)==reply
        assert len(calls)==(2 if method=='cancel' else 1)
        log(case,'selectors_success','explicit preview, exact HTTP/path/body/query, typed result; cancel repeated' if method=='cancel' else 'explicit preview, exact HTTP/path/body/query and typed result')
        for status in (401,403):
            with mock_resource(cls,lambda r:httpx.Response(status,json={'errorName':'FormalPermissionDenied','errorCode':'PERMISSION_DENIED','errorInstanceId':VID,'parameters':{}})) as client:
                try:consume(invoke(client,method,kwargs),method)
                except PalantirRPCException as e:assert e.name=='FormalPermissionDenied'
                else:raise AssertionError('denial swallowed')
            log(case,f'http_{status}','service denial propagated')
        def timeout(req):raise httpx.ReadTimeout('formal fixture timeout',request=req)
        with mock_resource(cls,timeout) as client:
            try:consume(invoke(client,method,kwargs),method)
            except Exception as e:assert 'timeout' in str(e).lower() or 'timeout' in type(e).__name__.lower(),repr(e)
            else:raise AssertionError('timeout swallowed')
        log(case,'timeout','transport timeout surfaced; no inferred replay/business-effect guarantee')
        with mock_resource(cls,lambda r: (_ for _ in ()).throw(AssertionError('missing input reached HTTP'))) as client:
            try:getattr(client,method)(preview=True)
            except pydantic.ValidationError:pass
            else:raise AssertionError('missing required input accepted')
        log(case,'missing_required','local ValidationError before HTTP')
        def malformed(req):
            if reply is None:return httpx.Response(200,headers={'content-type':'text/event-stream'},content=b'data: {not-json}\n\n')
            return httpx.Response(200,content=b'{not-json',headers={'content-type':'application/json'})
        with mock_resource(cls,malformed) as client:
            try:consume(invoke(client,method,kwargs),method)
            except Exception as e:assert 'PUBLIC_SOCKET' not in str(e)
            else:raise AssertionError('malformed result accepted')
        log(case,'malformed','invalid JSON or SSE payload rejected')
        fixture=SKILL/f'examples/rest/085/v2/functions/{resource}/invoke_{method}.py'
        runpy.run_path(str(fixture),run_name='__main__')
        log(case,'reader_example','actual SDK request/result/named-source-errors passed under socket trap')
    for size in (1,100):
        requests=[]
        def batch(req):
            requests.append(req); assert len(json.loads(req.content))==size
            return httpx.Response(200,json={'data':[]})
        with mock_resource(QueryClient,batch) as c:assert c.get_by_rid_batch([{'rid':RID}]*size,preview=True).data==[]
        assert len(requests)==1
        log('F085-07',f'batch_{size}','valid boundary serialized; omitted records accepted without absence conclusion')
    for size in (0,101):
        with mock_resource(QueryClient,denied) as c:
            try:c.get_by_rid_batch([{'rid':RID}]*size,preview=True)
            except pydantic.ValidationError:pass
            else:raise AssertionError('batch bound accepted')
        log('F085-07',f'batch_{size}','local length validation, no request')
    for timeout_value in (None,280):
        def poll(req):
            assert json.loads(req.content)==({} if timeout_value is None else {'timeout':280})
            return httpx.Response(200,json={'type':'succeeded','value':6})
        with mock_resource(ExecutionClient,poll) as c:
            args={} if timeout_value is None else {'timeout':280}
            assert c.get_result('submitted-1',preview=True,request_timeout=300,**args).value==6
        log('F085-02',f'poll_{timeout_value}','exact timeout body and succeeded variant decoded')
    with mock_resource(QueryClient,lambda r:httpx.Response(200,json={'type':'completed','value':6})) as c: assert c.execute_async(NAME,parameters={},preview=True).value==6
    log('F085-04','completed','immediate completed variant needs no polling')
    with mock_resource(QueryClient,lambda r:httpx.Response(200,json=QUERY)) as c:
        assert c.get_by_rid(rid=RID,include_prerelease=True,preview=True).rid==RID
    log('F085-06','omitted_version','includePrerelease selector accepted with version omitted; fixture cannot prove live resolution')
    import sse_fixture
    for case,method in [('F085-08','streaming_execute'),('F085-09','streaming_execute_events')]:
        sse_fixture.verify(method,'StreamingExecuteEventsQueryPermissionDenied' if method.endswith('events') else 'StreamingExecuteQueryPermissionDenied')
        log(case,'finite_sse','data,partial error,event/decoded-byte/deadline budgets and closed transport')
        async def async_check():
            class AsyncTrackingStream(httpx.AsyncByteStream):
                closed=False
                async def __aiter__(self):yield framed(DATA)
                async def aclose(self):self.closed=True
            transport_stream=AsyncTrackingStream()
            def response_handler(req):
                assert dict(req.url.params)=={'preview':'true'}
                assert req.url.path=='/api/v2/functions/queries/scale/'+('streamingExecuteEvents' if method.endswith('events') else 'streamingExecute')
                return httpx.Response(200,headers={'content-type':'text/event-stream'},stream=transport_stream)
            async with mock_async_resource(AsyncQueryClient,response_handler) as c:
                wrapper=getattr(c,method)(NAME,parameters={},preview=True,request_timeout=5)
                assert type(wrapper).__name__=='AsyncSseContextManager'
                async with wrapper as response:
                    values=[event.data.value async for event in response.aiter_sse()]
                    assert values==[[6]]
                assert transport_stream.closed
        EVENT_LOOP.run_until_complete(async_check())
        log(case,'async_sse','AsyncSseContextManager, typed data and async context closure')
    for name in ('global_query.py','async_execution.py'):
        runpy.run_path(str(SKILL/'examples/rest/085'/name),run_name='__main__')
        log('F085-03' if name.startswith('global') else 'F085-04','worked_example',name+' ran real SDK fixtures')

if __name__=='__main__':
    start=datetime.now(timezone.utc).isoformat()
    # Windows creates an internal loopback wakeup socket while constructing a loop.
    # Construct before denying all subsequent socket connections, including loopback.
    EVENT_LOOP=asyncio.new_event_loop()
    with patch('socket.socket.connect',denied),patch('socket.create_connection',denied),patch('socket.getaddrinfo',denied):
        try:socket.create_connection(('www.palantir.com',443))
        except AssertionError as e:assert str(e)=='PUBLIC_SOCKET_DENIED'
        else:raise AssertionError('socket trap inactive')
        execute()
    EVENT_LOOP.close()
    data=json.loads((ROOT/'maintainer/rest-domain-independent-review-085.json').read_text())
    for op in data['operations']:
        for key in ('contract','behavior','example','helper'):
            if op.get(key):assert digest(SKILL/op[key])==op[key+'_sha256']
        spec=importlib.util.find_spec(op['source_module']);assert digest(Path(spec.origin))==op['source_sha256']
        op.update(independent_qa_agent='/root/formal085_finish/case085_approve_execute',testcase='TESTCASE-082',testexec='TESTEXEC-082',formal_case=f"F085-{data['operations'].index(op)+1:02}")
        resource,method=op['id'].split('.')[-2:]
        reader=f'examples/rest/085/v2/functions/{resource}/invoke_{method}.py'
        op.update(reader_example=reader,reader_example_sha256=digest(SKILL/reader))
    evidence={'story':'DEV-STORY-085','candidate_commit':'3e7146b0b1fba03538de3b24164294612ab2f7c3','source_sdk':'1.101.0','source_commit':data['source_commit'],'reviewer_agent':'/root/formal085_finish/case085_approve_execute','testcase':'TESTCASE-082','testexec':'TESTEXEC-082','verdict':'PASS','started_at':start,'finished_at':datetime.now(timezone.utc).isoformat(),'public_network':'denied sockets plus verified denial probe','tenant_verification':False,'operations':data['operations'],'checks':RESULTS,'harness_sha256':digest(Path(__file__))}
    (TMP/'feature015_rest085_formal_qa.json').write_text(json.dumps(evidence,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(RESULTS)} independent checks; 11/11 formal cases; all current source/asset hashes matched',flush=True)
