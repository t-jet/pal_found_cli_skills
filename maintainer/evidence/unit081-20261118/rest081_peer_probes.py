import ast, asyncio, hashlib, importlib, importlib.util, json, subprocess, sys
from pathlib import Path
from unittest.mock import patch
ROOT=Path.cwd(); TMP=ROOT/'.ept/tmp'; PEER=TMP/'rest081_independent_peer_20261118'
spec=importlib.util.spec_from_file_location('peer_target', PEER/'tests/test_offline_rest_081.py'); t=importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
results={}; ledger=[]
for resource, method in t.CASES:
    row=t.OPERATIONS[f'v2.ontologies.{resource}.{method}']; module=importlib.import_module(row['module'])
    sdkpath=row['module'].replace('.', '/')+'.py'
    data=subprocess.check_output(['git','-C',str(ROOT/'.ept/docs/customer_input/foundry-platform-python'),'show','168d51910570b6966afa2320333ab36f6a3f7ccf:'+sdkpath])
    digest=hashlib.sha256(data).hexdigest(); assert digest==hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest()==row['source_sha256']
    tree=ast.parse(data); cls=next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name==resource+'Client'); fn=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name==method)
    request=next(n for n in ast.walk(fn) if isinstance(n,ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr=='RequestInfo')
    fields={n.arg:ast.unparse(n.value) for n in request.keywords}
    assert all(fields[key]==value for key,value in row['wire'].items())
    ledger.append({'operation':f'v2.ontologies.{resource}.{method}','sdk_sha256':digest,'wire_fields':len(fields)})
results['independent_git_source_wire_ledger']=ledger
loop=asyncio.new_event_loop()
def killed(label, fn):
    try: fn()
    except (AssertionError, KeyError): results[label]='killed'
    else: raise AssertionError(label+' survived')
# Mutate reader payloads with their own assertions unchanged.
obj=t.load('OntologyObject','get'); obj['SUCCESS']['__primaryKey']=90001
killed('reader_object_identity', obj['verify'])
scenario=t.success_payload('OntologyScenario','list_scenario_edited_links'); scenario['data'][0]['sourceObject']['status']='ACTIVE'
killed('scenario_full_object_in_locator',lambda:t.assert_scenario_semantics('list_scenario_edited_links',scenario))
preview=t.load('OntologyObjectSet','create_temporary'); preview['invoke']=lambda c:c.with_raw_response.create_temporary(preview=False)
killed('beta_preview_false',lambda:t.assert_preview(preview))
# Truncation of actual SDK output must fail complete-page assertions.
consume=t.consume_sync
def truncating(*args,**kwargs):
    rows=consume(*args,**kwargs)
    return rows[:1] if isinstance(rows,list) else rows
with patch.object(t,'consume_sync',truncating):
    killed('native_pager_truncation',lambda:t.test_paging_crosses_empty_intermediate_page_and_stops_at_finite_end('OntologyObject','list','ordinary',False,loop))
async def ignored_close(self): pass
with patch.object(t.TrackedAsyncStream,'aclose',ignored_close):
    killed('async_cancellation_cleanup_omitted',lambda:t.test_async_task_cancellation_closes_stream_with_unread_bytes('OntologyObject','get',loop))
loop.close()
results['author_test_sha256']=hashlib.sha256((PEER/'tests/test_offline_rest_081.py').read_bytes()).hexdigest()
results['peer_head']=subprocess.check_output(['git','-C',str(PEER),'rev-parse','HEAD'],text=True).strip()
results['tracked_diff_exit']=subprocess.run(['git','-C',str(PEER),'diff','--exit-code'],capture_output=True).returncode
assert results['tracked_diff_exit']==0
(TMP/'rest081_peer_probe_results.json').write_text(json.dumps(results,indent=2))
print(json.dumps({key:value for key,value in results.items() if key!='independent_git_source_wire_ledger'},indent=2)); print('independent Git source/wire operations:',len(ledger))
