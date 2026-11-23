"""Recovery-author checks. Expectations come from frozen source and declared QA data."""
import ast
import asyncio
import copy
import hashlib
import importlib
import inspect
import json
from pathlib import Path
import re
import runpy
import subprocess
import textwrap
from functools import lru_cache
from contextlib import contextmanager
from unittest.mock import patch

import httpx
import pydantic
from foundry_sdk import PermissionDeniedError, ReadTimeout


def bind(harness):
    global H, BUDGETS
    H = harness
    BUDGETS = json.loads((H.HERE / 'rest079_formal_cases.json').read_text())['budgets']


def frozen_source_ledger(data, freeze):
    repo = H.HERE.parents[2] / '.ept/docs/customer_input/foundry-platform-python'
    cache = {}
    def source(path):
        if path not in cache:
            cache[path] = subprocess.check_output(['git', '-C', str(repo), 'show', data['source_commit'] + ':' + path])
        return cache[path]
    @lru_cache(None)
    def module_tree(module):
        path = module.replace('.', '/')
        if module in ('foundry_sdk', 'foundry_sdk._core'):
            path += '/__init__.py'
        else:
            path += '.py'
        return path, ast.parse(source(path))
    @lru_cache(None)
    def exported(module, name):
        path, tree = module_tree(module)
        if path.endswith('/__init__.py'):
            imports = [n for n in tree.body if isinstance(n, ast.ImportFrom) and any((a.asname or a.name) == name for a in n.names)]
            imported, = imports
            alias = next(a for a in imported.names if (a.asname or a.name) == name)
            return exported(imported.module, alias.name)
        return module + '.' + name
    @lru_cache(None)
    def definition(qualified):
        module, name = qualified.rsplit('.', 1)
        actual = exported(module, name)
        module, name = actual.rsplit('.', 1)
        path, tree = module_tree(module)
        def is_named(node):
            return ((isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name)
                    or (isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.target.id == name)
                    or (isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets)))
        matches = [n for n in tree.body if is_named(n)]
        assert len(matches) == 1, (qualified, actual, len(matches))
        return actual, path, tree, matches[0]
    checked = {}
    actual_to_public = {}
    for qualified, entry in freeze['model_pages'].items():
        actual, path, tree, node = definition(qualified)
        expected = ast.dump(ast.Module(body=[node], type_ignores=[]), include_attributes=False)
        assert entry['definition_ast'] == expected, ('Model definition differs from frozen source', qualified)
        checked[qualified] = {'source': path, 'source_sha256': hashlib.sha256(source(path)).hexdigest(), 'definition_ast': expected}
        actual_to_public[actual] = qualified
    # Resolve dependencies through both imported aliases and quoted forward references.
    def dependencies(tree, node):
        imported = {}
        modules = {}
        local_names = {n.name for n in tree.body if isinstance(n, ast.ClassDef)}
        local_names.update(n.target.id for n in tree.body if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name))
        local_names.update(t.id for n in tree.body if isinstance(n, ast.Assign) for t in n.targets if isinstance(t, ast.Name))
        local_module = next((actual.rsplit('.', 1)[0] for actual, public in actual_to_public.items()
                             if public in checked and definition(public)[2] is tree), None)
        for statement in tree.body:
            if isinstance(statement, ast.ImportFrom) and statement.module and statement.module.startswith('foundry_sdk'):
                for alias in statement.names:
                    local = alias.asname or alias.name
                    if alias.name in ('_core', 'models', 'errors'):
                        modules[local] = statement.module + '.' + alias.name
                    else:
                        imported[local] = statement.module + '.' + alias.name
            elif isinstance(statement, ast.Import):
                for alias in statement.names:
                    if alias.name.startswith('foundry_sdk'):
                        modules[alias.asname or alias.name] = alias.name
        nodes = list(ast.walk(node))
        for child in list(nodes):
            if isinstance(child, ast.Constant) and isinstance(child.value, str):
                try:
                    nodes.extend(ast.walk(ast.parse(child.value, mode='eval')))
                except SyntaxError:
                    pass
        found = set()
        for child in nodes:
            candidate = None
            if isinstance(child, ast.Name) and child.id in imported:
                candidate = imported[child.id]
            elif isinstance(child, ast.Name) and child.id in local_names and local_module:
                candidate = local_module + '.' + child.id
            elif isinstance(child, ast.Attribute) and isinstance(child.value, ast.Name) and child.value.id in modules:
                candidate = modules[child.value.id] + '.' + child.attr
            if candidate:
                module, name = candidate.rsplit('.', 1)
                try:
                    actual = exported(module, name)
                except (AssertionError, ValueError):
                    continue
                if actual in actual_to_public:
                    found.add(actual_to_public[actual])
                elif '.models.' in actual or '.errors.' in actual:
                    raise AssertionError(('Unresolved transitive model', actual))
        return found
    for qualified in checked:
        _, _, tree, node = definition(qualified)
        checked[qualified]['dependencies'] = sorted(dependencies(tree, node))
    operation_closures = {}
    reachable = set()
    for c in data['operations']:
        _, tree = module_tree(c['source']['module'])
        resource, method = c['operation'].split('.')[-2:]
        client = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == resource + 'Client')
        fn = next(n for n in client.body if isinstance(n, ast.FunctionDef) and n.name == method)
        pending = list(dependencies(tree, fn))
        closure = set()
        while pending:
            symbol = pending.pop()
            if symbol in closure:
                continue
            closure.add(symbol)
            pending.extend(checked[symbol]['dependencies'])
        operation_closures[c['operation']] = sorted(closure)
        reachable.update(closure)
    assert reachable == set(checked), ('Source-reachable closure differs', sorted(set(checked) - reachable), sorted(reachable - set(checked)))
    H.expect_assertion(lambda: assert_definition('wrong AST', next(iter(checked.values()))['definition_ast']))
    H.record('F079-CLOSURE', 'source_derived_per32_membership_and_changed_definition_mutant', operation_closures=operation_closures)
    # All referenced definitions are compared to source, including every field/alias/default/union literal.
    H.record('F079-CLOSURE', 'all_linked_model_definition_asts_match_frozen_source',
             definitions=len(checked), source_files=len(cache), ledger=checked)
    return checked


def assert_definition(actual, expected):
    assert actual == expected


def reader_source_checks(data):
    freeze = json.loads((H.HERE / 'rest079_assets_freeze.json').read_text())
    root = Path(freeze['skill_root'])
    register = json.loads((H.HERE / 'published_register.json').read_text())
    assert H.digest(H.HERE / 'published_register.json') == freeze['published_register_sha256']
    partition_path = H.HERE.parents[2] / '.ept/docs/deliverables/development/FEATURE-015-rest-operation-partitions.json'
    assert H.digest(partition_path) == freeze['partition_sha256']
    partition = json.loads(partition_path.read_text())['partitions']['DEV-STORY-079']['operation_ids']
    assert sorted(c['operation'] for c in data['operations']) == sorted(partition)
    assert len(data['operations']) == 32
    assert sum(c['source']['paged'] for c in data['operations']) == 11
    assert sum(c['source']['iterator'] for c in data['operations']) == 8
    all_ids = {row['id'] for row in register['operations']}
    assert len(all_ids) == 425 and register['sdk_release'] == '1.101.0'
    for source in freeze['source_documents'].values():
        assert H.digest(source['path']) == source['sha256']
    for c in data['operations']:
        binding = next(row for row in register['operations'] if row['id'] == c['operation'])
        assert binding == freeze['register_bindings'][c['operation']]
        contract = '\n'.join((root / part).read_text() for part in binding['parts'])
        assert contract.startswith('# ' + c['operation'] + '\n')
        assert 'release stage: ' + binding['stage'] in contract
        for fields in c['source']['methods'].values():
            for expression in fields['request_ast'].values():
                assert expression in contract, (c['operation'], expression)
        for mode, result in binding['response_modes'].items():
            assert '| ' + mode + ' | ' + result + ' |' in contract
        assert binding['client_path'] in contract
        first_signature = re.search(r'```python\n(def .*?)\n```', contract, re.S).group(1)
        signature = ast.parse(first_signature).body[0]
        sync_source = c['source']['methods'][c['operation'].split('.')[2] + 'Client']
        assert ast.dump(signature.args) == sync_source['arguments_ast']
        assert ast.unparse(signature.returns) == sync_source['return_annotation']
        assert c['availability']['stage'] == binding['stage']
        resource, method = c['operation'].split('.')[-2:]
        document = Path(freeze['source_documents'][resource]['path']).read_text()
        source_stage = re.search(r'\[\*\*' + re.escape(method) + r'\*\*\]\([^)]*\) \| \*\*\w+\*\* [^|]+\| ([^|]+) \|', document).group(1).strip()
        assert c['availability']['stage'] == source_stage
        H.expect_assertion(lambda: assert_definition('Invented Universal Availability', source_stage))
        section = document.split('# **' + method + '**', 1)[1].split('\n# **', 1)[0]
        assert c['source']['narrative_error_mentions'] == (['ObjectsExceededLimit'] if 'ObjectsExceededLimit' in section else [])
        assert c['source']['source_named_errors'] == []
        for target in re.findall(r'\]\(([^)]+)\)', contract):
            if not target.startswith(('http:', 'https:', '#')):
                assert ((root / c['reader']['contract']).parent / target.split('#')[0]).resolve().is_file(), target
        H.record(c, 'reader_contract_source_wire_modes_stage_and_all_links')
    # Resource indexes enumerate the entire425 operation set; v1/v2 entries remain distinct.
    discovered = set()
    for index in root.glob('references/rest/v*/*/index.md'):
        text = index.read_text()
        for relative in re.findall(r'\]\(([^)]+)\)', text):
            destination = (index.parent / relative.split('#')[0]).resolve()
            if '/contracts/' in destination.as_posix() and destination.is_file():
                title = destination.read_text().splitlines()[0].removeprefix('# ')
                if title in all_ids:
                    discovered.add(title)
    assert discovered == all_ids, (len(discovered), sorted(all_ids - discovered)[:5])
    catalog = (root / 'references/rest/catalog.md').read_text()
    assert '[v1.ontologies](v1/ontologies/index.md)' in catalog
    assert '[v2.ontologies](v2/ontologies/index.md)' in catalog
    assert 'references/rest-api.md' in (root / 'SKILL.md').read_text()
    assert 'v1.ontologies.ObjectType.get' in all_ids and 'v2.ontologies.ObjectType.get' in all_ids
    H.record('F079-DISCOVERY', 'exact425_catalog_service_navigation_distinct_versions', operation_ids=sorted(discovered))
    frozen_source_ledger(data, freeze)
    policies = {
        'ObjectType': ['at most100', 'filtered out', 'Object Storage V1', 'typed primary-key', 'plain property values', 'properties', 'visibility'],
        'ActionTypeFullMetadata': ['modifyInterfaceObject', 'modifyInterface', 'interfaceObjectToModify', 'target', 'newName'],
        'OntologyInterface': ['exactly one', 'propertyIdentifier', 'YEARS', 'QUARTERS', 'MONTHS', 'WEEKS', 'value=1', 'shared propert', '10,000', 'snapshot'],
        'OntologyValueType': ["fieldType={'type': 'date'}", 'empty constraints', '`struct`', 'version `1`'],
        'QueryType': ['100', 'filtered', 'permissions', 'parameter/result'],
    }
    for resource, terms in policies.items():
        text = (root / f'references/rest/v2/ontologies/{resource}.md').read_text()
        flat = re.sub(r'\s+', ' ', text)
        for term in terms:
            assert term in flat, (resource, term)
        H.record('F079-POLICY', resource + '_reader_content_assertions', claims=terms, live_policy_executed=False)


def local_decision(raw, validated):
    return {'decision': 'use' if validated else 'stop', 'retained': copy.deepcopy(raw), 'derived': 2 if validated else None}


def aggregation_guard(body):
    schema = {'deviceId': 'string', 'label': 'string', 'recordedAt': 'timestamp'}
    for selector in body['aggregation'] + body['groupBy']:
        if ('field' in selector) == ('propertyIdentifier' in selector):
            return False
        name = selector.get('field') or selector['propertyIdentifier'].get('apiName')
        if name not in schema:
            return False
        if selector['type'] == 'duration':
            if schema[name] not in ('date', 'timestamp'):
                return False
            if selector['unit'] in ('YEARS', 'QUARTERS', 'MONTHS', 'WEEKS') and selector['value'] != 1:
                return False
    return True


def deep_boundaries(data):
    by_id = {c['operation']: c for c in data['operations']}
    semantic_fault_matrix(by_id)
    c = by_id['v2.ontologies.OntologyInterface.aggregate']
    body = copy.deepcopy(c['wire']['body'])
    assert aggregation_guard(body)
    variants = []
    for fault in ('both-selectors', 'neither-selector', 'unknown-shared-property', 'wrong-duration-type', 'calendar-multiple'):
        bad = copy.deepcopy(body)
        if fault == 'both-selectors':
            bad['aggregation'][0]['propertyIdentifier'] = {'type': 'sharedProperty', 'apiName': 'deviceId'}
        elif fault == 'neither-selector':
            bad['aggregation'][0].pop('field')
        elif fault == 'unknown-shared-property':
            bad['aggregation'][0]['field'] = 'unknown079'
        elif fault == 'wrong-duration-type':
            bad['groupBy'][0]['field'] = 'label'
        else:
            bad['groupBy'][0].update(unit='MONTHS', value=2)
        assert not aggregation_guard(bad)
        decision = local_decision(bad, aggregation_guard(bad))
        assert decision['decision'] == 'stop' and decision['retained'] == bad and decision['derived'] is None
        variants.append({'fault': fault, 'decision': decision})
    shared = copy.deepcopy(body)
    shared['aggregation'][0].pop('field')
    shared['aggregation'][0]['propertyIdentifier'] = {'type': 'sharedProperty', 'apiName': 'deviceId'}
    assert aggregation_guard(shared)
    H.record(c, 'shared_property_selector_and_duration_local_guards', cases=variants, shared_selector=shared)
    # SDK Any-valued interface records retain unknown keys. Local derivation requires confirmed schema.
    c = by_id['v2.ontologies.OntologyInterface.search']
    unknown = copy.deepcopy(c)
    unknown['response']['data'][0]['unknown079'] = {'opaque': [1, {'server': True}]}
    observed = []
    def handler(request):
        H.check_wire(request, c)
        return H.response_for(unknown)
    with H.sync_client(c, handler) as client:
        raw = H.invoke(client, c, 'raw')
        try:
            decoded = H.typed_value(c, raw.decode())
        finally:
            raw.close()
    assert decoded['data'][0]['unknown079'] == unknown['response']['data'][0]['unknown079']
    decision = local_decision(decoded, set(decoded['data'][0]) <= {'__apiName', '__primaryKey', '__rid', 'deviceId', 'label', 'recordedAt'})
    assert decision['decision'] == 'stop' and decision['derived'] is None and decision['retained'] == decoded
    H.expect_assertion(lambda: assert_stop(local_decision(decoded, True)))
    H.record(c, 'opaque_sdk_keys_preserved_stop_local_derivation_and_bypass_mutant', decision=decision, server_validation_claim=False)
    aggregate = by_id['v2.ontologies.OntologyInterface.aggregate']
    mixed = copy.deepcopy(aggregate['response'])
    mixed['data'][0]['group']['unknown079'] = {'opaque': 7}
    decision = local_decision(mixed, set(mixed['data'][0]['group']) == {'recordedAt'})
    assert_stop(decision)
    H.expect_assertion(lambda: assert_stop(local_decision(mixed, True)))
    H.record(aggregate, 'mixed_confirmed_unknown_group_label_retained_and_bypass_rejected', decision=decision)
    for c in data['operations']:
        if not c['operation'].endswith(('.get_by_rid_batch', '.get_outgoing_link_types_by_object_type_rid_batch')):
            continue
        # Source documents a server limit; local SDK may serialize101. Enforce reader-side budget.
        def batch_guard(requests):
            return len(requests) <= 100
        assert batch_guard([{}] * 100) and not batch_guard([{}] * 101)
        H.expect_assertion(lambda: assert_batch_limit(lambda requests: True))
        kwargs = copy.deepcopy(c['kwargs'])
        template = kwargs['requests'][0]
        key, original = next(iter(template.items()))
        kwargs['requests'] = [{key: original if index == 0 else original + '-omitted' + str(index)} for index in range(100)]
        expected = copy.deepcopy(c)
        expected['wire'] = source_wire(c, {**kwargs, 'request_timeout': 7})
        calls = []
        def batch_handler(request):
            H.check_wire(request, expected)
            calls.append(request)
            return H.response_for(c)
        with H.sync_client(c, batch_handler) as client:
            raw = H.invoke(client, c, 'raw', kwargs)
            try:
                value = H.typed_value(c, raw.decode())
                H.semantic(c, value)
            finally:
                raw.close()
        requested = [item[key] for item in kwargs['requests']]
        returned = list(value['data']) if isinstance(value['data'], dict) else [item['rid'] for item in value['data']]
        omitted = sorted(set(requested) - set(returned))
        assert len(omitted) == 99
        assert len(calls) == 1
        kwargs['requests'].append({key: original + '-101'})
        with H.sync_client(c, batch_handler) as client:
            if batch_guard(kwargs['requests']):
                H.invoke(client, c, 'raw', kwargs)
        assert len(calls) == 1
        H.record(c, 'batch100_101_local_budget_and_visibility_omission', requested_count=100,
                 visible_count=1, omitted=omitted, absence_or_deletion_proven=False,
                 actual_requested=requested, actual_returned=returned, max100_requests=1, refused101_requests=0,
                 boundary='Reader guard only; no invented SDK/server rejection')


def semantic_fault_matrix(by_id):
    specs = [
        ('ObjectType.get', 'primary-key-member', ['primaryKey'], 'absent079'),
        ('ObjectType.get', 'title-member', ['titleProperty'], 'absent079'),
        ('ObjectType.get', 'primary-key-type', ['properties', 'deviceId', 'dataType'], {'type': 'integer'}),
        ('ObjectType.get', 'title-type', ['properties', 'label', 'dataType'], {'type': 'date'}),
        ('ObjectType.get_full_metadata', 'interface-membership', ['implementsInterfaces'], ['Unknown079']),
        ('ObjectType.get_full_metadata', 'backing-property', ['implementsInterfaces2', 'Inspectable079', 'properties', 'deviceId'], 'absent079'),
        ('ObjectType.get_full_metadata', 'link-implementation', ['implementsInterfaces2', 'Inspectable079', 'links'], {'inspectedPeers079': ['missing079']}),
        ('ObjectType.get_full_metadata', 'property-implementation-discriminator', ['implementsInterfaces2', 'Inspectable079', 'propertiesV2', 'label', 'type'], 'unknown079'),
        ('OntologyInterface.get', 'inheritance-self-cycle', ['extendsInterfaces'], ['Inspectable079']),
        ('OntologyInterface.get', 'inherited-member-type', ['allProperties', 'label', 'dataType'], {'type': 'integer'}),
        ('OntologyInterface.get', 'required-member', ['propertiesV2', 'deviceId', 'required'], False),
        ('OntologyInterface.get', 'implementation-required', ['allPropertiesV2', 'deviceId', 'requireImplementation'], False),
        ('OntologyInterface.get', 'link-target', ['links', 'inspectedPeers079', 'linkedEntityApiName', 'apiName'], 'Unknown079'),
        ('ActionType.get', 'parameter-type', ['parameters', 'device', 'dataType', 'interfaceTypeApiName'], 'Unknown079'),
        ('ActionTypeFullMetadata.get', 'summary-discriminator', ['actionType', 'operations', 0, 'type'], 'modifyInterface'),
        ('ActionTypeFullMetadata.get', 'full-rule-discriminator', ['fullLogicRules', 0, 'type'], 'modifyInterfaceObject'),
        ('ActionTypeFullMetadata.get', 'rule-target-reference', ['fullLogicRules', 0, 'interfaceObjectToModify'], 'absent079'),
        ('ActionTypeFullMetadata.get', 'rule-property-parameter-reference', ['fullLogicRules', 0, 'sharedPropertyArguments', 'label', 'parameterId'], 'absent079'),
        ('ObjectType.get_edits_history', 'typed-history-key', ['data', 0, 'objectPrimaryKey', 'deviceId', 'type'], 'integerValue'),
        ('ObjectType.get_edits_history', 'plain-create-key', ['data', 0, 'edit', 'properties', 'deviceId'], {'type': 'stringValue', 'value': 'D-079'}),
        ('OntologyValueType.get', 'date-versus-struct', ['constraints'], [{'type': 'struct', 'properties': {}}]),
        ('OntologyValueType.get', 'value-type-version', ['version'], '4'),
        ('QueryType.get', 'query-version', ['version'], '9.9.9'),
    ]
    for suffix, fault, path, replacement in specs:
        c = by_id['v2.ontologies.' + suffix]
        damaged = copy.deepcopy(c['response'])
        target = damaged
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = replacement
        H.expect_assertion(lambda: H.semantic(c, damaged))
        module, name = c['source']['response_type'].rsplit('.', 1)
        model = getattr(importlib.import_module(module), name)
        try:
            model.model_validate(damaged)
            sdk_shape = 'accepted'
        except pydantic.ValidationError:
            sdk_shape = 'rejected-by-source-model'
        H.record(c, 'nested_constraint_fault_' + fault, input_path=path, replacement=replacement,
                 sdk_model_shape=sdk_shape, local_semantic_check='rejected', server_validation_claim=False)


def assert_stop(decision):
    assert decision['decision'] == 'stop' and decision['derived'] is None


def assert_batch_limit(guard):
    assert guard([{}] * 100) and not guard([{}] * 101)


def source_wire(c, kwargs):
    module = importlib.import_module(c['source']['module'])
    method = c['operation'].split('.')[-1]
    fn = getattr(H.class_for(c), method)
    bound = inspect.signature(fn).bind(None, **kwargs)
    bound.apply_defaults()
    expressions = next(iter(c['source']['methods'].values()))['request_ast']
    values = {key: eval(compile(ast.parse(value, mode='eval'), '<frozen RequestInfo>', 'eval'), vars(module), bound.arguments)
              for key, value in expressions.items()}
    body = values['body']
    if isinstance(body, pydantic.BaseModel):
        body = body.model_dump(mode='json', by_alias=True, exclude_none=True)
    return {'method': values['method'], 'path': values['resource_path'].format(**values['path_params']),
            'query': {key: value for key, value in values['query_params'].items() if value is not None},
            'headers': values['header_params'], 'body': body}


def distributed(data):
    root = Path(json.loads((H.HERE / 'rest079_assets_freeze.json').read_text())['skill_root'])
    for c in data['operations']:
        resource, method = c['operation'].split('.')[-2:]
        path = root / f'examples/rest/079/v2/ontologies/{resource}/invoke_{method}.py'
        namespace = runpy.run_path(str(path), run_name='independent079_example')
        fn = namespace['invoke']
        call, = [n for n in ast.walk(ast.parse(textwrap.dedent(inspect.getsource(fn))))
                   if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == method]
        kwargs = {kw.arg: ast.literal_eval(kw.value) for kw in call.keywords}
        assert kwargs['request_timeout'] == 30
        expected = source_wire(c, kwargs)
        independent = copy.deepcopy(c)
        independent['wire'] = expected
        calls, responses = [], []
        def handler(request):
            assert request.extensions['timeout'] == dict(connect=30, read=30, write=30, pool=30)
            # Wire expected independently from frozen source plus invocation args, never EXPECTED constants.
            original_timeout = request.extensions['timeout']
            request.extensions['timeout'] = dict(connect=7, read=7, write=7, pool=7)
            try:
                H.check_wire(request, independent)
            finally:
                request.extensions['timeout'] = original_timeout
            calls.append(request)
            response = H.response_for(c)
            responses.append(response)
            return response
        with H.sync_client(c, handler) as client:
            raw = fn(client)
            try:
                value = H.typed_value(c, raw.decode())
                assert value == c['response']
                H.semantic(c, value)
            finally:
                raw.close()
        assert len(calls) == 1 and responses[0].is_closed
        wrong = copy.deepcopy(independent)
        wrong['wire']['path'] += '/wrong'
        H.expect_assertion(lambda: H.check_wire(calls[0], wrong))
        H.record(c, 'distributed_native_invoke_independent_source_wire_typed_payload',
                 invocation_inputs=kwargs, expected_wire=expected, example_sha256=H.digest(path),
                 independent_response=c['response'], product_EXPECTED_SUCCESS_oracle=False)


async def consume(pending):
    if hasattr(pending, '__aiter__'):
        return [item async for item in pending]
    return await pending


async def adverse(c):
    for asynchronous in (False, True):
        for failure in ('generic_403', 'timeout'):
            calls, responses = [], []
            def handler(request):
                H.check_wire(request, c)
                calls.append(request)
                if failure == 'timeout':
                    raise httpx.ReadTimeout('independent079 response lost', request=request)
                response = httpx.Response(403, json={'errorCode': 'PERMISSION_DENIED',
                    'errorName': 'IndependentDenied079', 'errorInstanceId': 'independent079-denied',
                    'parameters': {'operation': c['operation']}})
                responses.append(response)
                return response
            async def async_attempt(client):
                return await consume(H.invoke(client, c, 'ordinary'))
            try:
                if asynchronous:
                    async with H.async_client(c, handler) as client:
                        await async_attempt(client)
                else:
                    with H.sync_client(c, handler) as client:
                        value = H.invoke(client, c, 'ordinary')
                        if c['source']['iterator']:
                            list(value)
            except PermissionDeniedError as error:
                assert failure == 'generic_403'
                assert error.name == 'IndependentDenied079'
                assert error.error_instance_id == 'independent079-denied'
                assert error.parameters == {'operation': c['operation']}
            except ReadTimeout as error:
                assert failure == 'timeout' and isinstance(error.__cause__, httpx.ReadTimeout)
            else:
                raise AssertionError('Expected native ' + failure)
            assert len(calls) == 1 and all(r.is_closed for r in responses)
            H.record(c, ('async_' if asynchronous else 'sync_') + failure, requests=1, retries=0)
        calls = []
        kwargs = {**copy.deepcopy(c['kwargs']), 'request_timeout': 0}
        try:
            if asynchronous:
                async with H.async_client(c, lambda req: calls.append(req)) as client:
                    await consume(H.invoke(client, c, 'ordinary', kwargs))
            else:
                with H.sync_client(c, lambda req: calls.append(req)) as client:
                    result = H.invoke(client, c, 'ordinary', kwargs)
                    if c['source']['iterator']:
                        list(result)
        except pydantic.ValidationError:
            pass
        else:
            raise AssertionError('Invalid timeout reached transport')
        assert calls == []
        H.record(c, ('async_' if asynchronous else 'sync_') + 'invalid_timeout_zero_http')
    H.expect_assertion(lambda: H.typed_value(c, copy.deepcopy(c['response'])))
    H.record(c, 'plain_dict_in_place_of_typed_response_mutant_rejected')
    for mode in ('raw', 'stream'):
        for asynchronous in (False, True):
            for failure in ('generic_403', 'timeout'):
                calls, responses = [], []
                def handler(request):
                    H.check_wire(request, c)
                    calls.append(request)
                    if failure == 'timeout':
                        raise httpx.ReadTimeout('independent079 response lost', request=request)
                    response = httpx.Response(403, json={'errorCode': 'PERMISSION_DENIED',
                        'errorName': 'IndependentDenied079', 'errorInstanceId': 'independent079-denied',
                        'parameters': {'operation': c['operation']}})
                    responses.append(response)
                    return response
                try:
                    if asynchronous:
                        async with H.async_client(c, handler) as client:
                            if mode == 'stream':
                                async with H.invoke(client, c, mode):
                                    pass
                            else:
                                raw = await H.invoke(client, c, mode)
                                await raw.aclose()
                    else:
                        with H.sync_client(c, handler) as client:
                            if mode == 'stream':
                                with H.invoke(client, c, mode):
                                    pass
                            else:
                                H.invoke(client, c, mode).close()
                except PermissionDeniedError as error:
                    assert failure == 'generic_403' and error.name == 'IndependentDenied079'
                except ReadTimeout as error:
                    assert failure == 'timeout' and isinstance(error.__cause__, httpx.ReadTimeout)
                else:
                    raise AssertionError('Expected native wrapper failure')
                assert len(calls) == 1 and all(r.is_closed for r in responses)
                H.record(c, ('async_' if asynchronous else 'sync_') + mode + '_' + failure,
                         requests=1, retries=0, response_closed=True)


class SyncChunks(httpx.SyncByteStream):
    def __init__(self):
        self.reads = 0
        self.closed = False
    def __iter__(self):
        for chunk in (b'{"data":', b'[]}', b'never-read'):
            self.reads += 1
            yield chunk
    def close(self):
        self.closed = True


class AsyncChunks(httpx.AsyncByteStream):
    def __init__(self):
        self.reads = 0
        self.closed = False
    async def __aiter__(self):
        for chunk in (b'{"data":', b'[]}', b'never-read'):
            self.reads += 1
            yield chunk
    async def aclose(self):
        self.closed = True


def assert_lifetime(response, chunks, reads):
    assert response.is_closed and chunks.closed and chunks.reads == reads


async def lifetimes(c):
    # Caller consumption is bounded; the transport may deliver a larger chunk.
    for asynchronous in (False, True):
        chunks = AsyncChunks() if asynchronous else SyncChunks()
        responses = []
        def handler(request):
            H.check_wire(request, c)
            response = httpx.Response(200, stream=chunks)
            responses.append(response)
            return response
        byte_limit = BUDGETS['max_stream_bytes']
        if asynchronous:
            async with H.async_client(c, handler) as client:
                async with H.invoke(client, c, 'stream') as stream:
                    iterator = stream.aiter_bytes(chunk_size=byte_limit)
                    retained = await anext(iterator)
        else:
            with H.sync_client(c, handler) as client:
                with H.invoke(client, c, 'stream') as stream:
                    retained = next(stream.iter_bytes(chunk_size=byte_limit))
        assert byte_limit == len(retained) == 4 and retained == b'{"da'
        assert_lifetime(responses[0], chunks, 1)
        H.record(c, ('async_' if asynchronous else 'sync_') + 'caller_stream_byte_budget',
                 limit=byte_limit, consumed_bytes=len(retained), upstream_first_chunk_bytes=8,
                 retained_hex=retained.hex(), response_closed=True, completion_claim=False)
    for asynchronous in (False, True):
        for scenario in ('unread', 'interrupted', 'cancel') if asynchronous else ('unread', 'interrupted'):
            chunks = AsyncChunks() if asynchronous else SyncChunks()
            responses = []
            def handler(request):
                H.check_wire(request, c)
                response = httpx.Response(200, stream=chunks, headers={'Content-Type': 'application/json'})
                responses.append(response)
                return response
            if asynchronous:
                async with H.async_client(c, handler) as client:
                    entered = asyncio.Event()
                    async def work():
                        async with H.invoke(client, c, 'stream') as stream:
                            assert not responses[0].is_closed and chunks.reads == 0
                            if scenario == 'interrupted':
                                iterator = stream.aiter_bytes()
                                assert await anext(iterator) == b'{"data":'
                                raise ValueError('consumer079 interrupted')
                            if scenario == 'cancel':
                                entered.set()
                                await asyncio.Event().wait()
                    if scenario == 'cancel':
                        task = asyncio.create_task(work())
                        await asyncio.wait_for(entered.wait(), 2)
                        task.cancel()
                        try:
                            await task
                        except asyncio.CancelledError:
                            pass
                        else:
                            raise AssertionError('Cancellation swallowed')
                    else:
                        try:
                            await work()
                        except ValueError as error:
                            assert scenario == 'interrupted' and str(error) == 'consumer079 interrupted'
            else:
                with H.sync_client(c, handler) as client:
                    try:
                        with H.invoke(client, c, 'stream') as stream:
                            assert not responses[0].is_closed and chunks.reads == 0
                            if scenario == 'interrupted':
                                assert next(stream.iter_bytes()) == b'{"data":'
                                raise ValueError('consumer079 interrupted')
                    except ValueError as error:
                        assert scenario == 'interrupted' and str(error) == 'consumer079 interrupted'
            assert len(responses) == 1
            assert_lifetime(responses[0], chunks, int(scenario == 'interrupted'))
            H.record(c, ('async_' if asynchronous else 'sync_') + 'unfinished_stream_' + scenario,
                     read_chunks=chunks.reads, total_chunks=3, response_closed=True, body_closed=True)
        for malformed in (False, True):
            responses = []
            def handler(request):
                H.check_wire(request, c)
                response = (httpx.Response(200, stream=httpx.ByteStream(b'{bad-json'))
                            if malformed else H.response_for(c))
                responses.append(response)
                return response
            async def async_raw(client):
                raw = await H.invoke(client, c, 'raw')
                try:
                    if malformed:
                        try:
                            raw.decode()
                        except (ValueError, pydantic.ValidationError):
                            return
                        raise AssertionError('Malformed JSON decoded')
                    H.typed_value(c, raw.decode())
                    raise ValueError('consumer079 interrupted')
                finally:
                    await raw.aclose()
            try:
                if asynchronous:
                    async with H.async_client(c, handler) as client:
                        await async_raw(client)
                else:
                    with H.sync_client(c, handler) as client:
                        raw = H.invoke(client, c, 'raw')
                        try:
                            if malformed:
                                try:
                                    raw.decode()
                                except (ValueError, pydantic.ValidationError):
                                    pass
                                else:
                                    raise AssertionError('Malformed JSON decoded')
                            else:
                                H.typed_value(c, raw.decode())
                                raise ValueError('consumer079 interrupted')
                        finally:
                            raw.close()
            except ValueError as error:
                assert not malformed and str(error) == 'consumer079 interrupted'
            assert len(responses) == 1 and responses[0].is_closed
            H.record(c, ('async_' if asynchronous else 'sync_') + 'raw_' + ('decode_failure' if malformed else 'consumer_exception') + '_cleanup')
    H.expect_assertion(lambda: assert_lifetime(type('Open', (), {'is_closed': False})(), SyncChunks(), 0))
    H.record(c, 'open_response_cleanup_mutant_rejected')
    prebuffered = httpx.Response(200, json=c['response'])
    H.expect_assertion(lambda: assert_unread(prebuffered))
    H.record(c, 'prebuffered_stream_trap_rejected')
    for asynchronous in (False, True):
        chunks = AsyncChunks() if asynchronous else SyncChunks()
        responses = []
        def handler(request):
            response = httpx.Response(200, stream=chunks)
            responses.append(response)
            return response
        async def no_close(self):
            pass
        if asynchronous:
            async with H.async_client(c, handler) as client:
                with patch.object(H._core.api_client.AsyncApiResponse, 'aclose', no_close):
                    async with H.invoke(client, c, 'stream'):
                        pass
            H.expect_assertion(lambda: assert_lifetime(responses[0], chunks, 0))
            await responses[0].aclose()
        else:
            with H.sync_client(c, handler) as client:
                with patch.object(H._core.api_client.ApiResponse, 'close', lambda self: None):
                    with H.invoke(client, c, 'stream'):
                        pass
            H.expect_assertion(lambda: assert_lifetime(responses[0], chunks, 0))
            responses[0].close()
        assert_lifetime(responses[0], chunks, 0)
        H.record(c, ('async_' if asynchronous else 'sync_') + 'native_response_cleanup_bypass_mutant_rejected')


def assert_unread(response):
    assert not response.is_closed and not response.is_stream_consumed


def page_case(c, index, scenario):
    page = copy.deepcopy(c['response'])
    if scenario == 'empty':
        page['data'] = []
        if 'totalCount' in page:
            page['totalCount'] = '0'
        page.pop('nextPageToken', None)
        return page
    if scenario == 'intermediate-empty' and index == 0:
        page['data'] = []
        page['nextPageToken'] = 'cursor079-next'
        if 'totalCount' in page:
            page['totalCount'] = '1'
        return page
    if index:
        item = page['data'][0]
        if 'apiName' in item:
            item['apiName'] += 'Next'
        elif 'objectType' in item:
            item['objectType']['apiName'] += 'Next'
        elif 'actionType' in item:
            item['actionType']['apiName'] += 'Next'
        elif '__primaryKey' in item:
            item['__primaryKey'] += '-next'
        else:
            item['timestamp'] = '2026-11-16T09:00:00+00:00'
    if scenario in ('repeat', 'budget', 'items') or index == 0:
        page['nextPageToken'] = ('cursor079-budget-' + str(index + 1)) if scenario == 'budget' else 'cursor079-next'
    else:
        page.pop('nextPageToken', None)
    if scenario == 'items':
        page['data'].append(copy.deepcopy(page['data'][0]))
    if 'totalCount' in page:
        page['totalCount'] = '2'
    return page


async def paging(c):
    for asynchronous in (False, True):
        for scenario in ('complete', 'empty', 'intermediate-empty', 'repeat', 'budget', 'items'):
            calls, responses, rows, tokens = [], [], [], []
            max_pages = BUDGETS['max_pages']
            status, unconsumed, continuation = 'complete', [], None
            def handler(request):
                index = len(calls)
                assert index < (max_pages if scenario == 'budget' else 2), 'Bounded reader exceeded page budget'
                expected = copy.deepcopy(c)
                if index:
                    cursor = ('cursor079-budget-' + str(index)) if scenario == 'budget' else 'cursor079-next'
                    expected['wire'] = source_wire(c, {**c['kwargs'], 'page_token': cursor, 'request_timeout': 7})
                H.check_wire(request, expected)
                calls.append(request)
                response = H.response_for({**c, 'response': page_case(c, index, scenario)})
                responses.append(response)
                return response
            async def read(client, kwargs):
                raw = await H.invoke(client, c, 'raw', kwargs)
                try:
                    return H.typed_value(c, raw.decode())
                finally:
                    await raw.aclose()
            def read_sync(client, kwargs):
                raw = H.invoke(client, c, 'raw', kwargs)
                try:
                    return H.typed_value(c, raw.decode())
                finally:
                    raw.close()
            async def collect(client):
                nonlocal status, unconsumed, continuation
                for index in range(max_pages):
                    kwargs = copy.deepcopy(c['kwargs'])
                    if tokens:
                        kwargs['page_token'] = tokens[-1]
                    page = await read(client, kwargs) if asynchronous else read_sync(client, kwargs)
                    continuation = page.get('nextPageToken')
                    if scenario == 'items':
                        rows.extend(page['data'][:1])
                        unconsumed = page['data'][1:]
                        status = 'item-limit'
                        break
                    rows.extend(page['data'])
                    if not continuation:
                        break
                    if continuation in tokens:
                        status = 'repeated-token'
                        break
                    tokens.append(continuation)
                else:
                    status = 'page-limit'
            if asynchronous:
                async with H.async_client(c, handler) as client:
                    await collect(client)
            else:
                with H.sync_client(c, handler) as client:
                    await collect(client)
            expected_status = {'repeat': 'repeated-token', 'budget': 'page-limit', 'items': 'item-limit'}.get(scenario, 'complete')
            assert status == expected_status
            assert len(calls) == (3 if scenario == 'budget' else 2 if scenario in ('complete', 'repeat', 'intermediate-empty') else 1)
            assert len(rows) == (0 if scenario == 'empty' else 1 if scenario == 'intermediate-empty' else len(calls))
            if scenario == 'budget':
                assert tokens == ['cursor079-budget-1', 'cursor079-budget-2', 'cursor079-budget-3']
                assert continuation == 'cursor079-budget-3'
            assert all(r.is_closed for r in responses)
            assert len(unconsumed) == int(scenario == 'items')
            H.record(c, ('async_' if asynchronous else 'sync_') + 'finite_paging_' + scenario,
                     status=status, requests=len(calls), retained=rows, continuation=continuation, unconsumed=unconsumed)
        if c['source']['iterator']:
            for native_scenario in ('complete', 'early', 'intermediate-empty'):
                early = native_scenario == 'early'
                calls, responses = [], []
                def handler(request):
                    index = len(calls)
                    assert index < (1 if early else 2)
                    expected = copy.deepcopy(c)
                    if index:
                        expected['wire'] = source_wire(c, {**c['kwargs'], 'page_token': 'cursor079-next', 'request_timeout': 7})
                    H.check_wire(request, expected)
                    calls.append(request)
                    response = H.response_for({**c, 'response': page_case(c, index, native_scenario)})
                    responses.append(response)
                    return response
                values = []
                if asynchronous:
                    async with H.async_client(c, handler) as client:
                        iterator = H.invoke(client, c, 'ordinary')
                        assert hasattr(iterator, '__aiter__') and not inspect.isawaitable(iterator)
                        async for value in iterator:
                            values.append(H.typed_value(c, value, True))
                            if early:
                                break
                else:
                    with H.sync_client(c, handler) as client:
                        iterator = H.invoke(client, c, 'ordinary')
                        for value in iterator:
                            values.append(H.typed_value(c, value, True))
                            if early:
                                break
                assert len(calls) == (1 if early else 2)
                assert len(values) == (1 if early or native_scenario == 'intermediate-empty' else 2)
                assert all(r.is_closed for r in responses)
                H.record(c, ('async_' if asynchronous else 'sync_') + 'direct_iterator_' + native_scenario,
                         requests=len(calls), retained=values)
