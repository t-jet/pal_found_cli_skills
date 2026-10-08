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

Get a specific linked object that originates from another object. If there is no link between the two objects, `LinkedObjectNotFound` is thrown.

Read [exact contract](../../contracts/v2/ontologies/LinkedObject/get_linked_object.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/LinkedObject/invoke_get_linked_object.py): `python -B examples/rest/081/v2/ontologies/LinkedObject/invoke_get_linked_object.py` from skill root. Named failure in source text: `LinkedObjectNotFound`.

### `LinkedObject.list_linked_objects`

Stage: Stable. Required SDK arguments: `ontology`, `object_type`, `primary_key`, `link_type`.

Lists the linked objects for a specific object and the given link type. Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or repeated objects in the response pages. For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects. Each page may be smaller or larger than the requested page size. See the linked contract for further limits and query details.

Read [exact contract](../../contracts/v2/ontologies/LinkedObject/list_linked_objects.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/LinkedObject/invoke_list_linked_objects.py): `python -B examples/rest/081/v2/ontologies/LinkedObject/invoke_list_linked_objects.py` from skill root. Named failure in source text: `ObjectsExceededLimit`.

## Worked example

From an authorized `Order` key, list linked `Customer` objects with a finite page plan. Use get when one target key is known; handle `LinkedObjectNotFound` as a missing relationship or visibility condition.

The linked operation fixtures show actual SDK method invocation, serialized request and decoded response/error using a local mock transport. Their synthetic values are test data. Replace them with authorized identifiers and typed payloads from each linked contract; verify the live result under the intended identity before asserting a platform effect.

## Expected result and checks

Record exact operation ID, API version, release stage, branch, requested IDs, returned IDs, page/snapshot token, response mode and decoded result. For effectful calls, inspect validation/commit state and fresh target data; a successful HTTP response alone may not establish the business result. For lists, finish pagination before claiming completeness.

## Failures and recovery

On a missing or filtered result, verify Ontology/type/API names, branch and effective caller permissions. On schema rejection, compare payload fields, requiredness, aliases and discriminator values with the linked models. On a timeout after an effectful call, reconcile target or transaction state before retrying. Bound pages, streamed bytes and time windows; close streaming/raw responses according to [client lifetimes](../../client-behavior.md). Missing beta enablement is a prerequisite to resolve with the enrollment owner.
