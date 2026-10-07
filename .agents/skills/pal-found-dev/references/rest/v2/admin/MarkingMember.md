# v2 admin: MarkingMember

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Marking members are principals who can view resources protected by that marking.
Membership affects access to marked resources; it is not the same as permission to
administer the marking. Reading members requires administrative access.

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

Add the selected principals as marking members. Inspect membership afterward to confirm
who can view resources protected by this marking; membership is separate from resource-
role assignment.

[Exact parameters, request, result and error models](../../contracts/v2/admin/MarkingMember/add.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/MarkingMember/add.py):

```bash
python -B examples/rest/072/v2/admin/MarkingMember/add.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| AddMarkingMembersPermissionDenied | Could not add the MarkingMember. |
| GetMarkingPermissionDenied | The provided token does not have permission to view the marking. |
| MarkingNotFound | The given Marking could not be found. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### list

Read principals allowed to view resources protected by the marking. The endpoint ignores
pageSize and requires api:admin-write because only marking administrators can see these
members. Bound pages and total members independently of page size.

[Exact parameters, request, result and error models](../../contracts/v2/admin/MarkingMember/list.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/MarkingMember/list.py):

```bash
python -B examples/rest/072/v2/admin/MarkingMember/list.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| GetMarkingPermissionDenied | The provided token does not have permission to view the marking. |
| ListMarkingMembersPermissionDenied | The provided token does not have permission to list the members of this marking. |
| MarkingNotFound | The given Marking could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### remove

Remove the intended principals from marking membership and verify the resulting
membership. Consider remaining group membership when explaining effective marked-
resource access.

[Exact parameters, request, result and error models](../../contracts/v2/admin/MarkingMember/remove.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/MarkingMember/remove.py):

```bash
python -B examples/rest/072/v2/admin/MarkingMember/remove.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| GetMarkingPermissionDenied | The provided token does not have permission to view the marking. |
| MarkingNotFound | The given Marking could not be found. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |
| RemoveMarkingMembersPermissionDenied | Could not remove the MarkingMember. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
