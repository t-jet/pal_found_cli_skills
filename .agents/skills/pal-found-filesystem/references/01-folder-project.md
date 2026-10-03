# Folder and project operations

This part documents the `folder` (5) and `project` (7) resource clients (12
operations total). Read the [Filesystem entry](SKILL.md) first.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/filesystem/scripts/pal_found_filesystem_cli.py`;
SDK `foundry_sdk/v2/filesystem/{folder,project}.py` at pinned commit
`2da67907`. Reviewer architect (CODEREVIEW-045), 2026-10-03. QA baseline
TESTCASE-007.

## Workflow

1. Create a project (`project.create`) or from template
   (`project.create_from_template`).
2. Create folders inside it (`folder.create`).
3. Read folders and children (`folder.get`, `folder.children`), update
   (`folder.replace`).
4. Manage a project's organizations (`project.add_organizations`/
   `remove_organizations`).

## Operation records

### folder.children

- **Class**: read. Lists a folder's child resources.
- **Preconditions**: can read the folder.
- **Effect**: returns child resources, paged.
- **Inputs**: positional `resource_rid`; `--file-system-id`/`--paths`;
  paging options.
- **Success**: child resources; empty if none.
- **Example**: `pal-found-filesystem folder children <FOLDER_RID>`.

### folder.create

- **Class**: create. Creates a folder in a parent folder.
- **Preconditions**: can write the parent folder.
- **Effect**: creates the folder and returns it.
- **Inputs**: `--parent-folder-rid`, `--display-name`; optional `--path`
  and access fields.
- **Success**: the created folder (RID).
- **Failure**: exit 1 invalid input; exit 8 readonly block.
- **Example**: `pal-found-filesystem folder create --parent-folder-rid <PARENT_RID> --display-name "Raw"`.

### folder.get

- **Class**: read. Returns a folder by RID.
- **Preconditions**: can read the folder.
- **Effect**: returns the folder record.
- **Inputs**: positional `resource_rid`; optional `--file-system-id`/`--path`.
- **Success**: the folder record.
- **Failure**: exit 4 if missing.
- **Example**: `pal-found-filesystem folder get <FOLDER_RID>`.

### folder.get_batch

- **Class**: read. Returns several folders.
- **Preconditions**: can read each.
- **Effect**: returns a batch of folders.
- **Inputs**: positional JSON `body` list of resource RIDs.
- **Success**: list of folders.

### folder.replace

- **Class**: change. Replaces a folder's definition.
- **Preconditions**: can write the folder.
- **Effect**: replaces the folder's access/config; removed grants are dropped.
- **Inputs**: positional `resource_rid`; replacement JSON body/fields.
- **Success**: the updated folder.
- **Example**: `pal-found-filesystem folder replace <FOLDER_RID> --display-name "Raw Clean"`.

### project.add_organizations

- **Class**: change. Adds organizations to a project.
- **Preconditions**: can write the project.
- **Effect**: grants organizations access to the project.
- **Inputs**: positional `project_rid`; `--organization-rids` JSON list.
- **Success**: returns the project.
- **Example**: `pal-found-filesystem project add-organizations <PROJECT_RID> --organization-rids '["ri.org.main.org1"]'`.

### project.create

- **Class**: create. Creates a project.
- **Preconditions**: write access to create projects.
- **Effect**: creates the project and returns it.
- **Inputs**: `--enrollment-rid`, `--display-name`, `--project-description`;
  optional `--organization-rids`, `--default-roles`.
- **Success**: the created project (RID).
- **Example**: `pal-found-filesystem project create --enrollment-rid <ENROLLMENT_RID> --display-name "Analytics" --project-description "main analytics"`.

### project.create_from_template

- **Class**: create. Creates a project from a template.
- **Preconditions**: a template RID and enrollment write access.
- **Effect**: creates a project pre-populated from the template.
- **Inputs**: `--template-rid`, `--enrollment-rid`, `--display-name`;
  `--variable-values` JSON.
- **Success**: the created project.
- **Example**: `pal-found-filesystem project create-from-template --template-rid <TEMPLATE_RID> --enrollment-rid <ENR> --display-name "FromTpl" --variable-values '{}'`.

### project.get

- **Class**: read. Returns a project.
- **Preconditions**: can read the project.
- **Effect**: returns the project record.
- **Inputs**: positional `project_rid`.
- **Success**: the project.
- **Failure**: exit 4 if missing.
- **Example**: `pal-found-filesystem project get <PROJECT_RID>`.

### project.organizations

- **Class**: read. Lists a project's organizations.
- **Preconditions**: can read the project.
- **Effect**: returns organizations, paged.
- **Inputs**: positional `project_rid`; paging options.
- **Success**: organizations; empty if none.
- **Example**: `pal-found-filesystem project organizations <PROJECT_RID>`.

### project.remove_organizations

- **Class**: change. Removes organizations from a project.
- **Preconditions**: can write the project.
- **Effect**: revokes organizations' access.
- **Inputs**: positional `project_rid`; `--organization-rids` JSON list.
- **Success**: returns the project.

### project.replace

- **Class**: change. Replaces a project's definition.
- **Preconditions**: can write the project.
- **Effect**: replaces the project's organizations/description.
- **Inputs**: positional `project_rid`; replacement fields/body.
- **Success**: the updated project.

## Evidence and review

Reviewed against the installed `pal-found-filesystem` parser and pinned SDK
sources (commit `2da67907`). Writes (create/replace/add/remove
organizations) change project/folder access and are not reversible by the CLI.
`replace` drops grants not present in the new body. No unsupported operation
is documented as callable.
