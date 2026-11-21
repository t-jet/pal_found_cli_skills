"""Independent SDK source, HTTP fixture and semantic review; no shared writes."""
from pathlib import Path
import ast
import contextlib
import hashlib
import importlib
import importlib.util
import io
import json
import socket
import subprocess
import time
import traceback

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT / '.ept/tmp/feature015_integration'
BASE = REPO / '.agents/skills/pal-found-dev'
OUT = ROOT / '.ept/tmp/feature015_rest087_current_semantic_review.json'
ORACLE_PATH = REPO / 'tests/fixtures/offline/rest-acceptance/source-oracle.json'
ORACLE = json.loads(ORACLE_PATH.read_text())['operations']
REGISTER = json.loads((REPO / 'maintainer/rest-domain-authoring-register.json').read_text())
INITIAL = json.loads((ROOT / '.ept/tmp/rest087_initial_semantic_findings_20261022.json').read_text())

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def deny(*args, **kwargs):
    raise AssertionError('Independent review denies sockets and DNS')

socket.socket.connect = deny
socket.socket.connect_ex = deny
socket.create_connection = deny
socket.getaddrinfo = deny
guard_pass = False
try:
    socket.getaddrinfo('public.example', 443)
except AssertionError:
    guard_pass = True

NOTES = {
 'Agent.all_sessions': 'Caller/client-bounded sessions, newest updated first; result Agent version string must follow documented major.minor. No tenant visibility proved.',
 'Agent.get': 'Agent RID/version/metadata/parameters read. Latest-published selection and missing-version errors remain distinct from session creation.',
 'AgentVersion.get': 'Version string and numeric major/minor must agree. Version metadata does not include Agent application-variable definitions.',
 'AgentVersion.list': 'Version strings correspond to numeric major/minor; descending ordering and bounded paging are documented, single-page fixture establishes serialization only.',
 'Content.get': 'Exchange user text, generated Markdown and interruptedOutput/trace fields preserve response semantics; content retrieval is separate from continuation.',
 'Session.blocking_continue': 'One complete exchange after create; concurrent requests unsupported. Parameter input keys/types must match Agent configuration; interruptedOutput is preserved.',
 'Session.cancel': 'Message UUID identifies streamed exchange. Optional replacement response omitted; cancellation does not close original stream; request/body matches source.',
 'Session.create': 'Dedicated lifecycle fixture creates empty session with selected Agent version1.0, then reads/lists exact returned identity; no generation claim.',
 'Session.get': 'Dedicated lifecycle fixture checks session and Agent identities, version and zero-message metadata; typed not-found parameters remain scoped to both RIDs.',
 'Session.list': 'Dedicated lifecycle fixture preserves caller/client scope and finite page budget, explicit token progression and returned Agent/session identities.',
 'Session.delete': 'No-content success matches removal endpoint; guide distinguishes deletion from cancelling stream. Offline deletion is response handling only.',
 'Session.rag_context': 'Typed object/function contexts represent configured retrieval and remain distinct from generated answer; override skips automatic retrieval per source.',
 'Session.streaming_continue': 'Ordinary SDK bytes, incremental raw HTTP context rather than SSE events; cancellation UUID and context cleanup documented separately.',
 'Session.update_title': 'No-content response confirms update request handling; title is display metadata, session RID remains identity. Returned-title verification requires subsequent get.',
 'SessionTrace.get': 'Trace UUID, in-progress status and tool groups correspond to diagnostic progress; final completion requires bounded repeated reads, not generated text decoding.',
 'AnthropicModel.messages': 'Bounded maxTokens16 and USER/ASSISTANT content discriminate correctly; stopReason/usage checked. Multiple-input error parameters must exceed one.',
 'OpenAiModel.embeddings': 'Input batch and returned array-of-arrays align positionally. SDK response has no per-vector index field; guide needs explicit positional interpretation.',
 'Experiment.get': 'Experiment RID, parent Model RID, run metadata and discriminated metric/parameter shapes preserved; RUNNING does not establish completion.',
 'Experiment.search': 'Nested predicates follow typed filter union; bounded hits follow source maximum100. Single fixture does not prove full result coverage.',
 'ExperimentArtifactTable.json': 'JSON rows use source table metadata shape; caller must enforce response budget. Transport decoding does not establish artifact completeness.',
 'ExperimentArtifactTable.parquet': 'Binary bytes remain binary under raw response context; fixture checks wire/read/close, not valid Parquet content or tenant artifact availability.',
 'ExperimentSeries.json': 'Time-series typed values and paging match source default200/max1000; caller preserves continuation and bounds total pages.',
 'ExperimentSeries.parquet': 'Binary series response path and model/experiment/series named-error parameters retained; synthetic bytes are not a Parquet execution claim.',
 'LiveDeployment.create': 'Provisioning is asynchronous; direct Model/branch selector and runtime replica configuration preserved. GPU/thread error values must describe actual invalid constraints.',
 'LiveDeployment.get': 'Deployment RID, selected Model/version and isReady are distinct fields; ACTIVE alone is insufficient readiness according to source.',
 'LiveDeployment.list': 'Only direct deployments returned; optional branch selection and response Model/version locators preserved, not indirect deployment discovery.',
 'LiveDeployment.replace': 'Runtime-only replacement retains exact deployment identity; asynchronous rollout requires later state read, errors must express invalid GPU/thread values.',
 'LiveDeployment.transform_json': 'Synthetic feature/score schema explicit, readiness and selected version checked separately; invalid-input, execution-failure and timeout remain distinct.',
 'Model.create': 'Creates empty Model, parent-folder selector distinct from returned Model; no usable version or deployment inferred.',
 'Model.get': 'Frozen response contains Model RID only. Branch/version state requires separate documented operations; no state fields invented in fixture.',
 'Model.promote_version': 'Copy must produce distinct NEW Model Version RID from source; target Model, source version, copied version are different identities.',
 'ModelFunction.create': 'Function locator/apiName/isRowWise returned; compatible Model schema must be read through ModelVersion, not inferred from absent response fields.',
 'ModelFunction.get': 'Response contains function RID/version/displayName/apiName/isRowWise. Parent Model RID is request context; input/output schema comes from ModelVersion.',
 'ModelFunction.replace': 'Function metadata replacement under exact Model RID; response lacks input/output schema, so compatibility checks require ModelVersion.',
 'ModelStudio.create': 'Studio and parent folder identities preserved; creation does not configure or launch training.',
 'ModelStudio.get': 'Studio RID/folder/creation metadata read only; trainer/configuration selection uses separate resource endpoints.',
 'ModelStudio.launch': 'Latest configuration selected at launch time; returned run config_version compared to preread version with documented concurrent-writer race.',
 'ModelStudioConfigVersion.create': 'Trainer ID/version, worker inputs/outputs and resource allocation shape match SDK models; resource string shape alone does not prove schedulable resources.',
 'ModelStudioConfigVersion.get': 'Native SDK integer URL quoting failure retained before HTTP; bounded direct REST read decodes exact SDK model and named errors with response cleanup.',
 'ModelStudioConfigVersion.latest': 'Latest saved configuration read, version number and trainer identity retained; no training or capability claim from synthetic configuration.',
 'ModelStudioConfigVersion.list': 'Saved configuration versions enumerate typed trainer/worker/resource data; caller must bound paging and select returned number.',
 'ModelStudioRun.list': 'Runs retain run/build/job/config identities; submitted/running is distinct from successful training. Optional configuration selector and errors remain typed.',
 'ModelStudioTrainer.get': 'Trainer identity/version/type plus schemas and required inputs/outputs are read metadata; available trainer does not itself create a Studio configuration.',
 'ModelStudioTrainer.list': 'Available trainer list is metadata discovery, experimental flag preserved; real input/output specification and resource compatibility remain separate.',
 'ModelVersion.create': 'New version request carries discriminated model files/API and requirements; synthetic serialization does not deserialize executable dill or solve Conda dependencies.',
 'ModelVersion.get': 'Version RID/API/requirements/backing repositories preserved. Parent Model RID is required request context, not a returned model_rid field.',
 'ModelVersion.list': 'Version identities enumerated for exact parent Model; bounded page retrieval separate from deployment selection and valid model execution.',
}

rows = []
for index, original in enumerate(o for o in REGISTER['operations'] if o['story'] == 'DEV-STORY-087'):
    oid = original['id']; short = '.'.join(oid.split('.')[-2:]); oracle = ORACLE[oid]
    mod = importlib.import_module(oracle['module']); source = Path(mod.__file__)
    text = source.read_text(); tree = ast.parse(text)
    cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == oid.split('.')[-2] + 'Client')
    method = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == oid.split('.')[-1])
    request = next(n for n in ast.walk(method) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == 'RequestInfo')
    wire = {k.arg: ast.unparse(k.value) for k in request.keywords}
    example = BASE / original['example']; behavior = BASE / original['behavior']
    contract = BASE / ('references/rest/contracts/' + oid.replace('.', '/') + '.md')
    values = {}
    for n in ast.parse(example.read_text()).body:
        if isinstance(n, ast.Assign):
            try: values[n.targets[0].id] = ast.literal_eval(n.value)
            except (AttributeError, ValueError, TypeError): pass
    stdout = io.StringIO(); started = time.monotonic(); failure = None
    try:
        with contextlib.redirect_stdout(stdout):
            spec = importlib.util.spec_from_file_location('independent087_' + str(index), example)
            fixture = importlib.util.module_from_spec(spec); spec.loader.exec_module(fixture)
            getattr(fixture, original.get('fixture_entrypoint', 'verify'))()
    except Exception:
        failure = traceback.format_exc()
    findings = []
    errors = values.get('ERRORS', [])
    success = values.get('SUCCESS')
    if short in ('Agent.all_sessions', 'Agent.get', 'AgentVersion.get', 'AgentVersion.list'):
        vv = success.get('data', [success]) if isinstance(success, dict) else []
        for item in vv:
            version = item.get('agentVersion') if short == 'Agent.all_sessions' else item.get('version') if short == 'Agent.get' else item.get('string')
            if not isinstance(version, str) or len(version.split('.')) != 2 or not all(p.isdigit() for p in version.split('.')):
                findings.append({'code': 'AGENT_VERSION_FORMAT', 'reason': 'Source AgentVersionString documents majorVersion.minorVersion; successful version is ' + repr(version)})
            if short.startswith('AgentVersion.') and version != f"{item['version']['major']}.{item['version']['minor']}":
                findings.append({'code': 'AGENT_VERSION_MISMATCH', 'reason': 'Returned version string differs from numeric major/minor details.'})
    for error in errors:
        p = error['parameters']; name = error['name']; why = None
        if name == 'InvalidParameterType' and p['expectedType'] == p['receivedType']:
            why = 'Expected and received parameter types identical.'
        if name == 'GpuTypeNotAvailable' and p['requestedGpuType'] in p['availableGpuTypes']:
            why = 'Requested GPU is in available GPU set.'
        if name == 'InvalidGpuCount' and 1 <= p['providedGpuCount'] <= p['maxGpuCount']:
            why = 'GPU count is inside documented valid1..max range.'
        if name == 'ThreadCountTooHigh' and p['providedThreadCount'] <= p['maxThreadCount']:
            why = 'Provided thread count does not exceed maximum.'
        if name == 'MultipleSystemPromptsNotSupported' and p['systemPromptSize'] <= 1:
            why = 'Multiple system prompts error reports at most one prompt.'
        if name == 'MultipleToolResultContentsNotSupported' and p['toolResultContentsSize'] <= 1:
            why = 'Multiple tool contents error reports at most one content.'
        if why: findings.append({'code': 'ERROR_PARAMETERS_CONTRADICT_SOURCE', 'error': name, 'reason': why})
    if short == 'Model.promote_version' and success['rid'] == values['EXPECTED_BODY']['sourceModelVersionRid']:
        findings.append({'code': 'PROMOTION_REUSES_SOURCE_RID', 'reason': 'Copied version must receive new Model Version RID.'})
    behavior_text = behavior.read_text()
    if short == 'AgentVersion.get' and 'Read one Agent version to check its application-variable and tool definitions' in behavior_text:
        findings.append({'code': 'GUIDE_ABSENT_RETURN_FIELDS', 'reason': 'AgentVersion response only has string/version numeric details; app-variable definitions come from Agent.get with selected version.'})
    if short == 'ModelFunction.get' and 'verify its Model RID and input/output schema' in behavior_text:
        findings.append({'code': 'GUIDE_ABSENT_RETURN_FIELDS', 'reason': 'ModelFunction response lacks Model RID and input/output schema. Model RID is request context; ModelVersion.model_api supplies schema.'})
    if short == 'OpenAiModel.embeddings' and 'each vector index and dimension' in behavior_text:
        findings.append({'code': 'GUIDE_POSITIONAL_VECTOR_MAPPING', 'reason': 'Response data is list[list[float]], no vector index field. Explain positional input/response alignment explicitly.'})
    checks = {
        'source_module_matches_frozen_oracle': sha(source) == oracle['source_sha256'],
        'wire_matches_frozen_oracle': all(wire.get(k) == v for k, v in oracle['wire'].items()),
        'signature_matches_frozen_oracle': ast.unparse(method.args) == oracle['ordinary']['signature'],
        'fixture_executes_under_network_denial': failure is None,
        'contract_exists': contract.is_file(),
        'behavior_exists': behavior.is_file(),
    }
    for check, passed in checks.items():
        if not passed: findings.append({'code': 'CHECK_FAILED', 'check': check, 'reason': 'Independent check failed.'})
    family = '.'.join(oid.split('.')[:2]); model_module = Path(importlib.import_module('foundry_sdk.' + family + '.models').__file__)
    error_module = Path(importlib.import_module('foundry_sdk.' + family + '.errors').__file__)
    rows.append({
        'id': oid, 'verdict': 'FAIL' if findings else 'PASS',
        'source_module': str(source), 'source_module_sha256': sha(source),
        'source_method_lines': [method.lineno, method.end_lineno],
        'source_method_sha256': hashlib.sha256(ast.get_source_segment(text, method).encode()).hexdigest(),
        'source_docstring_sha256': hashlib.sha256(ast.get_docstring(method).encode()).hexdigest(),
        'frozen_documentation_sha256': oracle['documentation']['doc_sha256'],
        'source_model_module': str(model_module), 'source_model_module_sha256': sha(model_module),
        'source_error_module': str(error_module), 'source_error_module_sha256': sha(error_module),
        'behavior_path': original['behavior'], 'behavior_sha256': sha(behavior),
        'example_path': original['example'], 'example_sha256': sha(example),
        'contract_path': contract.relative_to(BASE).as_posix(), 'contract_sha256': sha(contract),
        'checks': checks, 'findings': findings,
        'manual_semantic_review': NOTES[short],
        'declared_error_count': len(errors),
        'fixture': {'status': 'PASS' if failure is None else 'FAIL', 'elapsed_seconds': round(time.monotonic()-started, 6), 'stdout': stdout.getvalue(), 'error': failure,
            'transport_scope': 'Real SDK request serialization through httpx.MockTransport plus response/error decode. ModelStudioConfigVersion.get preserves native pre-HTTP defect and uses separate bounded direct REST adapter. Shared sessions.py verifies create/get/list together.'},
    })

report = {
    'story': 'DEV-STORY-087', 'reviewer_agent': '/root/rest087_review_resume',
    'date': '2026-10-22 Europe/Sofia',
    'candidate_commit': subprocess.check_output(['git','rev-parse','HEAD'], cwd=REPO, text=True).strip(),
    'candidate_scope': 'Per-asset hashes bind current working tree; separate authors may edit owned files. Commit alone does not identify uncommitted assets.',
    'sdk_release': '1.101.0', 'oracle_sha256': sha(ORACLE_PATH),
    'network_guard': {'connect_connect_ex_create_connection_getaddrinfo': 'denied', 'guard_self_test': guard_pass},
    'scope': 'Independent manual lifecycle, identity, response model/error constraint review plus source AST/oracle and actual mocked HTTP fixtures. No tracker/ledger changes, formal QA acceptance or live tenant claim.',
    'initial_findings_artifact': {'path': '.ept/tmp/rest087_initial_semantic_findings_20261022.json', 'sha256': sha(ROOT / '.ept/tmp/rest087_initial_semantic_findings_20261022.json')},
    'summary': {v: sum(r['verdict'] == v for r in rows) for v in ('PASS','FAIL','UNCERTAIN')},
    'operations': rows,
}
assert len(rows) == 47
OUT.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report['summary']))
print('source/check failures', [(r['id'], [k for k,v in r['checks'].items() if not v]) for r in rows if not all(r['checks'].values())])
print('report', OUT)
