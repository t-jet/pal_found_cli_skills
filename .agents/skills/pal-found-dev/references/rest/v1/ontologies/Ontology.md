# v1 ontologies: Ontology

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

An Ontology is the semantic boundary for object, action and query types. Discover
visible ontologies, then retain the intended ontology RID for all subsequent v1 calls.
Similar display names do not establish identical schemas.

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
