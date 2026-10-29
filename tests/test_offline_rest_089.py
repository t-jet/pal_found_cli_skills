"""SDK101 transport checks and source-derived semantic regression guards."""

import copy
import inspect
import io
import runpy
import socket
import zipfile
from pathlib import Path

import pytest
from foundry_sdk.v2.connectivity import models as connectivity
from foundry_sdk.v2.connectivity.connection import ConnectionClient
from foundry_sdk.v2.sql_queries.sql_query import SqlQueryClient
from foundry_sdk.v2.streams.stream import StreamClient
from foundry_sdk.v2.streams.subscriber import SubscriberClient

ROOT = Path(__file__).parents[1]
DEV = ROOT / '.agents/skills/pal-found-dev'
EXAMPLES = DEV / 'examples/rest/089/v2'
FILES = sorted(EXAMPLES.rglob('invoke_*.py'))


@pytest.fixture(autouse=True)
def deny_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError('Network forbidden in offline REST089 tests')
    for name in ('connect', 'connect_ex'):
        monkeypatch.setattr(socket.socket, name, denied)
    for name in ('create_connection', 'getaddrinfo', 'gethostbyname', 'gethostbyname_ex'):
        monkeypatch.setattr(socket, name, denied)


@pytest.mark.parametrize('path', FILES, ids=lambda path: str(path.relative_to(EXAMPLES)))
def test_all_owned_examples_use_real_sdk_with_mock_http(path):
    runpy.run_path(str(path))['verify']()


def load(resource, method):
    return runpy.run_path(str(EXAMPLES / resource / f'invoke_{method}.py'))


def assert_semantics(case, example):
    body = example['EXPECTED_BODY']
    if case == 'connection':
        assert body['worker']['type'] == 'foundryWorker'
        assert body['worker']['networkEgressPolicyRids']
        assert body['configuration']['bucketUrl'].startswith('s3://')
        assert body['configuration']['bucketUrl'].endswith('/')
        assert example['SUCCESS']['configuration'] == body['configuration']
        assert example['SUCCESS']['worker'] == body['worker']
    elif case == 'secret':
        assert body['secrets'] and all(body['secrets'].values())
    elif case == 'jdbc':
        name = example['EXPECTED_QUERY']['fileName']
        assert name.endswith('.jar')
        with zipfile.ZipFile(io.BytesIO(body)) as jar:
            assert 'META-INF/MANIFEST.MF' in jar.namelist()
        config = example['SUCCESS']['configuration']
        assert config['type'] == 'jdbc'
        assert name in config['uploadedJdbcDrivers']
        connectivity.JdbcConnectionConfiguration.model_validate(config)
    elif case == 'query':
        assert body['config']['query'] == 'SELECT order_id, total FROM main.sales.orders LIMIT 100'
        assert example['SUCCESS']['config'] == body['config']
    elif case == 'record':
        records = [body['record']] if 'record' in body else body['records']
        assert records
        for record in records:
            assert set(record) == {'orderId', 'quantity'}
            assert isinstance(record['orderId'], str) and record['orderId']
            assert type(record['quantity']) is int
        assert example['SUCCESS'] is None
    elif case == 'reset':
        position = body['position']
        assert position['type'] == 'specific' and position['offsets']
        assert all(type(offset) is int and offset >= 0 for offset in position['offsets'].values())
        assert example['SUCCESS'] == position['offsets']
    elif case == 'end':
        assert example['SUCCESS']['0'] == 53 and example['SUCCESS']['1'] == 0


CASES = [
    ('connection', 'connectivity/Connection', 'create'),
    ('secret', 'connectivity/Connection', 'update_secrets'),
    ('jdbc', 'connectivity/Connection', 'upload_custom_jdbc_drivers'),
    ('query', 'connectivity/TableImport', 'create'),
    ('query', 'connectivity/TableImport', 'replace'),
    ('record', 'streams/Stream', 'publish_record'),
    ('record', 'streams/Stream', 'publish_records'),
    ('reset', 'streams/Subscriber', 'reset_offsets'),
    ('end', 'streams/Stream', 'get_end_offsets'),
]


@pytest.mark.parametrize('case,resource,method', CASES)
def test_meaningful_examples_reject_original_semantic_mutations(case, resource, method):
    example = load(resource, method)
    assert_semantics(case, example)
    mutated = dict(example)
    mutated['EXPECTED_BODY'] = copy.deepcopy(example['EXPECTED_BODY'])
    mutated['SUCCESS'] = copy.deepcopy(example['SUCCESS'])
    mutated['EXPECTED_QUERY'] = copy.deepcopy(example['EXPECTED_QUERY'])
    body = mutated['EXPECTED_BODY']
    if case == 'connection':
        body['worker'] = {'type': 'unknownWorker'}
    elif case == 'secret':
        body['secrets'] = {}
    elif case == 'jdbc':
        mutated['EXPECTED_QUERY']['fileName'] = 'synthetic-value'
    elif case == 'query':
        body['config']['query'] = 'synthetic-value'
    elif case == 'record':
        body.update({'record': {}} if 'record' in body else {'records': [{}]})
    elif case == 'reset':
        body['position']['offsets'] = {}
    elif case == 'end':
        mutated['SUCCESS'] = {}
    with pytest.raises((AssertionError, KeyError)):
        assert_semantics(case, mutated)


def test_sdk_source_contracts_ground_semantic_guards():
    assert 'trailing slash' in inspect.getsource(connectivity.S3ConnectionConfiguration)
    assert 'UnknownWorkerCannotBeUsedForCreatingOrUpdatingConnections' in inspect.getsource(ConnectionClient.create)
    assert '.jar' in inspect.getdoc(ConnectionClient.upload_custom_jdbc_drivers)
    assert 'next record' in inspect.getdoc(StreamClient.get_end_offsets)
    assert 'specific' in inspect.getdoc(SubscriberClient.reset_offsets)
    assert 'Arrow' in inspect.getdoc(SqlQueryClient.execute_ontology)
    assert inspect.signature(StreamClient.publish_record).return_annotation is None


def test_ontology_arrow_decode_and_budgets_reject_invalid_results():
    example = load('sql_queries/SqlQuery', 'execute_ontology')
    assert example['EXPECTED_BODY']['rowLimit'] == 10
    assert example['EXPECTED_BODY']['query'] == 'SELECT orderId FROM Orders LIMIT 10'
    assert example['EXPECTED_BODY']['ontologyIdentifier']
    decode = example['decode_result']
    assert decode(example['SUCCESS']) == [{'orderId': 'order-001'}]
    import pyarrow as pa
    with pytest.raises(pa.ArrowInvalid):
        decode(b'offline synthetic content')
    with pytest.raises(ValueError, match='byte budget'):
        decode(b'x' * (example['MAX_RESULT_BYTES'] + 1))
    sink = pa.BufferOutputStream()
    with pa.ipc.new_stream(sink, pa.schema([('orderId', pa.string())])) as writer:
        writer.write_table(pa.table({'orderId': ['order-001'] * 11}))
    with pytest.raises(ValueError, match='row budget'):
        decode(sink.getvalue().to_pybytes())


def test_dataset_and_publish_guidance_match_actual_return_shapes():
    dataset = load('streams/Dataset', 'create')
    assert set(dataset['SUCCESS']) == {'rid', 'name', 'parentFolderRid'}
    guide = (DEV / 'references/rest/v2/streams/Dataset.md').read_text()
    assert 'Stream.get(dataset_rid, stream_branch_name)' in guide
    assert 'response contains no stream or view identity' in guide
    stream = (DEV / 'references/rest/v2/streams/Stream.md').read_text()
    assert 'SDK returns `None`' in stream
    assert 'Confirm the returned write result' not in stream
