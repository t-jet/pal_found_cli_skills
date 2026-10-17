"""Synthetic global Query contract; actual SDK transport, no tenant execution."""

import json
import sys
from pathlib import Path

import httpx
from foundry_sdk import PalantirRPCException
from foundry_sdk.v2.functions.query import QueryClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'common'))
from mock_transport import mock_resource


def verify():
    # Synthetic published function: scale(amount: integer, factor: integer) -> integer.
    # Real argument/result definitions must come from the selected Query metadata.
    def request_check(request):
        assert request.url.path == '/api/v2/functions/queries/scale/execute'
        assert request.method == 'POST'
        assert request.url.params['preview'] == 'true'
        assert json.loads(request.content) == {
            'parameters': {'amount': 2, 'factor': 3}, 'version': '1.0.0', 'branch': 'master',
        }

    def success(request):
        request_check(request)
        return httpx.Response(200, json={'value': 6})

    with mock_resource(QueryClient, success) as client:
        result = client.execute('scale', parameters={'amount': 2, 'factor': 3},
                                version='1.0.0', branch='master', preview=True,
                                request_timeout=30)
        assert result.value == 6

    def denied(request):
        request_check(request)
        return httpx.Response(403, json={
            'errorName': 'ExecuteQueryPermissionDenied', 'errorCode': 'PERMISSION_DENIED',
            'parameters': {'queryApiName': 'scale'},
            'errorInstanceId': '00000000-0000-0000-0000-000000000004',
        })

    with mock_resource(QueryClient, denied) as client:
        try:
            client.execute('scale', parameters={'amount': 2, 'factor': 3},
                           version='1.0.0', branch='master', preview=True,
                           request_timeout=30)
        except PalantirRPCException as error:
            assert type(error).__name__ == 'ExecuteQueryPermissionDenied'
            assert error.parameters == {'queryApiName': 'scale'}
        else:
            raise AssertionError('denied Query accepted')


if __name__ == '__main__':
    verify()
    print('Pinned global Query arguments/result and named denial passed; no live function executed.')
