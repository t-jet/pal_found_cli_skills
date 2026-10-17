# v2 admin: MarkingCategory

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

A marking category groups marking definitions. Read category metadata when interpreting
or authoring a marking. Replacing category configuration is an administration change and
should be reviewed independently of resource marking changes.

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

Create a category using its complete request shape and retain the returned ID. Verify
its configuration before creating markings under that category.

This Public Beta endpoint requires `preview=true`; set `preview=True` in the SDK call.

[Exact parameters, request, result and error models](../../contracts/v2/admin/MarkingCategory/create.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/MarkingCategory/create.py):

```bash
python -B examples/rest/072/v2/admin/MarkingCategory/create.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CreateMarkingCategoryMissingInitialAdminRole | At least one ADMINISTER role assignment must be provided when creating a marking category. |
| CreateMarkingCategoryMissingOrganization | At least one organization must be provided when creating a marking category. |
| CreateMarkingCategoryPermissionDenied | Could not create the MarkingCategory. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get

Inspect the selected category's definition before interpreting or changing its markings.
Resolve category identity using the returned ID.

[Exact parameters, request, result and error models](../../contracts/v2/admin/MarkingCategory/get.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/MarkingCategory/get.py):

```bash
python -B examples/rest/072/v2/admin/MarkingCategory/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| GetMarkingCategoryPermissionDenied | The provided token does not have permission to view the marking category. |
| MarkingCategoryNotFound | The given MarkingCategory could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### list

Enumerate categories with page size at most 100 and finite continuation budgets. Compare
category identities and definitions rather than choosing by display name alone.

[Exact parameters, request, result and error models](../../contracts/v2/admin/MarkingCategory/list.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/MarkingCategory/list.py):

```bash
python -B examples/rest/072/v2/admin/MarkingCategory/list.py
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

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### replace

Read category configuration, replace the intended fields using the full request model,
then verify the returned category. Review the consequences for markings organized under
it.

This Public Beta endpoint requires `preview=true`; set `preview=True` in the SDK call.

[Exact parameters, request, result and error models](../../contracts/v2/admin/MarkingCategory/replace.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/MarkingCategory/replace.py):

```bash
python -B examples/rest/072/v2/admin/MarkingCategory/replace.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| GetMarkingCategoryPermissionDenied | The provided token does not have permission to view the marking category. |
| MarkingCategoryNotFound | The given MarkingCategory could not be found. |
| ReplaceMarkingCategoryPermissionDenied | Could not replace the MarkingCategory. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
