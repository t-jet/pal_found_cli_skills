"""Process sparse stream offsets before acknowledging a subscriber position.

SDK 1.101.0 uses in-process synthetic HTTP responses. No records are read from
Foundry and no subscriber position changes in an enrollment.
"""

import json
import sys
from pathlib import Path

import httpx
from foundry_sdk.v2.streams.subscriber import SubscriberClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
from mock_transport import mock_resource

DATASET = "ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001"
BRANCH = "orders"
SUBSCRIBER = "billing-worker"


def verify() -> None:
    requests = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        assert request.url.path.endswith(f"/streams/{BRANCH}/subscribers/{SUBSCRIBER}/" + (
            "readRecords" if len(requests) == 1 else "commitOffsets"
        ))
        body = json.loads(request.content)
        if len(requests) == 1:
            assert body == {"autoCommit": False, "limit": 2}
            return httpx.Response(200, json={"recordsByPartition": {"0": [
                {"offset": "50", "value": {"orderId": "A"}},
                {"offset": "52", "value": {"orderId": "B"}},
            ]}})
        assert body == {"offsets": {"0": 52}}
        return httpx.Response(200, json={"0": "52"})

    with mock_resource(SubscriberClient, handler) as subscriber:
        batch = subscriber.read_records(
            DATASET, BRANCH, SUBSCRIBER, auto_commit=False, limit=2,
            request_timeout=30,
        )
        records = batch.records_by_partition["0"]
        assert [record.value["orderId"] for record in records] == ["A", "B"]
        # Simulated durable business handling succeeds for both records.
        last_processed = records[-1].offset
        assert last_processed == 52
        committed = subscriber.commit_offsets(
            DATASET, BRANCH, SUBSCRIBER, offsets={"0": last_processed},
            request_timeout=30,
        )
        assert committed["0"] == last_processed
    assert len(requests) == 2


if __name__ == "__main__":
    verify()
    print("Sparse offsets 50,52 processed; last processed 52 committed through SDK")
