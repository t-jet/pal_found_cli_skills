"""Independent REST079 case harness; author validation cannot confer formal acceptance."""
import argparse
import ast
import asyncio
import copy
import dataclasses
import hashlib
import importlib
import importlib.metadata
import inspect
import json
from pathlib import Path
import socket
import sys
import textwrap
import time
from unittest.mock import patch
from contextlib import contextmanager, asynccontextmanager
from urllib.parse import unquote

import httpx
import pydantic
from foundry_sdk import Config, UserTokenAuth, PermissionDeniedError, ReadTimeout, _core

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
AUTHOR = '/root/rest079_formal_case_author_recover_20261118'
TOKEN = 'independent-qa079-token'
ROWS = []


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def record(case, name, **details):
    ROWS.append({'case_id': case['case_id'] if isinstance(case, dict) else case,
                 'check': name, 'result': 'PASS', **details})


def normalize(value):
    if isinstance(value, pydantic.BaseModel):
        return value.model_dump(mode='json', by_alias=True, exclude_unset=True)
    if isinstance(value, (list, tuple)):
        return [normalize(child) for child in value]
    if isinstance(value, dict):
        return {key: normalize(child) for key, child in value.items()}
    return value


def class_for(case, asynchronous=False):
    resource = case['operation'].split('.')[2]
    return getattr(importlib.import_module(case['source']['module']), ('Async' if asynchronous else '') + resource + 'Client')


@contextmanager
def sync_client(case, handler):
    with httpx.Client(transport=httpx.MockTransport(handler), timeout=7) as session:
        with patch('foundry_sdk._core.api_client.HttpClient', return_value=session):
            client = class_for(case)(auth=UserTokenAuth(token=TOKEN), hostname='qa079.invalid',
                                     config=Config(timeout=7, max_retries=0))
        yield client
    assert session.is_closed


@asynccontextmanager
async def async_client(case, handler):
    async with httpx.AsyncClient(transport=httpx.MockTransport(handler), timeout=7) as session:
        with patch('foundry_sdk._core.api_client.AsyncHttpClient', return_value=session):
            client = class_for(case, True)(auth=UserTokenAuth(token=TOKEN), hostname='qa079.invalid',
                                           config=Config(timeout=7, max_retries=0))
        yield client
    assert session.is_closed


def invoke(client, case, mode, kwargs=None):
    target = {'ordinary': client, 'raw': client.with_raw_response, 'stream': client.with_streaming_response}[mode]
    arguments = copy.deepcopy(case['kwargs'] if kwargs is None else kwargs)
    timeout = arguments.pop('request_timeout', 7)
    return getattr(target, case['operation'].split('.')[-1])(**arguments, request_timeout=timeout)


def check_wire(request, case):
    wire = case['wire']
    assert request.method == wire['method']
    assert unquote(request.url.path) == '/api' + wire['path']
    assert sorted(request.url.params.multi_items()) == sorted(httpx.QueryParams(wire['query']).multi_items())
    assert request.headers['Authorization'] == 'Bearer ' + TOKEN
    for name, value in wire['headers'].items():
        assert request.headers[name] == value
    assert (json.loads(request.content) if request.content else None) == wire['body']
    assert request.extensions['timeout'] == dict(connect=7, read=7, write=7, pool=7)


def typed_value(case, value, element=False):
    module_name, name = case['source']['element_type' if element else 'response_type'].rsplit('.', 1)
    expected = getattr(importlib.import_module(module_name), name)
    assert type(value) is expected, (type(value), expected)
    return normalize(value)


def semantic(case, value):
    category = case['semantic']
    if isinstance(value, list):
        for item in value:
            semantic(case, item)
        return
    if category not in ('aggregate_schema', 'history') and 'data' in value:
        values = value['data']
        if isinstance(values, dict):
            assert set(values) == {'ri.qa.main.object-type.device079'}
            values = [item for children in values.values() for item in children]
        for item in values:
            semantic(case, item)
        return
    if case['semantic'] == 'device_schema':
        assert value['apiName'] == 'Device079'
        if 'object_type' in case['kwargs']:
            assert value['apiName'] == case['kwargs']['object_type']
        for selector in ('primaryKey', 'titleProperty'):
            field = value[selector]
            assert field in value['properties']
            assert value['properties'][field]['dataType'] == {'type': 'string'}
        assert value['primaryKey'] == 'deviceId' and value['titleProperty'] == 'label'
    elif case['semantic'] == 'action_rule':
        summary = value['actionType']
        assert summary['apiName'] == 'rename-device079'
        if 'action_type' in case['kwargs']:
            assert summary['apiName'] == case['kwargs']['action_type']
        operation, = summary['operations']
        rule, = value['fullLogicRules']
        assert operation == {'type': 'modifyInterfaceObject', 'interfaceTypeApiName': 'Inspectable079'}
        assert rule['type'] == 'modifyInterface'
        parameter = summary['parameters'][rule['interfaceObjectToModify']]
        assert parameter['required'] is True
        assert parameter['dataType'] == {'type': 'interfaceObject', 'interfaceTypeApiName': 'Inspectable079'}
        assert rule['sharedPropertyArguments'] == {'label': {'type': 'parameterId', 'parameterId': 'labelText'}}
        assert summary['parameters']['labelText']['dataType'] == {'type': 'string'}
    elif case['semantic'] == 'aggregate_schema':
        body = case['wire']['body']
        schema = {'deviceId': 'string', 'label': 'string', 'recordedAt': 'timestamp'}
        for selector in body['aggregation'] + body['groupBy']:
            assert ('field' in selector) != ('propertyIdentifier' in selector)
            name = selector.get('field') or selector['propertyIdentifier']['apiName']
            assert name in schema
            if selector['type'] == 'duration':
                assert schema[name] in ('timestamp', 'date')
                if selector['unit'] in ('YEARS', 'QUARTERS', 'MONTHS', 'WEEKS'):
                    assert selector['value'] == 1
        bucket, = value['data']
        assert bucket['metrics'] == [{'name': body['aggregation'][0]['name'], 'value': 2}]
        assert bucket['group'] == {'recordedAt': '2026-11-16T00:00:00Z'}
        assert value['accuracy'] == 'APPROXIMATE'
    elif category == 'action_summary':
        assert value['apiName'] == 'rename-device079'
        assert value['parameters']['device']['dataType'] == {'type': 'interfaceObject', 'interfaceTypeApiName': 'Inspectable079'}
        assert value['parameters']['labelText']['dataType'] == {'type': 'string'}
        assert value['parameters']['device']['required'] and value['parameters']['labelText']['required']
        assert value['operations'] == [{'type': 'modifyInterfaceObject', 'interfaceTypeApiName': 'Inspectable079'}]
    elif category == 'device_full':
        semantic({**case, 'semantic': 'device_schema'}, value['objectType'])
        assert value['implementsInterfaces'] == ['Inspectable079']
        assert set(value['implementsInterfaces2']) == {'Inspectable079'}
        mapping = value['implementsInterfaces2']['Inspectable079']
        assert mapping['links'] == {'inspectedPeers079': ['relatedDevices079']}
        for field, kind in [('deviceId', 'string'), ('label', 'string'), ('recordedAt', 'timestamp')]:
            local = mapping['properties'][field]
            assert local in value['objectType']['properties']
            assert value['sharedPropertyTypeMapping'][field] == local
            assert mapping['propertiesV2'][field] == {'type': 'localPropertyImplementation', 'propertyApiName': local}
            assert value['objectType']['properties'][local]['dataType'] == {'type': kind}
        semantic({**case, 'semantic': 'object_link'}, value['linkTypes'][0])
    elif category == 'object_link':
        assert value['apiName'] == 'relatedDevices079'
        assert value['objectTypeApiName'] == 'Device079' and value['cardinality'] == 'MANY'
    elif category == 'interface_link':
        assert value['apiName'] == 'inspectedPeers079' and value['required'] is True
        assert value['linkedEntityApiName'] == {'type': 'interfaceTypeApiName', 'apiName': 'Inspectable079'}
        assert value['cardinality'] == 'MANY'
    elif category == 'interface':
        assert value['apiName'] == 'Inspectable079'
        assert value['extendsInterfaces'] == value['allExtendsInterfaces'] == []
        assert value['apiName'] not in value['extendsInterfaces'] + value['allExtendsInterfaces']
        assert value['implementedByObjectTypes'] == ['Device079']
        for name, kind in [('deviceId', 'string'), ('label', 'string'), ('recordedAt', 'timestamp')]:
            for field in ('properties', 'allProperties', 'propertiesV2'):
                assert value[field][name]['dataType'] == {'type': kind}
                assert value[field][name]['required'] is True
            assert value['allPropertiesV2'][name]['requireImplementation'] is True
        assert value['links'] == value['allLinks']
        semantic({**case, 'semantic': 'interface_link'}, value['links']['inspectedPeers079'])
    elif category == 'object_record':
        key = 'D-080' if case['operation'].endswith('.list_interface_linked_objects') else 'D-079'
        assert value['__apiName'] == 'Device079' and value['__primaryKey'] == value['deviceId'] == key
        assert value['label'] == 'Device ' + key and value['recordedAt'] == '2026-11-16T08:00:00Z'
    elif category == 'history':
        for entry in value['data']:
            primary = entry['objectPrimaryKey']['deviceId']
            assert primary == {'type': 'stringValue', 'value': 'D-079'}
            assert entry['edit']['type'] == 'createEdit' and entry['edit']['objectType'] == 'Device079'
            assert entry['edit']['properties']['deviceId'] == primary['value']
            assert entry['edit']['properties']['label'] == 'Valve 079'
            assert entry['timestamp'] == '2026-11-16T08:00:00+00:00'
    elif category == 'value_type':
        assert value['apiName'] == 'InspectionDate079' and value['version'] == '3'
        assert value['fieldType'] == {'type': 'date'} and value['constraints'] == []
    elif category == 'query':
        assert value['apiName'] == 'countDevices079' and value['version'] == '2.3.0'
        assert value['parameters']['labelPrefix'] == {'dataType': {'type': 'string'}, 'required': True}
        assert value['output'] == {'type': 'integer'} and value['typeReferences'] == {}
    elif category == 'ontology':
        assert value['apiName'] == 'qa-ontology079' and value['rid'] == 'ri.qa.main.ontology.inspection079'
    elif category == 'ontology_full':
        semantic({**case, 'semantic': 'ontology'}, value['ontology'])
        for field, key, nested in [('objectTypes', 'Device079', 'device_full'),
                                    ('actionTypes', 'rename-device079', 'action_summary'),
                                    ('queryTypes', 'countDevices079', 'query'),
                                    ('interfaceTypes', 'Inspectable079', 'interface'),
                                    ('valueTypes', 'InspectionDate079', 'value_type')]:
            assert set(value[field]) == {key}
            semantic({**case, 'semantic': nested}, value[field][key])
        assert set(value['sharedPropertyTypes']) == {'deviceId', 'label', 'recordedAt'}
    else:
        raise AssertionError('Unhandled semantic category ' + category)


def response_for(case):
    return httpx.Response(200, stream=httpx.ByteStream(json.dumps(case['response']).encode()),
                          headers={'Content-Type': 'application/json'})


def sync_success(case, mode):
    responses = []
    def handler(request):
        check_wire(request, case)
        response = response_for(case)
        responses.append(response)
        return response
    with sync_client(case, handler) as client:
        pending = invoke(client, case, mode)
        if mode == 'stream':
            with pending as response:
                assert not responses[0].is_closed
                value = json.loads(b''.join(response.iter_bytes()))
        elif mode == 'raw':
            try:
                value = typed_value(case, pending.decode())
            finally:
                pending.close()
        elif case['source']['iterator']:
            assert hasattr(pending, '__next__')
            value = [typed_value(case, item, True) for item in pending]
        else:
            value = typed_value(case, pending)
        expected = case['response']['data'] if mode == 'ordinary' and case['source']['iterator'] else case['response']
        assert value == expected, (case['operation'], mode, value, expected)
        semantic(case, value)
    assert len(responses) == 1 and responses[0].is_closed
    record(case, 'sync_' + mode, actual=value, expected=case['response'], requests=1, closed=True)


async def async_success(case, mode):
    responses = []
    def handler(request):
        check_wire(request, case)
        response = response_for(case)
        responses.append(response)
        return response
    async with async_client(case, handler) as client:
        pending = invoke(client, case, mode)
        if mode == 'stream':
            async with pending as response:
                assert not responses[0].is_closed
                value = json.loads(b''.join([chunk async for chunk in response.aiter_bytes()]))
        elif mode == 'ordinary' and case['source']['iterator']:
            assert hasattr(pending, '__aiter__') and not inspect.isawaitable(pending)
            value = [typed_value(case, item, True) async for item in pending]
        else:
            assert inspect.isawaitable(pending)
            result = await pending
            if mode == 'raw':
                try:
                    assert not inspect.iscoroutinefunction(result.decode)
                    assert inspect.iscoroutinefunction(result.aclose)
                    value = typed_value(case, result.decode())
                finally:
                    await result.aclose()
            else:
                value = typed_value(case, result)
        expected = case['response']['data'] if mode == 'ordinary' and case['source']['iterator'] else case['response']
        assert value == expected, (case['operation'], mode, value, expected)
        semantic(case, value)
    assert len(responses) == 1 and responses[0].is_closed
    record(case, 'async_' + mode, actual=value, expected=case['response'], requests=1, closed=True)


def source_check(case):
    module = importlib.import_module(case['source']['module'])
    assert digest(module.__file__) == case['source']['sha256']
    resource, method = case['operation'].split('.')[-2:]
    tree = ast.parse(Path(module.__file__).read_bytes())
    for class_name, expected in case['source']['wrapper_factories'].items():
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == class_name)
        init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == '__init__')
        stub = next(n for n in init.body if isinstance(n, ast.FunctionDef) and n.name == method)
        assignment = next(n for n in init.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Attribute) and t.attr == method for t in n.targets))
        assert ast.unparse(stub.args.args[0].annotation) == expected['response_annotation']
        assert ast.unparse(assignment.value) == expected['factory']
    for client_name, expected in case['source']['methods'].items():
        fn = getattr(getattr(module, client_name), method)
        node = ast.parse(textwrap.dedent(inspect.getsource(fn))).body[0]
        assert ast.dump(node.args) == expected['arguments_ast']
        assert ast.unparse(node.returns) == expected['return_annotation']
        assert isinstance(node, ast.AsyncFunctionDef) == expected['coroutine_definition']
        request, = [n for n in ast.walk(node) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == 'RequestInfo']
        actual = {kw.arg: ast.unparse(kw.value) for kw in request.keywords}
        assert actual == expected['request_ast']
        assert actual['throwable_errors'] == '{}'
    record(case, 'exact_frozen_source_signatures_wire_and_zero_named_errors')


def expect_assertion(function):
    try:
        function()
    except Exception as error:
        assert isinstance(error, (AssertionError, KeyError)) or isinstance(error.__cause__, AssertionError), type(error)
    else:
        raise AssertionError('Negative control survived')


def semantic_controls(case):
    damaged = copy.deepcopy(case['response'])
    category = case['semantic']
    target = damaged
    if 'data' in target and category not in ('aggregate_schema', 'history'):
        target = next(iter(target['data'].values()))[0] if isinstance(target['data'], dict) else target['data'][0]
    if category == 'device_schema':
        target['properties'].pop(target['primaryKey'])
    elif category == 'device_full':
        target['implementsInterfaces2']['Inspectable079']['properties']['deviceId'] = 'absent'
    elif category == 'action_rule':
        target['actionType']['parameters']['labelText']['dataType'] = {'type': 'date'}
    elif category == 'action_summary':
        target['parameters']['device']['required'] = False
    elif category == 'history':
        target['data'][0]['edit']['properties']['deviceId'] = 'wrong-key'
    elif category == 'interface':
        target['extendsInterfaces'] = ['Inspectable079']
    elif category == 'object_record':
        target['__primaryKey'] = 'wrong-key'
    elif category == 'value_type':
        target['constraints'] = [{'type': 'struct', 'properties': {}}]
    elif category == 'query':
        target['output'] = {'type': 'string'}
    elif category == 'ontology_full':
        target['ontology']['apiName'] = 'wrong-ontology'
    elif category == 'ontology':
        target['apiName'] = 'wrong-ontology'
    elif category in ('object_link', 'interface_link'):
        target['cardinality'] = 'ONE'
    else:
        damaged['data'][0]['metrics'][0]['name'] = 'wrongMetric'
    expect_assertion(lambda: semantic(case, damaged))
    record(case, 'independent_semantic_mutant_rejected')
    native = _core.ApiClient.call_api
    for fault in ('path', 'query'):
        def damaged_request(self, info):
            if fault == 'path':
                info = dataclasses.replace(info, resource_path=info.resource_path + '/wrong')
            else:
                info = dataclasses.replace(info, query_params={**info.query_params, 'wrongQuery': '1'})
            return native(self, info)
        with patch.object(_core.ApiClient, 'call_api', damaged_request):
            expect_assertion(lambda: sync_success(case, 'ordinary'))
        record(case, 'native_sdk_' + fault + '_mutant_rejected')


def freeze_check(data):
    freeze = json.loads((HERE / 'rest079_assets_freeze.json').read_text())
    assert freeze['published_skills'] == data['published_skills']
    skill = Path(freeze['skill_root'])
    for path, expected in freeze['assets'].items():
        assert digest(skill / path) == expected, path
    for path, expected in freeze['runtime_sources'].items():
        assert digest(path) == expected, path
    assert importlib.metadata.version('foundry-platform-sdk') == '1.101.0'
    record('F079-FREEZE', 'reader_assets_hash_bound', assets=len(freeze['assets']))


def denied(*args, **kwargs):
    raise AssertionError('PUBLIC_NETWORK_DENIED_F079')


async def run(data):
    import additional_checks
    additional_checks.bind(sys.modules[__name__])
    additional_checks.reader_source_checks(data)
    for case in data['operations']:
        source_check(case)
        semantic_controls(case)
        for mode in ('ordinary', 'raw', 'stream'):
            sync_success(case, mode)
            await async_success(case, mode)
        await additional_checks.adverse(case)
        await additional_checks.lifetimes(case)
        if case['source']['paged']:
            await additional_checks.paging(case)
    additional_checks.deep_boundaries(data)
    additional_checks.distributed(data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--author-check', action='store_true')
    parser.add_argument('--executor')
    parser.add_argument('--approval')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    data = json.loads((HERE / 'rest079_formal_cases.json').read_text())
    if not args.author_check:
        authors = {AUTHOR, data['original_author_identity']}
        assert args.executor and args.executor not in authors, 'Different formal executor required'
        assert args.approval, 'Independent approval required'
        approval = json.loads(Path(args.approval).read_text())
        assert approval['disposition'] == 'APPROVED'
        assert approval['reviewer_identity'] not in authors | {args.executor}
        for key, name in [('case_sha256', 'rest079_formal_cases.json'), ('harness_sha256', 'rest079_formal_execute.py'),
                          ('additional_checks_sha256', 'additional_checks.py'), ('feature_sha256', 'rest079_formal_cases.feature'),
                          ('freeze_sha256', 'rest079_assets_freeze.json')]:
            assert approval[key] == digest(HERE / name), ('Review hash mismatch', name)
        assert approval['testcase_closed'] is True and approval['testexec_prerequisites_verified'] is True
    freeze_check(data)
    loop = asyncio.new_event_loop()
    failure = None
    try:
        with patch.object(socket.socket, 'connect', denied), patch.object(socket.socket, 'connect_ex', denied), \
             patch.object(socket, 'getaddrinfo', denied), patch.object(socket, 'create_connection', denied), \
             patch.object(httpx.HTTPTransport, 'handle_request', denied), \
             patch.object(httpx.AsyncHTTPTransport, 'handle_async_request', denied):
            loop.run_until_complete(run(data))
            expect_assertion(lambda: socket.getaddrinfo('public.example.invalid', 443))
            record('F079-NETWORK', 'denial_probe', actual='PUBLIC_NETWORK_DENIED_F079')
    except BaseException as error:
        failure = error
        ROWS.append({'result': 'FAIL', 'error': repr(error)})
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
    kind = 'AUTHOR_DRY_RUN' if args.author_check else 'FORMAL_EXECUTION'
    report = {'kind': kind, 'formal_execution': not args.author_check, 'author_identity': AUTHOR,
              'executor_identity': args.executor, 'outcome': kind + ('_FAIL' if failure else '_PASS'), 'elapsed_seconds': time.perf_counter() - start,
              'case_sha256': digest(HERE / 'rest079_formal_cases.json'),
              'harness_sha256': digest(__file__), 'checks': ROWS}
    report['additional_checks_sha256'] = digest(HERE / 'additional_checks.py')
    report['freeze_sha256'] = digest(HERE / 'rest079_assets_freeze.json')
    report['feature_sha256'] = digest(HERE / 'rest079_formal_cases.feature')
    args.output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'outcome': report['outcome'], 'checks': len(ROWS), 'formal_execution': not args.author_check}))
    if failure:
        raise failure


if __name__ == '__main__':
    main()
