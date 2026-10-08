# ActionType operations

[REST development](../../../rest-api.md) | [Ontology service](index.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

Action type metadata describes the callable Action API name, parameters and availability. Read it before constructing an apply request; discovery grants no permission to submit an Action.

## Prerequisites

Use the frozen Foundry Python SDK 1.101.0 and an authorized Ontology, branch, resource identifier, acting identity and exact type/parameter names from the enrollment. Prepare the linked local models before a live request. Synthetic examples run offline with the prepared SDK and mock transport; real reads or writes require enrollment access, resource permissions and any listed beta enablement. An administrator or resource owner supplies missing grants and capability access.

## Procedure and operation choices

Select the operation below, read its exact request/response/error model, then adapt the linked SDK fixture with authorized resource values. The fixture uses synthetic identifiers and checks serialized transport; it does not assert tenant behavior. Record branch, version, page/snapshot context, response and named errors for the actual call.

### `ActionType.get`

Stage: Stable. Required SDK arguments: `ontology`, `action_type`.

Gets a specific action type with the given API name.

Read [exact contract](../../contracts/v2/ontologies/ActionType/get.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/ActionType/invoke_get.py): `python -B examples/rest/079/v2/ontologies/ActionType/invoke_get.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `ActionType.get_by_rid`

Stage: Stable. Required SDK arguments: `ontology`, `action_type_rid`.

Gets a specific action type with the given RID.

Read [exact contract](../../contracts/v2/ontologies/ActionType/get_by_rid.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/ActionType/invoke_get_by_rid.py): `python -B examples/rest/079/v2/ontologies/ActionType/invoke_get_by_rid.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `ActionType.get_by_rid_batch`

Stage: Public Beta. Required SDK arguments: `ontology`, `requests`.

Gets a list of action types by RID in bulk. Action types are filtered from the response if they don't exist or the requesting token lacks the required permissions. The maximum batch size for this endpoint is 100.

Read [exact contract](../../contracts/v2/ontologies/ActionType/get_by_rid_batch.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/ActionType/invoke_get_by_rid_batch.py): `python -B examples/rest/079/v2/ontologies/ActionType/invoke_get_by_rid_batch.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `ActionType.list`

Stage: Stable. Required SDK arguments: `ontology`.

Lists the action types for the given Ontology. Each page may be smaller than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response.

Read [exact contract](../../contracts/v2/ontologies/ActionType/list.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/ActionType/invoke_list.py): `python -B examples/rest/079/v2/ontologies/ActionType/invoke_list.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `ActionType.search`

Stage: Private Beta. Required SDK arguments: `ontology`.

Search for action types in the given Ontology that match the provided filters. Results are returned by relevance of the match unless an explicit `orderBy` is provided. Each page may be smaller than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response. Search results are eventually consistent with the latest Ontology version and may lag slightly behind the last Ontology modification.

Read [exact contract](../../contracts/v2/ontologies/ActionType/search.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/ActionType/invoke_search.py): `python -B examples/rest/079/v2/ontologies/ActionType/invoke_search.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

## Worked example

Discover an approved `changePriority` Action in the selected Ontology. Resolve its parameter identifiers and types, then test an allowed and a denied identity before any submission. A missing result in a bulk response can reflect filtering, so compare requested and returned RIDs.

```python
# `client` comes from the local REST authentication guide. Replace these
# illustrative API names with values returned by the authorized Ontology.
ontology = "dispatch"
action_type = client.ontologies.Ontology.ActionType.get(
    ontology=ontology, action_type="changePriority", branch="master"
)
assert action_type.api_name == "changePriority"
assert {"ticket", "priority"} <= set(action_type.parameters)
for parameter_id in ("ticket", "priority"):
    print(parameter_id, action_type.parameters[parameter_id].data_type)
```

The `data_type` and parameter IDs must match the actual Action definition before
constructing `Action.apply(parameters=...)`. A denied lookup or missing parameter
stops submission. The response model is [ActionTypeV2](../../models/v2/ontologies/models/ActionTypeV2.md),
and [Action application](Action.md) covers its separate permission and validation result.

The linked operation fixtures show actual SDK method invocation, serialized request and decoded response/error using a local mock transport. Their synthetic values are test data. Replace them with authorized identifiers and typed payloads from each linked contract; verify the live result under the intended identity before asserting a platform effect.

## Expected result and checks

Record exact operation ID, API version, release stage, branch, requested IDs, returned IDs, page/snapshot token, response mode and decoded result. For effectful calls, inspect validation/commit state and fresh target data; a successful HTTP response alone may not establish the business result. For lists, finish pagination before claiming completeness.

## Failures and recovery

On a missing or filtered result, verify Ontology/type/API names, branch and effective caller permissions. On schema rejection, compare payload fields, requiredness, aliases and discriminator values with the linked models. On a timeout after an effectful call, reconcile target or transaction state before retrying. Bound pages, streamed bytes and time windows; close streaming/raw responses according to [client lifetimes](../../client-behavior.md). Missing beta enablement is a prerequisite to resolve with the enrollment owner.
