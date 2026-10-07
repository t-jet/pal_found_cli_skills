# v2 admin: Role

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

A Role definition describes an administration role identified by its ID. Resolve a
definition before constructing a role assignment. Reading a role definition does not
assign it or establish that it is valid for every administrative scope.

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

Retrieve a role definition by ID and inspect its meaning before using it in an
assignment. Scope eligibility still comes from the target organization or enrollment
API.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Role/get.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/Role/get.py):

```bash
python -B examples/rest/072/v2/admin/Role/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| RoleNotFound | The given Role could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_batch

Resolve up to 500 role definitions per batch and match returned IDs with requested roles
before constructing administration changes.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Role/get_batch.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/Role/get_batch.py):

```bash
python -B examples/rest/072/v2/admin/Role/get_batch.py
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
