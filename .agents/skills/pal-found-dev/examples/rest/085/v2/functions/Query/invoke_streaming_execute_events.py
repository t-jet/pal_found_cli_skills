"""Verify SDK Query SSE data, error, budgets and cleanup without network access."""

from sse_fixture import verify


if __name__ == "__main__":
    verify("streaming_execute_events", "StreamingExecuteEventsQueryPermissionDenied")
    print("v2.functions.Query.streaming_execute_events: SSE fixtures passed")
