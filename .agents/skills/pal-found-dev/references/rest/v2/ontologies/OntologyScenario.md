# OntologyScenario operations

[REST development](../../../rest-api.md) | [Ontology service](index.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

A scenario holds provisional Ontology edits against a base. Inspect edited entities and conflicts before treating scenario results as ready for delivery. These private beta APIs require enablement.

## Prerequisites

Use the frozen Foundry Python SDK 1.101.0 and an authorized Ontology, branch, resource identifier, acting identity and exact type/parameter names from the enrollment. Prepare the linked local models before a live request. Synthetic examples run offline with the prepared SDK and mock transport; real reads or writes require enrollment access, resource permissions and any listed beta enablement. An administrator or resource owner supplies missing grants and capability access.

## Procedure and operation choices

Select the operation below, read its exact request/response/error model, then adapt the linked SDK fixture with authorized resource values. The fixture uses synthetic identifiers and checks serialized transport; it does not assert tenant behavior. Record branch, version, page/snapshot context, response and named errors for the actual call.

The inspection fixtures share one illustrative schema: `Order` has `orderId` and `status`; `Worker` has `workerId` and `displayName`; `assignedWorker` is a many-to-many link from `Order` to `Worker`. `ORD-101` and `WRK-7` identify the same edited order and linked worker across responses. These names show how request types, returned object locators and link results fit together. Replace the schema with the enrolled Ontology's API names before a live call.

### `OntologyScenario.create_scenario`

Stage: Private Beta. Required SDK arguments: `ontology`.

Creates an ontology scenario.

Read [exact contract](../../contracts/v2/ontologies/OntologyScenario/create_scenario.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyScenario/invoke_create_scenario.py): `python -B examples/rest/081/v2/ontologies/OntologyScenario/invoke_create_scenario.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `OntologyScenario.list_scenario_conflicting_objects`

Stage: Private Beta. Required SDK arguments: `ontology`, `scenario_rid`, `object_type`.

Returns the list of objects with edits that conflict with edits to the scenario's base for a specific object type. A conflict occurs when an object has been edited both within the scenario and on the scenario's base after the scenario was created. Only objects that the user has permission to view are returned. Conflict detection takes into account changes that are not reflected in the user-visible object data. As a result, this endpoint may report false positives. An object may be returned as conflicting even if its data has not actually changed on the scenario's base. Each page may be smaller than the requested page size.

Read [exact contract](../../contracts/v2/ontologies/OntologyScenario/list_scenario_conflicting_objects.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyScenario/invoke_list_scenario_conflicting_objects.py): `python -B examples/rest/081/v2/ontologies/OntologyScenario/invoke_list_scenario_conflicting_objects.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `OntologyScenario.list_scenario_edited_entity_types`

Stage: Private Beta. Required SDK arguments: `ontology`, `scenario_rid`.

Returns the object types and link types that have been modified within a given scenario. The response contains the list of object type API names that have been modified, and the list of many-to-many link types that have been modified, grouped by their source object type. One-to-many link type edits are surfaced as object edits on the object type that owns the foreign key property.

Read [exact contract](../../contracts/v2/ontologies/OntologyScenario/list_scenario_edited_entity_types.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyScenario/invoke_list_scenario_edited_entity_types.py): `python -B examples/rest/081/v2/ontologies/OntologyScenario/invoke_list_scenario_edited_entity_types.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `OntologyScenario.list_scenario_edited_link_types`

Stage: Private Beta. Required SDK arguments: `ontology`, `scenario_rid`, `object_type`.

Returns the list of outgoing links that have been modified within a given scenario for an object type. Note that only many-to-many link type are returned by this endpoint. One-to-many link type edits are surfaced as object edits on the object type that owns the foreign key property.

Read [exact contract](../../contracts/v2/ontologies/OntologyScenario/list_scenario_edited_link_types.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyScenario/invoke_list_scenario_edited_link_types.py): `python -B examples/rest/081/v2/ontologies/OntologyScenario/invoke_list_scenario_edited_link_types.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `OntologyScenario.list_scenario_edited_links`

Stage: Private Beta. Required SDK arguments: `ontology`, `scenario_rid`, `object_type`, `link_type`.

Returns the list of edited links within a given scenario for a specific object type and link type, grouped by source object. Only works for many-to-many link types. Only links where the user has permission to view both objects are returned. Each page may be smaller than the requested page size.

Read [exact contract](../../contracts/v2/ontologies/OntologyScenario/list_scenario_edited_links.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyScenario/invoke_list_scenario_edited_links.py): `python -B examples/rest/081/v2/ontologies/OntologyScenario/invoke_list_scenario_edited_links.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `OntologyScenario.list_scenario_edited_object_types`

Stage: Private Beta. Required SDK arguments: `ontology`, `scenario_rid`.

Returns the list of object type API names that have been modified within a given scenario.

Read [exact contract](../../contracts/v2/ontologies/OntologyScenario/list_scenario_edited_object_types.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyScenario/invoke_list_scenario_edited_object_types.py): `python -B examples/rest/081/v2/ontologies/OntologyScenario/invoke_list_scenario_edited_object_types.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `OntologyScenario.list_scenario_edited_objects`

Stage: Private Beta. Required SDK arguments: `ontology`, `scenario_rid`, `object_type`.

Returns the list of objects that have been edited within a given scenario for a specific object type. Only objects that the user has permission to view are returned. Each page may be smaller than the requested page size.

Read [exact contract](../../contracts/v2/ontologies/OntologyScenario/list_scenario_edited_objects.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyScenario/invoke_list_scenario_edited_objects.py): `python -B examples/rest/081/v2/ontologies/OntologyScenario/invoke_list_scenario_edited_objects.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

## Worked example

Create an authorized test scenario, inspect edited `Order` objects and links, and list conflicts after the base changes. Resolve each conflicting object through the owning workflow before using scenario output as a proposed change.

```python
from itertools import islice

ontology = "dispatch"  # authorized Ontology identifier
api = client.ontologies.OntologyScenario
created = api.create_scenario(ontology=ontology, preview=True)
scenario_rid = created.scenario_rid

edited = list(islice(api.list_scenario_edited_objects(
    ontology=ontology,
    scenario_rid=scenario_rid,
    object_type="Order",
    page_size=20,
    preview=True,
), 20))
conflicts = list(islice(api.list_scenario_conflicting_objects(
    ontology=ontology,
    scenario_rid=scenario_rid,
    object_type="Order",
    page_size=20,
    preview=True,
), 20))
print(scenario_rid, len(edited), len(conflicts))
```

The returned `scenario_rid` must be propagated to every inspection operation;
it is not an object type or branch name. This code caps each iterator at 20
items and cannot claim a complete inventory. Add a time budget for live calls.
A conflict result can be a false positive because detection
also considers changes invisible in current object data. Compare the object and
its base history before resolving it. Results contain only objects visible to
the caller; an empty list does not prove no scenario edit exists.

The linked operation fixtures show actual SDK method invocation, serialized request and decoded response/error using a local mock transport. Their synthetic values are test data. Replace them with authorized identifiers and typed payloads from each linked contract; verify the live result under the intended identity before asserting a platform effect.

## Expected result and checks

Record exact operation ID, API version, release stage, branch, requested IDs, returned IDs, page/snapshot token, response mode and decoded result. For effectful calls, inspect validation/commit state and fresh target data; a successful HTTP response alone may not establish the business result. For lists, finish pagination before claiming completeness.

## Failures and recovery

On a missing or filtered result, verify Ontology/type/API names, branch and effective caller permissions. On schema rejection, compare payload fields, requiredness, aliases and discriminator values with the linked models. On a timeout after an effectful call, reconcile target or transaction state before retrying. Bound pages, streamed bytes and time windows; close streaming/raw responses according to [client lifetimes](../../client-behavior.md). Missing beta enablement is a prerequisite to resolve with the enrollment owner.
