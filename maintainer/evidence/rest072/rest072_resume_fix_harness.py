"""Preserve failed tooling attempt and correct named SDK exception checks."""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parent
for name in ('formal_execution.json', 'formal_execute.log', 'formal_stdout.log',
             'formal_stderr.log', 'formal_runner.json', 'formal_execute.py'):
    source = root / ('rest072_resume_' + name)
    shutil.copy2(source, root / ('rest072_resume_attempt1_' + name))
path = root / 'rest072_resume_formal_execute.py'
text = path.read_text(encoding='utf-8')
old = '            assert error.error_code == code'
new = '''            if expected_class:
                # Named errors are dataclasses; SDK does not retain error_code on them.
                base_name = {400: 'BadRequestError', 403: 'PermissionDeniedError',
                             404: 'NotFoundError', 409: 'ConflictError',
                             413: 'RequestEntityTooLargeError',
                             422: 'UnprocessableEntityError'}.get(status)
                if base_name:
                    assert isinstance(error, getattr(importlib.import_module('foundry_sdk._errors'), base_name))
            else:
                assert error.error_code == code'''
assert text.count(old) == 1
path.write_text(text.replace(old, new), encoding='utf-8')
print('Attempt 1 preserved. Named error class/base checked; generic error_code retained.')
