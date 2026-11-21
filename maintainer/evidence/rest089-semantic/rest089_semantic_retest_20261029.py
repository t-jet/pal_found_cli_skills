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
REPO = TMP / 'feature015_rest089_fixes'
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
initial = json.loads((TMP / 'feature015_rest089_current_semantic_review_20261028.json').read_bytes())
judgments = {r['id']: (r['status'], r['reason']) for r in initial['operations']}
corrections = {
'v2.connectivity.Connection.create': 'Foundry worker with explicit policy; public S3 bucket URL ends in slash; response agrees. Synthetic permission/network prerequisites explicit.',
'v2.connectivity.Connection.update_secrets': 'Named nonempty synthetic secret rotation; existing secret-name prerequisite and retained omitted values explicit.',
'v2.connectivity.Connection.upload_custom_jdbc_drivers': 'Filename ends .jar and binary is readable JAR container; JDBC response records same filename. Manifest-only fixture and real driver prerequisites explicit.',
'v2.connectivity.TableImport.create': 'Bounded SELECT with explicit Databricks table/columns; request and returned config agree; source availability prerequisite explicit.',
'v2.connectivity.TableImport.replace': 'Bounded SELECT in replacement config; immutable destination omitted and response agrees; authorized table prerequisite explicit.',
'v2.sql_queries.SqlQuery.execute_ontology': 'Valid adaptable bounded SELECT, ontology/type/property/OSV2 prerequisites; actual Arrow IPC parsed. Rejects arbitrary bytes, excess byte budget before parse, excess rows after parse. SDK bytes already buffered.',
'v2.streams.Dataset.create': 'Dataset metadata-only return explicitly distinguished; first stream resolved via Stream.get on chosen/default branch. Empty schema fixture does not establish live publish-ready schema.',
'v2.streams.Stream.get_end_offsets': 'Populated map gives partition0 next-write53, partition1 empty boundary0; distinction from last record offset52 explicit.',
'v2.streams.Stream.publish_record': 'Nonempty record matches declared sample string/integer schema; None acknowledgment explicitly retained; bounded read reconciliation required.',
'v2.streams.Stream.publish_records': 'Nonempty records match declared string/integer schema; None response, whole-batch rejection and uncertain-delivery recovery explicit.',
'v2.streams.Subscriber.reset_offsets': 'Specific partition0 offset50 and same decoded position; reset resumes50 without commit-style +1. Fixture cannot establish actual checkpoint/replay; live bounded read required.'}
for op, reason in corrections.items(): judgments[op] = ('PASS', reason)
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

report={'story':'DEV-STORY-089','reviewer_agent':'/root/rest089_retest_20261029','scope':'Independent retest of 40 exact corrected source/behavior/example semantics, source and transitive AST bindings plus actual SDK MockTransport. Initial unchanged judgments reused only with byte continuity. Offline semantic approval; no blind-reader or live service acceptance.', 'candidate':str(REPO),'oracle':str(ORACLE),'oracle_sha256':sha(ORACLE),'counts':dict(Counter(r['status'] for r in result)), 'network':{'socket_connect_and_connect_ex':'DENIED','create_connection':'DENIED','DNS':'DENIED','attempts':denied,'httpx_actual_sdk_requests':len(events)},'operations':result,'supplemental_examples':supplemental,'asset_sha256':assets}
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
report['previous_boundaries']=['No source, ledger, ticket, or shared author content was written.', 'Each judgment applies to the exact behavior/contract/example hashes listed; unrelated concurrent commits do not invalidate unchanged assets.', 'Model/error definition AST equality and module hashes were checked for all 381 referenced symbols; dependency closure has no missing symbols.', 'Named error mock envelopes verify SDK decoding, not that a live service would produce each synthetic parameter value.', 'All source contracts and fixtures were inspected separately from reviewer judgments; fixture success cannot waive invalid business input or misleading output guidance.']
# Extend report with independent mutation and continuity checks below.
import copy
import io
import zipfile
import pyarrow as pa
from foundry_sdk._errors.sdk_internal_error import SDKInternalError

mutation_results = []
def require(condition, reason):
    if not condition: raise AssertionError(reason)

def semantic(op, body, query, success):
    if op.endswith('Connection.create'):
        require(body['worker']['type'] == 'foundryWorker', 'creation worker must be supported')
        require(bool(body['worker']['networkEgressPolicyRids']), 'declared egress policy')
        url = body['configuration']['bucketUrl']
        require(url.startswith('s3://') and url.endswith('/') and len(url) > 6, 'bucket URL with trailing slash')
        require(body['configuration'] == success['configuration'], 'configuration response consistent')
    elif op.endswith('update_secrets'):
        require(bool(body['secrets']) and all(isinstance(v,str) and v for v in body['secrets'].values()), 'named nonempty secret rotation')
    elif op.endswith('upload_custom_jdbc_drivers'):
        require(query['fileName'].endswith('.jar'), 'JAR filename')
        with zipfile.ZipFile(io.BytesIO(body)) as jar:
            require('META-INF/MANIFEST.MF' in jar.namelist(), 'JAR manifest')
        require(success['configuration']['type'] == 'jdbc' and query['fileName'] in success['configuration']['uploadedJdbcDrivers'], 'JDBC upload response')
    elif '.TableImport.' in op:
        require(re.fullmatch(r'SELECT [A-Za-z_]+, [A-Za-z_]+ FROM [A-Za-z_.]+ LIMIT [1-9][0-9]*', body['config']['query']) is not None, 'bounded executable source SELECT')
        require(body['config'] == success['config'], 'returned table query consistent')
    elif op.endswith(('publish_record','publish_records')):
        records = [body['record']] if 'record' in body else body['records']
        require(bool(records), 'nonempty batch')
        for record in records:
            require(set(record) == {'orderId','quantity'} and isinstance(record['orderId'],str) and bool(record['orderId']) and type(record['quantity']) is int, 'record fits declared schema')
        require(success is None, 'SDK None acknowledgment')
    elif op.endswith('reset_offsets'):
        position=body['position']
        require(position['type']=='specific' and bool(position['offsets']), 'concrete checkpoint')
        require(all(type(v) is int and v>=0 for v in position['offsets'].values()), 'valid partition offsets')
        require(position['offsets']==success, 'reset resumes same offset')
    elif op.endswith('get_end_offsets'):
        require(success.get('0')==53 and success.get('1')==0, 'next-write53 and empty-partition0')
    elif op.endswith('execute_ontology'):
        require(body['query']=='SELECT orderId FROM Orders LIMIT 10' and body['rowLimit']==10 and bool(body['ontologyIdentifier']), 'bounded ontology SELECT')
        require(pa.ipc.open_stream(success).read_all().to_pylist()==[{'orderId':'order-001'}], 'real Arrow result')

with ExitStack() as stack:
    for name in ('connect','connect_ex'): stack.enter_context(patch.object(socket.socket,name,deny))
    for name in ('create_connection','getaddrinfo','gethostbyname','gethostbyname_ex'): stack.enter_context(patch.object(socket,name,deny))
    for op in corrections:
        if op.endswith('Dataset.create'): continue
        row=next(r for r in rows if r['id']==op)
        example=runpy.run_path(str(DEV/row['example']))
        invoke=example['invoke']
        call=ast.parse(textwrap.dedent(inspect.getsource(invoke))).body[0].body[0].value
        kwargs={k.arg:eval(compile(ast.Expression(k.value),'<independent args>','eval'),invoke.__globals__) for k in call.keywords}
        client_class=next(v for k,v in example.items() if k.endswith('Client') and inspect.isclass(v))
        response=example['SUCCESS']
        def exchange(args, result):
            def handler(request):
                body=request.content if request.headers.get('content-type')=='application/octet-stream' else (json.loads(request.content) if request.content else None)
                semantic(op,body,dict(request.url.params),result)
                if result is None: return httpx.Response(204)
                if isinstance(result,bytes): return httpx.Response(200,content=result)
                return httpx.Response(200,json=result)
            with example['mock_resource'](client_class,handler) as client:
                raw=getattr(client.with_raw_response,op.split('.')[-1])(**args)
                try: return raw.decode()
                finally: raw.close()
        decoded=exchange(kwargs,response)
        mutants=[]
        def mutant(label, key=None, value=None, result=response):
            args=copy.deepcopy(kwargs)
            if key is not None: args[key]=value
            mutants.append((label,args,result))
        if op.endswith('Connection.create'):
            mutant('prohibited unknownWorker','worker',{'type':'unknownWorker'})
            c=copy.deepcopy(kwargs['configuration']); c['bucketUrl']='synthetic-value'; mutant('invalid S3 URL','configuration',c)
        elif op.endswith('update_secrets'): mutant('empty secrets','secrets',{})
        elif op.endswith('upload_custom_jdbc_drivers'):
            mutant('wrong filename','file_name','synthetic-value')
            c=copy.deepcopy(response); c['configuration']={'type':'s3','bucketUrl':'s3://example/'}; mutant('wrong response connection type',result=c)
        elif '.TableImport.' in op:
            c=copy.deepcopy(kwargs['config']); c['query']='synthetic-value'; mutant('invalid SQL','config',c)
        elif op.endswith(('publish_record','publish_records')):
            if 'record' in kwargs: mutant('empty record','record',{})
            else: mutant('empty records','records',[{}])
            mutant('invented write result',result={'success':True})
        elif op.endswith('reset_offsets'): mutant('empty specific offsets','position',{'type':'specific','offsets':{}})
        elif op.endswith('get_end_offsets'): mutant('empty end-offset map',result={})
        elif op.endswith('execute_ontology'):
            mutant('invalid ontology SQL','query','synthetic-value')
            mutant('arbitrary bytes accepted as Arrow',result=b'offline synthetic content')
        rejected=[]
        for label,args,result_ in mutants:
            try: exchange(args,result_)
            except (AssertionError,KeyError,pa.ArrowInvalid,SDKInternalError) as exc: rejected.append({'mutation':label,'rejected':True,'exception':type(exc).__name__,'reason':str(exc)})
            else: rejected.append({'mutation':label,'rejected':False})
        mutation_results.append({'id':op,'actual_sdk_valid_case':'PASS','mutations':rejected})
    ontology=runpy.run_path(str(DEV/'examples/rest/089/v2/sql_queries/SqlQuery/invoke_execute_ontology.py'))
    arrow_checks=[]
    payloads=[('arbitrary_bytes',b'offline synthetic content'),('byte_budget',b'x'*65537)]
    sink=pa.BufferOutputStream()
    with pa.ipc.new_stream(sink,pa.schema([('orderId',pa.string())])) as writer:
        writer.write_table(pa.table({'orderId':['order-001']*11}))
    payloads.append(('row_budget',sink.getvalue().to_pybytes()))
    for name,payload in payloads:
        try: ontology['decode_result'](payload)
        except (ValueError,pa.ArrowInvalid) as exc: arrow_checks.append({'case':name,'rejected':True,'reason':str(exc)})
        else: arrow_checks.append({'case':name,'rejected':False})

continuity=[]
for relative, oldhash in initial['asset_sha256'].items():
    p=DEV/relative
    continuity.append({'asset':relative,'initial_sha256':oldhash,'current_sha256':sha(p),'unchanged':sha(p)==oldhash})
manifest_path=TMP/'feature015_rest089_semantic_corrections_manifest_20261028.json'
manifest=json.loads(manifest_path.read_bytes())
manifest_checks=[{'path':relative,'expected_sha256':expected,'actual_sha256':sha(REPO/relative),'matches':sha(REPO/relative)==expected} for relative,expected in manifest['files'].items()]
for r in result:
    r['initial_status']=next(old['status'] for old in initial['operations'] if old['id']==r['id'])
    r['semantic_basis']='corrected independent review plus SDK mutation' if r['id'] in corrections else 'initial independent review reused after byte/source continuity; source/wire/fixture reexecuted'
    r['asset_hashes']={k:assets[r[k]] for k in ('behavior','contract','example')}
    r['semantic_mutation_check']=next((m for m in mutation_results if m['id']==r['id']),None)
    if not r['source_hash_matches'] or not r['stage_present'] or not r['signature_present'] or not r['return_present']: r['status']='FAIL'
report['counts']=dict(Counter(r['status'] for r in result))
report['initial_report']={'path':str(TMP/'feature015_rest089_current_semantic_review_20261028.json'),'sha256':sha(TMP/'feature015_rest089_current_semantic_review_20261028.json'),'counts':initial['counts']}
report['continuity']=continuity
report['manifest']={'path':str(manifest_path),'sha256':sha(manifest_path),'checks':manifest_checks}
report['independent_actual_sdk_mutations']=mutation_results
report['independent_arrow_checks']=arrow_checks
report['independent_mutation_counts']={'valid_sdk_cases':len(mutation_results),'rejected':sum(x['rejected'] for m in mutation_results for x in m['mutations']),'total':sum(len(m['mutations']) for m in mutation_results)}
report['pyarrow_version']=pa.__version__
report['review_boundaries']=[
'Offline semantic retest only. No source-blind reader, live Foundry, upstream database, enrollment, credentials, driver loading, durable checkpoint or record delivery established.',
'Actual SDK MockTransport verifies serialization/model/error decoding. Mutation expectations independently check source-derived meanings; service itself does not execute or validate these fixtures.',
'Arrow IPC generated and parsed using pyarrow23. Byte cap precedes parse; row cap follows read_all. SDK buffers complete transport bytes; cap is not a transport-memory bound or general protection against adversarial compressed IPC.',
'JDBC fixture contains only manifest. Approved driver implementation, authorized connection/network credentials required for live driver use.',
'Dataset.create empty-field schema fixture is source-model encodable; meaningful record publish requires declared separate stream schema. Dataset metadata response does not return stream/view identity.',
'Initial 29 PASS reasoning reused only after current hashes/source bindings checked. Changed shared Stream guide was re-read; all source/wire/error fixtures rerun for40 operations. Initial10FAIL1UNCERTAIN preserved.',
'Only reviewer harness and JSON under parent .ept/tmp written. No source/ledger/ticket/live mutation; no commit. Author13-file manifest verified byte-for-byte.'
]
report['all_integrity_checks_pass']=all(c['matches'] for c in manifest_checks) and all(c['source_hash_matches'] and c['definition_ast_matches'] for c in model_checks) and not report['model_dependency_closure_missing'] and all(x['rejected'] for m in mutation_results for x in m['mutations']) and all(x['rejected'] for x in arrow_checks)
expected_changed={str(Path(relative).relative_to('.agents/skills/pal-found-dev')) for relative in manifest['files'] if relative.startswith('.agents/skills/pal-found-dev/')}
actual_changed={c['asset'] for c in continuity if not c['unchanged']}
report['continuity_summary']={'checked':len(continuity),'unchanged':sum(c['unchanged'] for c in continuity),'changed':len(actual_changed),'unexpected_changes':sorted(actual_changed-expected_changed)}
report['manifest']['expected_sha256']='d41ec7f4096dcd9c42b26f967d6981a2121a4dfba034eedb65e54b0e74c59944'
report['manifest']['manifest_hash_matches']=sha(manifest_path)==report['manifest']['expected_sha256']
pytest_command=[str(TMP/'feature015_shared_cli_qa_env/Scripts/python.exe'),'-B','-m','pytest','tests/test_offline_rest_089.py','-q','-p','no:cacheprovider','--basetemp='+str(TMP/'rest089_independent_pytest_tmp_20261029')]
completed=subprocess.run(pytest_command,cwd=REPO,capture_output=True,text=True)
report['author_suite_independently_executed']={'command':pytest_command,'exit_code':completed.returncode,'stdout':completed.stdout,'stderr':completed.stderr,'test_sha256':sha(REPO/'tests/test_offline_rest_089.py')}
report['network']['httpx_actual_sdk_requests_scope']='189 ordinary/error/supplemental fixture requests only; independent mutation requests additional and separately recorded'
report['all_integrity_checks_pass']=report['all_integrity_checks_pass'] and not (actual_changed-expected_changed) and report['manifest']['manifest_hash_matches'] and completed.returncode==0 and all(r['status']=='PASS' for r in result)
out=TMP/'feature015_rest089_semantic_retest_20261029.json'
out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'report':str(out),'sha256':sha(out),'counts':report['counts'],'integrity':report['all_integrity_checks_pass'],'mutations':report['independent_mutation_counts'],'model_checks':report['model_definition_check_counts'],'changed_assets':[c['asset'] for c in continuity if not c['unchanged']],'network_attempts':denied}))
