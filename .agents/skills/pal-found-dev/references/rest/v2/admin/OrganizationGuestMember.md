# v2 admin: OrganizationGuestMember

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Guest membership allows a principal to participate as an organization guest. Primary
membership is a different relationship. A successful request against a primary member
does not prove that guest membership was added or removed.

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

Add the selected guest principals, then list guests to verify actual membership. Adding
a primary member still returns success but does not create guest membership.

[Exact parameters, request, result and error models](../../contracts/v2/admin/OrganizationGuestMember/add.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/OrganizationGuestMember/add.py):

```bash
python -B examples/rest/072/v2/admin/OrganizationGuestMember/add.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| AddOrganizationGuestMembersPermissionDenied | Could not add the OrganizationGuestMember. |
| OrganizationNotFound | The given Organization could not be found. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### list

Enumerate organization guests and preserve principal types/IDs. This inventory does not
replace primary-organization membership information.

[Exact parameters, request, result and error models](../../contracts/v2/admin/OrganizationGuestMember/list.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/OrganizationGuestMember/list.py):

```bash
python -B examples/rest/072/v2/admin/OrganizationGuestMember/list.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| ListOrganizationGuestMembersPermissionDenied | The provided token does not have permission to list guest members for this organization. |
| OrganizationNotFound | The given Organization could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### remove

Remove selected guests and confirm the guest inventory. Removing a primary member
through this endpoint succeeds without removing primary membership.

[Exact parameters, request, result and error models](../../contracts/v2/admin/OrganizationGuestMember/remove.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/OrganizationGuestMember/remove.py):

```bash
python -B examples/rest/072/v2/admin/OrganizationGuestMember/remove.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| OrganizationNotFound | The given Organization could not be found. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |
| RemoveOrganizationGuestMembersPermissionDenied | Could not remove the OrganizationGuestMember. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
