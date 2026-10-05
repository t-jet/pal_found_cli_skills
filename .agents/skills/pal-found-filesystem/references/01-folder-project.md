# Folder and project operations

Projects group resources for collaboration and are the main boundary for discretionary role grants.
Folders organize resources within projects; resource RIDs identify them independently of their
paths. Spaces contain projects and limit their organization scope. Resource markings and
organization requirements are mandatory access controls, so a project role alone may not grant
access.

Platform context: [Palantir
documentation](https://www.palantir.com/docs/foundry/getting-started/projects-and-resources). The
behavior below describes the installed CLI commands.
parser. Replace example identifiers and configuration values with values from your Foundry
enrollment.

## Operation records

### folder.children

- **Behavior:** List all child Resources of the Folder. This is a paged endpoint. The page size will
  be limited to 2,000 results per page. If no page size is provided, this page size will also be
  used as the default.
- **Before use:** The resource or container must be accessible to the requesting identity.
- **Inputs:** positional `folder_rid`; required none; optional none.
- **Result:** `ListChildrenOfFolderResponse`.
- **Failure or follow-up:** An empty page is not proof there are no more results; follow the
  returned page token when present.
- **Example:** `pal-found-filesystem folder children FOLDER_RID`

### folder.create

- **Behavior:** Creates a new Folder.
- **Before use:** Choose a writable parent folder in an accessible project.
- **Inputs:** positional none; required `--display-name`, `--parent-folder-rid`; optional none.
  `parent_folder_rid`: The parent folder Resource Identifier (RID). For Projects, this will be the
  Space RID and for Spaces, this value will be the root folder (`ri.compass.main.folder.0`).
- **Result:** `Folder`.
- **Failure or follow-up:** An invalid configuration or insufficient permission rejects folder
  creation; use the returned RID for later calls.
- **Example:** `pal-found-filesystem folder create --display-name Orders --parent-folder-rid PARENT_FOLDER_RID`

### folder.get

- **Behavior:** Get the Folder with the specified rid.
- **Before use:** The resource or container must be accessible to the requesting identity.
- **Inputs:** positional `folder_rid`; required none; optional none.
- **Result:** `Folder`.
- **Failure or follow-up:** A missing or inaccessible folder returns an error, except where the SDK
  declares an optional result.
- **Example:** `pal-found-filesystem folder get FOLDER_RID`

### folder.get_batch

- **Behavior:** Fetches multiple folders in a single request. The maximum batch size for this
  endpoint is 1000.
- **Before use:** The resource or container must be accessible to the requesting identity.
- **Inputs:** positional `body`; required none; optional none. `body`: Body of the request
- **Result:** `GetFoldersBatchResponse`.
- **Failure or follow-up:** Check the returned entries: batch endpoints may omit missing or
  inaccessible resources, so compare the result with requested RIDs.
- **Example:** `pal-found-filesystem folder get-batch '[{"folderRid":"ri.compass.main.folder.01a79a9d-e293-48db-a585-9ffe221536e8"}]'`

### folder.replace

- **Behavior:** Replace the Folder with the specified rid.
- **Before use:** The target container must exist where applicable and be writable under the project
  or space access rules.
- **Inputs:** positional `folder_rid`; required `--display-name`, `--parent-folder-rid`; optional
  `--preview`. `parent_folder_rid`: The parent folder Resource Identifier (RID). For Projects, this
  will be the Space RID and for Spaces, this value will be the root folder
  (`ri.compass.main.folder.0`). `preview`: Enables the use of preview functionality.
- **Parameter notes:** `--preview` opts into the preview API behavior when enabled for the enrollment.
- **Result:** `Folder`.
- **Failure or follow-up:** An invalid replacement payload or insufficient permission leaves the
  folder unchanged; read it again after success.
- **Example:** `pal-found-filesystem folder replace FOLDER_RID --display-name Orders --parent-folder-rid PARENT_FOLDER_RID`

### project.add_organizations

- **Behavior:** Adds a list of Organizations to a Project.
- **Before use:** The target container must exist where applicable and be writable under the project
  or space access rules.
- **Inputs:** positional `project_rid`; required `--organization-rids`; optional none.
- **Result:** `None`.
- **Failure or follow-up:** Invalid identifiers or insufficient permission reject the change; read
  the project afterward to verify its state.
- **Example:** `pal-found-filesystem project add-organizations PROJECT_RID --organization-rids '["ORGANIZATION_RID"]'`

### project.create

- **Behavior:** Creates a new Project. Note that third-party applications using this endpoint via
  OAuth2 cannot be associated with an Ontology SDK as this will reduce the scope of operations to
  only those within specified projects. When creating the application, select "No, I won't use an
  Ontology SDK" on the Resources page.
- **Before use:** Choose a space where you can create projects, organization scope, and initial role
  grants.
- **Inputs:** positional none; required `--default-roles`, `--display-name`, `--organization-rids`,
  `--role-grants`, `--space-rid`; optional `--description`, `--resource-level-role-grants-allowed`.
  `resource_level_role_grants_allowed`: Whether role grants should be allowed on individual
  resources within the Project. When not specified, defaults to true.
- **Parameter notes:** `--description` stores project summary text. `--resource-level-role-grants-allowed` controls whether individual resources in the project can have role grants; its default is true.
- **Result:** `Project`.
- **Failure or follow-up:** An invalid configuration or insufficient permission rejects project
  creation; use the returned RID for later calls.
- **Example:** `pal-found-filesystem project create --default-roles '["8bf49052-dc37-4528-8bf0-b551cfb71268"]' --display-name Orders --organization-rids '["ORGANIZATION_RID"]' --role-grants '{"8bf49052-dc37-4528-8bf0-b551cfb71268":[{"principalId":"f05f8da4-b84c-4fca-9c77-8af0b13d11de","principalType":"GROUP"}]}' --space-rid SPACE_RID`

### project.create_from_template

- **Behavior:** Creates a project from a project template.
- **Before use:** The template must be accessible; provide its required variable values and
  permissions for the destination.
- **Inputs:** positional none; required `--template-rid`, `--variable-values`; optional
  `--default-roles`, `--organization-rids`, `--project-description`.
- **Parameter notes:** `--default-roles` supplies initial project role IDs, `--organization-rids` selects the project organization scope, and `--project-description` sets its description.
- **Result:** `Project`.
- **Failure or follow-up:** Invalid input or insufficient access to the project is returned through
  the CLI error envelope.
- **Example:** `pal-found-filesystem project create-from-template --template-rid TEMPLATE_RID --variable-values '{"name":"my project name"}'`

### project.get

- **Behavior:** Get the Project with the specified rid.
- **Before use:** The resource or container must be accessible to the requesting identity.
- **Inputs:** positional `project_rid`; required none; optional none.
- **Result:** `Project`.
- **Failure or follow-up:** A missing or inaccessible project returns an error, except where the SDK
  declares an optional result.
- **Example:** `pal-found-filesystem project get PROJECT_RID`

### project.organizations

- **Behavior:** List of Organizations directly applied to a Project. The number of Organizations on
  a Project is typically small so the `pageSize` and `pageToken` parameters are not required.
- **Before use:** The resource or container must be accessible to the requesting identity.
- **Inputs:** positional `project_rid`; required none; optional none.
- **Result:** `ListOrganizationsOfProjectResponse`.
- **Failure or follow-up:** An empty page is not proof there are no more results; follow the
  returned page token when present.
- **Example:** `pal-found-filesystem project organizations PROJECT_RID`

### project.remove_organizations

- **Behavior:** Removes Organizations from a Project.
- **Before use:** The target container must exist where applicable and be writable under the project
  or space access rules.
- **Inputs:** positional `project_rid`; required `--organization-rids`; optional none.
- **Result:** `None`.
- **Failure or follow-up:** A missing project, invalid target, or insufficient permission rejects
  the removal. Confirm the resulting state with a read operation.
- **Example:** `pal-found-filesystem project remove-organizations PROJECT_RID --organization-rids '["ORGANIZATION_RID"]'`

### project.replace

- **Behavior:** Replace the Project with the specified rid.
- **Before use:** The target container must exist where applicable and be writable under the project
  or space access rules.
- **Inputs:** positional `project_rid`; required `--display-name`; optional `--description`,
  `--preview`. `display_name`: The display name of the Project. Must be unique and cannot contain a
  / `description`: The description associated with the Project. `preview`: Enables the use of
  preview functionality.
- **Parameter notes:** `--description` sets project summary text; `--preview` opts into preview API behavior when enabled.
- **Result:** `Project`.
- **Failure or follow-up:** An invalid replacement payload or insufficient permission leaves the
  project unchanged; read it again after success.
- **Example:** `pal-found-filesystem project replace PROJECT_RID --display-name Orders`
