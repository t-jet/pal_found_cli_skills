"""v1.ontologies.OntologyObject.aggregate: SDK request, decoded result and declared error fixtures.

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
from foundry_sdk.v1.ontologies.ontology_object import OntologyObjectClient

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / 'common'))
from mock_transport import mock_resource

EXPECTED_METHOD = 'POST'
EXPECTED_PATH = '/api/v1/ontologies/ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001/objects/Asset/aggregate'
EXPECTED_BODY = {'aggregation': [{'field': 'properties.assetId',
                  'name': 'distinctAssets',
                  'type': 'approximateDistinct'}],
 'groupBy': [{'field': 'properties.inspectionDate',
              'duration': 'P1D',
              'type': 'duration'}]}
EXPECTED_QUERY = {}
EXPECTED_HEADERS = {'Content-Type': 'application/json', 'Accept': 'application/json'}
SUCCESS = {'data': [{'group': {'properties.inspectionDate': '2026-10-01'},
           'metrics': [{'name': 'distinctAssets', 'value': 1.0}]}]}
# This mock chooses a request-like label and ISO date value. The SDK response
# group is Dict[str, Any]; it specifies neither convention nor bucket boundaries.
ERRORS = []

def invoke(client):
    return client.with_raw_response.aggregate(ontology_rid='ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001', object_type='Asset', aggregation=[{'field': 'properties.assetId', 'name': 'distinctAssets', 'type': 'approximateDistinct'}], group_by=[{'field': 'properties.inspectionDate', 'duration': 'P1D', 'type': 'duration'}], request_timeout=30)

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

def check_result(result, request):
    body = json.loads(request.content)
    group = body['groupBy'][0]
    assert group['field'] == 'properties.inspectionDate', 'Duration grouping needs declared date field'
    assert group['duration'] == 'P1D', 'Expected ISO 8601 one-day duration'
    metric = body['aggregation'][0]
    assert metric['field'] == 'properties.assetId', 'Metric field missing from Asset schema'
    for bucket in result['data']:
        # Inspect actual returned labels without mapping them to request fields.
        assert isinstance(bucket['group'], dict)
        for label in bucket['group']:
            assert isinstance(label, str), 'SDK group labels are strings'
            # Values remain opaque until the application confirms their meaning.
        assert bucket['metrics'][0]['name'] == metric['name'], 'Metric alias differs from request'
        value = bucket['metrics'][0]['value']
        assert isinstance(value, (int, float)) and value >= 0, 'Distinct count needs nonnegative numeric value'


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
        calls.append(request)
        if isinstance(SUCCESS, bytes):
            return httpx.Response(200, content=SUCCESS)
        if SUCCESS is None:
            return httpx.Response(204)
        return httpx.Response(200, json=SUCCESS)
    with mock_resource(OntologyObjectClient, success) as client:
        raw = invoke(client)
        try:
            result = normalized(raw.decode())
            check_result(result, calls[-1])
            assert result == SUCCESS
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
        with mock_resource(OntologyObjectClient, failure) as client:
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
    print('v1.ontologies.OntologyObject.aggregate' + ': serialized request, decoded result and ' + str(len(ERRORS)) + ' named errors passed')
