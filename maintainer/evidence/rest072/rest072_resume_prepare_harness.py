"""Preserve original harness while naming this executor's output artifacts."""
from pathlib import Path

root = Path(__file__).resolve().parent
text = (root / 'rest072_formal_execute.py').read_text(encoding='utf-8')
text = text.replace("PENDING = TMP / 'rest072_formal_execution_pending.json'",
                    "PENDING = TMP / 'rest072_resume_formal_execution.json'")
text = text.replace("LOG = TMP / 'rest072_formal_execute.log'",
                    "LOG = TMP / 'rest072_resume_formal_execute.log'")
text = text.replace("evidence = dict(story='DEV-STORY-072', testcase='TESTCASE-075',",
                    "evidence = dict(story='DEV-STORY-072', testcase='TESTCASE-075', executor_identity='/root/formal072_resume/independent072',")
(root / 'rest072_resume_formal_execute.py').write_text(text, encoding='utf-8')
print('Fresh harness prepared; execution NOT_RUN')
