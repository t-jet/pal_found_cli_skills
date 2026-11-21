# v1 ontologies: OntologyObject

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Ontology objects are typed records addressed by a primary key. Queries, aggregation and
linked-object traversal operate on those records. Object listing is not snapshot-
consistent: changing data can produce omissions or repetitions across pages.

## Prepare the application

Use prepared SDK 1.101.0 and an authorized identity for the intended enrollment. Resolve
the resource identities and complete request models linked below before calling a
method. Offline fixtures use synthetic identities and an actual SDK HTTP transport; they
need prepared Python, SDK and httpx and contact no enrollment.

Verify the application grants, resource permissions and capability enablement in the
tenant. SDK source does not enumerate a universal role or scope for every operation;
operation-specific documented requirements below take precedence. Source does not
provide a universal idempotency guarantee. For uncertain writes, retain request identity
and reconcile through authorized reads before repeating.

## Operations and outcome checks

## Synthetic object schema

The examples use synthetic object type `Asset`, string primary key `assetId`, string
property `status`, and date property `inspectionDate` (`LocalDate` in v1 metadata).
Asset `A-1` has status `ready` and inspection date `2026-10-01`. ObjectType get/list
examples declare these properties. The outgoing `facility` link has cardinality ONE
and target type `Facility`, whose string primary key is `facilityId` and whose string
property is `name`. Linked reads return `F-1`, named `North depot`, with a different
RID from source asset `A-1`. These synthetic schemas establish fixture meaning only.

Read [ObjectType](ObjectType.md) metadata or an approved offline metadata snapshot
before authoring tenant code. Resolve the real API name, primary-key type,
property types and outgoing link definitions. Convert application inputs to
those exact types and check returned properties before making a decision. A
generic property map permits many shapes; only tenant metadata establishes the
application's intended schema.

### aggregate

Construct aggregations compatible with object property types and inspect the result
model. Preserve grouping and aggregation identities when using the result in application
decisions.

The example groups date field `properties.inspectionDate` by ISO 8601 duration `P1D`
and approximately counts distinct `properties.assetId` values as `distinctAssets`.
Its mock response chooses label `properties.inspectionDate`, string value
`2026-10-01` and numeric metric value `1.0`.
Duration grouping applies only to date types. FieldNameV1 requires
`properties.{propertyApiName}`; bare property names are unsuitable here. The SDK's
string aliases alone do not enforce these request constraints.

The response model defines `group` as `Dict[str, Any]`. Frozen source specifies
neither a response-label convention nor a representation for group values. The
mock label and ISO date string are illustrative choices. Exact fixture roundtrip
checks SDK serialization and decoding; it establishes no server grouping behavior.
Keep returned labels and values intact when inspecting a result:

```python
for bucket in decoded_result["data"]:
    for returned_label, returned_value in bucket["group"].items():
        print(returned_label, returned_value)
```

Before mapping a label to a requested field, confirm its meaning and value shape
from documentation or an approved response/schema for the intended enrollment.
Use the confirmed returned label and check its presence before indexing. If a
label is absent or its value fails the confirmed schema, retain the response and
request, stop the derived calculation, and resolve the mismatch before retrying
or changing the mapping. Request field syntax alone cannot establish that mapping.
Computing bucket boundaries also needs confirmed interval, calendar and timezone
semantics; `P1D` and this synthetic string do not establish them. This example
performs no boundary calculation and makes no live server guarantee.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/OntologyObject/aggregate.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/OntologyObject/aggregate.py):

```bash
python -B examples/rest/077/v1/ontologies/OntologyObject/aggregate.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

No named operation failures are declared by this frozen SDK method. Generic API,
authentication, transport and decoding failures remain possible; preserve the error
envelope and request identity rather than inventing a domain-specific exception.

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get

Read a typed object by its primary key in the intended ontology. Validate tenant-defined
property shape against ObjectType metadata before using the record.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/OntologyObject/get.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/OntologyObject/get.py):

```bash
python -B examples/rest/077/v1/ontologies/OntologyObject/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

No named operation failures are declared by this frozen SDK method. Generic API,
authentication, transport and decoding failures remain possible; preserve the error
envelope and request identity rather than inventing a domain-specific exception.

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_linked_object

Retrieve a particular target linked from the source object. LinkedObjectNotFound means
the specified link is absent; direct target existence is a different check.

Resolve `Asset.facility` metadata to target `Facility`, then use target primary key
`F-1`. Check returned `facilityId`, not source `assetId`; source and target keys belong
to different schemas. A target's direct existence does not establish this link.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/OntologyObject/get_linked_object.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/OntologyObject/get_linked_object.py):

```bash
python -B examples/rest/077/v1/ontologies/OntologyObject/get_linked_object.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

No named operation failures are declared by this frozen SDK method. Generic API,
authentication, transport and decoding failures remain possible; preserve the error
envelope and request identity rather than inventing a domain-specific exception.

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### list

Enumerate objects with source-compatible filters and bounded pages/items. Listing is not
consistent across data changes, so de-duplicate identities when appropriate and report
partial results explicitly.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/OntologyObject/list.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/OntologyObject/list.py):

```bash
python -B examples/rest/077/v1/ontologies/OntologyObject/list.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

No named operation failures are declared by this frozen SDK method. Generic API,
authentication, transport and decoding failures remain possible; preserve the error
envelope and request identity rather than inventing a domain-specific exception.

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### list_linked_objects

Enumerate linked objects for the selected source and link type using supported filters.
Concurrent changes can omit or repeat objects; preserve identity and continuation when
bounded retrieval stops.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/OntologyObject/list_linked_objects.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/OntologyObject/list_linked_objects.py):

```bash
python -B examples/rest/077/v1/ontologies/OntologyObject/list_linked_objects.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

No named operation failures are declared by this frozen SDK method. Generic API,
authentication, transport and decoding failures remain possible; preserve the error
envelope and request identity rather than inventing a domain-specific exception.

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### search

Build a search query from the complete local union definitions and property types.
Inspect returned object identities and finite continuation; unsupported query/property
combinations require schema correction.

The prefix query uses FieldNameV1 `properties.status` with prefix `rea`, and requests
selected properties `assetId` and `status` using their API names. The returned asset
has status `ready`, which satisfies that predicate, and retains primary key `A-1`.
Keep query field paths distinct from selected-property names. This one-page fixture
has no continuation token; use the linked client behavior's finite-page procedure when
one is present.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/OntologyObject/search.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/OntologyObject/search.py):

```bash
python -B examples/rest/077/v1/ontologies/OntologyObject/search.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

No named operation failures are declared by this frozen SDK method. Generic API,
authentication, transport and decoding failures remain possible; preserve the error
envelope and request identity rather than inventing a domain-specific exception.

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
