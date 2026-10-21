# Object sets and query decisions

[Development guide](../../SKILL.md) | [Ontology overview](../ontology-compute.md)

## Concept and lifecycle

An Object Set describes selected objects and operations on that selection.
Filtering reduces membership; link traversal selects related objects; set
operations combine selections; aggregation computes summaries. Define the query
before materializing results. Empty results, inaccessible objects and a failed
request require different handling. A fetched page may represent only part of
the selection.

## Prerequisites

Prepare selected Ontology, exact generated type/property/link API names and
compatible TypeScript OSDK2.x client. The example uses the
[Order/Customer mapping](modeling.md): `totalCents` is numeric and `customer`
is a single link. Actual queries need authorized enrollment access and object
visibility. Local fixtures model query decisions, not server indexing or grants.

## Procedure

1. Start from the generated object type and explicit predicate. Verify property
   types and null handling; a string comparison is not a numeric range filter.
2. Select a bounded page, explicit order and pagination plan. Handle an empty
   page, a next-page token and query failures without showing false totals.
3. Traverse only named links declared by generated bindings. A single link
   uses `instance.$link.customer.fetchOne()`; a many link is an Object Set.
   Set traversal uses `pivotTo("linkApiName")` and can be filtered afterward.
4. Aggregate on the filtered set when the task needs a summary. OSDK2.x uses
   `$select` for metrics and `$groupBy` for groups. `$count` is a metric;
   property metrics use keys such as `"totalCents:sum"`. Do not mix 1.x syntax.
5. Bound page count, traversal breadth, loaded objects and query frequency.
   Inspect actual storage/version limits and query costs before scaling a
   fixture algorithm. Avoid collecting the entire enterprise set for a small UI.

## Worked example

For Orders `o1/c1/1200`, `o2/c1/500`, `o3/c2/2000`, the selection
`totalCents >=1000` contains `o1,o3`. Counts by customer are `c1:1,c2:1`.
Traversal from `o1` resolves Customer `c1` if the link exists and is visible.

```typescript
const highValue = client(Order).where({ totalCents: { $gte: 1000 } });
const page = await highValue.fetchPage({ $pageSize: 20 });
const counts = await highValue.aggregate({
  $select: { $count: "unordered" },
  $groupBy: { customerId: "exact" },
});
```

`client` and `Order` are actual prepared application bindings; their configuration
comes from the [local OSDK guide](../applications/osdk.md). The generated schema
must expose these exact fields. The [local query fixture](../../examples/ontology/query_fixture.mjs)
uses the same example predicate and complete expected membership/group result.
Run `node examples/ontology/query_fixture.mjs` from this skill root. It also
checks null exclusion and an empty selection. It does not execute this SDK code.

An interface selection uses the supported interface contract and generated
bindings, with optional-property handling from [interfaces](interfaces.md).
For raw REST operation/model inputs use [local SDK contracts](../rest-api.md).

## Expected result and checks

Verify membership and values, grouping shape and traversal endpoints. Record
whether all pages were consumed before claiming a complete result. Compare the
small fixture's exact IDs and counts with the actual query in its declared
permission context. No accessible rows is not proof that no objects exist.
Aggregation results in OSDK may differ from raw HTTP response shapes.

## Failures and recovery

For wrong results, inspect predicate types/nulls, branch/index freshness and
authorization. For missing links, check mapping and endpoint visibility. For
query limits or timeouts, narrow predicates, page results and bound traversal
before retrying. Reuse a known query/page token only within its valid context;
do not concatenate pages from different filters or changed security contexts.

Optional provenance: [OSDK2.x query contracts](https://www.palantir.com/docs/foundry/ontology-sdk/typescript-osdk),
[Object Set limitations](https://www.palantir.com/docs/foundry/ontologies/oss-limitations).
