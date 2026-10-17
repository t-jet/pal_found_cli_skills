# v2 admin: User

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Users are enrollment identities. Profile information, markings, authentication tokens
and group membership expose different parts of that identity. Token revocation affects
active sessions; a user profile lookup does not establish permission to manage that
user.

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

### delete

Confirm the target user ID and organization before deleting the user. Capture why
deactivation or token revocation alone would not satisfy the intended change. Check
resulting identity state through permitted administration reads.

[Exact parameters, request, result and error models](../../contracts/v2/admin/User/delete.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/User/delete.py):

```bash
python -B examples/rest/071/v2/admin/User/delete.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| DeleteUserPermissionDenied | Could not delete the User. |
| UserDeleted | The user is deleted. |
| UserNotFound | The given User could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get

Read a selected user by ID and verify organization and identifying fields before
administration. Missing visibility and missing identity require investigation rather
than creating a substitute user.

[Exact parameters, request, result and error models](../../contracts/v2/admin/User/get.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/User/get.py):

```bash
python -B examples/rest/071/v2/admin/User/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| UserDeleted | The user is deleted. |
| UserIsActive | The user is an active user. |
| UserNotFound | The given User could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_batch

Resolve multiple user IDs with at most 500 requests per batch. Match response identities
to requested users before evaluating or changing their access.

[Exact parameters, request, result and error models](../../contracts/v2/admin/User/get_batch.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/User/get_batch.py):

```bash
python -B examples/rest/071/v2/admin/User/get_batch.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

No named operation failures are declared by this frozen SDK method. Generic API,
authentication, transport and decoding failures remain possible; preserve the error
envelope and request identity rather than inventing a domain-specific exception.

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_current

Read the identity represented by the current token. Compare it with the intended
application identity before performing administration; the fixture token does not
identify a real enrollment user.

[Exact parameters, request, result and error models](../../contracts/v2/admin/User/get_current.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/User/get_current.py):

```bash
python -B examples/rest/071/v2/admin/User/get_current.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| GetCurrentUserPermissionDenied | Could not getCurrent the User. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_markings

Read markings of which the selected user is currently a member. Use marking IDs to
explain access, then inspect the marking definitions and resource requirements rather
than assuming membership grants every resource role.

[Exact parameters, request, result and error models](../../contracts/v2/admin/User/get_markings.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/User/get_markings.py):

```bash
python -B examples/rest/071/v2/admin/User/get_markings.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| GetMarkingsUserPermissionDenied | Could not getMarkings the User. |
| UserDeleted | The user is deleted. |
| UserNotFound | The given User could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### list

Enumerate users with bounded paging. Choose the include filter intentionally when
deleted identities matter; ordinary active-user search cannot supply that inventory.

[Exact parameters, request, result and error models](../../contracts/v2/admin/User/list.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/User/list.py):

```bash
python -B examples/rest/071/v2/admin/User/list.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| InvalidPageSize | The provided page size was zero or negative. Page sizes must be greater than zero. |
| UserDeleted | The user is deleted. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### profile_picture

Read the selected user's profile-picture content as bytes. Treat it as binary content
rather than JSON and close raw or streaming responses after consumption.

[Exact parameters, request, result and error models](../../contracts/v2/admin/User/profile_picture.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/User/profile_picture.py):

```bash
python -B examples/rest/071/v2/admin/User/profile_picture.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| GetProfilePictureOfUserPermissionDenied | Could not profilePicture the User. |
| InvalidProfilePicture | The user's profile picture is not a valid image |
| ProfileServiceNotPresent | The Profile service is unexpectedly not present. |
| UserDeleted | The user is deleted. |
| UserNotFound | The given User could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

## More operations

- [Part 2](User-2.md)
