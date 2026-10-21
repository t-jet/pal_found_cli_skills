# v2 admin: EnrollmentRoleAssignment

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Enrollment role assignments connect principals and roles at enrollment scope. Resolve
the enrollment, principal types and role identities before changing assignments.
Enrollment roles should not be confused with organization or resource roles.

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

Add at most 100 principal-role assignments to the selected enrollment. Validate
principal types and role IDs, then list assignments to compare intended access.

This Public Beta endpoint requires `preview=true`; set `preview=True` in the SDK call.

[Exact parameters, request, result and error models](../../contracts/v2/admin/EnrollmentRoleAssignment/add.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/EnrollmentRoleAssignment/add.py):

```bash
python -B examples/rest/072/v2/admin/EnrollmentRoleAssignment/add.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| AddEnrollmentRoleAssignmentsPermissionDenied | Could not add the EnrollmentRoleAssignment. |
| EnrollmentNotFound | The given Enrollment could not be found. |
| EnrollmentRoleNotFound | One of the provided role IDs was not found. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### list

Enumerate principals with roles in the selected enrollment. Preserve both principal and
role identities when explaining enrollment-wide access.

This Public Beta endpoint requires `preview=true`; set `preview=True` in the SDK call.

[Exact parameters, request, result and error models](../../contracts/v2/admin/EnrollmentRoleAssignment/list.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/EnrollmentRoleAssignment/list.py):

```bash
python -B examples/rest/072/v2/admin/EnrollmentRoleAssignment/list.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| EnrollmentNotFound | The given Enrollment could not be found. |
| ListEnrollmentRoleAssignmentsPermissionDenied | The provided token does not have permission to list assigned roles for this enrollment. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### remove

Remove at most 100 principal-role assignments from the confirmed enrollment. List
assignments afterward; removing one role does not establish that other access paths
disappeared.

This Public Beta endpoint requires `preview=true`; set `preview=True` in the SDK call.

[Exact parameters, request, result and error models](../../contracts/v2/admin/EnrollmentRoleAssignment/remove.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/EnrollmentRoleAssignment/remove.py):

```bash
python -B examples/rest/072/v2/admin/EnrollmentRoleAssignment/remove.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| EnrollmentNotFound | The given Enrollment could not be found. |
| EnrollmentRoleNotFound | One of the provided role IDs was not found. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |
| RemoveEnrollmentRoleAssignmentsPermissionDenied | Could not remove the EnrollmentRoleAssignment. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
