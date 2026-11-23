"""Independent REST077 QA harness. Author checks are never formal QA execution."""
import ast
import runpy
import sys
sys.dont_write_bytecode=True
import time
import argparse
import asyncio
import copy
import hashlib
import importlib
import importlib.metadata
import inspect
import json
import re
import socket
from contextlib import contextmanager, asynccontextmanager
from pathlib import Path
from unittest.mock import patch
from urllib.parse import unquote

import httpx
import pydantic
from foundry_sdk import Config, UserTokenAuth, PalantirRPCException
from foundry_sdk._errors import SDKInternalError
from foundry_sdk._errors.timeout_error import ReadTimeout

HERE=Path(__file__).resolve().parent
CASES=HERE/'rest077_formal_cases.json'
FREEZE=HERE/'rest077_assets_freeze.json'
AUTHOR='/root/rest077_case_correct_20261116'
TOKEN='qa-rest077-independent'
ROWS=[]
def evidence_json(value):
    if isinstance(value,bytes): return {'$bytes':value.decode()}
    raise TypeError(type(value).__name__)

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def materialize(v):
    if isinstance(v,dict):
        if set(v)=={'$bytes'}: return v['$bytes'].encode()
        return {k:materialize(x) for k,x in v.items()}
    if isinstance(v,list): return [materialize(x) for x in v]
    return v
def normalize(v):
    if isinstance(v,pydantic.BaseModel): return v.model_dump(by_alias=True,exclude_unset=True)
    return v
def record(c,check,**details): ROWS.append(dict(case_id=c['case_id'] if isinstance(c,dict) else c,check=check,result='PASS',**details))
def denied(*args,**kwargs): raise AssertionError('PUBLIC_SOCKET_DENIED')
def client_class(c,asynchronous=False):
    _,_,resource,_=c['operation'].split('.')
    return getattr(importlib.import_module(c['source']['module']),('Async' if asynchronous else '')+resource+'Client')
@contextmanager
def sync_client(c,handler):
    with httpx.Client(transport=httpx.MockTransport(handler),timeout=7) as transport:
        with patch('foundry_sdk._core.api_client.HttpClient',return_value=transport):
            client=client_class(c)(auth=UserTokenAuth(token=TOKEN),hostname='rest077.invalid',config=Config(timeout=7,max_retries=0))
        yield client,transport
    assert transport.is_closed
@asynccontextmanager
async def async_client(c,handler):
    async with httpx.AsyncClient(transport=httpx.MockTransport(handler),timeout=7) as transport:
        with patch('foundry_sdk._core.api_client.AsyncHttpClient',return_value=transport):
            client=client_class(c,True)(auth=UserTokenAuth(token=TOKEN),hostname='rest077.invalid',config=Config(timeout=7,max_retries=0))
        yield client,transport
    assert transport.is_closed
def invoke(client,c,mode='ordinary',kwargs=None):
    target=getattr(client,{'raw':'with_raw_response','streaming':'with_streaming_response'}[mode]) if mode!='ordinary' else client
    return getattr(target,c['operation'].split('.')[-1])(**materialize(copy.deepcopy(kwargs or c['kwargs'])),request_timeout=7)
def wire_check(request,c,token=None):
    exp=c['wire']; assert request.method==exp['method']
    assert unquote(request.url.path)=='/api'+exp['path'],str(request.url)
    q=copy.deepcopy(exp['query'])
    if token is not None and c['operation'].split('.')[-1]!='search': q['pageToken']=token
    pairs=[]
    for k,v in q.items():
        for value in v if isinstance(v,list) else [v]: pairs.append((k,str(value)))
    assert sorted(request.url.params.multi_items())==sorted(pairs),(request.url,q)
    assert request.headers['authorization']=='Bearer '+TOKEN
    for k,v in exp['headers'].items(): assert request.headers[k]==v,(k,request.headers)
    body=materialize(copy.deepcopy(exp['body']))
    if token is not None and c['operation'].split('.')[-1]=='search': body['pageToken']=token
    got=request.content if isinstance(body,bytes) else (json.loads(request.content) if request.content else None)
    assert got==body,(got,body)
    assert request.extensions['timeout']==dict(connect=7,read=7,write=7,pool=7)
def reply(payload):
    binary=isinstance(materialize(payload),bytes)
    content=materialize(payload) if binary else json.dumps(payload).encode()
    return httpx.Response(200,stream=httpx.ByteStream(content),headers={'Content-Type':'application/octet-stream' if binary else 'application/json'})
def expected(c,ordinary=False):
    result=materialize(c['response'])
    if ordinary and 'ITERATOR' in c['source']['methods'][c['operation'].split('.')[2]+'Client']['request']['response_mode']:
        return result['data']
    return result
def assert_runtime(c,value,element=False):
    binding=c['runtime_types']['element' if element else 'response']
    cls=bytes if binding=='builtins.bytes' else getattr(importlib.import_module(binding.rsplit('.',1)[0]),binding.rsplit('.',1)[1])
    assert type(value) is cls, (c['operation'], 'runtime type',type(value),cls)
    return value

def typed_normalize(c,value,element=False):
    return normalize(assert_runtime(c,value,element))

def semantic(c,value):
    resource,method=c['operation'].split('.')[-2:]
    if resource=='OntologyObject':
        if method=='aggregate':
            assert value['data'][0]['group']=={}
            assert value['data'][0]['metrics']==[{'name':'flightCount','value':1.0}]
            return
        rows=value if isinstance(value,list) else value.get('data',[value])
        linked='linked' in method
        for item in rows:
            props=item['properties']
            if linked:
                assert props['airportId']=='SOF' and 'flightId' not in props
                assert item['rid']!='ri.qa.main.object.flight077'
            else:
                assert props['flightId']=='QA-077' and props['status']=='scheduled'
                if method=='search': assert props['status']==c['kwargs']['query']['value']
    elif resource=='Attachment' and method!='read':
        assert value['filename']=='flight-qa.txt' and value['sizeBytes']==19 and value['rid']=='ri.qa.main.attachment.flight077'
        assert value['mediaType']=='text/plain'
    elif resource=='Action' and method=='validate':
        assert value['result']=='VALID' and all(x['result']=='VALID' for x in value['parameters'].values())
    elif resource=='Query': assert value['value']==1 and isinstance(value['value'],int)

def sync_modes(c):
    for mode in ['ordinary','raw','streaming']:
        calls=[]; responses=[]
        def handler(req):
            calls.append(req); wire_check(req,c); r=reply(c['response']); responses.append(r); return r
        with sync_client(c,handler) as (client,_):
            result=invoke(client,c,mode)
            if mode=='raw':
                try: assert result.status_code==200; value=typed_normalize(c,result.decode())
                finally: result.close()
            elif mode=='streaming':
                with result as stream:
                    assert not responses[0].is_closed
                    wire=b''.join(stream.iter_bytes())
                    value=wire if isinstance(materialize(c['response']),bytes) else json.loads(wire)
            elif 'ITERATOR' in c['source']['methods'][c['operation'].split('.')[2]+'Client']['request']['response_mode']:
                value=[typed_normalize(c,v,True) for v in result]
            else: value=typed_normalize(c,result)
            assert value==expected(c,mode=='ordinary'),(c['operation'],mode,value,expected(c,mode=='ordinary'))
            semantic(c,value)
        assert len(calls)==1 and all(r.is_closed for r in responses)
        record(c,'sync_'+mode,requests=1)

async def async_modes(c):
    for mode in ['ordinary','raw','streaming']:
        calls=[];responses=[]
        def handler(req):
            calls.append(req);wire_check(req,c);r=reply(c['response']);responses.append(r);return r
        async with async_client(c,handler) as (client,_):
            result=invoke(client,c,mode)
            if mode=='streaming':
                assert not inspect.isawaitable(result)
                async with result as stream:
                    assert not responses[0].is_closed
                    wire=b''.join([b async for b in stream.aiter_bytes()])
                    value=wire if isinstance(materialize(c['response']),bytes) else json.loads(wire)
            elif mode=='raw':
                result=await result
                try: assert result.status_code==200;value=typed_normalize(c,result.decode())
                finally: await result.aclose()
            elif hasattr(result,'__aiter__'):
                assert not inspect.isawaitable(result)
                value=[typed_normalize(c,v,True) async for v in result]
            else: value=typed_normalize(c,await result)
            assert value==expected(c,mode=='ordinary'),(c['operation'],mode,value)
            semantic(c,value)
        assert len(calls)==1 and all(r.is_closed for r in responses)
        record(c,'async_'+mode,requests=1)

def sync_adverse(c):
    for failure in ['generic_403','timeout']:
        calls=[];responses=[]
        def handler(req):
            calls.append(req);wire_check(req,c)
            if failure=='timeout': raise httpx.ReadTimeout('qa077 timeout',request=req)
            r=httpx.Response(403,json={'errorCode':'PERMISSION_DENIED','errorName':'IndependentDenied','errorInstanceId':'qa077-denied','parameters':{'operation':c['operation']}});responses.append(r);return r
        with sync_client(c,handler) as (client,_):
            try:
                value=invoke(client,c)
                if hasattr(value,'__iter__') and not isinstance(value,(dict,bytes,pydantic.BaseModel)): list(value)
            except PalantirRPCException as exc:
                assert failure=='generic_403';assert exc.name=='IndependentDenied';assert exc.error_instance_id=='qa077-denied'
            except ReadTimeout as exc:
                assert failure=='timeout' and isinstance(exc.__cause__,httpx.ReadTimeout),(type(exc),exc.__cause__)
            else: raise AssertionError('Expected failure '+failure)
        assert len(calls)==1 and all(r.is_closed for r in responses)
        record(c,failure,requests=1,automatic_retries=0)
    calls=[]
    with sync_client(c,lambda req:calls.append(req)) as (client,_):
        try: getattr(client,c['operation'].split('.')[-1])(**materialize(c['kwargs']),request_timeout=0)
        except pydantic.ValidationError: pass
        else: raise AssertionError('Zero timeout accepted')
    assert calls==[];record(c,'invalid_timeout_no_http')
    responses=[]
    def handler(req): r=reply(c['response']);responses.append(r);return r
    with sync_client(c,handler) as (client,_):
        try:
            with invoke(client,c,'streaming'):
                assert not responses[0].is_closed
                raise ValueError('consumer aborted')
        except ValueError: pass
    assert responses[0].is_closed;record(c,'stream_exception_cleanup')

async def async_adverse(c):
    for failure in ['generic_403','timeout']:
        calls=[];responses=[]
        def handler(req):
            calls.append(req);wire_check(req,c)
            if failure=='timeout': raise httpx.ReadTimeout('qa077 async timeout',request=req)
            response=httpx.Response(403,json={'errorCode':'PERMISSION_DENIED','errorName':'IndependentDenied','errorInstanceId':'qa077-denied','parameters':{}})
            responses.append(response);return response
        async with async_client(c,handler) as (client,_):
            try:
                value=invoke(client,c)
                if hasattr(value,'__aiter__'): value=[v async for v in value]
                else: await value
            except PalantirRPCException as exc: assert failure=='generic_403' and exc.name=='IndependentDenied'
            except ReadTimeout as exc: assert failure=='timeout' and isinstance(exc.__cause__,httpx.ReadTimeout)
            else: raise AssertionError('Expected async failure')
        assert len(calls)==1 and all(r.is_closed for r in responses);record(c,'async_'+failure,requests=1,response_closed=True)
    calls=[]
    async with async_client(c,lambda req:calls.append(req)) as (client,_):
        try:
            value=getattr(client,c['operation'].split('.')[-1])(**materialize(c['kwargs']),request_timeout=0)
            if hasattr(value,'__aiter__'): value=[v async for v in value]
            else: await value
        except pydantic.ValidationError: pass
        else: raise AssertionError('Async zero timeout accepted')
    assert calls==[];record(c,'async_invalid_timeout_no_http')
    responses=[];entered=asyncio.Event()
    def handler(req): r=reply(c['response']);responses.append(r);return r
    async with async_client(c,handler) as (client,_):
        async def consumer():
            async with invoke(client,c,'streaming'):
                assert not responses[0].is_closed
                entered.set();await asyncio.Event().wait()
        task=asyncio.create_task(consumer());await asyncio.wait_for(entered.wait(),1)
        task.cancel()
        try: await task
        except asyncio.CancelledError: pass
        else: raise AssertionError('Cancellation suppressed')
    assert responses[0].is_closed;record(c,'async_cancellation_cleanup')

def page_payload(c,index,next_token):
    page=copy.deepcopy(c['response'])
    item=page['data'][0]
    if index==1:
        if 'rid' in item: item['rid']=item['rid']+'-second'
        if 'apiName' in item: item['apiName']=item['apiName']+'Second'
        if c['operation'].split('.')[2]=='OntologyObject':
            key='airportId' if 'airportId' in item['properties'] else 'flightId';item['properties'][key]+='-second'
    if next_token: page['nextPageToken']=next_token
    else: page.pop('nextPageToken',None)
    if 'totalCount' in page: page['totalCount']=2
    return page
def finite_pages(c,repeat=False,limit=3):
    calls=[]; tokens=[];rows=[];status='complete'
    def handler(req):
        index=len(calls);assert index<2,'Unbounded pager'
        wire_check(req,c,'qa077-next' if index else None);calls.append(req)
        return reply(page_payload(c,index,'qa077-next' if index==0 or repeat else None))
    with sync_client(c,handler) as (client,_):
        for page_no in range(limit):
            kwargs=copy.deepcopy(c['kwargs'])
            if tokens: kwargs['page_token']=tokens[-1]
            response=invoke(client,c,'raw',kwargs)
            try: page=normalize(response.decode())
            finally: response.close()
            rows.extend(page['data']); nxt=page.get('nextPageToken')
            if not nxt: break
            if nxt in tokens: status='repeated-token';break
            tokens.append(nxt)
        else: status='page-limit'
    assert len(calls)==(1 if limit==1 else 2)
    assert len(rows)==len(calls)
    assert status==('page-limit' if limit==1 else 'repeated-token' if repeat else 'complete')
    if status=='complete': assert rows[0]!=rows[1]
    record(c,'finite_pages_'+status,pages=len(calls),retained_items=len(rows),retained_rows=rows,continuation=tokens[-1] if tokens else None)
async def async_pager(c):
    if 'ITERATOR' not in c['source']['methods'][c['operation'].split('.')[2]+'Client']['request']['response_mode']: return
    calls=[]
    def handler(req):
        i=len(calls);assert i<2;wire_check(req,c,'qa077-next' if i else None);calls.append(req);return reply(page_payload(c,i,'qa077-next' if i==0 else None))
    async with async_client(c,handler) as (client,_):
        result=invoke(client,c);rows=[]
        async for item in result:
            rows.append(normalize(item))
            assert len(rows)<=2
    assert len(rows)==len(calls)==2 and rows[0]!=rows[1];record(c,'async_iterator_two_pages')
def sync_pager(c):
    if 'ITERATOR' not in c['source']['methods'][c['operation'].split('.')[2]+'Client']['request']['response_mode']: return
    for early in [False,True]:
        calls=[]
        def handler(req):
            i=len(calls);assert i<2;wire_check(req,c,'qa077-next' if i else None);calls.append(req);return reply(page_payload(c,i,'qa077-next' if i==0 else None))
        with sync_client(c,handler) as (client,_):
            iterator=invoke(client,c)
            if early: rows=[normalize(next(iterator))]
            else: rows=[normalize(v) for v in iterator]
        assert len(rows)==len(calls)==(1 if early else 2)
        record(c,'iterator_early_stop' if early else 'iterator_two_pages')

def semantic_boundaries(data):
    lookup={c['operation']:c for c in data['operations']}
    validate=lookup['v1.ontologies.Action.validate'];apply=lookup['v1.ontologies.Action.apply'];calls=[]
    def handler(req): calls.append(req);return reply(data['invalid_action_result'])
    with sync_client(validate,handler) as (client,_):
        result=normalize(invoke(client,validate));assert result['result']=='INVALID'
        can_apply=result['result']=='VALID' and all(x['result']=='VALID' for x in result['submissionCriteria'])
        if can_apply: invoke(client,apply)
    assert len(calls)==1 and calls[0].url.path.endswith('/validate');record('F077-LIFECYCLE','invalid_validation_zero_mutation')
    schema=data['semantic_schema']['Flight']
    good=copy.deepcopy(lookup['v1.ontologies.OntologyObject.get']['response'])
    bad=copy.deepcopy(good);bad['properties']['flightId']=77
    def schema_contract(guard):
        assert guard(good,schema)['decision']=='use'
        rejected=guard(bad,schema)
        assert rejected['decision']=='stop' and rejected['retained']==bad
    schema_contract(schema_guard)
    expect_guard_failure(lambda: schema_contract(lambda value,schema: {'decision':'use','retained':value}))
    approved={'confirmedLabel':str}
    valid={'group':{'confirmedLabel':'2026-10-01'},'metrics':[{'name':'flightCount','value':1.0}]}
    unknown={'group':{'unconfirmed-server-label':{'raw':7}},'metrics':valid['metrics']}
    malformed={'group':{'confirmedLabel':{'raw':7}},'metrics':valid['metrics']}
    mixed=copy.deepcopy(data['aggregation_guard_cases']['mixed_confirmed_unknown'])
    def group_contract(guard):
        assert guard(valid,approved)['decision']=='use'
        for value in [unknown,malformed,mixed]:
            decision=guard(value,approved)
            assert decision['decision']=='stop' and decision['retained']==value and decision['derived'] is None
    group_contract(group_guard)
    def presence_only_mutant(bucket,confirmed):
        valid=all(label in bucket['group'] and type(bucket['group'][label]) is typ for label,typ in confirmed.items())
        return {'decision':'use' if valid else 'stop','retained':copy.deepcopy(bucket),'derived':bucket['metrics'][0]['value'] if valid else None}
    def mixed_contract(guard):
        result=guard(mixed,approved)
        assert result['decision']=='stop' and result['derived'] is None and result['retained']==mixed, 'Unconfirmed extra label permits unsafe derived computation'
    mixed_contract(group_guard)
    unsafe=presence_only_mutant(mixed,approved)
    assert unsafe['decision']=='use' and unsafe['derived']==1.0 and unsafe['retained']==mixed
    expect_guard_failure(lambda:mixed_contract(presence_only_mutant))
    record('F077-AGGREGATION','mixed_confirmed_unknown_label_and_presence_only_mutant',
           input=mixed,confirmed_mapping={'confirmedLabel':'builtins.str'},
           guarded=group_guard(mixed,approved),mutant=unsafe,mutant_detected=True,
           boundary='Local reader stops calculation; SDK/server group data remains opaque and retained')
    expect_guard_failure(lambda:group_contract(lambda value,schema:{'decision':'use','retained':value,'derived':7}))
    record('F077-SCHEMA','reader_metadata_guard_valid_reject_and_bypass_control')
    record('F077-AGGREGATION','confirmed_application_mapping_guard_and_bypass_control',server_group_values='opaque Any; no server policy invented')
    calls=[]
    def lifecycle_handler(req):
        calls.append(req)
        if req.url.path.endswith('/validate'): return reply(validate['response'])
        assert req.url.path.endswith('/apply')
        return httpx.Response(403,json={'errorCode':'PERMISSION_DENIED','errorName':'IndependentDenied','errorInstanceId':'qa077-denied','parameters':{}})
    with sync_client(validate,lifecycle_handler) as (client,_):
        value=normalize(invoke(client,validate));assert value['result']=='VALID'
        try: invoke(client,apply)
        except PalantirRPCException as exc: assert exc.name=='IndependentDenied'
        else: raise AssertionError('Validation incorrectly guarantees application')
    assert len(calls)==2;record('F077-LIFECYCLE','valid_validation_does_not_guarantee_apply')
    root=Path(json.loads(FREEZE.read_text())['skill_root'])
    policy={
        'Action':['eventually','immediately','20','notifications','uniqueness','user existence','uncertain'],
        'Attachment':['one hour','biweekly','*/*','application/octet-stream','does not prove','reconciliation'],
        'OntologyObject':['not snapshot','properties.','neither a response-label','timezone','label is absent'],
    }
    for resource,terms in policy.items():
        text=(root/f'references/rest/v1/ontologies/{resource}.md').read_text().lower()
        text=re.sub(r'\s+',' ',text)
        for term in terms: assert term in text,(resource,term)
        record('F077-POLICY',resource+'_documentation_only',executed_server_policy=False,source=data['policy_attribution'][resource])

def freeze_check(data,freeze):
    assert importlib.metadata.version('foundry-platform-sdk')=='1.101.0'
    for p,h in freeze['primary_sources'].items(): assert sha(p)==h,('primary source changed',p)
    root=Path(freeze['skill_root'])
    for p,h in freeze['assets'].items(): assert sha(root/p)==h,('reader asset changed',p)
    register=json.loads((root.parents[2]/'maintainer/rest-contract-register.json').read_text())
    for op,binding in freeze['register_bindings'].items():
        actual=next(x for x in register['operations'] if x['id']==op)
        assert {k:actual[k] for k in binding}==binding,('register source binding changed',op)
    assert len(data['operations'])==23 and sum(c['paged'] for c in data['operations'])==7
    assert all(not m['named_errors'] for c in data['operations'] for m in c['source']['methods'].values())
    record('F077-FREEZE','primary_and_reader_assets',assets=len(freeze['assets']),sources=len(freeze['primary_sources']))

def expect_guard_failure(check):
    try: check()
    except AssertionError: return
    raise AssertionError('Negative control failed to detect bypassed guard')

def schema_guard(value,schema):
    props=value.get('properties',{})
    valid=all(key in props and type(props[key]) is str for key in schema['primaryKey'])
    valid=valid and all(name not in props or definition['baseType']!='String' or type(props[name]) is str for name,definition in schema['properties'].items())
    return {'decision':'use' if valid else 'stop','retained':copy.deepcopy(value)}

def group_guard(bucket,confirmed):
    # Local reader decision only. SDK Dict[str, Any] still accepts opaque group data.
    retained=copy.deepcopy(bucket)
    if set(bucket['group'])-set(confirmed):
        return {'decision':'stop','retained':retained,'derived':None}
    valid=all(label in bucket['group'] and type(bucket['group'][label]) is typ for label,typ in confirmed.items())
    return {'decision':'use' if valid else 'stop','retained':retained,'derived':bucket['metrics'][0]['value'] if valid else None}

def uncertain_writes(data):
    lookup={c['operation']:c for c in data['operations']}
    for name in ['apply','apply_batch','upload']:
        c=lookup['v1.ontologies.'+('Attachment.' if name=='upload' else 'Action.')+name]
        calls=[];observations=[];server_effects=[]
        def lost_response(req):
            wire_check(req,c);calls.append(req)
            # Server accepted synthetic work before response was lost. Batch is partial.
            server_effects.append('QA-077')
            raise httpx.ReadTimeout('response lost after synthetic acceptance',request=req)
        state={'outcome':'unknown','request':copy.deepcopy(c['kwargs']),'partial':[], 'replay':False}
        with sync_client(c,lost_response) as (client,_):
            try: invoke(client,c)
            except ReadTimeout: pass
            else: raise AssertionError('Lost response must remain uncertain')
        if name=='upload':
            # Lost upload supplied no RID. This API has no lookup by upload attempt ID.
            state.update(decision='escalate-no-rid',reads=0)
        else:
            read=lookup['v1.ontologies.OntologyObject.get']
            # Independent authorized effect reads are observations, never proof of causality.
            keys=['QA-077','QA-078'] if name=='apply_batch' else ['QA-077']
            for key in keys:
                kwargs=copy.deepcopy(read['kwargs']);kwargs['primary_key']=key
                def observe(req):
                    assert req.method=='GET' and req.url.path.endswith('/'+key)
                    observations.append(req)
                    value=copy.deepcopy(read['response']);value['properties']['flightId']=key
                    value['properties']['status']='scheduled' if key in server_effects else 'pending'
                    return reply(value)
                with sync_client(read,observe) as (client,_):
                    item=normalize(invoke(client,read,kwargs=kwargs));state['partial'].append(item)
            state.update(decision='escalate-unresolved-causality',reads=len(observations))
            assert state['partial'][0]['properties']['status']=='scheduled'
            if name=='apply_batch': assert state['partial'][1]['properties']['status']=='pending'
        assert state['outcome']=='unknown' and state['replay'] is False
        assert len(calls)==1 and state['reads']<=2 and state['request']==c['kwargs']
        record(c,'lost_response_bounded_reconciliation_no_replay',state=state,synthetic_only=True)

async def extra_lifetimes(c):
    # Explicit checks complement six success modes. No synchronous cancellation claim.
    for asynchronous in [False,True]:
        for mode in ['raw','streaming']:
            responses=[]
            def handler(req):
                r=reply(c['response']);responses.append(r);return r
            if asynchronous:
                async with async_client(c,handler) as (client,transport):
                    try:
                        result=invoke(client,c,mode)
                        if mode=='raw':
                            raw=await result
                            try: assert_runtime(c,raw.decode());raise ValueError('consumer failed')
                            finally: await raw.aclose()
                        else:
                            async with result: raise ValueError('consumer failed')
                    except ValueError as exc: assert str(exc)=='consumer failed'
            else:
                with sync_client(c,handler) as (client,transport):
                    try:
                        raw=invoke(client,c,mode)
                        if mode=='raw':
                            try: assert_runtime(c,raw.decode());raise ValueError('consumer failed')
                            finally: raw.close()
                        else:
                            with raw: raise ValueError('consumer failed')
                    except ValueError as exc: assert str(exc)=='consumer failed'
            assert responses and all(r.is_closed for r in responses) and transport.is_closed
            record(c,('async_' if asynchronous else 'sync_')+mode+'_consumer_exception_cleanup')
    if c['operation'].endswith('Attachment.read'): return
    for asynchronous in [False,True]:
        responses=[]
        def broken(req):
            r=httpx.Response(200,stream=httpx.ByteStream(b'{invalid-json'),headers={'Content-Type':'application/json'});responses.append(r);return r
        failed=False
        if asynchronous:
            async with async_client(c,broken) as (client,transport):
                raw=await invoke(client,c,'raw')
                try: raw.decode()
                except Exception: failed=True
                finally: await raw.aclose()
        else:
            with sync_client(c,broken) as (client,transport):
                raw=invoke(client,c,'raw')
                try: raw.decode()
                except Exception: failed=True
                finally: raw.close()
        assert failed and responses[0].is_closed and transport.is_closed
        record(c,('async_' if asynchronous else 'sync_')+'raw_decode_failure_cleanup')

async def bounded_items(c):
    for asynchronous in [False,True]:
        calls=[];responses=[];rows=[];continuation=None
        def handler(req):
            assert not calls,'Item limit must prevent next request'
            wire_check(req,c);calls.append(req)
            payload=page_payload(c,0,'qa077-next')
            payload['data'].append(copy.deepcopy(payload['data'][0]))
            response=reply(payload);responses.append(response);return response
        if asynchronous:
            async with async_client(c,handler) as (client,transport):
                raw=await invoke(client,c,'raw')
                try: page=normalize(raw.decode())
                finally: await raw.aclose()
        else:
            with sync_client(c,handler) as (client,transport):
                raw=invoke(client,c,'raw')
                try: page=normalize(raw.decode())
                finally: raw.close()
        for item in page['data']:
            if len(rows)==1: break
            rows.append(item)
        continuation=page.get('nextPageToken')
        retained={'items':rows,'unconsumed':page['data'][len(rows):],'continuation':continuation,'status':'item-limit'}
        assert len(rows)==1 and len(retained['unconsumed'])==1 and continuation=='qa077-next'
        assert len(calls)==1 and responses[0].is_closed and transport.is_closed
        record(c,('async_' if asynchronous else 'sync_')+'explicit_item_bound_partial_retention',retained=retained)
    if c['runtime_types']['element'] is None: return
    calls=[];responses=[]
    def handler(req):
        assert not calls,'Async early stop fetched another page'
        calls.append(req);r=reply(page_payload(c,0,'qa077-next'));responses.append(r);return r
    async with async_client(c,handler) as (client,transport):
        iterator=invoke(client,c);rows=[]
        assert hasattr(iterator,'__aiter__') and not inspect.isawaitable(iterator)
        async for item in iterator:
            rows.append(typed_normalize(c,item,True));break
    assert len(calls)==len(rows)==1 and responses[0].is_closed and transport.is_closed
    record(c,'async_automatic_iterator_early_stop')

async def async_finite_pages(c,repeat=False,limit=3):
    calls=[];responses=[];tokens=[];rows=[];status='complete'
    def handler(req):
        index=len(calls);assert index<2,'Unbounded async pager'
        wire_check(req,c,'qa077-next' if index else None);calls.append(req)
        r=reply(page_payload(c,index,'qa077-next' if index==0 or repeat else None));responses.append(r);return r
    async with async_client(c,handler) as (client,transport):
        for page_no in range(limit):
            kwargs=copy.deepcopy(c['kwargs'])
            if tokens: kwargs['page_token']=tokens[-1]
            response=await invoke(client,c,'raw',kwargs)
            try: page=typed_normalize(c,response.decode())
            finally: await response.aclose()
            rows.extend(page['data']);nxt=page.get('nextPageToken')
            if not nxt: break
            if nxt in tokens: status='repeated-token';break
            tokens.append(nxt)
        else: status='page-limit'
    assert len(calls)==(1 if limit==1 else 2) and len(rows)==len(calls)
    assert status==('page-limit' if limit==1 else 'repeated-token' if repeat else 'complete')
    assert all(r.is_closed for r in responses) and transport.is_closed
    if status=='complete': assert rows[0]!=rows[1]
    record(c,'async_finite_pages_'+status,pages=len(calls),retained_rows=rows,continuation=tokens[-1] if tokens else None)

def corrupt_decoded(value):
    value=copy.deepcopy(value)
    if type(value) is bytes: return value+b'QA-corruption'
    if isinstance(value,dict):
        if not value: return {'QA_corruption':True}
        key=next(iter(value));value[key]=corrupt_decoded(value[key]);return value
    if isinstance(value,list):
        if not value: return ['QA-corruption']
        value[0]=corrupt_decoded(value[0]);return value
    if isinstance(value,str): return value+'QA-corruption'
    if isinstance(value,(int,float)): return value+1
    return 'QA-corruption'

def distributed_examples(data,freeze):
    root=Path(freeze['skill_root'])
    for c in data['operations']:
        resource,method=c['operation'].split('.')[-2:]
        path=root/f'examples/rest/077/v1/ontologies/{resource}/{method}.py'
        module=runpy.run_path(str(path),run_name='rest077_case_example')
        fn=module['invoke'];tree=ast.parse(inspect.getsource(fn))
        call=next(n for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr==method)
        assert isinstance(call.func.value,ast.Attribute) and call.func.value.attr=='with_raw_response'
        assert getattr(module[resource+'Client'],method)==getattr(client_class(c),method)
        kwargs={k.arg:ast.literal_eval(k.value) for k in call.keywords}
        assert kwargs.pop('request_timeout')==30
        baseline=[]
        def source_transport(req):
            baseline.append(req);return reply(c['response'])
        with sync_client(c,source_transport) as (client,_):
            raw=getattr(client.with_raw_response,method)(**kwargs,request_timeout=30)
            raw.close()
        assert len(baseline)==1
        source_request=baseline[0]
        actual_resource=module['mock_resource']
        @contextmanager
        def checked_resource(cls,handler):
            def independently_checked(req):
                assert req.method==source_request.method
                assert req.url.path==source_request.url.path
                assert req.url.params==source_request.url.params
                assert req.content==source_request.content
                for header in ['accept','content-type','content-length']:
                    assert req.headers.get(header)==source_request.headers.get(header)
                assert req.headers['authorization']=='Bearer offline-fixture-token'
                return handler(req)
            with actual_resource(cls,independently_checked) as client: yield client
        module['verify'].__globals__['mock_resource']=checked_resource
        # Invoke the unmodified distributed verify, but check runtime SDK identity before decode.
        original=fn;seen=[]
        class ObservedRaw:
            def __init__(self,raw,corrupt=False): self.raw=raw;self.corrupt=corrupt
            def decode(self):
                value=self.raw.decode();assert_runtime(c,value);seen.append(type(value).__name__)
                if self.corrupt: return corrupt_decoded(normalize(value))
                return value
            def close(self): self.raw.close()
        # Function globals returned by run_path are the shared execution dictionary.
        namespace=module['verify'].__globals__
        namespace['invoke']=lambda client:ObservedRaw(original(client))
        module['verify']()
        assert seen
        namespace['invoke']=lambda client:ObservedRaw(original(client),True)
        expect_guard_failure(module['verify'])
        record(c,'distributed_example_execute_and_corrupt_decode_control',asset=str(path.relative_to(root)),sha256=sha(path),runtime_types=seen,kwargs=kwargs)

async def run(data):
    for c in data['operations']:
        expect_guard_failure(lambda:assert_runtime(c,bytearray(b'wrong') if c['runtime_types']['response']=='builtins.bytes' else materialize(c['response'])))
        if c['runtime_types']['element']: expect_guard_failure(lambda:assert_runtime(c,c['response']['data'][0],True))
        record(c,'runtime_model_identity_negative_control')
        sync_modes(c);await async_modes(c);sync_adverse(c);await async_adverse(c);await extra_lifetimes(c)
        if c['paged']:
            finite_pages(c);finite_pages(c,repeat=True);finite_pages(c,limit=1);sync_pager(c);await async_pager(c);await bounded_items(c);await async_finite_pages(c);await async_finite_pages(c,repeat=True);await async_finite_pages(c,limit=1)
    semantic_boundaries(data);uncertain_writes(data);distributed_examples(data,json.loads(FREEZE.read_text()))
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--author-check',action='store_true');parser.add_argument('--executor-identity');parser.add_argument('--approval');parser.add_argument('--output',required=True)
    started=time.perf_counter();args=parser.parse_args();data=json.loads(CASES.read_text());freeze=json.loads(FREEZE.read_text())
    if not args.author_check:
        assert args.executor_identity and args.executor_identity!=AUTHOR,'Distinct executor required'
        approval=json.loads(Path(args.approval).read_text())
        assert approval['disposition']=='APPROVED' and approval['reviewer_identity'] not in [AUTHOR,args.executor_identity]
        assert approval['cases_sha256']==sha(CASES) and approval['harness_sha256']==sha(__file__)
        assert approval['feature_sha256']==sha(HERE/'rest077_formal_cases.feature') and approval['freeze_sha256']==sha(FREEZE)
        assert approval['testcase_closed'] is True and approval['testexec_prerequisites_verified'] is True
    freeze_check(data,freeze)
    try:
        with asyncio.Runner() as runner, patch.object(socket.socket,'connect',denied),patch.object(socket,'create_connection',denied),patch.object(socket,'getaddrinfo',denied):
            try: socket.create_connection(('example.com',443))
            except AssertionError as exc: assert str(exc)=='PUBLIC_SOCKET_DENIED'
            else: raise AssertionError('Denial probe failed')
            record('F077-ISOLATION','public_socket_denial_probe');runner.run(run(data))
        outcome='AUTHOR_DRY_RUN_PASS' if args.author_check else 'FORMAL_EXECUTION_PASS'
    except BaseException as exc:
        outcome='AUTHOR_DRY_RUN_FAIL' if args.author_check else 'FORMAL_EXECUTION_FAIL'
        ROWS.append({'result':'FAIL','error':repr(exc)})
        raise
    finally:
        Path(args.output).write_text(json.dumps({'outcome':outcome,'author_identity':AUTHOR,'executor_identity':args.executor_identity,'formal_execution':not args.author_check,'checks':ROWS,'cases_sha256':sha(CASES),'harness_sha256':sha(__file__),'freeze_sha256':sha(FREEZE),'feature_sha256':sha(HERE/'rest077_formal_cases.feature'),'elapsed_seconds':time.perf_counter()-started},indent=2,default=evidence_json)+'\n')
    print(json.dumps({'outcome':outcome,'checks':len(ROWS)}))
if __name__=='__main__': main()
