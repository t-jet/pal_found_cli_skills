"""Review normalization correction while retaining failed execution evidence."""
import ast
import datetime
import hashlib
import inspect
import json
from pathlib import Path
import pydantic
import foundry_sdk._core as core
from foundry_sdk._core.model_base import ModelBase
from foundry_sdk.v2.datasets.models import File

TMP=Path('.ept/tmp')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
harness=TMP/'rest074_formal_execute.py'
old=TMP/'rest074_exec_attempt1_rest074_formal_execute.py'
text=harness.read_text()
restored=text.replace('from datetime import date, datetime, timezone','from datetime import datetime, timezone').replace("mode='python', by_alias=True, exclude_unset=True","mode='json', by_alias=True, exclude_unset=True")
restored=restored.replace("    if isinstance(value, (date, datetime)):\n        return value.isoformat()\n",'')
assert restored==old.read_text(),'Normalization correction includes unreviewed changes'
tree=ast.parse(text)
fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='normalized')
env={'pydantic':pydantic,'datetime':datetime.datetime,'date':datetime.date}
exec(compile(ast.Module(body=[fn],type_ignores=[]),'<reviewed normalized>','exec'),env)
normalize=env['normalized']
literal={'path':'independent/review.csv','transactionRid':'ri.foundry.main.transaction.074','updatedTime':'2026-10-21T08:00:00Z','sizeBytes':37}
sample=File.model_validate(literal)
assert normalize(sample)==normalize(literal)
assert normalize(sample)['sizeBytes']==37
explicit=dict(literal,sizeBytes=None)
assert normalize(File.model_validate(explicit))==normalize(explicit)
omitted=dict(literal);omitted.pop('sizeBytes')
assert normalize(File.model_validate(omitted))==normalize(omitted)
assert normalize(datetime.date(2026,10,21))=='2026-10-21'
approval_path=TMP/'rest074_case_approval.json'
approval=json.loads(approval_path.read_text())
manifest=TMP/'rest074_formal_cases.json'
assert sha(manifest)==approval['manifest']['sha256']
failed=TMP/'rest074_exec_attempt1_rest074_formal_execution.json'
assert json.loads(failed.read_text())['execution']=='FAIL'
model_source=Path(inspect.getfile(ModelBase))
report={'reviewer_identity':'/root/formal074_prepare/independent_review','completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'verdict':'APPROVED','kind':'Harness normalization correction only; no client calls or formal re-execution','previous_harness_sha256':sha(old),'corrected_harness_sha256':sha(harness),'unchanged_manifest_sha256':sha(manifest),'source':{'model_base_path':str(model_source),'model_base_sha256':sha(model_source),'to_dict_source':inspect.getsource(ModelBase.to_dict),'core_Long':'Annotated[int, PlainSerializer(return_type=str, when_used=json)]'},'reason':'JSON serialization converts core.Long values to strings. Typed comparison must use Python values. Preserve aliases and exclude_unset; normalize dates explicitly. Frozen response literals remain unchanged.','checks':{'only_reviewed_normalization_delta':True,'long_integer_preserved':True,'datetime_normalized':True,'date_normalized':True,'explicit_null_preserved':True,'omitted_optional_field_stays_omitted':True,'failed_attempt_preserved':True},'failed_attempt_evidence':{'path':str(failed),'sha256':sha(failed)},'formal_execution':'NOT_RUN_BY_REVIEWER'}
out=TMP/'rest074_review_normalization_approval.json'
out.write_text(json.dumps(report,indent=2)+'\n')
approval['harness']['sha256']=sha(harness)
approval['normalization_correction_review']={'path':str(out),'sha256':sha(out)}
approval['formal_execution']='Attempt1 FAIL retained; corrected harness approved, rerun pending'
approval_path.write_text(json.dumps(approval,indent=2)+'\n')
print(json.dumps({'harness_sha256':sha(harness),'approval_sha256':sha(approval_path),'normalization_review_sha256':sha(out)}))
