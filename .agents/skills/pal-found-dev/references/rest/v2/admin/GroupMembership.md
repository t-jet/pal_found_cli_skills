# v2 admin: GroupMembership

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Membership discovery identifies groups associated with a user. Use it to explain access
paths rather than assuming that a displayed group name is an authorization decision. The
current-user group operation also includes transitive membership.

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

Enumerate a selected user's group memberships with bounded continuation. Source
identifies api:admin-read for this membership endpoint; verify the grant and user access
in the tenant.

[Exact parameters, request, result and error models](../../contracts/v2/admin/GroupMembership/list.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/GroupMembership/list.py):

```bash
python -B examples/rest/071/v2/admin/GroupMembership/list.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| InvalidPageSize | The provided page size was zero or negative. Page sizes must be greater than zero. |
| UserDeleted | The user is deleted. |
| UserNotFound | The given User could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
