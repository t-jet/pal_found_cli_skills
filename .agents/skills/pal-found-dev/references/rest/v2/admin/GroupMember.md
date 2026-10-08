# v2 admin: GroupMember

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Membership connects a user or another group to a group. Nested membership can make
access transitive. Resolve both principal identity and the destination group before
changing membership; similarly named users and groups are different principals.

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

### add

Resolve the destination group and each user/group principal, then add those members
using the request model. Read membership afterward to confirm intended identities rather
than relying on display names.

[Exact parameters, request, result and error models](../../contracts/v2/admin/GroupMember/add.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/GroupMember/add.py):

```bash
python -B examples/rest/071/v2/admin/GroupMember/add.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| AddGroupMembersPermissionDenied | Could not add the GroupMember. |
| GroupNotFound | The given Group could not be found. |
| InvalidGroupMembershipExpiration | The member expiration you provided does not conform to the Group's requirements for member expirations. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### list

Enumerate the destination group's user and group members. Inspect each principal type
and keep finite continuation budgets; nested groups are not equivalent to direct user
members.

[Exact parameters, request, result and error models](../../contracts/v2/admin/GroupMember/list.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/GroupMember/list.py):

```bash
python -B examples/rest/071/v2/admin/GroupMember/list.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| ExpirationForTransitiveGroupMembersNotSupported | You cannot pass includeExpirations if transitive is true. |
| GroupNotFound | The given Group could not be found. |
| InvalidPageSize | The provided page size was zero or negative. Page sizes must be greater than zero. |
| ListGroupMembersPermissionDenied | The provided token does not have permission to view the members of the given group. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### remove

Remove the intended member identities from the confirmed destination group. Read
membership afterward and account for other direct or transitive access paths when
interpreting the effect.

[Exact parameters, request, result and error models](../../contracts/v2/admin/GroupMember/remove.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/GroupMember/remove.py):

```bash
python -B examples/rest/071/v2/admin/GroupMember/remove.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| GroupNotFound | The given Group could not be found. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |
| RemoveGroupMembersPermissionDenied | Could not remove the GroupMember. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
