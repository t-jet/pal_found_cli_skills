# v2 admin: Group

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Groups collect users and other groups for access administration. Group identity,
organization visibility, membership and role assignments are separate concerns. A group
can exist without granting its members an application role. Preserve reserved multipass
attributes when replacing group configuration.

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

[Detailed worked procedure](Group-worked.md).

## Operations and outcome checks

### create

Create a named group with attributes and at least one organization RID. Compare returned
identity, visibility and attributes with the proposed review group before using it for
membership. Reserved multipass attributes belong to Foundry.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Group/create.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/Group/create.py):

```bash
python -B examples/rest/071/v2/admin/Group/create.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CreateGroupPermissionDenied | Could not create the Group. |
| GroupNameAlreadyExists | A group with this name already exists |
| InvalidGroupOrganizations | At least one Organization RID must be provided for a group |
| OrganizationNotFound | The given Organization could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### delete

Read and confirm the group ID before deleting that group. Capture the intended
membership and assignment impact for the administrator. Do not substitute deletion of a
similarly named group after a missing or denied result.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Group/delete.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/Group/delete.py):

```bash
python -B examples/rest/071/v2/admin/Group/delete.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| DeleteGroupPermissionDenied | Could not delete the Group. |
| GroupNotFound | The given Group could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get

Retrieve the intended group by ID and verify name and organization visibility before
acting on it. Retain the stable group ID rather than treating its display name as
identity.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Group/get.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/Group/get.py):

```bash
python -B examples/rest/071/v2/admin/Group/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| GroupNotFound | The given Group could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_batch

Retrieve several groups together, with at most 500 requests in a batch. Match returned
identities to requested IDs before using the response for access decisions.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Group/get_batch.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/Group/get_batch.py):

```bash
python -B examples/rest/071/v2/admin/Group/get_batch.py
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

Enumerate groups with explicit page and item budgets. Continuation tokens identify
remaining pages even when a page does not match the requested size. Preserve incomplete
enumeration state for the caller.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Group/list.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/Group/list.py):

```bash
python -B examples/rest/071/v2/admin/Group/list.py
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

### list_current

Find groups containing the current user directly or transitively. This operation
requires no particular scope and is available to authenticated users; do not substitute
it for another user's membership inventory.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Group/list_current.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/Group/list_current.py):

```bash
python -B examples/rest/071/v2/admin/Group/list_current.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| ListCurrentGroupsPermissionDenied | Could not listCurrent the Group. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### replace

Read the group first, retain every multipass-prefixed attribute exactly as returned,
then submit the replacement. Re-read the group to compare intended name, attributes and
organization visibility.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Group/replace.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/Group/replace.py):

```bash
python -B examples/rest/071/v2/admin/Group/replace.py
```

The example reads the current group, carries its `multipass:` attribute into the
replacement, and changes the `team` attribute. It checks both requests and the decoded
replacement, including each declared error. The replacement uses a raw response with
a 30-second timeout and closes it.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| AttributesNotEditable | One or more attributes are not editable. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are not editable. |
| GroupNameAlreadyExists | A group with this name already exists |
| GroupNotFound | The given Group could not be found. |
| InvalidGroupOrganizations | At least one Organization RID must be provided for a group |
| ReplaceGroupPermissionDenied | Could not replace the Group. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

## More operations

- [Part 2](Group-2.md)
