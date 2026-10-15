# OntologyTransaction operations

[REST development](../../../rest-api.md) | [Ontology service](index.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

A transaction groups ordered Ontology edits. Posting edits is an effectful step; timeout or uncertain response needs transaction-state reconciliation before replay.

## Prerequisites

Use the frozen Foundry Python SDK 1.101.0 and an authorized Ontology, branch, resource identifier, acting identity and exact type/parameter names from the enrollment. Prepare the linked local models before a live request. Synthetic examples run offline with the prepared SDK and mock transport; real reads or writes require enrollment access, resource permissions and any listed beta enablement. An administrator or resource owner supplies missing grants and capability access.

## Procedure and operation choices

Select the operation below, read its exact request/response/error model, then adapt the linked SDK fixture with authorized resource values. The fixture uses synthetic identifiers and checks serialized transport; it does not assert tenant behavior. Record branch, version, page/snapshot context, response and named errors for the actual call.

### `OntologyTransaction.post_edits`

Stage: Private Beta. Required SDK arguments: `ontology`, `transaction_id`, `edits`.

Applies a set of edits to a transaction in order.

Read [exact contract](../../contracts/v2/ontologies/OntologyTransaction/post_edits.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyTransaction/invoke_post_edits.py): `python -B examples/rest/081/v2/ontologies/OntologyTransaction/invoke_post_edits.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

## Worked example

Prepare two ordered edits for a known test object. Post them to the approved transaction, record its ID and result, then read resulting state through the authorized scenario or object route. On timeout, inspect transaction effects before posting again.

```python
from foundry_sdk.v2.ontologies.models import ModifyObjectEdit

transaction_id = approved_transaction_id  # obtained through authorized workflow
edits = [
    ModifyObjectEdit(object_type="Ticket", primary_key="T-1",
                     properties={"priority": "P0"}),
    ModifyObjectEdit(object_type="Ticket", primary_key="T-1",
                     properties={"reviewState": "Ready"}),
]
result = client.ontologies.OntologyTransaction.post_edits(
    ontology="dispatch", transaction_id=transaction_id,
    edits=edits, preview=True,
)
assert result is not None
```

`ModifyObjectEdit` sets the `modifyObject` discriminator and serializes SDK
fields to their wire aliases. Replace names and values with the actual type
contract. Edits are applied in list order. The response model has no fields
that prove a transaction was committed; inspect the transaction state and
target objects through the authorized workflow before reporting a durable
business change. Keep the same transaction ID when reconciling a timeout.

The linked operation fixtures show actual SDK method invocation, serialized request and decoded response/error using a local mock transport. Their synthetic values are test data. Replace them with authorized identifiers and typed payloads from each linked contract; verify the live result under the intended identity before asserting a platform effect.

## Expected result and checks

Record the Ontology identifier, transaction ID, ordered edit types, request outcome and any declared error. `post_edits` returns one response; it has no page token or list to exhaust. Verify transaction state and target objects through authorized reads before claiming a durable change. A successful HTTP response alone does not establish commit.

## Failures and recovery

On a missing or filtered result, verify Ontology/type/API names, branch and effective caller permissions. On schema rejection, compare payload fields, requiredness, aliases and discriminator values with the linked models. On a timeout after an effectful call, reconcile target or transaction state before retrying. Bound pages, streamed bytes and time windows; close streaming/raw responses according to [client lifetimes](../../client-behavior.md). Missing beta enablement is a prerequisite to resolve with the enrollment owner.
