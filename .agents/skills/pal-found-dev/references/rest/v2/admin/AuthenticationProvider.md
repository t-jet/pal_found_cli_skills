# v2 admin: AuthenticationProvider

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Authentication providers connect external identity sources to enrollment users and
groups. Preregistration establishes a user or group before first login through that
provider. These identities can then participate in group and role administration.

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

Resolve the provider RID and inspect its metadata before preregistering a user or group.
Do not infer provider identity from a user-facing login label alone.

[Exact parameters, request, result and error models](../../contracts/v2/admin/AuthenticationProvider/get.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/AuthenticationProvider/get.py):

```bash
python -B examples/rest/072/v2/admin/AuthenticationProvider/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| AuthenticationProviderNotFound | The given AuthenticationProvider could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### list

Discover authentication providers and retain their RIDs. Compare provider metadata with
the intended identity source before choosing a preregistration target.

[Exact parameters, request, result and error models](../../contracts/v2/admin/AuthenticationProvider/list.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/AuthenticationProvider/list.py):

```bash
python -B examples/rest/072/v2/admin/AuthenticationProvider/list.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| EnrollmentNotFound | The given Enrollment could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### preregister_group

Preregister a named group through the confirmed provider before its users log in. Retain
the group identity for later role or membership assignments; preregistration itself does
not grant those roles.

[Exact parameters, request, result and error models](../../contracts/v2/admin/AuthenticationProvider/preregister_group.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/AuthenticationProvider/preregister_group.py):

```bash
python -B examples/rest/072/v2/admin/AuthenticationProvider/preregister_group.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| AuthenticationProviderNotFound | The given AuthenticationProvider could not be found. |
| PreregisterGroupPermissionDenied | Could not preregisterGroup the AuthenticationProvider. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### preregister_user

Preregister a username through the confirmed provider before first login. Retain the
returned identity so groups and roles can be assigned deliberately before login.

[Exact parameters, request, result and error models](../../contracts/v2/admin/AuthenticationProvider/preregister_user.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/AuthenticationProvider/preregister_user.py):

```bash
python -B examples/rest/072/v2/admin/AuthenticationProvider/preregister_user.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| AuthenticationProviderNotFound | The given AuthenticationProvider could not be found. |
| PreregisterUserPermissionDenied | Could not preregisterUser the AuthenticationProvider. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
