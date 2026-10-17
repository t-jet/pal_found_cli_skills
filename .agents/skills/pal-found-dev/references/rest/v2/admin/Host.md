# v2 admin: Host

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Host discovery enumerates hosts visible through enrollment administration. Preserve
returned host metadata rather than synthesizing service URLs from names. Visibility of a
host does not prove that every platform capability is enabled on it.

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

### list

Enumerate visible hosts within finite page and item budgets. Retain supplied host
metadata and continuation state; do not infer capability enablement from host
visibility.

This Public Beta endpoint requires `preview=true`; set `preview=True` in the SDK call.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Host/list.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/Host/list.py):

```bash
python -B examples/rest/072/v2/admin/Host/list.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| EnrollmentNotFound | The given Enrollment could not be found. |
| InvalidPageSize | The provided page size was zero or negative. Page sizes must be greater than zero. |
| ListHostsPermissionDenied | You do not have permission to list hosts for this enrollment |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
