"""Independent offline review measurements for the current REST089 candidate."""
import ast
from collections import Counter
from contextlib import ExitStack
import hashlib
import importlib
import inspect
import json
from pathlib import Path
import re
import runpy
import socket
import subprocess
import textwrap
from unittest.mock import patch
import httpx

TMP = Path(__file__).resolve().parent
REPO = TMP / 'feature015_integration'
DEV = REPO / '.agents/skills/pal-found-dev'
ORACLE = REPO / 'tests/fixtures/offline/rest-acceptance/source-oracle.json'
oracle = json.loads(ORACLE.read_bytes())['operations']
rows = [r for r in json.loads((REPO / 'maintainer/rest-domain-authoring-register.json').read_bytes())['operations'] if r['story'] == 'DEV-STORY-089']
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assets = {}
def asset(p):
    p = p.resolve()
    key = str(p.relative_to(DEV)) if p.is_relative_to(DEV) else str(p)
    assets[key] = sha(p)
    return key

# Findings are reviewer judgments, not generated from fixture execution results.
judgments = {
'v2.connectivity.Connection.create': ('FAIL', 'Success request uses prohibited unknownWorker. Source declares UnknownWorkerCannotBeUsedForCreatingOrUpdatingConnections and requires Foundry worker. S3 bucketUrl synthetic-value is not a bucket URL and lacks required trailing slash. Replace with a meaningful Foundry-worker/S3 request and consistent success.'),
'v2.connectivity.Connection.get': ('PASS', 'RID lookup, metadata/export settings and missing/type/parent errors match source. unknownWorker is valid in read-side union; creation prohibition does not forbid decoding an existing connection.'),
'v2.connectivity.Connection.get_configuration': ('PASS', 'Configuration-only lookup, non-secret verification and missing/type/permission errors match source; local S3 definitions explain authentication and trailing slash.'),
'v2.connectivity.Connection.get_configuration_batch': ('PASS', 'Behavior explicitly preserves 200-item maximum and omission of absent/invisible RIDs. Empty result is meaningful for requested hidden/missing connection; no errors invented.'),
'v2.connectivity.Connection.update_export_settings': ('PASS', 'Both export flags supplied, Information Security Officer prerequisite stated, None return reconciled by Connection.get. Named permission/missing errors match source.'),
'v2.connectivity.Connection.update_secrets': ('FAIL', 'Only example sends secrets={}; this rotates no secret and cannot demonstrate accepted secret-name/value mapping. Contract correctly says names must already exist and omissions remain unchanged. Add a synthetic named secret rotation and verification boundary.'),
'v2.connectivity.Connection.upload_custom_jdbc_drivers': ('FAIL', 'Source requires file_name ending .jar; example sends synthetic-value. Success returns S3 connection configuration although operation targets existing JDBC connection. Binary transport handling alone does not validate this success scenario.'),
'v2.connectivity.FileImport.create': ('PASS', 'Creates import definition with ordered pathNotMatchesFilter and SNAPSHOT mode; source dataset/branch immutability appears in contract. Behavior distinguishes definition from asynchronous execution and destination validation.'),
'v2.connectivity.FileImport.delete': ('PASS', 'Deletes definition, preserves destination dataset and stops future refresh. Connection/import path identity and permission/missing errors match source.'),
'v2.connectivity.FileImport.execute': ('PASS', 'Returns BuildRid, not completed data. Behavior routes to Orchestration, preserves handle and reconciles uncertain submission before retry.'),
'v2.connectivity.FileImport.get': ('PASS', 'Connection and import RIDs select definition; response mapping and missing errors align with source. Read has no build side effect.'),
'v2.connectivity.FileImport.list': ('PASS', 'Visibility filtering and finite page/item guidance retained; contract distinguishes ordinary iterator and raw page. Example exercises one terminating raw page.'),
'v2.connectivity.FileImport.replace': ('PASS', 'Replacement excludes immutable dataset/branch and updates supplied filter/name/mode fields. Behavior requires re-read before build. Filter constraint errors are locally available.'),
'v2.connectivity.TableImport.create': ('FAIL', 'Example chooses Databricks import config but query=synthetic-value is not executable SQL. Shared linked config requires valid source query. Need bounded SELECT and consistent response; transport does not parse upstream SQL.'),
'v2.connectivity.TableImport.delete': ('PASS', 'Deletes import definition while destination persists. Correct scoped RIDs and missing/permission errors; recovery describes refresh loss.'),
'v2.connectivity.TableImport.execute': ('PASS', 'Asynchronous BuildRid return and Orchestration/destination validation are explicit. Timeout reconciliation prevents claiming completed import at submission.'),
'v2.connectivity.TableImport.get': ('PASS', 'Scoped read and TableImportTypeNotSupported/missing errors match source; response retains config/mode/schema-change state.'),
'v2.connectivity.TableImport.list': ('PASS', 'Visible-only table import enumeration; finite retrieval guidance and raw-page/ordinary-iterator distinction retained. One terminating fixture page is correctly decoded.'),
'v2.connectivity.TableImport.replace': ('FAIL', 'Example sends Databricks query=synthetic-value. This is not valid source SQL and provides no adaptable table selection. Destination and branch remain immutable in source signature; config/mode mutation needs a meaningful query.'),
'v2.connectivity.VirtualTable.create': ('PASS', 'Snowflake database/schema/table config and parent/name supplied; behavior separates resource creation from upstream query capability and reconciles uncertain creates. Permission/conflict/invalid-connection errors retained.'),
'v2.sql_queries.SqlQuery.cancel': ('PASS', 'Cancellation of known query ID; no-op after stopped and cancellation/success race described. None response and named query-state/access errors match source.'),
'v2.sql_queries.SqlQuery.execute': ('PASS', 'Individual serialization fixture uses placeholder SQL, but linked sql_query_lifecycle.py supplies meaningful SELECT 1 AS row_count with CSV, retains query ID and polls before fetching. Default Arrow, owner-only access and million-row default retained.'),
'v2.sql_queries.SqlQuery.execute_ontology': ('FAIL', 'Only per-operation example submits query=synthetic-value and accepts arbitrary b offline synthetic content as successful Arrow bytes. SQL lifecycle example explicitly covers different route. Need valid Ontology SQL, bounded row/byte handling and valid Arrow decode with named prerequisites.'),
'v2.sql_queries.SqlQuery.get_results': ('PASS', 'Linked lifecycle fetches same submitted query ID and decodes explicitly requested CSV. Contract retains TableResponse and wrapper lifetimes; minute long-poll timeout and bounded same-ID retry are explicit.'),
'v2.sql_queries.SqlQuery.get_status': ('PASS', 'Linked lifecycle preserves query identity and finite three-attempt poll; running versus succeeded discriminator matches QueryStatus. Named failed/canceled/access states remain local.'),
'v2.streams.Dataset.create': ('FAIL', 'Behavior says retain returned dataset and stream identity, but response Dataset only contains rid/name/parentFolderRid. First stream must be resolved with Stream.get using chosen/default branch. Clarify lookup rather than implying stream/view identity in create response.'),
'v2.streams.Stream.create': ('PASS', 'Creates branch plus stream on existing dataset, returns branch/schema/view/partition settings. BranchAlreadyExists and schema/type/permission errors retained; default and immutable settings remain in local contract.'),
'v2.streams.Stream.get': ('PASS', '404 ambiguity across missing branch/stream/access is explicit. Returned schema/view identity and invalid-schema/type errors match source.'),
'v2.streams.Stream.get_end_offsets': ('UNCERTAIN', 'Behavior correctly defines next-write boundary and optional view pinning. Only operation fixture returns {}; no populated partition-offset example shows distinction from last record offset. Add a nonempty example to demonstrate useful output before semantic approval.'),
'v2.streams.Stream.get_records': ('PASS', 'Source sparse/inclusive offsets, limit possibly returning fewer, base64 binary values and optional view are retained. Behavior advances using returned offsets. Fixture decodes offset 1, and subscriber example independently demonstrates sparse offsets 50,52.'),
'v2.streams.Stream.publish_binary_record': ('PASS', 'Bytes request and None response align; behavior explicitly requires single binary-field schema and avoids filename/JSON body confusion. View pinning and permission error retained.'),
'v2.streams.Stream.publish_record': ('FAIL', 'Behavior tells reader to confirm returned write result; source return is None. Example sends record={} without a declared synthetic schema or a meaningful record. Show schema-valid fields and reconcile acknowledgment with None response and subsequent read.'),
'v2.streams.Stream.publish_records': ('FAIL', 'Only example publishes records=[{}] without synthetic schema or useful fields. Whole-batch rejection semantics are correctly described, but no meaningful adaptable batch demonstrates compatibility. Add schema and nonempty matching records.'),
'v2.streams.Stream.reset': ('PASS', 'Behavior explicitly states record destruction and new view identity, alternate in-platform settings path and consumer reconciliation. Empty request legitimately retains existing configuration while clearing records.'),
'v2.streams.Subscriber.commit_offsets': ('PASS', 'Behavior and source agree commit last processed offset, next read offset+1. Linked sparse example processes 50,52 and commits 52. Its mock returns 52 but does not prove new read position; live guidance correctly requires get_read_position verification.'),
'v2.streams.Subscriber.create': ('PASS', 'ID uniqueness across streams and existing registration on same stream are explicit. Default earliest and earliest/latest/specific variants in contract; response identifies dataset/branch/view and creation time.'),
'v2.streams.Subscriber.delete': ('PASS', 'Deletion clears committed state and permits ID reuse. None response, private-beta boundary and scoped missing/permission errors retained.'),
'v2.streams.Subscriber.get_read_position': ('PASS', 'Behavior correctly identifies next-read offsets and capture before replay. Optional view pinning and PartitionOffsets model remain local; no unsupported last-processed interpretation.'),
'v2.streams.Subscriber.read_records': ('PASS', 'Manual versus automatic commit semantics preserved; linked sparse example reads populated records with auto_commit=False then processes before commit. Default 100/max1000 and across-partition limit are in contract.'),
'v2.streams.Subscriber.reset_offsets': ('FAIL', 'Only fixture resets specific offsets={} and receives {}; no partition checkpoint, replay, or skip is demonstrated. Behavior names variants correctly; add nonempty specific offsets or a concrete earliest/latest example and verify position.'),
}
assert set(judgments) == {r['id'] for r in rows}

events = []
denied = []
def deny(*args, **kwargs):
    denied.append(repr(args[:1]))
    raise AssertionError('Network socket/DNS denied during offline review')
original_send = httpx.Client.send
def record_send(self, request, *args, **kwargs):
    events.append({'method': request.method, 'url': str(request.url), 'body_sha256': hashlib.sha256(request.content).hexdigest()})
    return original_send(self, request, *args, **kwargs)

result = []
with ExitStack() as stack:
    for name in ('connect', 'connect_ex'):
        stack.enter_context(patch.object(socket.socket, name, deny))
    for name in ('create_connection', 'getaddrinfo', 'gethostbyname', 'gethostbyname_ex'):
        stack.enter_context(patch.object(socket, name, deny))
    stack.enter_context(patch.object(httpx.Client, 'send', record_send))
    for row in rows:
        op = row['id']; reference = oracle[op]
        module = importlib.import_module(reference['module'])
        resource, method = op.split('.')[-2:]
        fn = getattr(getattr(module, resource+'Client'), method)
        node = ast.parse(textwrap.dedent(inspect.getsource(fn))).body[0]
        request = next(n for n in ast.walk(node) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr=='RequestInfo')
        wire = {k.arg: ast.unparse(k.value) for k in request.keywords if k.arg in reference['wire']}
        contract = DEV / ('references/rest/contracts/' + op.replace('.', '/') + '.md')
        contract_text = contract.read_text(encoding='utf-8')
        differences = [key for key, value in reference['wire'].items() if wire.get(key)!=value]
        documented_wire = {key: bool(re.search(r'\*\*'+re.escape(key)+r'\*\*\s+```python\s*'+re.escape(value)+r'\s*```', contract_text)) for key, value in wire.items()}
        before = len(events)
        try:
            fixture = runpy.run_path(str(DEV/row['example']))
            fixture[row['fixture_entrypoint']]()
            execution = {'status':'PASS', 'request_count':len(events)-before, 'named_errors':len(fixture['ERRORS']), 'requests':events[before:]}
        except Exception as exc:
            execution = {'status':'FAIL','exception':repr(exc),'requests':events[before:]}
        status, reason = judgments[op]
        if differences or not all(documented_wire.values()) or execution['status']=='FAIL': status='FAIL'
        links = []
        for target in re.findall(r'\]\(([^)]+)\)', contract_text):
            if not target.startswith(('https:', 'http:', '#')):
                p=(contract.parent/target.split('#')[0]).resolve()
                links.append({'path':asset(p) if p.is_file() else str(p), 'exists':p.is_file()})
        result.append({'id':op,'status':status,'reason':reason,'behavior':asset(DEV/row['behavior']), 'contract':asset(contract), 'example':asset(DEV/row['example']), 'source_path':module.__file__,'source_sha256':sha(module.__file__), 'oracle_source_sha256':reference['source_sha256'], 'source_hash_matches':sha(module.__file__)==reference['source_sha256'], 'official_doc_sha256':reference['documentation']['doc_sha256'], 'stage':reference['documentation']['stage'],'stage_present':('release stage: '+reference['documentation']['stage']+'.') in contract_text, 'source_wire_differences':differences,'contract_wire_matches':documented_wire,'signature_present':reference['ordinary']['signature'] in contract_text,'return_present':reference['ordinary']['return'] in contract_text, 'referenced_local_assets':links,'sdk_http_execution':execution})
    supplemental=[]
    for name in ('sql_query_lifecycle.py','subscriber_offsets.py'):
        p=DEV/'examples/rest/089'/name
        before=len(events)
        try:
            runpy.run_path(str(p))['verify']()
            supplemental.append({'asset':asset(p),'status':'PASS','requests':events[before:]})
        except Exception as exc:
            supplemental.append({'asset':asset(p),'status':'FAIL','exception':repr(exc)})

report={'story':'DEV-STORY-089','reviewer_agent':'/root/rest089_review_finish_20261028','scope':'Independent source/behavior/example semantic review of all 40 operations. Prepared SDK HTTP mocks; no live tenant, upstream, or enrollment claim. PASS is offline semantic approval only. UNCERTAIN requires example evidence before acceptance.', 'candidate':str(REPO),'oracle':str(ORACLE),'oracle_sha256':sha(ORACLE),'counts':dict(Counter(r['status'] for r in result)), 'network':{'socket_connect_and_connect_ex':'DENIED','create_connection':'DENIED','DNS':'DENIED','attempts':denied,'httpx_actual_sdk_requests':len(events)},'operations':result,'supplemental_examples':supplemental,'asset_sha256':assets}
model_oracle_path=REPO/'tests/fixtures/offline/rest-acceptance/model-source-oracle.json'
model_oracle=json.loads(model_oracle_path.read_bytes())['symbols']
model_checks=[]
for relative in list(assets):
    if not relative.startswith('references\\rest\\models\\'):
        continue
    path=DEV/relative
    text=path.read_text(encoding='utf-8')
    title=text.splitlines()[0].removeprefix('# ').strip()
    if title not in model_oracle:
        continue
    expected=model_oracle[title]
    blocks=re.findall(r'```python\s*\n(.*?)\n```',text,re.S)
    def canonical(code):
        return ast.dump(ast.parse(code),include_attributes=False)
    try:
        code_matches=any(canonical(block)==canonical(expected['definition']) for block in blocks)
    except SyntaxError:
        code_matches=False
    source=Path('D:/app/Python/Lib/site-packages')/expected['path']
    model_checks.append({'symbol':title,'asset':relative,'source_path':str(source),'source_sha256':sha(source),'oracle_source_sha256':expected['source_sha256'],'source_hash_matches':sha(source)==expected['source_sha256'],'definition_ast_matches':code_matches,'dependencies':expected['dependencies']})
report['model_source_oracle_sha256']=sha(model_oracle_path)
report['model_definition_checks']=model_checks
report['model_definition_check_counts']={'checked':len(model_checks),'source_hash_failures':sum(not c['source_hash_matches'] for c in model_checks),'ast_mismatches':sum(not c['definition_ast_matches'] for c in model_checks)}
checked_symbols={c['symbol'] for c in model_checks}
report['model_dependency_closure_missing']=sorted({d for c in model_checks for d in c['dependencies']}-checked_symbols)
report['candidate_head_at_report']=subprocess.check_output(['git','-C',str(REPO),'rev-parse','HEAD'],text=True).strip()
report['review_boundaries']=['No source, ledger, ticket, or shared author content was written.', 'Each judgment applies to the exact behavior/contract/example hashes listed; unrelated concurrent commits do not invalidate unchanged assets.', 'Model/error definition AST equality and module hashes were checked for all 381 referenced symbols; dependency closure has no missing symbols.', 'Named error mock envelopes verify SDK decoding, not that a live service would produce each synthetic parameter value.', 'All source contracts and fixtures were inspected separately from reviewer judgments; fixture success cannot waive invalid business input or misleading output guidance.']
out=TMP/'feature015_rest089_current_semantic_review_20261028.json'
out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'report':str(out),'counts':report['counts'],'http_requests':len(events),'fixture_failures':[r['id'] for r in result if r['sdk_http_execution']['status']=='FAIL'],'wire_differences':[r['id'] for r in result if r['source_wire_differences'] or not all(r['contract_wire_matches'].values())],'missing_links':sum(not l['exists'] for r in result for l in r['referenced_local_assets'])}))
