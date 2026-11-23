# v1 ontologies: ObjectType

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

ObjectType metadata describes object properties and outgoing link types. Object API
names and link API names are schema identities. Resolve their definitions before
querying objects or traversing links; metadata is separate from object instances.

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

## Synthetic metadata

The get example requests and returns `Asset`. Its primary-key list is `['assetId']`;
properties declare `assetId` and `status` as `String`, and `inspectionDate` as
`LocalDate`. The list example also declares `Facility`, keyed by string `facilityId`,
with string property `name`. The outgoing `facility` link from Asset identifies
Facility as target with cardinality ONE. Use that target schema for linked-object
results. Every primary-key entry must resolve to a declared property.

Frozen v1 `ObjectType` exposes an optional type `displayName` and no `titleProperty`
field. The display name labels the type; it does not establish an object's title
property. API v2 `ObjectTypeV2` instead requires a scalar `primaryKey` and
`titleProperty`, each naming a property in its schema. Do not invent a v1 title
field or copy v2 metadata into a v1 response. See [API version comparison](Ontology.md#api-v1-and-v2).

### get

Read object-type metadata by API name and inspect properties/primary-key schema before
constructing object requests.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/ObjectType/get.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/ObjectType/get.py):

```bash
python -B examples/rest/077/v1/ontologies/ObjectType/get.py
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

### get_outgoing_link_type

Resolve one outgoing link type from the selected object type. Inspect source/target
identities before following object links.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/ObjectType/get_outgoing_link_type.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/ObjectType/get_outgoing_link_type.py):

```bash
python -B examples/rest/077/v1/ontologies/ObjectType/get_outgoing_link_type.py
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

Discover object types in the intended ontology with bounded continuation. Retain API
names and schemas for subsequent object access.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/ObjectType/list.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/ObjectType/list.py):

```bash
python -B examples/rest/077/v1/ontologies/ObjectType/list.py
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

### list_outgoing_link_types

Enumerate outgoing link metadata for the selected object type. Inspect each target type
and cardinality before authoring traversal code.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/ObjectType/list_outgoing_link_types.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/ObjectType/list_outgoing_link_types.py):

```bash
python -B examples/rest/077/v1/ontologies/ObjectType/list_outgoing_link_types.py
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
