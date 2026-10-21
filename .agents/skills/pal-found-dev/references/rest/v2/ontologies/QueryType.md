# QueryType operations

[REST development](../../../rest-api.md) | [Ontology service](index.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

Query type metadata defines the callable query name and parameter/result contract. It is distinct from executing the query and from reading its underlying objects.

## Prerequisites

Use the frozen Foundry Python SDK 1.101.0 and an authorized Ontology, branch, resource identifier, acting identity and exact type/parameter names from the enrollment. Prepare the linked local models before a live request. Synthetic examples run offline with the prepared SDK and mock transport; real reads or writes require enrollment access, resource permissions and any listed beta enablement. An administrator or resource owner supplies missing grants and capability access.

## Procedure and operation choices

Select the operation below, read its exact request/response/error model, then adapt the linked SDK fixture with authorized resource values. The fixture uses synthetic identifiers and checks serialized transport; it does not assert tenant behavior. Record branch, version, page/snapshot context, response and named errors for the actual call.

### `QueryType.get`

Stage: Stable. Required SDK arguments: `ontology`, `query_api_name`.

Gets a specific query type with the given API name.

Read [exact contract](../../contracts/v2/ontologies/QueryType/get.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/QueryType/invoke_get.py): `python -B examples/rest/079/v2/ontologies/QueryType/invoke_get.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `QueryType.get_by_rid_batch`

Stage: Private Beta. Required SDK arguments: `ontology`, `requests`.

Gets a list of query types by RID in bulk. Query types are filtered from the response if they don't exist or the requesting token lacks the required permissions. The maximum batch size for this endpoint is 100.

Read [exact contract](../../contracts/v2/ontologies/QueryType/get_by_rid_batch.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/QueryType/invoke_get_by_rid_batch.py): `python -B examples/rest/079/v2/ontologies/QueryType/invoke_get_by_rid_batch.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `QueryType.list`

Stage: Stable. Required SDK arguments: `ontology`.

Lists the query types for the given Ontology. Each page may be smaller than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response.

Read [exact contract](../../contracts/v2/ontologies/QueryType/list.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/QueryType/invoke_list.py): `python -B examples/rest/079/v2/ontologies/QueryType/invoke_list.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

## Worked example

Discover a permitted `ordersByStatus` query and compare its parameter types with the supplied filter. Treat a filtered bulk result as visibility-limited; execute only after checking caller identity and query access.

The linked operation fixtures show actual SDK method invocation, serialized request and decoded response/error using a local mock transport. Their synthetic values are test data. Replace them with authorized identifiers and typed payloads from each linked contract; verify the live result under the intended identity before asserting a platform effect.

## Expected result and checks

Record exact operation ID, API version, release stage, branch, requested IDs, returned IDs, page/snapshot token, response mode and decoded result. For effectful calls, inspect validation/commit state and fresh target data; a successful HTTP response alone may not establish the business result. For lists, finish pagination before claiming completeness.

## Failures and recovery

On a missing or filtered result, verify Ontology/type/API names, branch and effective caller permissions. On schema rejection, compare payload fields, requiredness, aliases and discriminator values with the linked models. On a timeout after an effectful call, reconcile target or transaction state before retrying. Bound pages, streamed bytes and time windows; close streaming/raw responses according to [client lifetimes](../../client-behavior.md). Missing beta enablement is a prerequisite to resolve with the enrollment owner.
