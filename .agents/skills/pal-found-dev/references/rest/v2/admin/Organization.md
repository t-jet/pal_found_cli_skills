# v2 admin: Organization

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Organizations define identity and access boundaries within an enrollment. Their
metadata, available roles, role assignments and guest membership have separate APIs.
Resolve the organization before adding principals or interpreting its marking.

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

### create

Create the intended organization from its request model, retain the RID and verify
returned configuration. Plan membership and role assignment separately; creation alone
does not configure every user's access.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Organization/create.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/Organization/create.py):

```bash
python -B examples/rest/072/v2/admin/Organization/create.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CreateOrganizationMissingInitialAdminRole | At least one organization:administrator role grant must be provided when creating a organization. |
| CreateOrganizationPermissionDenied | Could not create the Organization. |
| EnrollmentNotFound | The given Enrollment could not be found. |
| OrganizationNameAlreadyExists | An organization with the same name already exists. |
| OrganizationNotFound | The given Organization could not be found. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get

Read an organization by RID and verify its identity before administering members or
roles. Resolve visibility failures rather than choosing another organization
automatically.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Organization/get.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/Organization/get.py):

```bash
python -B examples/rest/072/v2/admin/Organization/get.py
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

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### list_available_roles

Discover role definitions assignable to principals for this organization. Use those
returned role IDs when constructing organization assignments; do not reuse arbitrary
enrollment roles.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Organization/list_available_roles.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/Organization/list_available_roles.py):

```bash
python -B examples/rest/072/v2/admin/Organization/list_available_roles.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| ListAvailableRolesOrganizationPermissionDenied | Could not listAvailableRoles the Organization. |
| OrganizationNotFound | The given Organization could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### replace

Read the organization, submit the intended replacement and compare resulting
configuration. Treat it as an identity-boundary administration change.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Organization/replace.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/Organization/replace.py):

```bash
python -B examples/rest/072/v2/admin/Organization/replace.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| InvalidHostName | The provided hostname must be a valid domain name. The only allowed characters are letters, numbers, periods, and hyphens. |
| OrganizationNameAlreadyExists | An organization with the same name already exists. |
| OrganizationNotFound | The given Organization could not be found. |
| ReplaceOrganizationPermissionDenied | Could not replace the Organization. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
