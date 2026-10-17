# ResourceRole: filesystem operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

Resource roles grant a principal an explicit role on one resource. Resolve the principal and role name from the enrollment, inspect existing assignments, and verify the effective assignment after a change.

Prepare SDK 1.101.0 and an identity authorized for the exact tenant resource. Check each contract for its API stage and endpoint-specific restrictions. No universal role or retry guarantee is implied by these operations. For an uncertain write, read the exact RID and effect before repeating it.

## Python client route

With a configured `FoundryClient` named `client`, use `client.filesystem.Resource.Role` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.

## Operations

### add

Assign a documented role to the intended principal on this resource. Verify the role list before relying on the grant.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/ResourceRole/add.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/ResourceRole/add.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### list

List the roles on the selected resource. Use this to verify specific principals and role names after a change.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/ResourceRole/list.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/ResourceRole/list.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### remove

Remove a specific role assignment from this resource and confirm it is absent from the subsequent role list.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/ResourceRole/remove.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/ResourceRole/remove.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

## Assign and verify one role

Use the prepared `FoundryClient` from [authentication](../../authentication.md).
Resolve `resource_rid`, `principal_id` and `role_id` in the intended enrollment.
The principal is a discriminated value; `PrincipalIdOnly` identifies a user or
group by ID without guessing its type. [Other principal forms](../../models/v2/filesystem/models/ResourceRolePrincipalIdentifier.md)
are available when the task calls for them.

```python
from foundry_sdk.v2.filesystem.models import PrincipalIdOnly, ResourceRoleIdentifier
from types import SimpleNamespace

role = ResourceRoleIdentifier(
    resource_role_principal=PrincipalIdOnly(principal_id=principal_id),
    role_id=role_id,
)
client.filesystem.Resource.Role.add(resource_rid, roles=[role], request_timeout=30)
def is_requested_grant(item):
    return (item.role_id == role_id and
            getattr(item.resource_role_principal, "principal_id", None) == principal_id)

# A grant to another principal with the same role must never satisfy this check.
other = SimpleNamespace(role_id=role_id, resource_role_principal=SimpleNamespace(principal_id="other"))
assert not is_requested_grant(other)

cursor = None
seen = set()
matched = None
for _ in range(10):
    # Each call fetches one page; read `.data` without iterating the SDK iterator.
    page = client.filesystem.Resource.Role.list(
        resource_rid, include_inherited=False, page_size=100,
        page_token=cursor, request_timeout=30,
    )
    matched = next((item for item in page.data if is_requested_grant(item)), None)
    if matched is not None:
        break
    following = page.next_page_token
    if following is None:
        break
    if following == cursor or following in seen:
        raise RuntimeError("Repeated role-list page token; grant remains unconfirmed")
    seen.add(following)
    cursor = following
if matched is None:
    raise LookupError("requested principal and role not confirmed within 10 pages")
```

Each call above fetches one page. The example inspects at most ten pages, even
if an empty page carries a continuation token. If it reaches that budget
without a match, the result is unconfirmed rather
than absent. `add` and `remove` return `None`, so verify by listing direct
roles. Before removing an assignment, match both principal and role in the
result; a role name alone is insufficient. Permission denial calls
for checking access to that resource and the exact principal, not changing the
target RID.
The [composed-client regression](../../../../examples/rest/073/v2/filesystem/resource_role_principal_check.py)
exercises a same-role grant to the wrong principal, an empty continuation page
and a repeated token with synthetic SDK transport.
