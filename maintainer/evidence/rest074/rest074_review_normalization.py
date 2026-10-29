"""Inspect original SDK Python versus JSON model values without operation calls."""
import datetime
import hashlib
import inspect
import json
from pathlib import Path
import foundry_sdk._core as core
from foundry_sdk._core.model_base import ModelBase
from foundry_sdk.v2.datasets.models import File

manifest=json.loads(Path('.ept/tmp/rest074_formal_cases.json').read_text())
nulls=[]
def walk(value,path):
    if isinstance(value,dict):
        for key,item in value.items():
            if item is None:nulls.append(path+'.'+key)
            else:walk(item,path+'.'+key)
    elif isinstance(value,list):
        for index,item in enumerate(value):walk(item,path+'['+str(index)+']')
for row in manifest['operations']:
    walk(row['success']['json'],row['operation']+'.success')
    for extra in row['additional_cases']:
        if 'success' in extra:walk(extra['success'].get('json'),row['operation']+'.'+extra['name'])
        if 'response' in extra:walk(extra['response'],row['operation']+'.'+extra['name'])
        for index,r in enumerate(extra.get('responses',[])):walk(r,row['operation']+'.'+extra['name']+str(index))
sample=File.model_validate({'path':'x','transactionRid':'ri.foundry.main.transaction.074','updatedTime':'2026-10-21T08:00:00Z','sizeBytes':37})
assert sample.model_dump(mode='json',by_alias=True,exclude_unset=True)['sizeBytes']=='37'
assert sample.to_dict()['sizeBytes']==37
assert sample.model_dump(mode='python',by_alias=True,exclude_unset=True)['sizeBytes']==37
print(json.dumps({'nested_explicit_nulls':nulls,'to_dict_source':inspect.getsource(ModelBase.to_dict),'core_Long':str(core.Long),'python_dump':repr(sample.model_dump(mode='python',by_alias=True,exclude_unset=True))}))
