# v2 admin: OrganizationRoleAssignment

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Organization roles connect principals to responsibilities at organization scope.
Discover available roles from the organization and identify principals before changing
assignments. These assignments differ from enrollment-wide and project roles.

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

Add at most 100 principal-role assignments after discovering roles available to the
organization. List assignments afterward to verify requested principals and roles.

[Exact parameters, request, result and error models](../../contracts/v2/admin/OrganizationRoleAssignment/add.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/OrganizationRoleAssignment/add.py):

```bash
python -B examples/rest/072/v2/admin/OrganizationRoleAssignment/add.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| AddOrganizationRoleAssignmentsPermissionDenied | Could not add the OrganizationRoleAssignment. |
| OrganizationNotFound | The given Organization could not be found. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### list

Inspect principal-role assignments for the selected organization. Preserve identities
and scope when explaining access; enrollment assignments are separate.

[Exact parameters, request, result and error models](../../contracts/v2/admin/OrganizationRoleAssignment/list.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/OrganizationRoleAssignment/list.py):

```bash
python -B examples/rest/072/v2/admin/OrganizationRoleAssignment/list.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| ListOrganizationRoleAssignmentsPermissionDenied | The provided token does not have permission to list assigned roles for this organization. |
| OrganizationNotFound | The given Organization could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### remove

Remove at most 100 intended assignments from the confirmed organization. Verify
remaining assignments and other access paths before declaring access removed.

[Exact parameters, request, result and error models](../../contracts/v2/admin/OrganizationRoleAssignment/remove.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/OrganizationRoleAssignment/remove.py):

```bash
python -B examples/rest/072/v2/admin/OrganizationRoleAssignment/remove.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| OrganizationNotFound | The given Organization could not be found. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |
| RemoveOrganizationRoleAssignmentsPermissionDenied | Could not remove the OrganizationRoleAssignment. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
