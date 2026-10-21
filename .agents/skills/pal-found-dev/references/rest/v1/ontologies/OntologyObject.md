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

The direct-object example uses synthetic object type `Asset`, string primary key
`assetId`, and string property `status`. Its returned properties identify asset
`A-1` with status `ready`. The fixture exercises SDK decoding of a tenant-defined
property map; it does not assert that `Asset` exists in a real ontology.

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
