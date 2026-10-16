# OntologyObjectSet operations

[REST development](../../../rest-api.md) | [Ontology service](index.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

An Object Set is a definition of selected objects. Loading and aggregating evaluate that definition; a temporary set has a one-hour lifetime and is not a durable inventory.

## Prerequisites

Use the frozen Foundry Python SDK 1.101.0 and an authorized Ontology, branch, resource identifier, acting identity and exact type/parameter names from the enrollment. Prepare the linked local models before a live request. Synthetic examples run offline with the prepared SDK and mock transport; real reads or writes require enrollment access, resource permissions and any listed beta enablement. An administrator or resource owner supplies missing grants and capability access.
The beta examples pass the SDK's `preview=True` selector. The published
`create_temporary` and `load_objects_or_interfaces` endpoints require it.

## Procedure and operation choices

Select the operation below, read its exact request/response/error model, then adapt the linked SDK fixture with authorized resource values. The fixture uses synthetic identifiers and checks serialized transport; it does not assert tenant behavior. Record branch, version, page/snapshot context, response and named errors for the actual call.

### `OntologyObjectSet.aggregate`

Stage: Stable. Required SDK arguments: `ontology`, `aggregation`, `group_by`, `object_set`.

Aggregates the ontology objects present in the `ObjectSet` from the provided object set definition.

Read [exact contract](../../contracts/v2/ontologies/OntologyObjectSet/aggregate.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyObjectSet/invoke_aggregate.py): `python -B examples/rest/081/v2/ontologies/OntologyObjectSet/invoke_aggregate.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `OntologyObjectSet.create_temporary`

Stage: Public Beta. Required SDK arguments: `ontology`, `object_set`.

Creates a temporary `ObjectSet` from the given definition. This `ObjectSet` expires after one hour.
The published endpoint requires `preview=true`; pass `preview=True` to the SDK.
The fixture uses a base `Asset` set and checks the returned temporary RID.

Read [exact contract](../../contracts/v2/ontologies/OntologyObjectSet/create_temporary.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyObjectSet/invoke_create_temporary.py): `python -B examples/rest/081/v2/ontologies/OntologyObjectSet/invoke_create_temporary.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `OntologyObjectSet.get`

Stage: Private Beta. Required SDK arguments: `ontology`, `object_set_rid`.

Gets the definition of the `ObjectSet` with the given RID.

Read [exact contract](../../contracts/v2/ontologies/OntologyObjectSet/get.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyObjectSet/invoke_get.py): `python -B examples/rest/081/v2/ontologies/OntologyObjectSet/invoke_get.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `OntologyObjectSet.load`

Stage: Stable. Required SDK arguments: `ontology`, `object_set`, `select`.

Load the ontology objects present in the `ObjectSet` from the provided object set definition. For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects. Note that null value properties will not be returned. Vector properties will not be returned unless included in the `select` parameter.

Read [exact contract](../../contracts/v2/ontologies/OntologyObjectSet/load.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyObjectSet/invoke_load.py): `python -B examples/rest/081/v2/ontologies/OntologyObjectSet/invoke_load.py` from skill root. Named failure in source text: `ObjectsExceededLimit`.

### `OntologyObjectSet.load_links`

Stage: Private Beta. Required SDK arguments: `ontology`, `links`, `object_set`.

Loads the specified links from the defined object set. Links are defined as a link type API name and object locators for the source and target objects where only the `__primaryKey` and `__apiName` properties are loaded. Links are grouped by source object locator; however, the links for a given source object may be split over multiple entries with the same source object locator. Please keep these limitations in mind: - Links returned may be stale. For example, primary keys returned by this endpoint may not exist anymore. - This endpoint requests links for 1,000 objects at a time. See the linked contract for further limits and query details.

Read [exact contract](../../contracts/v2/ontologies/OntologyObjectSet/load_links.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyObjectSet/invoke_load_links.py): `python -B examples/rest/081/v2/ontologies/OntologyObjectSet/invoke_load_links.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `OntologyObjectSet.load_multiple_object_types`

Stage: Public Beta. Required SDK arguments: `ontology`, `object_set`, `select`.

Load the ontology objects present in the `ObjectSet` from the provided object set definition. The resulting objects may be scoped to an object type, in which all the selected properties on the object type are returned, or scoped to an interface, in which only the object type properties that implement the properties of any interfaces in its scope are returned. For objects that are scoped to an interface in the result, a mapping from interface to object implementation is returned in order to interpret the objects as the interfaces that they implement. See the linked contract for further limits and query details.

Read [exact contract](../../contracts/v2/ontologies/OntologyObjectSet/load_multiple_object_types.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyObjectSet/invoke_load_multiple_object_types.py): `python -B examples/rest/081/v2/ontologies/OntologyObjectSet/invoke_load_multiple_object_types.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `OntologyObjectSet.load_objects_or_interfaces`

Stage: Public Beta. Required SDK arguments: `ontology`, `object_set`, `select`.

Load the ontology objects present in the `ObjectSet` from the provided object set definition. If the requested object set contains interfaces and the object can be viewed as an interface, it will contain the properties defined by the interface. If not, it will contain the properties defined by its object type. This allows directly loading all objects of an interface where all objects are viewed as the interface, for example. Note that the result object set cannot contain a mix of objects with "interface" properties and "object type" properties. See the linked contract for further limits and query details.
The published endpoint requires `preview=true`; pass `preview=True` to the SDK.
The fixture loads a base `Asset` set and checks object identity, selected data, and total count.

Read [exact contract](../../contracts/v2/ontologies/OntologyObjectSet/load_objects_or_interfaces.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyObjectSet/invoke_load_objects_or_interfaces.py): `python -B examples/rest/081/v2/ontologies/OntologyObjectSet/invoke_load_objects_or_interfaces.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

## Worked example

Prepare a bounded `Order` Object Set definition, create a temporary handle when reuse is needed, then load a page and aggregate that same selection. Verify type scope and page completion before claiming a total.

```python
from foundry_sdk.v2.ontologies.models import ObjectSetBaseType, ObjectSetReferenceType

ontology = "dispatch"  # use the authorized Ontology identifier
selection = ObjectSetBaseType(object_type="Order")  # actual type API name
temporary = client.ontologies.OntologyObjectSet.create_temporary(
    ontology=ontology, object_set=selection, preview=True
)
assert temporary.object_set_rid

page = client.ontologies.OntologyObjectSet.load(
    ontology=ontology,
    object_set=ObjectSetReferenceType(reference=temporary.object_set_rid),
    select=["orderId", "status"],
    page_size=20,
    snapshot=True,
)
for order in page.data:
    print(order.get("orderId"), order.get("status"))
next_token = page.next_page_token
```

Use `next_token` as `page_token` with the same `ObjectSetReferenceType` and
branch until it is absent or the agreed page budget ends. The returned
temporary RID can be read through `get`; it expires after one hour. Do not
reuse it after expiry. The `ObjectSetBaseType` discriminator
and `LoadObjectSetResponseV2` fields are defined in the linked local models.
An Object Storage V1 result has a 10,000-object limit; do not claim complete
enumeration after `ObjectsExceededLimit`. Null-valued properties are omitted
from `load`, so missing `status` needs interpretation before business use.

The linked operation fixtures show actual SDK method invocation, serialized request and decoded response/error using a local mock transport. Their synthetic values are test data. Replace them with authorized identifiers and typed payloads from each linked contract; verify the live result under the intended identity before asserting a platform effect.

## Expected result and checks

Record exact operation ID, API version, release stage, branch, requested IDs, returned IDs, page/snapshot token, response mode and decoded result. For effectful calls, inspect validation/commit state and fresh target data; a successful HTTP response alone may not establish the business result. For lists, finish pagination before claiming completeness.

## Failures and recovery

On a missing or filtered result, verify Ontology/type/API names, branch and effective caller permissions. On schema rejection, compare payload fields, requiredness, aliases and discriminator values with the linked models. On a timeout after an effectful call, reconcile target or transaction state before retrying. Bound pages, streamed bytes and time windows; close streaming/raw responses according to [client lifetimes](../../client-behavior.md). Missing beta enablement is a prerequisite to resolve with the enrollment owner.
