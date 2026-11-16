"""v2.ontologies.GeotemporalSeriesProperty.load_geotemporal_series_entries: SDK request, decoded result and declared error fixtures.

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
from foundry_sdk.v2.ontologies.geotemporal_series_property import GeotemporalSeriesPropertyClient

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'common'))
from mock_transport import mock_resource

EXPECTED_METHOD = 'POST'
EXPECTED_PATH = '/api/v2/ontologies/synthetic-value/objects/Asset/A-1/geotemporalSeries/synthetic-value/loadEntries'
EXPECTED_BODY = {'range': {'type': 'absolute',
           'startTime': '2026-01-01T00:00:00+00:00',
           'endTime': '2026-01-01T00:02:00+00:00'},
 'additionalProperties': ['speed'],
 'pageSize': 1}
EXPECTED_QUERY = {'preview': None, 'sdkPackageRid': None, 'sdkVersion': None}
EXPECTED_HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json'}
SUCCESS = {'data': [{'time': '2026-01-01T00:00:00+00:00',
           'position': {'type': 'Point', 'coordinates': [23.3, 42.7]},
           'speed': 12.5}],
 'nextPageToken': 'next-synthetic-page'}
ERRORS = []

def invoke(client, page_token=None):
    return client.with_raw_response.load_geotemporal_series_entries(
        ontology='synthetic-value', object_type='Asset', primary_key='A-1',
        property='synthetic-value', additional_properties=['speed'],
        range=EXPECTED_BODY['range'], page_size=1, page_token=page_token,
        request_timeout=30)

def load_entries(client, page_budget=3):
    """Return complete bounded results, or fail without claiming completeness."""
    token = None
    seen = set()
    entries = []
    for _ in range(page_budget):
        raw = invoke(client, token)
        try:
            page = raw.decode()
        finally:
            raw.close()
        for entry in page.data:
            if 'time' not in entry or 'position' not in entry:
                raise ValueError('Expected time and position in geotemporal entry')
        entries.extend(page.data)
        token = page.next_page_token
        if token is None:
            return entries
        if token in seen:
            raise ValueError('Repeated geotemporal page token')
        seen.add(token)
    raise ValueError('Geotemporal page budget exceeded; result incomplete')

def check_request(request, page_token=None):
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
        body = dict(EXPECTED_BODY)
        if page_token is not None:
            body['pageToken'] = page_token
        assert json.loads(request.content) == body

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
    second = {'time': '2026-01-01T00:01:00Z',
              'position': {'type': 'Point', 'coordinates': [23.31, 42.71]},
              'speed': 13.0}
    def success(request):
        token = None if not calls else 'next-synthetic-page'
        check_request(request, token)
        calls.append(token)
        return httpx.Response(200, json=SUCCESS if token is None else {'data': [second]})
    with mock_resource(GeotemporalSeriesPropertyClient, success) as client:
        entries = load_entries(client)
    assert calls == [None, 'next-synthetic-page']
    assert entries == SUCCESS['data'] + [second]
    for error_case in ERRORS:
        def failure(request):
            check_request(request)
            return httpx.Response(error_case['status'], json={
                'errorName':error_case['name'], 'errorCode':error_case['code'],
                'parameters':error_case['parameters'],
                'errorInstanceId':'00000000-0000-0000-0000-000000000004',
            })
        with mock_resource(GeotemporalSeriesPropertyClient, failure) as client:
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
    print('v2.ontologies.GeotemporalSeriesProperty.load_geotemporal_series_entries' + ': serialized request, decoded result and ' + str(len(ERRORS)) + ' named errors passed')
