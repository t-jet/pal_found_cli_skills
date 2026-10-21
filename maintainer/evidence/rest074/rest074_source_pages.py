from pathlib import Path
p=Path('.ept/tmp/rest074_source_build_cases.py');s=p.read_text();s=s.replace("if field:item[field]=('ri.foundry.main.resource.page'+suffix+'074') if field in ('rid','jobRid') else", "if field:item[field]=('ri.foundry.main.'+('job' if field=='jobRid' else 'transaction')+'.page'+suffix+'074') if field in ('rid','jobRid') else")
s=s.replace("else:page['data']=['ri.foundry.main.resource.page'+suffix+'074']", "else:page['data']=['ri.scheduler.main.schedule.page'+suffix+'074']")
p.write_text(s)
