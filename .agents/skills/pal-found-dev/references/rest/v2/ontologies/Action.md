# Action operations

[REST development](../../../rest-api.md) | [Ontology service](index.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

Applying an Action validates typed parameters and may edit objects, links or side effects. HTTP 200 alone does not establish a successful Action: inspect validation and subsequent state.

## Prerequisites

Use the frozen Foundry Python SDK 1.101.0 and an authorized Ontology, branch, resource identifier, acting identity and exact type/parameter names from the enrollment. Prepare the linked local models before a live request. Synthetic examples run offline with the prepared SDK and mock transport; real reads or writes require enrollment access, resource permissions and any listed beta enablement. An administrator or resource owner supplies missing grants and capability access.

## Procedure and operation choices

Select the operation below, read its exact request/response/error model, then adapt the linked SDK fixture with authorized resource values. The fixture uses synthetic identifiers and checks serialized transport; it does not assert tenant behavior. Record branch, version, page/snapshot context, response and named errors for the actual call.

### `Action.apply`

Stage: Stable. Required SDK arguments: `ontology`, `action`, `parameters`.

Applies an action using the given parameters. Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible. Edits to objects or links in Object Storage V2 will be visible immediately after the action completes. Note that a 200 HTTP status code only indicates that the request was received and processed by the server. See the validation result in the response body to determine if the action was applied successfully. Note that parameter default values are not currently supported by this endpoint.

Read [exact contract](../../contracts/v2/ontologies/Action/apply.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/Action/invoke_apply.py): `python -B examples/rest/083/v2/ontologies/Action/invoke_apply.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `Action.apply_batch`

Stage: Stable. Required SDK arguments: `ontology`, `action`, `requests`.

Applies multiple actions (of the same Action Type) using the given parameters. Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible. Edits to objects or links in Object Storage V2 will be visible immediately after the action completes. Up to 20 actions may be applied in one call. Actions that only modify objects in Object Storage v2 and do not call Functions may receive a higher limit. Note that notifications are not currently supported by this endpoint.

Read [exact contract](../../contracts/v2/ontologies/Action/apply_batch.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/Action/invoke_apply_batch.py): `python -B examples/rest/083/v2/ontologies/Action/invoke_apply_batch.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `Action.apply_batch_with_overrides`

Stage: Private Beta. Required SDK arguments: `ontology`, `action`, `requests`.

Applies multiple actions (of the same Action Type) with per-item overrides for UniqueIdentifier and CurrentTime generated action parameters. Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible. Edits to objects or links in Object Storage V2 will be visible immediately after the action completes. Up to 20 actions may be applied in one call. Actions that only modify objects in Object Storage v2 and do not call Functions may receive a higher limit. Note that notifications are not currently supported by this endpoint.

Read [exact contract](../../contracts/v2/ontologies/Action/apply_batch_with_overrides.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/Action/invoke_apply_batch_with_overrides.py): `python -B examples/rest/083/v2/ontologies/Action/invoke_apply_batch_with_overrides.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `Action.apply_with_overrides`

Stage: Private Beta. Required SDK arguments: `ontology`, `action`, `overrides`, `request`.

Same as regular apply action operation, but allows specifying overrides for UniqueIdentifier and CurrentTime generated action parameters.

Read [exact contract](../../contracts/v2/ontologies/Action/apply_with_overrides.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/Action/invoke_apply_with_overrides.py): `python -B examples/rest/083/v2/ontologies/Action/invoke_apply_with_overrides.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

## Worked example

For `changePriority`, first verify Action type and caller permissions, then apply one test case with known target and priority. Read the response validation, reread the object, and verify each configured external side effect separately. Batch methods require items of the same Action type.

```python
ontology = "dispatch"  # authorized Ontology identifier
definition = client.ontologies.Ontology.ActionType.get(
    ontology=ontology, action_type="changePriority"
)
assert {"ticket", "priority"} <= set(definition.parameters)

result = client.ontologies.Action.apply(
    ontology=ontology,
    action="changePriority",
    parameters={"ticket": "T-1", "priority": "P0"},
)
if result.validation is None or result.validation.result != "VALID":
    raise RuntimeError("Action failed validation; inspect criteria and parameters")
current = client.ontologies.OntologyObject.get(
    ontology=ontology, object_type="Ticket", primary_key="T-1"
)
assert current.get("priority") == "P0"
```

`ActionTypeV2.parameters` and the target's object type come from the actual
Ontology, and the supplied values must satisfy that Action's declared types.
An HTTP 200 response can still contain `validation.result == "INVALID"`.
For Object Storage V1, a fresh read may lag the edit; use a bounded verification
window. Confirm notifications/webhooks separately, since an object edit does not
prove those side effects completed. On timeout, reconcile the target and any
correlated side-effect record before repeating the Action.

The linked operation fixtures show actual SDK method invocation, serialized request and decoded response/error using a local mock transport. Their synthetic values are test data. Replace them with authorized identifiers and typed payloads from each linked contract; verify the live result under the intended identity before asserting a platform effect.

## Expected result and checks

Record exact operation ID, API version, release stage, branch, requested IDs, returned IDs, page/snapshot token, response mode and decoded result. For effectful calls, inspect validation/commit state and fresh target data; a successful HTTP response alone may not establish the business result. For lists, finish pagination before claiming completeness.

## Failures and recovery

On a missing or filtered result, verify Ontology/type/API names, branch and effective caller permissions. On schema rejection, compare payload fields, requiredness, aliases and discriminator values with the linked models. On a timeout after an effectful call, reconcile target or transaction state before retrying. Bound pages, streamed bytes and time windows; close streaming/raw responses according to [client lifetimes](../../client-behavior.md). Missing beta enablement is a prerequisite to resolve with the enrollment owner.
