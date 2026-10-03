# Resource operations

This part documents the `resource` resource client (11 operations). A resource
is the roll-up category in Filesystem that includes projects, folders,
datasets, and documents. Read the [Filesystem entry](SKILL.md) first.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/filesystem/scripts/pal_found_filesystem_cli.py`;
SDK `foundry_sdk/v2/filesystem/resource.py` at pinned commit `2da67907`.
Reviewer architect (CODEREVIEW-045), 2026-10-03. QA baseline TESTCASE-007.

## Operation records

### resource.add_markings

- **Class**: change. Adds markings to a resource.
- **Preconditions**: can write the resource and apply the markings.
- **Effect**: classifies the resource with additional markings (access).
- **Inputs**: positional `resource_rid`; `--marking-ids` JSON list.
- **Success**: returns the resource.
- **Example**: `pal-found-filesystem resource add-markings <RESOURCE_RID> --marking-ids '["marking.PHI"]'`.

### resource.delete

- **Class**: delete. Deletes a resource to the trash (soft delete).
- **Preconditions**: can delete the resource.
- **Effect**: moves the resource to trash; it can be restored with `resource.restore`.
- **Inputs**: positional `resource_rid`; `--file-system-id`/`--path`.
- **Success**: returns the deleted resource; not a permanent erase.
- **Example**: `pal-found-filesystem resource delete <RESOURCE_RID>`.

### resource.get

- **Class**: read. Returns a resource by RID.
- **Preconditions**: can read the resource.
- **Effect**: returns the resource record.
- **Inputs**: positional `resource_rid`; optional `--file-system-id`/`--path`.
- **Success**: the resource record.
- **Failure**: exit 4 if missing.
- **Example**: `pal-found-filesystem resource get <RESOURCE_RID>`.

### resource.get_access_requirements

- **Class**: read. Returns the access/entitlement requirements for a resource.
- **Preconditions**: can read the resource.
- **Effect**: returns what is required to access the resource.
- **Inputs**: positional `resource_rid`.
- **Success**: access requirements.

### resource.get_batch

- **Class**: read. Returns several resources.
- **Preconditions**: can read each.
- **Effect**: returns a batch of resources.
- **Inputs**: positional JSON `body` list of RIDs.
- **Success**: list of resources.

### resource.get_by_path

- **Class**: read. Returns a resource by its path (and file system id).
- **Preconditions**: can read the resource.
- **Effect**: returns the resource at the path, distinct from `get` (which uses
  RID).
- **Inputs**: `--path`, `--file-system-id`.
- **Success**: the resource; exit 4 if no resource at the path.
- **Failure**: exit 4 not found at path.
- **Example**: `pal-found-filesystem resource get-by-path --path /project/folder --file-system-id <FS_ID>`.

### resource.get_by_path_batch

- **Class**: read. Returns several resources by paths.
- **Preconditions**: can read each.
- **Effect**: returns resources for the requested paths.
- **Inputs**: `--path`/`--paths` JSON; `--file-system-id`.
- **Success**: list of resources.

### resource.markings

- **Class**: read. Lists a resource's markings.
- **Preconditions**: can read the resource.
- **Effect**: returns markings, paged.
- **Inputs**: positional `resource_rid`; paging options.
- **Success**: markings; empty if none.

### resource.permanently_delete

- **Class**: delete (destructive). Permanently erases a resource.
- **Preconditions**: can permanently delete; confirm the resource is intended
  for permanent removal (no `restore` recovery).
- **Effect**: permanently deletes the resource.
- **Inputs**: positional `resource_rid`.
- **Success**: returns the deleted resource.
- **Failure**: exit 8 readonly block; exit 3 permission.
- **Example**: `pal-found-filesystem resource permanently-delete <RESOURCE_RID>`.

### resource.remove_markings

- **Class**: change. Removes markings from a resource.
- **Preconditions**: can write the resource.
- **Effect**: removes the markings (access classification).
- **Inputs**: positional `resource_rid`; `--marking-ids` JSON list.
- **Success**: returns the resource.

### resource.restore

- **Class**: change. Restores a soft-deleted resource.
- **Preconditions**: can restore; the resource is in trash.
- **Effect**: moves the resource back from trash.
- **Inputs**: positional `resource_rid`.
- **Success**: returns the restored resource.
- **Example**: `pal-found-filesystem resource restore <RESOURCE_RID>`.

## Evidence and review

Reviewed against the installed `pal-found-filesystem` parser and pinned SDK
sources (commit `2da67907`). `permanently_delete` is destructive and flagged
before invocation; `delete` is soft (restorable); markings writes change
access. A zero exit means the CLI request completed, not that a permanent
erase is always recovered elsewhere. No unsupported operation is documented as
callable.
