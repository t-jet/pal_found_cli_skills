"""Prepare a REST074 harness from independently exercised transport utilities."""
from pathlib import Path

TMP = Path(__file__).resolve().parent
text = (TMP / 'rest072_resume_formal_execute.py').read_text(encoding='utf-8')
text = text.replace('REST072', 'REST074').replace('rest072', 'rest074').replace('DEV-STORY-072', 'DEV-STORY-074').replace('TESTCASE-075', 'TESTCASE-076').replace('independent-qa-072', 'independent-qa-074').replace('000000000072', '000000000074').replace('/root/formal072_resume/independent072', '/root/formal074_prepare/independent_review')
text = text.replace("rest074_resume_formal_execution.json", "rest074_formal_execution.json").replace("rest074_resume_formal_execute.log", "rest074_formal_execute.log")
text = text.replace("assert len(manifest['operations']) == 40", "assert len(manifest['operations']) == 52")
start = text.index('def semantic_check(')
end = text.index('\n\ndef success(', start)
text = text[:start] + '''def semantic_check(case, kwargs, value, label):
    operation = case['operation']
    if value is None or not isinstance(value, dict):
        return
    if '.File.' in operation and operation.rsplit('.', 1)[1] in ('get', 'upload'):
        assert value['path'] == kwargs['file_path'], 'Returned metadata belongs to another file'
    if operation in ('v2.datasets.Dataset.get_schema', 'v2.datasets.Dataset.put_schema'):
        assert value['branchName'] == kwargs['branch_name'], 'Returned schema belongs to another branch'
        if operation.endswith('.put_schema'):
            assert value['schema'] == kwargs['schema']
    if operation == 'v2.datasets.View.add_primary_key':
        assert value['primaryKey'] == kwargs['primary_key']
    if operation == 'v2.datasets.View.remove_backing_datasets':
        branch = kwargs.get('branch', 'master')
        removed = {(item['datasetRid'], item.get('branch', branch)) for item in kwargs['backing_datasets']}
        returned = {(item['datasetRid'], item.get('branch', branch)) for item in value['backingDatasets']}
        assert removed.isdisjoint(returned)
        assert returned, 'Independent removal fixture must retain a distinct survivor'
    if '.Transaction.' in operation:
        if operation.endswith('.abort'):
            assert value['status'] == 'ABORTED'
        if operation.endswith('.commit'):
            assert value['status'] == 'COMMITTED'
        if operation.endswith('.create'):
            assert value['status'] == 'OPEN'
        if 'transaction_rid' in kwargs and 'rid' in value:
            assert value['rid'] == kwargs['transaction_rid']


def materialize(value):
    if isinstance(value, dict):
        if set(value) == {'__bytes_hex__'}:
            return bytes.fromhex(value['__bytes_hex__'])
        return {key: materialize(item) for key, item in value.items()}
    if isinstance(value, list):
        return [materialize(item) for item in value]
    return value


def response(reply):
    if 'content_hex' in reply:
        return httpx.Response(reply['http_status'], content=bytes.fromhex(reply['content_hex']))
    if reply['http_status'] == 204:
        return httpx.Response(204)
    return httpx.Response(reply['http_status'], json=reply['json'])


def expected_result(reply):
    return bytes.fromhex(reply['content_hex']) if 'content_hex' in reply else reply['json']
''' + text[end:]
text = text.replace("body = json.loads(request.content) if request.content else None\n    assert body == expected['body'], (body, expected['body'])", "expected_body = materialize(expected['body'])\n    body = request.content if isinstance(expected_body, bytes) else (json.loads(request.content) if request.content else None)\n    assert body == expected_body, (body, expected_body)")
text = text.replace('**copy.deepcopy(kwargs)', '**materialize(copy.deepcopy(kwargs))')
text = text.replace("response = (httpx.Response(204) if reply['http_status'] == 204 else\n                        httpx.Response(reply['http_status'], json=reply['json']))", "reply_response = response(reply)")
text = text.replace("response = (httpx.Response(reply['http_status']) if reply['http_status'] == 204\n                        else httpx.Response(reply['http_status'], json=reply['json']))", "reply_response = response(reply)")
text = text.replace('responses.append(response)\n            return response', 'responses.append(reply_response)\n            return reply_response')
text = text.replace("normalized(case['success']['json'])", "normalized(expected_result(case['success']))")
text = text.replace("expected = reply['json']", "expected = expected_result(reply)")
text = text.replace("pydantic.TypeAdapter(hints[key]).validate_python(value)", "pydantic.TypeAdapter(hints[key]).validate_python(materialize(value))")
text = text.replace("pydantic.TypeAdapter(response_type).validate_python(case['success']['json'])", "pydantic.TypeAdapter(response_type).validate_python(expected_result(case['success']))")
text = text.replace("semantic_check(case, case['request']['kwargs'], case['success']['json'], 'success')", "semantic_check(case, case['request']['kwargs'], expected_result(case['success']), 'success')")
text = text.replace("if case['success']['http_status'] != 204:", "if case['success']['http_status'] != 204 and 'content_hex' not in case['success']:")
# Replace domain-specific additional-case dispatcher with literal, explicit variants.
start = text.index("        for extra in case.get('additional_cases', []):", text.index('def execute('))
end = text.index('\n\ndef preflight(', start)
text = text[:start] + '''        for extra in case.get('additional_cases', []):
            label = extra['name']
            if 'requests' in extra:
                calls = []
                def page(request):
                    index = len(calls)
                    assert index < len(extra['requests']), 'finite page budget exceeded'
                    wire_check(request, extra['expected_wires'][index])
                    calls.append(request)
                    return httpx.Response(200, json=extra['responses'][index])
                with resource(cls, page) as (client, _):
                    token, items = None, []
                    for index, kwargs in enumerate(extra['requests']):
                        assert kwargs.get('page_token') == token
                        result = normalized(invoke(client, method, kwargs))
                        assert result == normalized(extra['responses'][index])
                        items.extend(result['data'])
                        token = result.get('nextPageToken')
                    assert token == extra['expected_terminal_token']
                    assert len(items) == 2 and items[0] != items[1]
                assert len(calls) == extra['expected_request_count']
                record(case['case_id'], label, requests=len(calls), items=items)
            elif 'error' in extra:
                error = next(row for row in case['errors'] if row['name'] == extra['error'])
                failure(case, cls, method, error['status'], error['name'], error['errorCode'], error['parameters'], error['expected']['exception_class'], extra['request'], extra['expected_wire'])
            elif 'request' in extra and 'expected_wire' in extra:
                reply = extra.get('success', dict(http_status=extra.get('response_status', case['success']['http_status']), json=extra.get('response', extra.get('expected_result'))))
                success(case, cls, method, extra['request'], extra['expected_wire'], reply, label)
            elif label != 'required argument omitted':
                raise AssertionError('Additional case lacks executable expectations: ' + label)
''' + text[end:]
# Streaming wrappers share wire and typed or binary result oracles, with explicit context closure.
start = text.index('\n\ndef execute(')
stream = '''

def streaming_success(case, cls, method):
    calls, responses = [], []
    def handler(request):
        wire_check(request, case['request']['expected_wire'])
        calls.append(request)
        reply = response(case['success'])
        responses.append(reply)
        return reply
    with resource(cls, handler) as (client, _):
        if not hasattr(client.with_streaming_response, method):
            return
        with getattr(client.with_streaming_response, method)(**materialize(case['request']['kwargs']), request_timeout=7) as wrapper:
            assert normalized(wrapper.decode()) == normalized(expected_result(case['success']))
        assert responses[0].is_closed
    assert len(calls) == 1
    record(case['case_id'], 'sync_stream_closed', requests=1)


async def async_streaming_success(case, cls, method):
    calls, responses = [], []
    def handler(request):
        wire_check(request, case['request']['expected_wire'])
        calls.append(request)
        reply = response(case['success'])
        responses.append(reply)
        return reply
    async with async_resource(cls, handler) as (client, _):
        if not hasattr(client.with_streaming_response, method):
            return
        async with getattr(client.with_streaming_response, method)(**materialize(case['request']['kwargs']), request_timeout=7) as wrapper:
            assert normalized(await wrapper.decode()) == normalized(expected_result(case['success']))
        assert responses[0].is_closed
    assert len(calls) == 1
    record(case['case_id'], 'async_stream_closed', requests=1)
'''
text = text[:start] + stream + text[start:]
text = text.replace("        for error in case['errors']:\n            failure(", "        streaming_success(case, cls, method)\n        EVENT_LOOP.run_until_complete(async_streaming_success(case, getattr(module, 'Async' + name + 'Client'), method))\n        for error in case['errors']:\n            failure(")
text = text.replace("PENDING = TMP / 'rest074_formal_execution.json'", "PENDING = TMP / 'rest074_formal_execution.json'")
# This generation prepares files only; formal execution remains gated in main().
compile(text, str(TMP / 'rest074_formal_execute.py'), 'exec')
(TMP / 'rest074_formal_execute.py').write_text(text, encoding='utf-8')
print('REST074 harness prepared; execution NOT_RUN')
