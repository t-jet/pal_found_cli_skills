# v2 admin: UserProviderInfo

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

User provider information describes identity-provider associations. Read it for the
intended user before changing external identity information. A provider replacement is
distinct from updating a user profile or assigning application access.

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

Inspect a user's provider information for the selected identity. Correlate provider and
external identifiers before using that mapping in a governance workflow.

[Exact parameters, request, result and error models](../../contracts/v2/admin/UserProviderInfo/get.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/UserProviderInfo/get.py):

```bash
python -B examples/rest/071/v2/admin/UserProviderInfo/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| GetUserProviderInfoPermissionDenied | The provided token does not have permission to view the provider information for the given user. |
| UserDeleted | The user is deleted. |
| UserNotFound | The given User could not be found. |
| UserProviderInfoNotFound | The given UserProviderInfo could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### replace

Read the current provider mapping, apply the intended replacement, then compare the
resulting external identity fields. Verify tenant identity-management prerequisites
before changing provider data.

[Exact parameters, request, result and error models](../../contracts/v2/admin/UserProviderInfo/replace.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/UserProviderInfo/replace.py):

```bash
python -B examples/rest/071/v2/admin/UserProviderInfo/replace.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CannotReplaceProviderInfoForPrincipalInProtectedRealm | Provider information for Principals in this Realm cannot be replaced. |
| GetUserProviderInfoPermissionDenied | The provided token does not have permission to view the provider information for the given user. |
| ReplaceUserProviderInfoPermissionDenied | Could not replace the UserProviderInfo. |
| UserDeleted | The user is deleted. |
| UserNotFound | The given User could not be found. |
| UserProviderInfoNotFound | The given UserProviderInfo could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
