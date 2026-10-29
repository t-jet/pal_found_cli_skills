# OntologyObject operations

[REST development](../../../rest-api.md) | [Ontology service](index.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

Object reads use object type and primary-key values from the selected Ontology. A page or aggregate can be filtered by instance permissions; empty output is not proof of an empty backing dataset.

## Prerequisites

Use the frozen Foundry Python SDK 1.101.0 and an authorized Ontology, branch, resource identifier, acting identity and exact type/parameter names from the enrollment. Prepare the linked local models before a live request. Synthetic examples run offline with the prepared SDK and mock transport; real reads or writes require enrollment access, resource permissions and any listed beta enablement. An administrator or resource owner supplies missing grants and capability access.

## Procedure and operation choices

Select the operation below, read its exact request/response/error model, then adapt the linked SDK fixture with authorized resource values. The fixture uses synthetic identifiers and checks serialized transport; it does not assert tenant behavior. Record branch, version, page/snapshot context, response and named errors for the actual call.

### `OntologyObject.aggregate`

Stage: Stable. Required SDK arguments: `ontology`, `object_type`, `aggregation`, `group_by`.

Aggregate object fields. The [Palantir aggregate example](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-objects/aggregate-objects) finds `min_tenure` and groups by `city`; the fixture also filters by `name`. Check each returned metric against its group, plus `accuracy`. `AggregationGroupCountExceededLimit` arrives as SDK `BadRequestError` with wire code `INVALID_ARGUMENT`; narrow the filter or reduce group count before retrying.

Read [exact contract](../../contracts/v2/ontologies/OntologyObject/aggregate.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyObject/invoke_aggregate.py): `python -B examples/rest/081/v2/ontologies/OntologyObject/invoke_aggregate.py` from skill root. Named failure from [Palantir's error table](https://www.palantir.com/docs/foundry/api/general/overview/errors): `AggregationGroupCountExceededLimit`.

### `OntologyObject.count`

Stage: Private Beta. Required SDK arguments: `ontology`, `object_type`.

Returns a count of the objects of the given object type.
The fixture opts into preview and checks the decoded `count` for a concrete
`Asset` selection. Treat a missing count as unknown, not zero.

Read [exact contract](../../contracts/v2/ontologies/OntologyObject/count.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyObject/invoke_count.py): `python -B examples/rest/081/v2/ontologies/OntologyObject/invoke_count.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `OntologyObject.get`

Stage: Stable. Required SDK arguments: `ontology`, `object_type`, `primary_key`.

Get a known object. The [Palantir get example](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-objects/get-object) uses object type API name `employee` and key `50030`; the fixture checks its returned `__primaryKey` and `__apiName`. `ObjectNotFound` arrives as SDK `NotFoundError` and may indicate missing access as well as a missing object.

Read [exact contract](../../contracts/v2/ontologies/OntologyObject/get.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyObject/invoke_get.py): `python -B examples/rest/081/v2/ontologies/OntologyObject/invoke_get.py` from skill root. Named failure from [Palantir's error table](https://www.palantir.com/docs/foundry/api/general/overview/errors): `ObjectNotFound`.

### `OntologyObject.list`

Stage: Stable. Required SDK arguments: `ontology`, `object_type`.

List objects for one type. The [Palantir list example](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-objects/list-objects) shows `Employee` records and a `nextPageToken`. Continue while that token exists; page size alone does not signal completion. Use `snapshot=True` when a stable traversal matters. Object Storage V1 limits results to 10,000 and can return `ObjectsExceededLimit` as SDK `BadRequestError`; Object Storage V2 has no such object count limit.

Read [exact contract](../../contracts/v2/ontologies/OntologyObject/list.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyObject/invoke_list.py): `python -B examples/rest/081/v2/ontologies/OntologyObject/invoke_list.py` from skill root. Named failure in source text: `ObjectsExceededLimit`.

### `OntologyObject.search`

Stage: Stable. Required SDK arguments: `ontology`, `object_type`, `select`.

Search one object type with a `where` query and explicit selected properties. The [Palantir search example](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-objects/search-objects) filters `Employee` by `age == 21`. Compare returned property values and `totalCount`; continue via `nextPageToken` when present. If a filter property is not searchable, `PropertiesNotSearchable` arrives as SDK `BadRequestError` with wire code `INVALID_ARGUMENT`.

Read [exact contract](../../contracts/v2/ontologies/OntologyObject/search.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/OntologyObject/invoke_search.py): `python -B examples/rest/081/v2/ontologies/OntologyObject/invoke_search.py` from skill root. Named failure from [Palantir's error table](https://www.palantir.com/docs/foundry/api/general/overview/errors): `PropertiesNotSearchable`.

## Worked example

With a configured `foundry_sdk.v2.FoundryClient` named `client`, replace these illustrative values with an authorized Ontology, object type, key and property API names. The list method normally yields an iterator; its raw wrapper exposes page tokens.

```python
objects = client.ontologies.OntologyObject
employee = objects.get(
    ontology="palantir", object_type="employee", primary_key="50030",
)
assert employee["__primaryKey"] == 50030
assert employee["__apiName"] == "Employee"

page_token = None
listed_keys = []
while True:
    raw = objects.with_raw_response.list(
        ontology="palantir", object_type="employee", page_size=100,
        page_token=page_token, snapshot=True,
    )
    try:
        page = raw.decode()
    finally:
        raw.close()
    listed_keys.extend(obj["__primaryKey"] for obj in page.data)
    page_token = page.next_page_token
    if page_token is None:
        break
assert 50030 in listed_keys

matches = objects.search(
    ontology="palantir", object_type="employee",
    select=["employeeId", "firstName", "lastName", "age"],
    where={"type": "eq", "field": "age", "value": 21},
)
assert all(obj["age"] == 21 for obj in matches.data)
summary = objects.aggregate(
    ontology="palantir", object_type="employee",
    aggregation=[{"type": "min", "field": "tenure", "name": "min_tenure"}],
    group_by=[{"type": "exact", "field": "city"}],
    where={"type": "eq", "field": "age", "value": 21},
)
assert summary.accuracy == "ACCURATE"
```

The search can also return `next_page_token`; page through it before treating results as complete. `OntologyObject.count` is Private Beta and counts the given type: `objects.count(ontology="palantir", object_type="employee", preview=True).count`. Confirm beta access before calling it. Local fixtures check returned object identities, the search filter, aggregate group and metric, count, and named errors where documented.

The linked operation fixtures show actual SDK method invocation, serialized request and decoded response/error using a local mock transport. Their synthetic values are test data. Replace them with authorized identifiers and typed payloads from each linked contract; verify the live result under the intended identity before asserting a platform effect.

## Expected result and checks

Record exact operation ID, API version, release stage, branch, requested IDs, returned IDs, page/snapshot token, response mode and decoded result. For effectful calls, inspect validation/commit state and fresh target data; a successful HTTP response alone may not establish the business result. For lists, finish pagination before claiming completeness.

## Failures and recovery

On a missing or filtered result, verify Ontology/type/API names, branch and effective caller permissions. On schema rejection, compare payload fields, requiredness, aliases and discriminator values with the linked models. On a timeout after an effectful call, reconcile target or transaction state before retrying. Bound pages, streamed bytes and time windows; close streaming/raw responses according to [client lifetimes](../../client-behavior.md). Missing beta enablement is a prerequisite to resolve with the enrollment owner.
