"""Preserve attempt 3 and test decoded pages and ordinary iterator modes."""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parent
for name in ('formal_execution.json', 'formal_execute.log', 'formal_stdout.log',
             'formal_stderr.log', 'formal_runner.json', 'formal_execute.py'):
    shutil.copy2(root / ('rest072_resume_' + name), root / ('rest072_resume_attempt3_' + name))
path = root / 'rest072_resume_formal_execute.py'
text = path.read_text(encoding='utf-8')
text = text.replace("return getattr(client, method)(**copy.deepcopy(kwargs), request_timeout=7)",
                    "return getattr(client, method)(**copy.deepcopy(kwargs), request_timeout=7, _sdk_internal={'response_mode': 'DECODED'})")
needle = 'def execute(manifest):'
addition = '''async def ordinary_async_iterator(case, cls, method):
    calls = []
    def handler(request):
        calls.append(request)
        wire_check(request, case['request']['expected_wire'])
        return httpx.Response(200, json=case['success']['json'])
    async with async_resource(cls, handler) as (client, _):
        iterator = getattr(client, method)(**case['request']['kwargs'], request_timeout=7)
        assert not inspect.isawaitable(iterator)
        assert normalized(await anext(iterator)) == normalized(case['success']['json']['data'][0])
    assert len(calls) == 1
    record(case['case_id'], 'ordinary_async_iterator_bounded', requests=1)


def ordinary_iterator(case, module, cls, method):
    calls = []
    def handler(request):
        calls.append(request)
        wire_check(request, case['request']['expected_wire'])
        return httpx.Response(200, json=case['success']['json'])
    with resource(cls, handler) as (client, _):
        iterator = getattr(client, method)(**case['request']['kwargs'], request_timeout=7)
        assert normalized(next(iterator)) == normalized(case['success']['json']['data'][0])
    assert len(calls) == 1
    record(case['case_id'], 'ordinary_sync_iterator_bounded', requests=1)
    EVENT_LOOP.run_until_complete(ordinary_async_iterator(case, getattr(module, 'Async' + cls.__name__), method))


'''
assert text.count(needle) == 1
text = text.replace(needle, addition + needle)
needle = "        success(case, cls, method)\n"
assert text.count(needle) == 1
text = text.replace(needle, "        if 'ITERATOR' in case['source']['request_expressions']['response_mode']:\n            ordinary_iterator(case, module, cls, method)\n" + needle)
path.write_text(text, encoding='utf-8')
print('Attempt 3 preserved. Explicit decoded pages plus bounded sync/async iterator checks.')
