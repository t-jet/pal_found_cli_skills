from pathlib import Path
p=Path('.ept/tmp/rest074_source_build_cases.py');s=p.read_text();s=s.replace("elif k=='page_size':kw[k]=2", "elif k=='path_prefix':kw[k]='inspections-independent/'\n  elif k=='page_size':kw[k]=2")
s=s.replace("BINARY='inspection,status\\n074,independent\\n'", "BINARY='inspection_id,status\\n074,independent\\n'")
s=s.replace("SCHEMA={'fieldSchemaList':[{'type':'STRING','name':'inspection_id','nullable':False}]}","SCHEMA={'fieldSchemaList':[{'type':'STRING','name':'inspection_id','nullable':False},{'type':'STRING','name':'status','nullable':False}]}")
needle=" success={'http_status':204 if ret is None else 200"
insert=""" if op=='v2.datasets.Dataset.get_health_check_reports':
  reply={'data':{'ri.health.main.check.independent074':{'rid':'ri.health.main.report.independent074','check':{'rid':'ri.health.main.check.independent074','groups':[],'config':{'type':'buildStatus','subject':{'datasetRid':DATASET,'branchId':'master'},'statusCheckConfig':{'severity':'CRITICAL'}}},'result':{'status':'PASSED'},'createdTime':'2026-10-21T08:00:00Z'}}}
 if op=='v2.datasets.Dataset.get_health_checks':reply={'data':['ri.health.main.check.independent074']}
 if op=='v2.datasets.Dataset.get_schedules':reply={'data':['ri.scheduler.main.schedule.independent074']}
 if op=='v2.datasets.Dataset.jobs':reply={'data':[{'jobRid':'ri.foundry.main.job.independent074'}]}
 if op=='v2.datasets.Transaction.build':reply='ri.foundry.main.build.independent074'
 if op=='v2.datasets.Transaction.job':reply='ri.foundry.main.job.independent074'
 if fn=='transactions':
  reply={'data':[{'rid':TX,'transactionType':'APPEND','status':'COMMITTED','createdTime':'2026-10-21T08:00:00Z','closedTime':'2026-10-21T08:01:00Z'}]}
 if r=='File' and fn=='list':reply={'data':[{'path':'inspections-independent/status.csv','transactionRid':TX,'updatedTime':'2026-10-21T08:00:00Z','sizeBytes':len(BINARY.encode())}]}
"""
s=s.replace(needle,insert+needle)
s=s.replace("'Assert ordinary result equals content_utf8 encoded as UTF-8 bytes.'", "'Assert ordinary result equals bytes.fromhex(content_hex).'")
s=s.replace("'Typed return normalizes to success.json'", "'Typed return normalizes to success.json'")
s=s.replace("'source_condition':", "'source_condition':")
p.write_text(s)
