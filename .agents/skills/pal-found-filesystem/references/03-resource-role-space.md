# Resource role and space operations

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

### resource_role.add

- **Behavior:** Grants the specified roles to principals on this resource. Each `roles` entry
  identifies a principal and a role ID; inherited project roles and mandatory access requirements
  still apply.
- **Before use:** The resource, principals, and role IDs must exist; changing grants requires
  permission on that resource.
- **Inputs:** positional `resource_rid`; required `--roles`; optional none.
- **Result:** `None`.
- **Failure or follow-up:** Invalid identifiers or insufficient permission reject the change; read
  the resource role afterward to verify its state.
- **Example:** `pal-found-filesystem resource-role add RESOURCE_RID --roles '[{"resourceRolePrincipal":{"type":"principalIdOnly","principalId":"f05f8da4-b84c-4fca-9c77-8af0b13d11de"},"roleId":"8bf49052-dc37-4528-8bf0-b551cfb71268"}]'`

### resource_role.list

- **Behavior:** Lists principal-to-role assignments on the resource. Add
  `--include-inherited` to include assignments inherited from its containers;
  without it, the response covers direct assignments.
- **Before use:** The resource or container must be accessible to the requesting identity.
- **Inputs:** positional `resource_rid`; required none; optional `--include-inherited`.
  `include_inherited`: Whether to include inherited roles on the resource.
- **Result:** `ListResourceRolesResponse`.
- **Failure or follow-up:** An empty page is not proof there are no more results; follow the
  returned page token when present.
- **Example:** `pal-found-filesystem resource-role list RESOURCE_RID`

### resource_role.remove

- **Behavior:** Removes the specified principal and role assignments from this resource. It does not
  remove roles inherited from a parent project.
- **Before use:** The resource, principals, and role IDs must exist; changing grants requires
  permission on that resource.
- **Inputs:** positional `resource_rid`; required `--roles`; optional none.
- **Result:** `None`.
- **Failure or follow-up:** A missing resource role, invalid target, or insufficient permission
  rejects the removal. Confirm the resulting state with a read operation.
- **Example:** `pal-found-filesystem resource-role remove RESOURCE_RID --roles '[{"resourceRolePrincipal":{"type":"principalIdOnly","principalId":"f05f8da4-b84c-4fca-9c77-8af0b13d11de"},"roleId":"8bf49052-dc37-4528-8bf0-b551cfb71268"}]'`

### space.create

- **Behavior:** Creates a space in an enrollment to contain projects. Its organization list sets
  space visibility. The deletion-policy organization list sets the Last Out policy: removing the
  last listed organization can delete the space and its projects.
- **Before use:** The enrollment and organizations must exist, and the caller must have
  space-management authority.
- **Inputs:** positional none; required `--deletion-policy-organizations`, `--display-name`,
  `--enrollment-rid`, `--organizations`; optional `--default-role-set-id`, `--description`,
  `--file-system-id`, `--preview`, `--usage-account-rid`. The organization list controls who can
  access the space. The deletion-policy list controls when the space and its projects are deleted
  after those organizations are removed; both lists must refer to the enrollment.
- **Parameter notes:** `--default-role-set-id` chooses the role set projects in the space must use; `--description` is space summary text; `--file-system-id` sets its filesystem identifier; `--usage-account-rid` associates a usage account; `--preview` opts into preview API behavior.
- **Result:** `Space`.
- **Failure or follow-up:** An invalid configuration or insufficient permission rejects space
  creation; use the returned RID for later calls.
- **Example:** `pal-found-filesystem space create --deletion-policy-organizations '["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"]' --display-name Orders --enrollment-rid ENROLLMENT_RID --organizations '["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"]'`

### space.delete

- **Behavior:** Delete the space. This will only work if the Space is empty, meaning any Projects or
  Resources have been deleted first.
- **Before use:** The space must be empty of projects and resources, and the caller needs
  permission to delete it.
- **Inputs:** positional `space_rid`; required none; optional `--preview`. `preview`: Enables the
  use of preview functionality.
- **Parameter notes:** `--preview` opts into preview API behavior when enabled for the enrollment.
- **Result:** `None`.
- **Failure or follow-up:** A missing space, invalid target, or insufficient permission rejects the
  removal. Confirm the resulting state with a read operation.
- **Example:** `pal-found-filesystem space delete SPACE_RID`

### space.get

- **Behavior:** Reads the space's metadata and organization scope by RID.
- **Before use:** The resource or container must be accessible to the requesting identity.
- **Inputs:** positional `space_rid`; required none; optional `--preview`. `preview`: Enables the
  use of preview functionality.
- **Parameter notes:** `--preview` opts into preview API behavior when enabled for the enrollment.
- **Result:** `Space`.
- **Failure or follow-up:** A missing or inaccessible space returns an error, except where the SDK
  declares an optional result.
- **Example:** `pal-found-filesystem space get SPACE_RID`

### space.list

- **Behavior:** Lists spaces visible to the caller in pages. A page can be shorter or longer than
  requested; continue with `nextPageToken` until it is absent.
- **Before use:** The resource or container must be accessible to the requesting identity.
- **Inputs:** positional none; required none; optional none.
- **Result:** `ListSpacesResponse`.
- **Failure or follow-up:** An empty page is not proof there are no more results; follow the
  returned page token when present.
- **Example:** `pal-found-filesystem space list`

### space.replace

- **Behavior:** Replaces the space's editable metadata, including its display name, description,
  default role set, or usage account. It does not move projects or alter their RIDs.
- **Before use:** The target container must exist where applicable and be writable under the project
  or space access rules.
- **Inputs:** positional `space_rid`; required `--display-name`; optional `--default-role-set-id`,
  `--description`, `--preview`, `--usage-account-rid`. `default_role_set_id`: The ID of the default
  Role Set for this Space, which defines the set of roles that Projects in this Space must use. If
  not provided, the default Role Set for Projects will be used. `description`: The description of
  the Space. `preview`: Enables the use of preview functionality.
- **Parameter notes:** `--default-role-set-id` chooses the role set for projects in the space; `--description` changes space summary text; `--usage-account-rid` changes its usage account; `--preview` opts into preview API behavior.
- **Result:** `Space`.
- **Failure or follow-up:** An invalid replacement payload or insufficient permission leaves the
  space unchanged; read it again after success.
- **Example:** `pal-found-filesystem space replace SPACE_RID --display-name Orders`
