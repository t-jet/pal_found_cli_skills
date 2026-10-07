# v1 ontologies: Query

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

A Query executes configured Ontology logic using its API name and supplied parameters.
Tenant-defined argument and result shapes come from QueryType metadata. Optional
parameters may be omitted; required parameters still need schema-compatible values.

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

## Synthetic query schema

The executable `execute` example assumes a synthetic query named `asset-status`.
It accepts required string parameter `assetId` and returns an object with string
fields `assetId` and `status`. The fixture requests `A-1` and returns
`{"assetId": "A-1", "status": "ready"}`. These are complete example values,
not a built-in Foundry query or a promise about another ontology.

For tenant code, read [QueryType](QueryType.md) for the selected API name and
inspect its parameter and result definitions. Substitute the authorized API
name, required parameter IDs and values. Check returned fields against that
schema before updating application state. Obtain metadata through authorized
enrollment access or a preprovisioned approved metadata snapshot; public internet
access is unnecessary for this procedure.

### execute

Read QueryType metadata, supply required tenant-defined parameters and omit optional
ones when intended. Execute the configured API name and validate the returned result
against its metadata.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/Query/execute.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/Query/execute.py):

```bash
python -B examples/rest/077/v1/ontologies/Query/execute.py
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
