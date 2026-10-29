"""v2.sql_queries.SqlQuery.execute_ontology: SDK request, decoded result and declared error fixtures.

Synthetic identifiers do not name tenant resources. Prepared SDK 1.101.0/httpx
and pyarrow required. No network connections or live mutations occur.

Assume example-ontology exposes an Orders object type with string orderId,
backed by Object Storage V2 and visible to the caller. Replace these names with
authorized ontology/type/property API names. This synchronous route returns
Arrow IPC bytes directly. rowLimit and LIMIT bound rows; the decoder rejects
oversized payloads before Arrow parsing. SDK bytes are already buffered, so this
check bounds decode work, not transport memory. The fixture does not run SQL.
"""
import json
import sys
import urllib.parse
import datetime
from pathlib import Path

import httpx
import pyarrow as pa
from foundry_sdk import PalantirRPCException
from foundry_sdk.v2.sql_queries.sql_query import SqlQueryClient

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'common'))
from mock_transport import mock_resource

EXPECTED_METHOD = 'POST'
EXPECTED_PATH = '/api/v2/sqlQueries/executeOntology'
QUERY = 'SELECT orderId FROM Orders LIMIT 10'
EXPECTED_BODY = {'query': QUERY, 'ontologyIdentifier': 'example-ontology', 'rowLimit': 10}
EXPECTED_QUERY = {'preview': None}
EXPECTED_HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/octet-stream'}
sink = pa.BufferOutputStream()
with pa.ipc.new_stream(sink, pa.schema([('orderId', pa.string())])) as writer:
    writer.write_table(pa.table({'orderId': ['order-001']}))
SUCCESS = sink.getvalue().to_pybytes()
MAX_RESULT_BYTES = 65536

def decode_result(payload):
    if len(payload) > MAX_RESULT_BYTES:
        raise ValueError('Ontology result exceeds byte budget')
    table = pa.ipc.open_stream(payload).read_all()
    if table.num_rows > 10:
        raise ValueError('Ontology result exceeds row budget')
    assert table.schema == pa.schema([('orderId', pa.string())])
    return table.to_pylist()
ERRORS = [{'name': 'ExecuteOntologySqlQueryPermissionDenied',
  'status': 403,
  'code': 'PERMISSION_DENIED',
  'parameters': {}},
 {'name': 'OntologyObjectTypeNotFound',
  'status': 404,
  'code': 'NOT_FOUND',
  'parameters': {'objectTypeRid': 'ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001'}},
 {'name': 'OntologyQueryFailed',
  'status': 500,
  'code': 'INTERNAL',
  'parameters': {'errorMessage': 'synthetic-value'}},
 {'name': 'OntologyQueryInvalidObjectBackend',
  'status': 400,
  'code': 'INVALID_ARGUMENT',
  'parameters': {'objectTypeRids': ['ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001'],
                 'linkTypeRids': ['ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001']}},
 {'name': 'OntologyQueryNestedObjectSetTooLarge',
  'status': 400,
  'code': 'INVALID_ARGUMENT',
  'parameters': {'nestedObjectSetSize': 1, 'maxAllowedNestedObjectSetSize': 1}},
 {'name': 'OntologyQueryStringColumnTooLong',
  'status': 400,
  'code': 'INVALID_ARGUMENT',
  'parameters': {'columnName': 'synthetic-value'}},
 {'name': 'QueryParseError',
  'status': 400,
  'code': 'INVALID_ARGUMENT',
  'parameters': {'errorMessage': 'synthetic-value'}}]

def invoke(client):
    return client.with_raw_response.execute_ontology(query=QUERY, ontology_identifier='example-ontology', row_limit=10, request_timeout=30)

def check_request(request):
    assert request.method == EXPECTED_METHOD
    assert urllib.parse.unquote(request.url.path) == EXPECTED_PATH
    assert request.headers['Authorization'] == 'Bearer offline-fixture-token'
    for key, value in EXPECTED_HEADERS.items():
        if value is None:
            assert key not in request.headers
        else:
            assert request.headers[key] == str(value)
    expected = httpx.QueryParams({key: value for key,value in EXPECTED_QUERY.items() if value is not None})
    assert sorted(request.url.params.multi_items()) == sorted(expected.multi_items())
    if isinstance(EXPECTED_BODY, bytes):
        assert request.content == EXPECTED_BODY
    elif EXPECTED_BODY is not None:
        assert json.loads(request.content) == EXPECTED_BODY

def normalized(value):
    if isinstance(value, dict):
        return {key: normalized(child) for key,child in value.items()}
    if isinstance(value, (list, tuple)):
        return [normalized(child) for child in value]
    if isinstance(value, (datetime.datetime, datetime.date)):
        return value.isoformat()
    if isinstance(value, bytes):
        return bytes(value)
    if hasattr(value, 'model_dump'):
        return value.model_dump(mode='json', by_alias=True, exclude_none=True)
    return value

def verify():
    calls = []
    def success(request):
        check_request(request)
        calls.append(True)
        if isinstance(SUCCESS, bytes):
            return httpx.Response(200, content=SUCCESS)
        if SUCCESS is None:
            return httpx.Response(204)
        return httpx.Response(200, json=SUCCESS)
    with mock_resource(SqlQueryClient, success) as client:
        raw = invoke(client)
        try:
            payload = raw.decode()
            assert normalized(payload) == SUCCESS
            assert decode_result(payload) == [{'orderId': 'order-001'}]
        finally:
            raw.close()
    assert len(calls) == 1
    for error_case in ERRORS:
        def failure(request):
            check_request(request)
            return httpx.Response(error_case['status'], json={
                'errorName':error_case['name'], 'errorCode':error_case['code'],
                'parameters':error_case['parameters'],
                'errorInstanceId':'00000000-0000-0000-0000-000000000004',
            })
        with mock_resource(SqlQueryClient, failure) as client:
            try:
                raw = invoke(client)
                raw.close()
            except PalantirRPCException as error:
                assert error.name == error_case['name']
                assert type(error).__name__ == error_case['name']
                assert normalized(error.parameters) == error_case['parameters']
            else:
                raise AssertionError('Expected ' + error_case['name'])

if __name__ == '__main__':
    verify()
    print('v2.sql_queries.SqlQuery.execute_ontology' + ': serialized request, decoded result and ' + str(len(ERRORS)) + ' named errors passed')
