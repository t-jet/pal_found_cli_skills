import importlib,pydantic,json
for ver in ('v1','v2'):
 m=importlib.import_module('foundry_sdk.'+ver+'.datasets.models')
 for n in ('Branch','Dataset','Transaction','GetDatasetSchemaResponse','GetSchemaDatasetsBatchResponse','GetHealthCheckReportsResponse','ListHealthChecksResponse','GetJobResponse','GetSchemaDatasetsBatchRequestElement','GetDatasetJobsSort','GetDatasetJobsQuery','DatasetSchema'):
  if hasattr(m,n):
   s=pydantic.TypeAdapter(getattr(m,n)).json_schema(); print(ver,n,json.dumps(s))
