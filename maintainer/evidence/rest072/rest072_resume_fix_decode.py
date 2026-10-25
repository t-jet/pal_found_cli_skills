"""Preserve attempt 2 and check the SDK's wrapped malformed JSON failure."""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parent
for name in ('formal_execution.json', 'formal_execute.log', 'formal_stdout.log',
             'formal_stderr.log', 'formal_runner.json', 'formal_execute.py'):
    shutil.copy2(root / ('rest072_resume_' + name), root / ('rest072_resume_attempt2_' + name))
path = root / 'rest072_resume_formal_execute.py'
text = path.read_text(encoding='utf-8')
text = text.replace('from foundry_sdk import Config, PalantirRPCException, UserTokenAuth',
                    'from foundry_sdk import Config, PalantirRPCException, UserTokenAuth\nfrom foundry_sdk._errors import SDKInternalError')
old = '''                except (ValueError, pydantic.ValidationError):
                    pass'''
new = '''                except (ValueError, pydantic.ValidationError):
                    pass
                except SDKInternalError as error:
                    assert isinstance(error.__cause__, json.JSONDecodeError), repr(error.__cause__)'''
assert text.count(old) == 1
path.write_text(text.replace(old, new), encoding='utf-8')
print('Attempt 2 preserved; SDK wrapped JSONDecodeError checked.')
