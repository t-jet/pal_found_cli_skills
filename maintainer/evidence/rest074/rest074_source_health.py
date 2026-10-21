import pydantic,json
from foundry_sdk.v2.datasets import models as m
s=pydantic.TypeAdapter(m.GetHealthCheckReportsResponse).json_schema()
for name in ['DatasetSubject','CheckReport','Check','BuildStatusCheckConfig']:
 print(name,json.dumps(s['$defs'][name]))
