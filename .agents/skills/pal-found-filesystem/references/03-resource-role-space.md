# Resource role and space operations

This part documents the `resource_role` (3) and `space` (5) resource clients (8
operations total). Read the [Filesystem entry](SKILL.md) first.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/filesystem/scripts/pal_found_filesystem_cli.py`;
SDK `foundry_sdk/v2/filesystem/{resource_role,space}.py` at pinned commit
`2da67907`. Reviewer architect (CODEREVIEW-045), 2026-10-03. QA baseline
TESTCASE-007.

## Operation records

### resource_role.add

- **Class**: change. Assigns a role to a resource.
- **Preconditions**: can write the resource.
- **Effect**: grants the role on the resource to the principal/set.
- **Inputs**: positional `resource_rid`; `--role-grants` JSON.
- **Success**: returns the resource.
- **Example**: `pal-found-filesystem resource-role add <RESOURCE_RID> --role-grants '{"ri.principal.user.u1":["viewer"]}'`.

### resource_role.list

- **Class**: read. Lists roles on a resource.
- **Preconditions**: can read the resource.
- **Effect**: returns the resource's role grants, paged.
- **Inputs**: positional `resource_rid`; paging options.
- **Success**: role grants; empty if none.

### resource_role.remove

- **Class**: change. Removes a role from a resource.
- **Preconditions**: can write the resource.
- **Effect**: revokes the role grant.
- **Inputs**: positional `resource_rid`; `--role-grants` JSON.
- **Success**: returns the resource.

### space.create

- **Class**: create. Creates a space.
- **Preconditions**: write access to create spaces.
- **Effect**: creates a space and returns it.
- **Inputs**: `--display-name`, `--description`, `--file-system-id`; optional
  access/default-role fields (`--default-role-set-id`,
  `--resource-level-role-grants-allowed`).
- **Success**: the created space (RID).
- **Example**: `pal-found-filesystem space create --display-name "Sandbox" --file-system-id <FS_ID>`.

### space.delete

- **Class**: delete. Deletes a space.
- **Preconditions**: can delete the space.
- **Effect**: removes the space.
- **Inputs**: positional `space_rid`.
- **Success**: returns the deleted space.

### space.get

- **Class**: read. Returns a space.
- **Preconditions**: can read the space.
- **Effect**: returns the space record.
- **Inputs**: positional `space_rid`.
- **Success**: the space.
- **Failure**: exit 4 if missing.

### space.list

- **Class**: read. Lists spaces.
- **Preconditions**: can read spaces.
- **Effect**: returns spaces, paged.
- **Inputs**: paging options.
- **Success**: spaces; empty if none.

### space.replace

- **Class**: change. Replaces a space's definition.
- **Preconditions**: can write the space.
- **Effect**: replaces the space's config/default roles.
- **Inputs**: positional `space_rid`; replacement fields/body.
- **Success**: the updated space.

## Evidence and review

Reviewed against the installed `pal-found-filesystem` parser and pinned SDK
sources (commit `2da67907`). `space.delete` and marker writes are destructive
or change access immediately; `add`/`remove` role grants affect who can act on
a resource. No unsupported operation is documented as callable.
