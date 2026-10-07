# v2 admin: Enrollment

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

An enrollment is an administration boundary containing organizations and platform
identities. An explicitly selected enrollment and the current user's primary-
organization enrollment can differ. Verify which boundary an administration application
is operating within.

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

Read enrollment metadata by RID and confirm the administration boundary before choosing
organization or role-assignment targets.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Enrollment/get.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/Enrollment/get.py):

```bash
python -B examples/rest/072/v2/admin/Enrollment/get.py
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

### get_current

Read the enrollment associated with the current user's primary organization. Compare its
RID with the intended boundary; do not assume every accessible organization belongs to
that enrollment.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Enrollment/get_current.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/Enrollment/get_current.py):

```bash
python -B examples/rest/072/v2/admin/Enrollment/get_current.py
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
| GetCurrentEnrollmentPermissionDenied | Could not getCurrent the Enrollment. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
