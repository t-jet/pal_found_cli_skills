# GeotemporalSeriesProperty operations

[REST development](../../../rest-api.md) | [Ontology service](index.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

A geotemporal series reference loads time-bounded entries for one object's property. The result is an ordered, typed series, not an ordinary scalar object field.

## Prerequisites

Use the frozen Foundry Python SDK 1.101.0 and an authorized Ontology, branch, resource identifier, acting identity and exact type/parameter names from the enrollment. Prepare the linked local models before a live request. Synthetic examples run offline with the prepared SDK and mock transport; real reads or writes require enrollment access, resource permissions and any listed beta enablement. An administrator or resource owner supplies missing grants and capability access.

## Procedure and operation choices

Select the operation below, read its exact request/response/error model, then adapt the linked SDK fixture with authorized resource values. The fixture uses synthetic identifiers and checks serialized transport; it does not assert tenant behavior. Record branch, version, page/snapshot context, response and named errors for the actual call.

### `GeotemporalSeriesProperty.load_geotemporal_series_entries`

Stage: Private Beta. Required SDK arguments: `ontology`, `object_type`, `primary_key`, `property`, `additional_properties`, `range`.

Load the geotemporal series entries for a given object's geotemporal series reference property within the specified time range. Each entry in the response is a map of property names to values, following the same structure as `OntologyObjectV2`. Use the `additionalProperties` field in the request to control which properties are included in each entry depending on the underlying geotemporal integration. Results are paginated. Use the `nextPageToken` from the response to retrieve subsequent pages. Geotemporal series integrations with only "dataset archive" enabled are not supported.

Read [exact contract](../../contracts/v2/ontologies/GeotemporalSeriesProperty/load_geotemporal_series_entries.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/GeotemporalSeriesProperty/invoke_load_geotemporal_series_entries.py): `python -B examples/rest/083/v2/ontologies/GeotemporalSeriesProperty/invoke_load_geotemporal_series_entries.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

## Worked example

Resolve an accessible asset's series property, request a narrow timestamp interval, inspect returned entries and pagination/limits, and distinguish an empty time window from missing property access.

The linked operation fixtures show actual SDK method invocation, serialized request and decoded response/error using a local mock transport. Their synthetic values are test data. Replace them with authorized identifiers and typed payloads from each linked contract; verify the live result under the intended identity before asserting a platform effect.

## Expected result and checks

Record exact operation ID, API version, release stage, branch, requested IDs, returned IDs, page/snapshot token, response mode and decoded result. For effectful calls, inspect validation/commit state and fresh target data; a successful HTTP response alone may not establish the business result. For lists, finish pagination before claiming completeness.

## Failures and recovery

On a missing or filtered result, verify Ontology/type/API names, branch and effective caller permissions. On schema rejection, compare payload fields, requiredness, aliases and discriminator values with the linked models. On a timeout after an effectful call, reconcile target or transaction state before retrying. Bound pages, streamed bytes and time windows; close streaming/raw responses according to [client lifetimes](../../client-behavior.md). Missing beta enablement is a prerequisite to resolve with the enrollment owner.
