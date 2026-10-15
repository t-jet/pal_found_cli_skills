# TimeSeriesValueBankProperty operations

[REST development](../../../rest-api.md) | [Ontology service](index.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

A value-bank time series can combine history and live integrations. Latest-value resolution may prefer live data; streaming is a separate bounded operation.

## Prerequisites

Use the frozen Foundry Python SDK 1.101.0 and an authorized Ontology, branch, resource identifier, acting identity and exact type/parameter names from the enrollment. Prepare the linked local models before a live request. Synthetic examples run offline with the prepared SDK and mock transport; real reads or writes require enrollment access, resource permissions and any listed beta enablement. An administrator or resource owner supplies missing grants and capability access.

## Procedure and operation choices

Select the operation below, read its exact request/response/error model, then adapt the linked SDK fixture with authorized resource values. The fixture uses synthetic identifiers and checks serialized transport; it does not assert tenant behavior. Record branch, version, page/snapshot context, response and named errors for the actual call.

### `TimeSeriesValueBankProperty.get_latest_value`

Stage: Stable. Required SDK arguments: `ontology`, `object_type`, `primary_key`, `property_name`.

Get the latest value of a property backed by a timeseries. If a specific geotime series integration has both a history and a live integration, we will give precedence to the live integration.

Read [exact contract](../../contracts/v2/ontologies/TimeSeriesValueBankProperty/get_latest_value.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/TimeSeriesValueBankProperty/invoke_get_latest_value.py): `python -B examples/rest/083/v2/ontologies/TimeSeriesValueBankProperty/invoke_get_latest_value.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `TimeSeriesValueBankProperty.stream_values`

Stage: Stable. Required SDK arguments: `ontology`, `object_type`, `primary_key`, `property`.

Stream all of the points of a time series property (this includes geotime series references).

Read [exact contract](../../contracts/v2/ontologies/TimeSeriesValueBankProperty/stream_values.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/TimeSeriesValueBankProperty/invoke_stream_values.py): `python -B examples/rest/083/v2/ontologies/TimeSeriesValueBankProperty/invoke_stream_values.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

## Worked example

Read the latest approved sensor value, record its timestamp and integration context, then consume a bounded stream for comparison. Do not equate one latest value with a complete history.

```python
api = client.ontologies.TimeSeriesValueBankProperty
latest = api.get_latest_value(
    ontology="operations", object_type="Sensor", primary_key="S-1",
    property_name="temperature", branch="master"
)
if latest is not None:
    print(latest.time, latest.value)

total_bytes = 0
with api.with_streaming_response.stream_values(
    ontology="operations", object_type="Sensor", primary_key="S-1",
    property="temperature", branch="master", request_timeout=30
) as response:
    for chunk in response.iter_bytes():
        total_bytes += len(chunk)
        if total_bytes > 1_000_000:
            raise ValueError("time-series byte budget exceeded")
```

`get_latest_value` uses `property_name`; `stream_values` uses `property` in
SDK 1.101.0. Both calls must target the same actual property and branch.
`latest` may be `None`; when history and live integrations both exist, the
latest-value endpoint gives live data precedence. A bounded stream and a
latest-value read have different completeness and recency meaning.

The linked operation fixtures show actual SDK method invocation, serialized request and decoded response/error using a local mock transport. Their synthetic values are test data. Replace them with authorized identifiers and typed payloads from each linked contract; verify the live result under the intended identity before asserting a platform effect.

## Expected result and checks

Record exact operation ID, API version, release stage, branch, requested IDs, returned IDs, page/snapshot token, response mode and decoded result. For effectful calls, inspect validation/commit state and fresh target data; a successful HTTP response alone may not establish the business result. For lists, finish pagination before claiming completeness.

## Failures and recovery

On a missing or filtered result, verify Ontology/type/API names, branch and effective caller permissions. On schema rejection, compare payload fields, requiredness, aliases and discriminator values with the linked models. On a timeout after an effectful call, reconcile target or transaction state before retrying. Bound pages, streamed bytes and time windows; close streaming/raw responses according to [client lifetimes](../../client-behavior.md). Missing beta enablement is a prerequisite to resolve with the enrollment owner.
