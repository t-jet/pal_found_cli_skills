# v2 admin: User, continued

[Resource overview](User.md) | [Client behavior](../../client-behavior.md)

### revoke_all_tokens

Revoke all active tokens, including browser sessions and long-lived development tokens.
Active browser users must authenticate again. The caller needs permission to manage
users for the target user's organization; verify this before submission.

[Exact parameters, request, result and error models](../../contracts/v2/admin/User/revoke_all_tokens.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/User/revoke_all_tokens.py):

```bash
python -B examples/rest/071/v2/admin/User/revoke_all_tokens.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| RevokeAllTokensUserPermissionDenied | Could not revokeAllTokens the User. |
| UserDeleted | The user is deleted. |
| UserNotFound | The given User could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### search

Search active users with case-insensitive prefixes of username, given name or family
name. For deleted users, use list with include=DELETED. Resolve candidate IDs before
administration.

[Exact parameters, request, result and error models](../../contracts/v2/admin/User/search.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/User/search.py):

```bash
python -B examples/rest/071/v2/admin/User/search.py
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
| SearchUsersPermissionDenied | Could not search the User. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
