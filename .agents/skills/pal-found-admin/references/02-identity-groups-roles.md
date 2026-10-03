# Admin identity: groups, memberships, and roles

This part documents the Admin identity operations for groups, group members
and memberships, expiration policies, provider info, and roles (23
operations). Read the general [identifiers, auth, and access
control](../pal-found/references/02-identifiers-auth-access.md) part first if
you are new to Admin.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/admin/scripts/pal_found_admin_cli.py`;
SDK `foundry_sdk/v2/admin/{group,group_member,group_membership,group_membership_expiration_policy,group_provider_info,role}.py`
at pinned commit `2da67907`. Reviewer architect (CODEREVIEW-042), 2026-10-03.
QA baseline TESTCASE-009.

## Workflow

1. List/read groups (`group.list`, `group.get`) to find the group by name or
   RID.
2. Create groups (`group.create`) and manage their members
   (`group_member.add`/`list`/`remove`, `group_membership.list`).
3. Set membership expiration policy (`group_membership_expiration_policy.replace`)
   where required.
4. Assign roles to groups (`group`/`role` and membership semantics) and read
   roles (`role.get`, `role.get_batch`).

## Common rules

All commands accept `--timeout`, `--format json|toon|auto`, `--pretty`.
Get-batch commands take a positional JSON `body`. Deletes/removes are
destructive: a zero exit means the change was accepted; confirm with a follow
up `get`/`list` when the platform may propagate late.

## Operation records

### group.create

- **Class**: create. Creates a new group.
- **Preconditions**: write access to create groups in the enrollment.
- **Effect**: creates a group and returns it.
- **Inputs**: required name and organization/attributes; `--attributes`,
  `--organizations` (JSON) and scalar `--name`/`--description` where shown.
- **Success**: the created group, including its RID.
- **Failure**: exit 1 invalid input (duplicate name, missing principal);
  exit 3 permission; exit 8 readonly block.
- **Example**: `pal-found-admin group create --name "Data Engineers"`.

### group.delete

- **Class**: delete. Deletes a group.
- **Preconditions**: write access; confirm no dependent memberships/grants.
- **Effect**: permanently deletes the group.
- **Inputs**: positional `group_rid`.
- **Success**: returns the deleted group.
- **Failure**: exit 4 if group not found; exit 3 permission.
- **Example**: `pal-found-admin group delete <GROUP_RID>`.

### group.get

- **Class**: read. Returns a single group.
- **Preconditions**: read access.
- **Effect**: returns the group.
- **Inputs**: positional `group_rid`.
- **Success**: the group record.
- **Failure**: exit 4 if RID wrong.
- **Example**: `pal-found-admin group get <GROUP_RID>`.

### group.get_batch

- **Class**: read. Returns several groups.
- **Preconditions**: read on each group.
- **Effect**: returns a batch of groups.
- **Inputs**: positional JSON `body` list of group RIDs.
- **Success**: list of group records.
- **Failure**: exit 1 malformed body.
- **Example**: `pal-found-admin group get-batch --body '["g1","g2"]'`.

### group.list

- **Class**: read. Lists groups.
- **Preconditions**: read access.
- **Effect**: returns a page of groups.
- **Inputs**: paging options.
- **Success**: list; empty if none visible.
- **Example**: `pal-found-admin group list --page-size 100`.

### group.list_current

- **Class**: read. Lists groups that the current user belongs to.
- **Preconditions**: a valid token.
- **Effect**: returns the caller's groups.
- **Inputs**: paging options.
- **Success**: list of the caller's groups.
- **Example**: `pal-found-admin group list-current`.

### group.replace

- **Class**: change. Replaces a group's definition.
- **Preconditions**: write access.
- **Effect**: replaces the group's attributes/organizations; result reflects
  the new definition.
- **Inputs**: positional `group_rid`; replacement JSON fields.
- **Success**: the updated group.
- **Example**: `pal-found-admin group replace <GROUP_RID> --name "New Name"`.

### group.search

- **Class**: read. Searches groups by query.
- **Preconditions**: read access.
- **Effect**: returns matching groups.
- **Inputs**: `--where`/query and paging.
- **Success**: matches; empty if none.
- **Example**: `pal-found-admin group search --query 'engineering'`.

### group_member.add

- **Class**: change. Adds a member to a group.
- **Preconditions**: write access on the group and the principal.
- **Effect**: adds the principal to the group.
- **Inputs**: positional `group_rid`; `--principal-ids` or `--members`.
- **Success**: returns the group with the added member.
- **Example**: `pal-found-admin group-member add <GROUP_RID> --principal-ids '["ri.principal.user.u1"]'`.

### group_member.list

- **Class**: read. Lists a group's members.
- **Preconditions**: read access on the group.
- **Effect**: returns group members, paged.
- **Inputs**: positional `group_rid`; paging.
- **Success**: members; empty if none.
- **Example**: `pal-found-admin group-member list <GROUP_RID>`.

### group_member.remove

- **Class**: change. Removes a member from a group.
- **Preconditions**: write access.
- **Effect**: removes the principal.
- **Inputs**: positional `group_rid`; principal identifier.
- **Success**: returns the group after removal.
- **Example**: `pal-found-admin group-member remove <GROUP_RID> --principal-id <PID>`.

### group_membership.list

- **Class**: read. Lists the memberships of a principal.
- **Preconditions**: read access.
- **Effect**: returns memberships, paged.
- **Inputs**: positional principal id; paging.
- **Success**: memberships; empty means no memberships.
- **Example**: `pal-found-admin group-membership list <PID>`.

### group_membership_expiration_policy.get

- **Class**: read. Returns the membership expiration policy.
- **Preconditions**: read access.
- **Effect**: returns whether/for how long memberships expire.
- **Inputs**: positional `group_rid`.
- **Success**: the expiration policy.
- **Example**: `pal-found-admin group-membership-expiration-policy get <GROUP_RID>`.

### group_membership_expiration_policy.replace

- **Class**: change. Sets the membership expiration policy.
- **Preconditions**: write access.
- **Effect**: replaces the expiration policy; `--maximum-duration` bounds how
  long a membership lasts.
- **Inputs**: positional `group_rid`; `--maximum-duration`/`--maximum-value`.
- **Success**: the updated policy.
- **Example**: `pal-found-admin group-membership-expiration-policy replace <GROUP_RID> --maximum-duration 90d`.

### group_provider_info.get

- **Class**: read. Returns a group's provider info.
- **Preconditions**: read access.
- **Effect**: returns provider-scoped group identity.
- **Inputs**: positional `group_rid`.

### group_provider_info.replace

- **Class**: change. Replaces a group's provider info.
- **Preconditions**: write access.
- **Effect**: replaces provider identity mapping.
- **Inputs**: positional `group_rid`; provider fields.

### role.get

- **Class**: read. Returns a single role.
- **Preconditions**: read access.
- **Effect**: returns the role.
- **Inputs**: positional `role_rid`.
- **Success**: the role record.
- **Example**: `pal-found-admin role get <ROLE_RID>`.

### role.get_batch

- **Class**: read. Returns several roles.
- **Preconditions**: read access.
- **Effect**: returns a batch of roles.
- **Inputs**: positional JSON `body` list of role RIDs.
- **Success**: list of roles.
- **Example**: `pal-found-admin role get-batch --body '["r1","r2"]'`.

## Evidence and review

Each record was reviewed against the installed `pal-found-admin`
parser/dispatch and pinned SDK sources (commit `2da67907`). Read-class
operations never write; create/delete/replace/remove class operations write
and may be destructive. No unsupported operation is documented as callable.
