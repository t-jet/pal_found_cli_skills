# v2 admin: Marking

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Markings protect resources or express classification. Marking identity, category,
membership and administration roles are different records. A governance application must
resolve marking IDs and understand their constraints before attaching them to resources.

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

Resolve the category and intended marking configuration, create the marking, then retain
its ID. Review its membership and administration separately before applying it to
resources.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Marking/create.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/Marking/create.py):

```bash
python -B examples/rest/072/v2/admin/Marking/create.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CreateMarkingMissingInitialAdminRole | At least one ADMINISTER role assignment must be provided when creating a marking. |
| CreateMarkingPermissionDenied | Could not create the Marking. |
| GetMarkingCategoryPermissionDenied | The provided token does not have permission to view the marking category. |
| MarkingCategoryNotFound | The given MarkingCategory could not be found. |
| MarkingNameInCategoryAlreadyExists | A marking with the same name already exists in the category. |
| MarkingNameIsEmpty | The marking name is empty. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get

Retrieve a marking by ID and inspect category and configuration before applying it or
changing membership. Similar display names can refer to different protection boundaries.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Marking/get.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/Marking/get.py):

```bash
python -B examples/rest/072/v2/admin/Marking/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| GetMarkingPermissionDenied | The provided token does not have permission to view the marking. |
| MarkingNotFound | The given Marking could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_batch

Retrieve marking definitions together with at most 500 requests per batch. Match
returned identities with requested IDs before deriving classification or access policy.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Marking/get_batch.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/Marking/get_batch.py):

```bash
python -B examples/rest/072/v2/admin/Marking/get_batch.py
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

### list

Enumerate markings with page size at most 100 and finite page/item limits. Preserve
continuation state when the budget ends rather than reporting a complete policy
inventory.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Marking/list.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/Marking/list.py):

```bash
python -B examples/rest/072/v2/admin/Marking/list.py
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

### parse_classifications

Parse classification strings into marking IDs. Inspect both parsed results and the
errors collection: unparseable strings return human-readable errors and must not be
silently treated as unclassified. This Public Beta endpoint requires `preview=true`;
set `preview=True` in the SDK call. Submit 1–1000 entries, counting duplicates.
The API parses duplicate strings once, returns `MissingBatchRequest` for an empty
list, and returns `BatchRequestSizeExceededLimit` for more than 1000 entries.
SDK 1.101.0 sends either invalid list length to the API without local validation.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Marking/parse_classifications.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/Marking/parse_classifications.py):

```bash
python -B examples/rest/072/v2/admin/Marking/parse_classifications.py
```

The example checks request serialization, verifies that every submitted string
appears in exactly one result map, and checks each SDK-declared error. It uses
one raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CbacUnavailable | CBAC is not available. |
| ParseClassificationsPermissionDenied | The provided token does not have permission to parse the given classification strings. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### replace

Read the marking definition, construct a replacement for that ID and compare returned
configuration. Coordinate changes with its policy owner before modifying a protection
boundary.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Marking/replace.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/Marking/replace.py):

```bash
python -B examples/rest/072/v2/admin/Marking/replace.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| GetMarkingCategoryPermissionDenied | The provided token does not have permission to view the marking category. |
| GetMarkingPermissionDenied | The provided token does not have permission to view the marking. |
| MarkingNameInCategoryAlreadyExists | A marking with the same name already exists in the category. |
| MarkingNameIsEmpty | The marking name is empty. |
| MarkingNotFound | The given Marking could not be found. |
| ReplaceMarkingPermissionDenied | Could not replace the Marking. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
