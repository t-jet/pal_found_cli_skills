# v2 admin: Group, continued

[Resource overview](Group.md) | [Client behavior](../../client-behavior.md)

### search

Use a case-insensitive group-name prefix to discover candidates. Verify the returned
group ID and organization before using a matching name in membership or role changes.

[Exact parameters, request, result and error models](../../contracts/v2/admin/Group/search.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/Group/search.py):

```bash
python -B examples/rest/071/v2/admin/Group/search.py
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
| SearchGroupsPermissionDenied | Could not search the Group. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
