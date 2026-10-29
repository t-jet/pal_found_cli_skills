"""Preserve passing attempt 4 and exercise iterator termination explicitly."""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parent
for name in ('formal_execution.json', 'formal_execute.log', 'formal_stdout.log',
             'formal_stderr.log', 'formal_runner.json', 'formal_execute.py'):
    shutil.copy2(root / ('rest072_resume_' + name), root / ('rest072_resume_attempt4_' + name))
path = root / 'rest072_resume_formal_execute.py'
text = path.read_text(encoding='utf-8')
start = text.index('async def ordinary_async_iterator(')
end = text.index('def execute(manifest):', start)
replacement = '''def iterator_fixture(case):
    fixture = next(row for row in case['additional_cases'] if row['name'] == 'finite continuation')
    assert fixture['expected_terminal_token'] is None
    assert not fixture['responses'][-1].get('nextPageToken')
    return fixture


async def ordinary_async_iterator(case, cls, method):
    fixture, calls = iterator_fixture(case), []
    def handler(request):
        index = len(calls)
        assert index < fixture['expected_request_count'], 'iterator exceeded finite page budget'
        wire_check(request, fixture['expected_wires'][index])
        calls.append(request)
        return httpx.Response(200, json=fixture['responses'][index])
    async with async_resource(cls, handler) as (client, _):
        iterator = getattr(client, method)(**fixture['requests'][0], request_timeout=7)
        assert not inspect.isawaitable(iterator)
        items = []
        async for item in iterator:
            items.append(normalized(item))
            assert len(items) <= 2
        assert items == normalized([item for page in fixture['responses'] for item in page['data']])
    assert len(calls) == fixture['expected_request_count']
    record(case['case_id'], 'ordinary_async_iterator_terminal_closed', requests=len(calls), items=items)


def ordinary_iterator(case, module, cls, method):
    fixture, calls = iterator_fixture(case), []
    def handler(request):
        index = len(calls)
        assert index < fixture['expected_request_count'], 'iterator exceeded finite page budget'
        wire_check(request, fixture['expected_wires'][index])
        calls.append(request)
        return httpx.Response(200, json=fixture['responses'][index])
    with resource(cls, handler) as (client, _):
        iterator = getattr(client, method)(**fixture['requests'][0], request_timeout=7)
        items = [normalized(item) for item in iterator]
        assert items == normalized([item for page in fixture['responses'] for item in page['data']])
    assert len(calls) == fixture['expected_request_count']
    record(case['case_id'], 'ordinary_sync_iterator_terminal_closed', requests=len(calls), items=items)
    EVENT_LOOP.run_until_complete(ordinary_async_iterator(case, getattr(module, 'Async' + cls.__name__), method))


'''
path.write_text(text[:start] + replacement + text[end:], encoding='utf-8')
print('Passing attempt 4 preserved; ordinary iterators now reach exact two-page terminal state.')
