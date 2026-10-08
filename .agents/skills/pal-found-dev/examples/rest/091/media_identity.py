"""Synthetic media identity and bounded bytes through actual SDK transport."""

import base64
import sys
from pathlib import Path

import httpx
from foundry_sdk.v2.media_sets.media_set import MediaSetClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'common'))
from mock_transport import mock_resource

SET = 'ri.mediasets.main.media-set.inspections'
ITEM = 'ri.mediasets.main.media-item.pixel'
PNG = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+a5n8AAAAASUVORK5CYII=')


def verify():
    observed = []

    def serve(request):
        observed.append(str(request.url.path))
        assert request.method == 'GET'
        if request.url.path.endswith('/' + SET):
            return httpx.Response(200, json={
                'rid': SET, 'mediaSchema': 'IMAGERY', 'defaultBranchName': 'master',
                'transactionPolicy': {'type': 'batchTransactions'}, 'pathsRequired': True,
            })
        assert request.url.path.endswith('/' + ITEM + '/content')
        return httpx.Response(200, content=PNG, headers={'Content-Type': 'image/png'})

    with mock_resource(MediaSetClient, serve) as client:
        metadata = client.get(SET, request_timeout=30)
        assert metadata.media_schema == 'IMAGERY'
        assert metadata.transaction_policy.type == 'batchTransactions'
        assert metadata.paths_required is True
        chunks = bytearray()
        with client.with_streaming_response.read(SET, ITEM, request_timeout=30) as response:
            for chunk in response.iter_bytes():
                if len(chunks) + len(chunk) > 1024:
                    raise ValueError('media byte budget exceeded')
                chunks.extend(chunk)
        assert bytes(chunks) == PNG
        assert bytes(chunks).startswith(b'\x89PNG\r\n\x1a\n')
    assert len(observed) == 2


if __name__ == '__main__':
    verify()
    print('Media schema/policy and bounded PNG byte transport passed; no tenant upload performed.')
