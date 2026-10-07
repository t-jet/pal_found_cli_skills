# v2 admin: GroupProviderInfo

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Provider information associates a group with authentication-provider data. Treat it as
identity configuration rather than ordinary display metadata. Resolve the group and
provider relationship before proposing a replacement.

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

Read the selected group's provider information and correlate its provider identities
with the intended authentication source. Preserve this result before proposing an
identity-configuration change.

[Exact parameters, request, result and error models](../../contracts/v2/admin/GroupProviderInfo/get.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/GroupProviderInfo/get.py):

```bash
python -B examples/rest/071/v2/admin/GroupProviderInfo/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| GetGroupProviderInfoPermissionDenied | The provided token does not have permission to view the provider information for the given group. |
| GroupNotFound | The given Group could not be found. |
| GroupProviderInfoNotFound | The given GroupProviderInfo could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### replace

Replace provider information for the confirmed group using the exact request model. Re-
read and compare external identifiers; a similar display name is insufficient evidence
that the provider mapping is correct.

[Exact parameters, request, result and error models](../../contracts/v2/admin/GroupProviderInfo/replace.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/GroupProviderInfo/replace.py):

```bash
python -B examples/rest/071/v2/admin/GroupProviderInfo/replace.py
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
| GetGroupProviderInfoPermissionDenied | The provided token does not have permission to view the provider information for the given group. |
| GroupNotFound | The given Group could not be found. |
| GroupProviderInfoNotFound | The given GroupProviderInfo could not be found. |
| ReplaceGroupProviderInfoPermissionDenied | Could not replace the GroupProviderInfo. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
