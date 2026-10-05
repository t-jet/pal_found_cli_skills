# Resource operations

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

### resource.add_markings

- **Behavior:** Adds a list of Markings to a resource.
- **Before use:** The resource and marking IDs must exist; changing markings requires the applicable
  governance permissions.
- **Inputs:** positional `resource_rid`; required `--marking-ids`; optional none.
- **Result:** `None`.
- **Failure or follow-up:** Invalid identifiers or insufficient permission reject the change; read
  the resource afterward to verify its state.
- **Example:** `pal-found-filesystem resource add-markings RESOURCE_RID --marking-ids '["18212f9a-0e63-4b79-96a0-aae04df23336"]'`

### resource.delete

- **Behavior:** Move the given resource to the trash. Following this operation, the resource can be
  restored, using the `restore` operation, or permanently deleted using the `permanentlyDelete`
  operation.
- **Before use:** The resource must exist and the caller must have the required deletion or restore
  authority.
- **Inputs:** positional `resource_rid`; required none; optional none.
- **Result:** `None`.
- **Failure or follow-up:** A missing resource, invalid target, or insufficient permission rejects
  the removal. Confirm the resulting state with a read operation.
- **Example:** `pal-found-filesystem resource delete RESOURCE_RID`

### resource.get

- **Behavior:** Get the Resource with the specified rid.
- **Before use:** The resource or container must be accessible to the requesting identity.
- **Inputs:** positional `resource_rid`; required none; optional none.
- **Result:** `Resource`.
- **Failure or follow-up:** A missing or inaccessible resource returns an error, except where the
  SDK declares an optional result.
- **Example:** `pal-found-filesystem resource get RESOURCE_RID`

### resource.get_access_requirements

- **Behavior:** Returns a list of access requirements a user needs in order to view a resource.
  Access requirements are composed of Organizations and Markings, and can either be applied directly
  to the resource or inherited.
- **Before use:** The resource or container must be accessible to the requesting identity.
- **Inputs:** positional `resource_rid`; required none; optional none.
- **Result:** `AccessRequirements`.
- **Failure or follow-up:** Invalid input or insufficient access to the resource is returned through
  the CLI error envelope.
- **Example:** `pal-found-filesystem resource get-access-requirements RESOURCE_RID`

### resource.get_batch

- **Behavior:** Fetches multiple resources in a single request. Returns a map from RID to the
  corresponding resource. If a resource does not exist, or if it is a root folder or space, its RID
  will not be included in the map. At most 1,000 resources should be requested at once. The maximum
  batch size for this endpoint is 1000.
- **Before use:** The resource or container must be accessible to the requesting identity.
- **Inputs:** positional `body`; required none; optional none. `body`: Body of the request
- **Result:** `GetResourcesBatchResponse`.
- **Failure or follow-up:** Check the returned entries: batch endpoints may omit missing or
  inaccessible resources, so compare the result with requested RIDs.
- **Example:** `pal-found-filesystem resource get-batch '[{"resourceRid":"ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"}]'`

### resource.get_by_path

- **Behavior:** Get a Resource by its absolute path.
- **Before use:** The resource or container must be accessible to the requesting identity.
- **Inputs:** positional none; required `--path`; optional none. `path`: The path to the Resource.
  The leading slash is optional.
- **Result:** `Resource`.
- **Failure or follow-up:** A missing or inaccessible resource returns an error, except where the
  SDK declares an optional result.
- **Example:** `pal-found-filesystem resource get-by-path --path '/Example Project/Orders'`

### resource.get_by_path_batch

- **Behavior:** Gets multiple Resources by their absolute paths. Returns a list of resources. If a
  path does not exist, is inaccessible, or refers to a root folder or space, it will not be included
  in the response. At most 1,000 paths should be requested at once. The maximum batch size for this
  endpoint is 1000.
- **Before use:** The resource or container must be accessible to the requesting identity.
- **Inputs:** positional `body`; required none; optional none. `body`: Body of the request
- **Result:** `GetByPathResourcesBatchResponse`.
- **Failure or follow-up:** Check the returned entries: batch endpoints may omit missing or
  inaccessible resources, so compare the result with requested RIDs.
- **Example:** `pal-found-filesystem resource get-by-path-batch '[{"path":"/My Organization-abcd/My Important Project/My Dataset"}]'`

### resource.markings

- **Behavior:** List of Markings directly applied to a resource. The number of Markings on a
  resource is typically small so the `pageSize` and `pageToken` parameters are not required.
- **Before use:** The resource or container must be accessible to the requesting identity.
- **Inputs:** positional `resource_rid`; required none; optional none.
- **Result:** `ListMarkingsOfResourceResponse`.
- **Failure or follow-up:** An empty page is not proof there are no more results; follow the
  returned page token when present.
- **Example:** `pal-found-filesystem resource markings RESOURCE_RID`

### resource.permanently_delete

- **Behavior:** Permanently delete the given resource from the trash. If the Resource is not
  directly trashed, a `ResourceNotTrashed` error will be thrown.
- **Before use:** The resource must exist and the caller must have the required deletion or restore
  authority.
- **Inputs:** positional `resource_rid`; required none; optional none.
- **Result:** `None`.
- **Failure or follow-up:** A missing resource, invalid target, or insufficient permission rejects
  the removal. Confirm the resulting state with a read operation.
- **Example:** `pal-found-filesystem resource permanently-delete RESOURCE_RID`

### resource.remove_markings

- **Behavior:** Removes Markings from a resource.
- **Before use:** The resource and marking IDs must exist; changing markings requires the applicable
  governance permissions.
- **Inputs:** positional `resource_rid`; required `--marking-ids`; optional none.
- **Result:** `None`.
- **Failure or follow-up:** A missing resource, invalid target, or insufficient permission rejects
  the removal. Confirm the resulting state with a read operation.
- **Example:** `pal-found-filesystem resource remove-markings RESOURCE_RID --marking-ids '["18212f9a-0e63-4b79-96a0-aae04df23336"]'`

### resource.restore

- **Behavior:** Restore the given resource and any directly trashed ancestors from the trash. If the
  resource is not trashed, this operation will be ignored.
- **Before use:** The resource must exist and the caller must have the required deletion or restore
  authority.
- **Inputs:** positional `resource_rid`; required none; optional none.
- **Result:** `None`.
- **Failure or follow-up:** Invalid input or insufficient access to the resource is returned through
  the CLI error envelope.
- **Example:** `pal-found-filesystem resource restore RESOURCE_RID`
