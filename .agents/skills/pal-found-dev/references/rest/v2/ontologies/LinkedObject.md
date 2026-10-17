# LinkedObject operations

[REST development](../../../rest-api.md) | [Ontology service](index.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

Link traversal starts from a known source object and outgoing link type. A link definition and an actual visible linked object are different; pagination may observe changing data.

## Prerequisites

Use the frozen Foundry Python SDK 1.101.0 and an authorized Ontology, branch, resource identifier, acting identity and exact type/parameter names from the enrollment. Prepare the linked local models before a live request. Synthetic examples run offline with the prepared SDK and mock transport; real reads or writes require enrollment access, resource permissions and any listed beta enablement. An administrator or resource owner supplies missing grants and capability access.

## Procedure and operation choices

Select the operation below, read its exact request/response/error model, then adapt the linked SDK fixture with authorized resource values. The fixture uses synthetic identifiers and checks serialized transport; it does not assert tenant behavior. Record branch, version, page/snapshot context, response and named errors for the actual call.

### `LinkedObject.get_linked_object`

Stage: Stable. Required SDK arguments: `ontology`, `object_type`, `primary_key`, `link_type`, `linked_object_primary_key`.

Get one target from a source object's outgoing link. The [Palantir get example](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/linked-objects/get-linked-object) uses object type API name `employee`, source key `50030`, link `directReport`, and target key `80060`. The fixture checks a matching target object. Handle `LinkedObjectNotFound` through the SDK's `NotFoundError`; the wire error can also mean the token cannot access the target.

Read [exact contract](../../contracts/v2/ontologies/LinkedObject/get_linked_object.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/LinkedObject/invoke_get_linked_object.py): `python -B examples/rest/081/v2/ontologies/LinkedObject/invoke_get_linked_object.py` from skill root. Named failure in source text: `LinkedObjectNotFound`.

### `LinkedObject.list_linked_objects`

Stage: Stable. Required SDK arguments: `ontology`, `object_type`, `primary_key`, `link_type`.

List targets for an outgoing link. The [Palantir list example](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/linked-objects/list-linked-objects) shows `employee` key `50030` with `directReport` targets. Follow `nextPageToken` until absent. Pages can change during traversal; use `snapshot=True` when consistency matters. Object Storage V1 limits results to 10,000; `ObjectsExceededLimit` arrives as SDK `BadRequestError` with wire name `ObjectsExceededLimit` and code `INVALID_ARGUMENT`. Object Storage V2 has no such object count limit.

Read [exact contract](../../contracts/v2/ontologies/LinkedObject/list_linked_objects.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/LinkedObject/invoke_list_linked_objects.py): `python -B examples/rest/081/v2/ontologies/LinkedObject/invoke_list_linked_objects.py` from skill root. Named failure in source text: `ObjectsExceededLimit`.

## Worked example

From an authorized source `Employee` key, list `directReport` targets with a bounded page size. Use get when the target key is known. Compare returned `__primaryKey` and `__apiName` with the requested target.

The linked operation fixtures show actual SDK method invocation, serialized request and decoded response/error using a local mock transport. Their synthetic values are test data. Replace them with authorized identifiers and typed payloads from each linked contract; verify the live result under the intended identity before asserting a platform effect.

## Expected result and checks

Record exact operation ID, API version, release stage, branch, requested IDs, returned IDs, page/snapshot token, response mode and decoded result. For effectful calls, inspect validation/commit state and fresh target data; a successful HTTP response alone may not establish the business result. For lists, finish pagination before claiming completeness.

## Failures and recovery

On a missing or filtered result, verify Ontology/type/API names, branch and effective caller permissions. On schema rejection, compare payload fields, requiredness, aliases and discriminator values with the linked models. On a timeout after an effectful call, reconcile target or transaction state before retrying. Bound pages, streamed bytes and time windows; close streaming/raw responses according to [client lifetimes](../../client-behavior.md). Missing beta enablement is a prerequisite to resolve with the enrollment owner.
