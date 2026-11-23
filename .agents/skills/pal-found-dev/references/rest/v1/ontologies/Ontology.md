# v1 ontologies: Ontology

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

An Ontology is the semantic boundary for object, action and query types. Discover
visible ontologies, then retain the intended ontology RID for all subsequent v1 calls.
Similar display names do not establish identical schemas.

## API v1 and v2

These guides describe SDK 1.101.0's `foundry_sdk.v1.ontologies` clients and `/api/v1`
routes. Choose the API version before adapting code. The v2 clients have separate
contracts, request models and response models; changing the URL version alone is
insufficient.

| Concern | API v1 | API v2 in the same SDK release |
| --- | --- | --- |
| Ontology selector | `ontology_rid: OntologyRid`, an ontology RID | `ontology: OntologyIdentifier`, API name or RID |
| Object type metadata | `ObjectType.primaryKey` is a list; optional type `displayName`; no `titleProperty` | `ObjectTypeV2.primaryKey` is one property name; required `titleProperty`, `displayName`, `pluralDisplayName` and icon |
| Property metadata | `Property.baseType` describes the value type | `PropertyV2.dataType` uses a typed union |
| Object records | `OntologyObject` wraps `properties` and `rid` | `OntologyObjectV2` is a property-name/value dictionary, without the v1 wrapper |
| Action application | Separate `Action.validate`; `apply` returns empty `ApplyActionResponse`; explicit parameters, no defaults | `Action.apply` accepts `ApplyActionRequestOptions` (`mode`, `returnEdits`) and returns `SyncApplyActionResponseV2` with optional validation/edits |

Local v2 contracts: [ontology get](../../contracts/v2/ontologies/Ontology/get.md),
[object type get](../../contracts/v2/ontologies/ObjectType/get.md),
[object get](../../contracts/v2/ontologies/OntologyObject/get.md), and
[action apply](../../contracts/v2/ontologies/Action/apply.md).
Source distinctions come from SDK 1.101.0 `v1/ontologies/models.py`,
`v2/ontologies/models.py`, and each version's `action.py` and `ontology_object.py`.

Object Storage V1 and Object Storage V2 describe storage backends, independently of
HTTP API v1/v2. A v1 Action can affect either backend: its documented edit visibility
is eventual for Object Storage V1 and immediate after completion for Object Storage
V2. The v1 API prefix does not identify the storage backend. Confirm the backend and
operation-specific limits for the target object type before choosing a recovery plan.

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

### get

Read the intended ontology by RID and compare returned metadata with the application's
expected semantic boundary.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/Ontology/get.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/Ontology/get.py):

```bash
python -B examples/rest/077/v1/ontologies/Ontology/get.py
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

Discover ontologies visible to the caller and retain the chosen RID. Visibility reflects
caller access and does not prove that every object/action/query is accessible.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/Ontology/list.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/Ontology/list.py):

```bash
python -B examples/rest/077/v1/ontologies/Ontology/list.py
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
