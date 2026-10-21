"""Submit, poll and consume a bounded CSV SQL result with SDK 1.101.0.

The in-process HTTP fixture stands in for Foundry. It does not execute SQL or
prove dataset access in an enrollment.
"""

import csv
import io
import json
import sys
from pathlib import Path

import httpx
from foundry_sdk.v2.sql_queries.sql_query import SqlQueryClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
from mock_transport import mock_resource


def verify() -> None:
    query_id = "synthetic-count-1"
    polls = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal polls
        if request.url.path == "/api/v2/sqlQueries/execute":
            assert request.method == "POST"
            assert json.loads(request.content) == {
                "query": "SELECT 1 AS row_count", "serializationFormat": "CSV"
            }
            return httpx.Response(200, json={"type": "running", "queryId": query_id})
        if request.url.path == f"/api/v2/sqlQueries/{query_id}/getStatus":
            assert request.method == "GET"
            polls += 1
            return httpx.Response(200, json={
                "type": "running" if polls == 1 else "succeeded", "queryId": query_id
            })
        assert request.url.path == f"/api/v2/sqlQueries/{query_id}/getResults"
        assert request.method == "GET"
        assert request.headers["Accept"] == "application/octet-stream"
        return httpx.Response(200, content=b"row_count\n1\n")

    with mock_resource(SqlQueryClient, handler) as queries:
        submission = queries.execute(
            query="SELECT 1 AS row_count", serialization_format="CSV", request_timeout=30,
        )
        assert submission.query_id == query_id
        for _ in range(3):
            status = queries.get_status(query_id, request_timeout=30)
            if status.type == "succeeded":
                break
        else:
            raise AssertionError("SQL query did not finish within polling budget")
        payload = queries.get_results(query_id, request_timeout=65)
        rows = list(csv.DictReader(io.StringIO(payload.decode("utf-8"))))
        assert rows == [{"row_count": "1"}]
    assert polls == 2


if __name__ == "__main__":
    verify()
    print("SQL submitted, polled and bounded CSV result decoded through SDK")
