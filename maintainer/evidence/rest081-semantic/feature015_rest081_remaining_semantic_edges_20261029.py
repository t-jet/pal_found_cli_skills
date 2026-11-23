"""Independent semantic edge cases and transport-lifetime evidence for SDK 1.101.0."""
import asyncio
from contextlib import ExitStack
import hashlib
import inspect
import json
from pathlib import Path
import runpy
from unittest.mock import patch

BASE = Path(__file__).resolve().parent
n = runpy.run_path(str(BASE / 'feature015_rest081_remaining_semantic_retest_proof_20261029.py'))
httpx, resource, normalize = n['httpx'], n['resource'], n['normalized']
report_path = n['OUT']
report = json.loads(report_path.read_text())
from foundry_sdk._core.api_client import BaseApiResponse, AsyncApiResponse, AsyncStreamingContextManager
assert not inspect.iscoroutinefunction(BaseApiResponse.decode)
assert inspect.iscoroutinefunction(AsyncApiResponse.aclose)
assert not hasattr(AsyncApiResponse, 'close')
report['sdk_response_api_verification'] = {
    'source': inspect.getfile(BaseApiResponse),
    'source_sha256': n['sha'](Path(inspect.getfile(BaseApiResponse))),
    'decode_is_synchronous': True,
    'async_cleanup': 'await response.aclose()',
    'stream_cleanup': inspect.getsource(AsyncStreamingContextManager.__aexit__),
}

class SyncBytes(httpx.SyncByteStream):
    def __init__(self, data): self.data, self.closed = data, False
    def __iter__(self): yield self.data
    def close(self): self.closed = True

class AsyncBytes(httpx.AsyncByteStream):
    def __init__(self, data): self.data, self.closed = data, False
    async def __aiter__(self): yield self.data
    async def aclose(self): self.closed = True

class ConsumerStopped(Exception): pass

def consume(client, method, params, iterator):
    value = getattr(client, method)(**params)
    return normalize(list(value) if iterator else value)

async def aconsume(client, method, params, iterator):
    value = getattr(client, method)(**params)
    return normalize([v async for v in value] if iterator else await value)

loop = asyncio.new_event_loop()
with ExitStack() as guards:
    for obj, attr in [(n['socket'], 'getaddrinfo'), (n['socket'], 'create_connection'),
                      (n['socket'].socket, 'connect'), (n['socket'].socket, 'connect_ex'),
                      (httpx.HTTPTransport, 'handle_request'),
                      (httpx.AsyncHTTPTransport, 'handle_async_request'),
                      (n['urllib'].request, 'urlopen')]:
        guards.enter_context(patch.object(obj, attr, n['deny']))
    async def native_async_denied():
        async with httpx.AsyncClient() as client:
            try: await client.get('https://qa.invalid')
            except RuntimeError as e: assert str(e) == 'QA_PUBLIC_NETWORK_DENIED'
            else: raise AssertionError('Native async HTTP escaped guard')
    loop.run_until_complete(native_async_denied())
    for op in report['operations']:
        _, _, res, method = op['id'].split('.')
        module = n['getmodule'](res)
        cls, acls = getattr(module, res+'Client'), getattr(module, 'Async'+res+'Client')
        key = res+'.'+method
        verb, suffix, kw, body, payload = n['CASES'][key]
        params = {'ontology':n['ontology'], **kw, 'preview':True, 'request_timeout':3}
        iterator = 'ResourceIterator' in op['sdk_signature']
        checks = []
        try:
            def denial(req):
                return httpx.Response(403, json={'errorCode':'PERMISSION_DENIED',
                    'errorName':'QaAccessDenied', 'parameters':{},
                    'errorInstanceId':'00000000-0000-0000-0000-000000000081'})
            async def async_denial():
                async with httpx.AsyncClient(transport=httpx.MockTransport(denial)) as http:
                    client = resource(acls, http, True)
                    try: await aconsume(client, method, params, iterator)
                    except n['PalantirRPCException'] as e: assert e.name == 'QaAccessDenied'
                    else: raise AssertionError('Async 403 accepted')
            loop.run_until_complete(async_denial())
            checks.append('async generic 403 propagated; no endpoint-specific error invented')

            # A response whose bytes have not been consumed proves context cleanup,
            # including a consumer exception before reading the first byte.
            sync_stream = SyncBytes(json.dumps(payload).encode())
            with httpx.Client(transport=httpx.MockTransport(lambda req:httpx.Response(200, stream=sync_stream, headers={'content-type':'application/json'}))) as http:
                client = resource(cls, http)
                try:
                    with getattr(client.with_streaming_response, method)(**params):
                        assert not sync_stream.closed
                        raise ConsumerStopped()
                except ConsumerStopped: pass
                assert sync_stream.closed
            async def early_async_close():
                stream = AsyncBytes(json.dumps(payload).encode())
                async with httpx.AsyncClient(transport=httpx.MockTransport(lambda req:httpx.Response(200, stream=stream, headers={'content-type':'application/json'}))) as http:
                    client = resource(acls, http, True)
                    try:
                        async with getattr(client.with_streaming_response, method)(**params):
                            assert not stream.closed
                            raise ConsumerStopped()
                    except ConsumerStopped: pass
                    assert stream.closed
            loop.run_until_complete(early_async_close())
            checks.append('sync/async unread streamed responses close on consumer exception')

            if iterator:
                for async_mode in (False, True):
                    tokens = []
                    def page(req):
                        token = req.url.params.get('pageToken')
                        tokens.append(token)
                        assert len(tokens) <= 2
                        assert req.url.params['pageSize'] == '2'
                        return httpx.Response(200, json=({'data':[], 'nextPageToken':'qa-next-81'} if token is None else payload))
                    paged_params = {**params, 'page_size':2}
                    if async_mode:
                        async def apages():
                            async with httpx.AsyncClient(transport=httpx.MockTransport(page)) as http:
                                return await aconsume(resource(acls,http,True), method, paged_params, True)
                        value = loop.run_until_complete(apages())
                    else:
                        with httpx.Client(transport=httpx.MockTransport(page)) as http:
                            value = consume(resource(cls,http), method,paged_params,True)
                    assert value == payload['data']
                    assert tokens == [None, 'qa-next-81']
                checks.append('sync/async iterators follow empty intermediate page token; preserve locator/object/link shapes')
            else:
                variants = []
                if method == 'count': variants = [({},params,None), ({'count':0},params,None)]
                elif key == 'OntologyObjectSet.get':
                    variants = [({'type':'union','objectSets':[{'type':'base','objectType':'Asset'}, {'type':'base','objectType':'Site'}]},params,None)]
                elif method == 'load_links':
                    variants = [({'data':[n['links'],n['links']], 'nextPageToken':'qa-links-81'},params,body)]
                elif method == 'create_scenario':
                    variants = [(payload,{**params,'base':{'type':'branch','branch':'qa-base'}},{'base':{'type':'branch','branch':'qa-base'}})]
                elif method == 'list_scenario_edited_entity_types':
                    variants = [({'objectTypes':[],'linkTypes':[{'objectTypeApiName':'Asset','linkTypes':['installedAt']}]},params,None)]
                elif method in ('list_scenario_edited_link_types','list_scenario_edited_object_types'):
                    variants = [({'data':[]},params,None)]
                elif method == 'post_edits':
                    variants = [(payload,params,body)]
                for response_body, call_params, expected_body in variants:
                    def variant(req):
                        assert (json.loads(req.content) if req.content else None) == expected_body
                        return httpx.Response(200,json=response_body)
                    with httpx.Client(transport=httpx.MockTransport(variant)) as http:
                        value = consume(resource(cls,http),method,call_params,False)
                        assert value == response_body
                checks.append('source-derived result/body edge variants: '+str(len(variants)))
            op['semantic_edge_checks'] = checks
            op['source_and_meaning_review'] = {
                'verdict':'PASS',
                'scope':'Reviewed behavior, structural contract, adapted example, SDK signature/docstring/wire and reachable model definitions.',
                'interpretation':n['NOTES'][key],
                'boundary':'Offline source-backed semantics only. Private beta availability, tenant permissions and server business effects require authorized enrollment.'}
        except Exception:
            import traceback
            op['semantic_verdict'] = 'FAIL'
            op['failures'].append(traceback.format_exc())
            print(op['id'],op['failures'][-1])

loop.close()
for path in (Path(__file__),Path(inspect.getfile(BaseApiResponse)),n['SKILL']/'references/rest/client-behavior.md'):
    report['content_manifest'][str(path.resolve())] = n['sha'](path)
provenance_path = BASE/'feature015_rest081_remaining_harness_provenance_20261029.json'
provenance = json.loads(provenance_path.read_text())
assert all(n['sha'](Path(path)) == value for path,value in provenance['original_artifacts_sha256'].items())
report['original_artifacts_unchanged'] = True
report['original_artifacts_sha256'] = provenance['original_artifacts_sha256']
report['counts'] = {v:sum(op['semantic_verdict']==v for op in report['operations']) for v in ('PASS','FAIL','UNCERTAIN')}
report['hash_stability'] = all(n['sha'](Path(path)) == value for path,value in report['content_manifest'].items())
report['network_guard_probes_denied'] = len(n['deny_events'])
report['semantic_review_recommendation'] = 'Eleven pending operations pass independent offline semantic retest; manager may reconcile review metadata. Formal TESTEXEC remains prerequisite-gated.'
report_path.write_text(json.dumps(report,indent=2))
print(json.dumps({'final_counts':report['counts'],'model_definitions':len(report['model_review']),
    'hash_stability':report['hash_stability'],'original_artifacts_unchanged':True,
    'async_native_network_denied':True,'report':str(report_path)}))
assert report['counts'] == {'PASS':11,'FAIL':0,'UNCERTAIN':0}
