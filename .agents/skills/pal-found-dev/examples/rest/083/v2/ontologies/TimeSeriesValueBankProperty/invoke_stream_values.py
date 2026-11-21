"""v2.ontologies.TimeSeriesValueBankProperty.stream_values: SDK request, decoded result and declared error fixtures.

JSON array is a synthetic fixture encoding, not an SDK wire-format guarantee.
Verify enrollment schema and framing before adapting the parser.
Synthetic identifiers do not name tenant resources. Prepared SDK 1.101.0/httpx
required. No network connections or live mutations occur.
"""
import json
import sys
import urllib.parse
import datetime
from pathlib import Path

import httpx
from foundry_sdk import PalantirRPCException
from foundry_sdk.v2.ontologies.time_series_value_bank_property import TimeSeriesValueBankPropertyClient

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'common'))
from mock_transport import mock_resource

EXPECTED_METHOD = 'POST'
EXPECTED_PATH = '/api/v2/ontologies/synthetic-value/objects/Asset/A-1/timeseries/synthetic-value/streamValues'
EXPECTED_BODY = {'range': {'type': 'absolute',
           'startTime': '2026-01-01T00:00:00+00:00',
           'endTime': '2026-01-01T00:02:00+00:00'}}
EXPECTED_QUERY = {'branch': None, 'sdkPackageRid': None, 'sdkVersion': None}
EXPECTED_HEADERS = {'Content-Type': 'application/json', 'Accept': '*/*'}
SUCCESS = (b'[{"time": "2026-01-01T00:00:00+00:00", "value": 21.5}, {"time": "2026-01-01T00:01'
 b':00Z", "value": 22.0}]')
ERRORS = []

def invoke(client):
    return client.with_raw_response.stream_values(ontology='synthetic-value', object_type='Asset', primary_key='A-1', property='synthetic-value', range=EXPECTED_BODY['range'], request_timeout=30)

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

# This JSON array is a synthetic fixture encoding. Verify enrollment framing
# and property value types before adapting its parser to live data.
MAX_BYTES = 4096
EXPECTED_RECORDS = [{'time': '2026-01-01T00:00:00+00:00', 'value': 21.5}, {'time': '2026-01-01T00:01:00Z', 'value': 22.0}]

def parse_records(chunks, byte_budget=MAX_BYTES):
    payload = bytearray()
    for chunk in chunks:
        if len(payload) + len(chunk) > byte_budget:
            raise ValueError('Time-series byte budget exceeded; result incomplete')
        payload.extend(chunk)
    records = json.loads(payload)
    if not isinstance(records, list):
        raise ValueError('Fixture expects a JSON array')
    for record in records:
        if not isinstance(record, dict) or 'time' not in record or 'value' not in record:
            raise ValueError('Fixture expects time and value fields')
        stamp = datetime.datetime.fromisoformat(record['time'].replace('Z', '+00:00'))
        start = datetime.datetime.fromisoformat(EXPECTED_BODY['range']['startTime'].replace('Z', '+00:00'))
        end = datetime.datetime.fromisoformat(EXPECTED_BODY['range']['endTime'].replace('Z', '+00:00'))
        if stamp.tzinfo is None or not start <= stamp < end:
            raise ValueError('Point outside requested interval')
    return records

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
    with mock_resource(TimeSeriesValueBankPropertyClient, success) as client:
        raw = invoke(client)
        try:
            payload = raw.decode()
            assert payload == SUCCESS
            assert parse_records([payload[:17], payload[17:]]) == EXPECTED_RECORDS
        finally:
            raw.close()
    with mock_resource(TimeSeriesValueBankPropertyClient, success) as client:
        with client.with_streaming_response.stream_values(
            ontology='synthetic-value', object_type='Asset', primary_key='A-1',
            property='synthetic-value', range=EXPECTED_BODY['range'],
            request_timeout=30
        ) as response:
            assert parse_records(response.iter_bytes(chunk_size=17)) == EXPECTED_RECORDS
        assert response._response.is_closed
    assert len(calls) == 2
    for error_case in ERRORS:
        def failure(request):
            check_request(request)
            return httpx.Response(error_case['status'], json={
                'errorName':error_case['name'], 'errorCode':error_case['code'],
                'parameters':error_case['parameters'],
                'errorInstanceId':'00000000-0000-0000-0000-000000000004',
            })
        with mock_resource(TimeSeriesValueBankPropertyClient, failure) as client:
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
    print('v2.ontologies.TimeSeriesValueBankProperty.stream_values' + ': serialized request, decoded result and ' + str(len(ERRORS)) + ' named errors passed')
