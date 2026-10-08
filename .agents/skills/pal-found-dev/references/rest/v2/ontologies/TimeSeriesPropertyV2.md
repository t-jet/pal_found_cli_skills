# TimeSeriesPropertyV2 operations

[REST development](../../../rest-api.md) | [Ontology service](index.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

Time-series properties expose first, last and streamed points. Streaming may span many values; clients must bound consumption and close response resources.

## Prerequisites

Use the frozen Foundry Python SDK 1.101.0 and an authorized Ontology, branch, resource identifier, acting identity and exact type/parameter names from the enrollment. Prepare the linked local models before a live request. Synthetic examples run offline with the prepared SDK and mock transport; real reads or writes require enrollment access, resource permissions and any listed beta enablement. An administrator or resource owner supplies missing grants and capability access.

## Procedure and operation choices

Select the operation below, read its exact request/response/error model, then adapt the linked SDK fixture with authorized resource values. The fixture uses synthetic identifiers and checks serialized transport; it does not assert tenant behavior. Record branch, version, page/snapshot context, response and named errors for the actual call.

### `TimeSeriesPropertyV2.get_first_point`

Stage: Stable. Required SDK arguments: `ontology`, `object_type`, `primary_key`, `property`.

Get the first point of a time series property.

Read [exact contract](../../contracts/v2/ontologies/TimeSeriesPropertyV2/get_first_point.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/TimeSeriesPropertyV2/invoke_get_first_point.py): `python -B examples/rest/083/v2/ontologies/TimeSeriesPropertyV2/invoke_get_first_point.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `TimeSeriesPropertyV2.get_last_point`

Stage: Stable. Required SDK arguments: `ontology`, `object_type`, `primary_key`, `property`.

Get the last point of a time series property.

Read [exact contract](../../contracts/v2/ontologies/TimeSeriesPropertyV2/get_last_point.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/TimeSeriesPropertyV2/invoke_get_last_point.py): `python -B examples/rest/083/v2/ontologies/TimeSeriesPropertyV2/invoke_get_last_point.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `TimeSeriesPropertyV2.stream_points`

Stage: Stable. Required SDK arguments: `ontology`, `object_type`, `primary_key`, `property`.

Stream all of the points of a time series property.

Read [exact contract](../../contracts/v2/ontologies/TimeSeriesPropertyV2/stream_points.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/TimeSeriesPropertyV2/invoke_stream_points.py): `python -B examples/rest/083/v2/ontologies/TimeSeriesPropertyV2/invoke_stream_points.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

## Worked example

For an approved sensor property, read first and last points, then stream a bounded interval/sample. Compare timestamps and values; close streaming handles on normal exit or error.

```python
api = client.ontologies.TimeSeriesPropertyV2
key = dict(ontology="operations", object_type="Sensor",
           primary_key="S-1", property="temperature")
first = api.get_first_point(**key)
last = api.get_last_point(**key)
if first is not None and last is not None:
    assert first.time <= last.time
    print(first.time, first.value, last.time, last.value)

byte_budget = 1_000_000
received = 0
with api.with_streaming_response.stream_points(
    **key, format="JSON", request_timeout=30
) as response:
    for chunk in response.iter_bytes():
        received += len(chunk)
        if received > byte_budget:
            raise ValueError("time-series byte budget exceeded")
        # Decode complete JSON records using the selected stream format.
```

First/last can return `None`. A stream returns bytes, not a typed point
iterator. Set a `range` model for a time-bounded request; its field contract is
linked from `stream_points`. The context manager closes the HTTP response even
when parsing or budget checks fail. Compare actual timestamps, since the latest
point may be older than the business freshness requirement.

The linked operation fixtures show actual SDK method invocation, serialized request and decoded response/error using a local mock transport. Their synthetic values are test data. Replace them with authorized identifiers and typed payloads from each linked contract; verify the live result under the intended identity before asserting a platform effect.

## Expected result and checks

Record exact operation ID, API version, release stage, branch, requested IDs, returned IDs, page/snapshot token, response mode and decoded result. For effectful calls, inspect validation/commit state and fresh target data; a successful HTTP response alone may not establish the business result. For lists, finish pagination before claiming completeness.

## Failures and recovery

On a missing or filtered result, verify Ontology/type/API names, branch and effective caller permissions. On schema rejection, compare payload fields, requiredness, aliases and discriminator values with the linked models. On a timeout after an effectful call, reconcile target or transaction state before retrying. Bound pages, streamed bytes and time windows; close streaming/raw responses according to [client lifetimes](../../client-behavior.md). Missing beta enablement is a prerequisite to resolve with the enrollment owner.
