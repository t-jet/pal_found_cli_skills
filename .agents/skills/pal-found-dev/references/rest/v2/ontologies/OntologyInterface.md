# OntologyInterface operations

[REST development](../../../rest-api.md) | [Ontology service](index.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

Interfaces present a shared type contract across implementing object types. Interface object lists and aggregations depend on each implementing type's permissions and supported beta behavior.

## Prerequisites

Use the frozen Foundry Python SDK 1.101.0 and an authorized Ontology, branch, resource identifier, acting identity and exact type/parameter names from the enrollment. Prepare the linked local models before a live request. Synthetic examples run offline with the prepared SDK and mock transport; real reads or writes require enrollment access, resource permissions and any listed beta enablement. An administrator or resource owner supplies missing grants and capability access.

## Procedure and operation choices

Select the operation below, read its exact request/response/error model, then adapt the linked SDK fixture with authorized resource values. The fixture uses synthetic identifiers and checks serialized transport; it does not assert tenant behavior. Record branch, version, page/snapshot context, response and named errors for the actual call.

### `OntologyInterface.aggregate`

Stage: Private Beta. Required SDK arguments: `ontology`, `interface_type`, `aggregation`, `group_by`.

This endpoint will be removed once TS OSDK is updated to use `objectSets/aggregate` with interface object sets. Perform functions on object fields in the specified ontology and of the specified interface type. Any properties specified in the query must be shared property type API names defined on the interface.

Read [exact contract](../../contracts/v2/ontologies/OntologyInterface/aggregate.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/OntologyInterface/invoke_aggregate.py): `python -B examples/rest/079/v2/ontologies/OntologyInterface/invoke_aggregate.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `OntologyInterface.get`

Stage: Public Beta. Required SDK arguments: `ontology`, `interface_type`.

Gets a specific interface type with the given API name.

Read [exact contract](../../contracts/v2/ontologies/OntologyInterface/get.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/OntologyInterface/invoke_get.py): `python -B examples/rest/079/v2/ontologies/OntologyInterface/invoke_get.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `OntologyInterface.get_outgoing_interface_link_type`

Stage: Private Beta. Required SDK arguments: `ontology`, `interface_type`, `interface_link_type`.

Get an outgoing interface link type for an interface type.

Read [exact contract](../../contracts/v2/ontologies/OntologyInterface/get_outgoing_interface_link_type.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/OntologyInterface/invoke_get_outgoing_interface_link_type.py): `python -B examples/rest/079/v2/ontologies/OntologyInterface/invoke_get_outgoing_interface_link_type.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `OntologyInterface.list`

Stage: Public Beta. Required SDK arguments: `ontology`.

Lists the interface types for the given Ontology. Each page may be smaller than the requested page size. However, it is guaranteed that if there are more results available, at least one result will be present in the response.

Read [exact contract](../../contracts/v2/ontologies/OntologyInterface/list.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/OntologyInterface/invoke_list.py): `python -B examples/rest/079/v2/ontologies/OntologyInterface/invoke_list.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `OntologyInterface.list_interface_linked_objects`

Stage: Private Beta. Required SDK arguments: `ontology`, `interface_type`, `object_type`, `primary_key`, `interface_link_type`.

Lists the linked objects for a specific object and the given interface link type. Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or repeated objects in the response pages. For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects. See the linked contract for further limits and query details.

Read [exact contract](../../contracts/v2/ontologies/OntologyInterface/list_interface_linked_objects.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/OntologyInterface/invoke_list_interface_linked_objects.py): `python -B examples/rest/079/v2/ontologies/OntologyInterface/invoke_list_interface_linked_objects.py` from skill root. Named failure in source text: `ObjectsExceededLimit`.

### `OntologyInterface.list_objects_for_interface`

Stage: Private Beta. Required SDK arguments: `ontology`, `interface_type`.

Lists the objects for the given Ontology and interface type. Note that this endpoint does not guarantee consistency, unless you use the snapshot flag specified below. Changes to the data could result in missing or repeated objects in the response pages. For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects. See the linked contract for further limits and query details.

Read [exact contract](../../contracts/v2/ontologies/OntologyInterface/list_objects_for_interface.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/OntologyInterface/invoke_list_objects_for_interface.py): `python -B examples/rest/079/v2/ontologies/OntologyInterface/invoke_list_objects_for_interface.py` from skill root. Named failure in source text: `ObjectsExceededLimit`.

### `OntologyInterface.list_outgoing_interface_link_types`

Stage: Private Beta. Required SDK arguments: `ontology`, `interface_type`.

List the outgoing interface link types for an interface type.

Read [exact contract](../../contracts/v2/ontologies/OntologyInterface/list_outgoing_interface_link_types.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/OntologyInterface/invoke_list_outgoing_interface_link_types.py): `python -B examples/rest/079/v2/ontologies/OntologyInterface/invoke_list_outgoing_interface_link_types.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `OntologyInterface.search`

Stage: Private Beta. Required SDK arguments: `ontology`, `interface_type`, `augmented_interface_property_types`, `augmented_properties`, `augmented_shared_property_types`, `other_interface_types`, `selected_interface_property_types`, `selected_object_types`, `selected_shared_property_types`.

This endpoint will be removed once TS OSDK is updated to use `objectSets/loadObjects` with interface object sets. Search for objects in the specified ontology and interface type. Any properties specified in the "where" or "orderBy" parameters must be shared property type API names defined on the interface. The following search queries are supported:

Read [exact contract](../../contracts/v2/ontologies/OntologyInterface/search.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/079/v2/ontologies/OntologyInterface/invoke_search.py): `python -B examples/rest/079/v2/ontologies/OntologyInterface/invoke_search.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

## Worked example

Discover an approved `Trackable` interface, inspect its outgoing interface links, then list bounded visible implementations. Compare returned type and primary key per result. Preserve snapshot and cursor choices when reading changing data.

The get/list, object-list, linked-object, search and aggregate fixtures share a [declared synthetic schema](../../../../examples/rest/079/synthetic_schema.py). `Trackable` has no parent interface and requires shared properties `assetId` (string), `name` (string), and `observedAt` (timestamp). `Asset` implements each through a local property of the same name. Its `relatedAssets` link implements the interface's `peers` link to other `Trackable` objects. The linked-object fixture reads peers of `Asset/A-1` and returns `Asset/A-2`; object-list and search return `Asset/A-1`. Results carry `__apiName`, `__primaryKey`, and selected business properties so callers can distinguish implementations and object identities.

The aggregate fixture requests approximate distinct `assetId` values, names the metric `distinctAssets`, and groups `observedAt` into one-day intervals. Each aggregation or grouping must supply exactly one of `field` and `propertyIdentifier`. Duration grouping requires a date or timestamp property; `YEARS`, `QUARTERS`, `MONTHS`, and `WEEKS` require `value=1`. Property names must be shared properties on the requested interface. The synthetic response names the requested metric and its timestamp group. These checks illustrate schema consistency; they do not establish live aggregation accuracy, enrollment availability, or access to every implementation.

Search supplies the required selection and augmentation containers explicitly. This fixture selects `Asset` and the three declared shared properties, with empty augmentation maps and empty additional-interface selections. Adapt those selections together with the interface schema; arbitrary names can decode locally even when an enrollment would reject them.

The linked operation fixtures show actual SDK method invocation, serialized request and decoded response/error using a local mock transport. Their synthetic values are test data. Replace them with authorized identifiers and typed payloads from each linked contract; verify the live result under the intended identity before asserting a platform effect.

## Expected result and checks

Record exact operation ID, API version, release stage, branch, requested IDs, returned IDs, page/snapshot token, response mode and decoded result. For effectful calls, inspect validation/commit state and fresh target data; a successful HTTP response alone may not establish the business result. For lists, finish pagination before claiming completeness.

## Failures and recovery

On a missing or filtered result, verify Ontology/type/API names, branch and effective caller permissions. On schema rejection, compare payload fields, requiredness, aliases and discriminator values with the linked models. On a timeout after an effectful call, reconcile target or transaction state before retrying. Bound pages, streamed bytes and time windows; close streaming/raw responses according to [client lifetimes](../../client-behavior.md). Missing beta enablement is a prerequisite to resolve with the enrollment owner.
