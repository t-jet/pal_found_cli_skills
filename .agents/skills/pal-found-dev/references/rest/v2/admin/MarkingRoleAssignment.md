# v2 admin: MarkingRoleAssignment

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Marking role assignments distinguish USE, DECLASSIFY and ADMINISTER responsibilities.
For organization markings, ADMINISTER is managed through organization role assignments;
this resource accepts USE and DECLASSIFY only.

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

Add supported principal-role assignments. For organization markings use only USE or
DECLASSIFY here; manage ADMINISTER through OrganizationRoleAssignment.

[Exact parameters, request, result and error models](../../contracts/v2/admin/MarkingRoleAssignment/add.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/MarkingRoleAssignment/add.py):

```bash
python -B examples/rest/072/v2/admin/MarkingRoleAssignment/add.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| AddMarkingRoleAssignmentsPermissionDenied | Could not add the MarkingRoleAssignment. |
| GetMarkingPermissionDenied | The provided token does not have permission to view the marking. |
| MarkingNotFound | The given Marking could not be found. |
| OrganizationMarkingAdministerRoleNotSupported | The ADMINISTER role on Organization markings cannot be managed through the Marking Role Assignments endpoints. To manage administrator roles for an Organization, use the Organization Role Assignment endpoints instead. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### list

Read principal-role assignments for the marking. pageSize is ignored, so application
item/page budgets must bound retrieval independently.

[Exact parameters, request, result and error models](../../contracts/v2/admin/MarkingRoleAssignment/list.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/MarkingRoleAssignment/list.py):

```bash
python -B examples/rest/072/v2/admin/MarkingRoleAssignment/list.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| ListMarkingRoleAssignmentsPermissionDenied | The provided token does not have permission to list assigned roles for this marking. |
| MarkingNotFound | The given Marking could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### remove

Remove intended principal-role assignments. Organization-marking ADMINISTER changes
belong to OrganizationRoleAssignment rather than this endpoint.

[Exact parameters, request, result and error models](../../contracts/v2/admin/MarkingRoleAssignment/remove.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/MarkingRoleAssignment/remove.py):

```bash
python -B examples/rest/072/v2/admin/MarkingRoleAssignment/remove.py
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
| ListMarkingRoleAssignmentsPermissionDenied | The provided token does not have permission to list assigned roles for this marking. |
| MarkingNotFound | The given Marking could not be found. |
| OrganizationMarkingAdministerRoleNotSupported | The ADMINISTER role on Organization markings cannot be managed through the Marking Role Assignments endpoints. To manage administrator roles for an Organization, use the Organization Role Assignment endpoints instead. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |
| RemoveMarkingMembersPermissionDenied | Could not remove the MarkingMember. |
| RemoveMarkingRoleAssignmentsPermissionDenied | Could not remove the MarkingRoleAssignment. |
| RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed | You cannot remove all administrators from a marking. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
