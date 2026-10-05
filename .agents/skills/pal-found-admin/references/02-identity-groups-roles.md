# Identity: groups and roles

Groups gather principals so access can be granted consistently. Group membership can convey roles, while expiration policy limits its lifetime. A role is a set of permissions, and mandatory organization and marking requirements still apply. See [users and groups](https://www.palantir.com/docs/foundry/security/users-and-groups) and [projects and roles](https://www.palantir.com/docs/foundry/security/projects-and-roles). Examples follow SDK `docs/v2/Admin` and the Admin CLI parser. Replace sample identifiers before running.

## Operation records

### group.create

Create a group that can receive grants on behalf of its members. `--name` is its display name, and optional `--description` explains its purpose. `--organizations` names the organizations whose members can see the group; at least one is required. `--attributes` supplies its structured attributes. Names starting with `multipass:` are reserved for Foundry, so use ordinary names for custom attributes. The returned group ID is the value to use in membership and role assignment commands.

Required input: `--attributes`, `--name`, `--organizations`. Optional: `--description`. The SDK returns `Group` on success. This changes identity or access state. Read the affected resource afterward to verify the intended result.  Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin group create --attributes '{"department":["Finance"]}' --name 'Finance Analysts' --organizations '["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"]' --description 'Analysts with access to finance reports'`

### group.delete

Delete the group identified by `group_id`. A group can be a member of another group and can receive roles, so inspect its direct members and access assignments before deleting it. This CLI has no undo operation for group deletion.

Required input: `group_id`. Success is HTTP 204 with no resource body. A later `group get` can check whether the ID still resolves; it cannot recover the deleted group. An unknown group, insufficient permission, or CLI access policy can reject deletion.

**Example:** `pal-found-admin group delete 0950264e-01c8-4e83-81a9-1a6b7f77621a`

### group.get

Read a group by principal ID before changing its members or replacing its attributes. The response includes its name, organizations, and attributes. A group can contain users or other groups; use `group-member list` to inspect membership.

Required input: `group_id`. The SDK returns `Group` on success. The operation does not change Foundry state.  An unknown ID or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin group get 0950264e-01c8-4e83-81a9-1a6b7f77621a`

### group.get_batch

Resolve up to 500 group IDs in one batch, for example IDs found in role assignments. The positional `body` is a JSON array of `groupId` requests. Compare response IDs against the requested IDs before using the result as a complete inventory.

Required input: `body`. The SDK returns `GetGroupsBatchResponse` on success. The operation does not change Foundry state. Compare returned IDs with requested IDs; some endpoints omit unknown or inaccessible records. The endpoint accepts at most 500 group IDs. An unknown ID or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin group get-batch '[{"groupId":"0d1fe74e-2b70-4a93-9b1a-80070637788b"}]'`

### group.list

List groups visible to the caller to discover IDs for membership or role operations. Results are paged; a page can be shorter or longer than requested. Continue with the returned `nextPageToken` until it is absent.

Required input: no required operation arguments. The SDK returns `ListGroupsResponse` on success. The operation does not change Foundry state. An empty response means no visible matches; page forward when a continuation token is returned.  Authentication or permission errors stop the read; an empty visible result is not an API failure.

**Example:** `pal-found-admin group list`

### group.list_current

List groups containing the authenticated user, directly or through nested groups. If the user belongs to A and A belongs to B, both appear. Unlike `group-membership list` for an arbitrary user, this self-service call does not require `api:admin-read` scope.

Required input: no required operation arguments. The SDK returns `ListCurrentGroupsResponse` on success. The operation does not change Foundry state. Direct and transitive groups are included, so nested group access appears in the response. Authentication or permission errors stop the read; an empty visible result is not an API failure.

**Example:** `pal-found-admin group list-current`

### group.replace

Replace a group's `--name` (display name), `--organizations` (organization RIDs whose members can see it), optional `--description` (purpose), and `--attributes` (value arrays keyed by attribute name). This is a full replacement: first run `group get`, then carry every existing `multipass:` attribute into `--attributes` exactly as returned. Omitting one can break its identity-provider linkage or other managed identity information.

Required input: `group_id`, `--attributes`, `--name`, `--organizations`. Optional: `--description`. The SDK returns `Group` on success. This changes identity or access state. Read the affected resource afterward to verify the intended result. Send every existing `multipass:` attribute exactly as returned by `group.get`; dropping one is not a safe partial update. Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin group replace 0950264e-01c8-4e83-81a9-1a6b7f77621a --attributes '{"department":["Finance"]}' --name 'Finance Analysts' --organizations '["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"]' --description 'Finance reporting team'`

### group.search

Find groups by a case-insensitive prefix of their name. Supply the query-string filter through `--where`; search helps resolve a group name before changing membership, while `group list` is appropriate for inventory. A search for `Data` can match names beginning with `Data`, not arbitrary substrings.

Required input: `--where`. The SDK returns `SearchGroupsResponse` on success. The operation does not change Foundry state. An empty response means no visible matches; page forward when a continuation token is returned. The API performs a case-insensitive prefix search on group name. Authentication or permission errors stop the read; an empty visible result is not an API failure.

**Example:** `pal-found-admin group search --where '{"type":"queryString","value":"Data"}'`

### group_member.add

Add one or more user or group principals to a group. `--principal-ids` is their JSON array of IDs; `--expiration` sets an absolute expiry timestamp for temporary membership. Membership can convey access granted to the group, and nested group membership can affect transitive access. Confirm the target group and principal IDs before adding them.

Required input: `group_id`, `--principal-ids` as a JSON array. Optional: `--expiration`, an absolute timestamp for temporary membership. Success is HTTP 204 with no resource body. A group expiration policy may require a limit on new memberships. Run `group-member list` on the group to verify direct membership, or `group-membership list <USER_ID> --transitive` to inspect inherited membership. Unknown principals, invalid expiration, policy violations, or insufficient permission can reject the addition.

**Example:** `pal-found-admin group-member add 0950264e-01c8-4e83-81a9-1a6b7f77621a --principal-ids '["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]'`

### group_member.list

List user or group principals inheriting the group's grants. `--include-expirations` adds direct members' expiry times; `--transitive` follows nested groups. The flags cannot both be true. Results are paged; pass returned `nextPageToken` as `--page-token` to continue, even if the current page is short.

Required input: `group_id`. `--include-expirations` shows expiration times for temporary direct members. `--transitive` includes members inherited through nested groups. These flags are mutually exclusive when true; choose one view per request. The SDK returns `ListGroupMembersResponse` without changing membership. An empty response means no visible matches; continue with `--page-token` when a token is returned. Authentication or permission errors stop the read.

**Example:** `pal-found-admin group-member list 0950264e-01c8-4e83-81a9-1a6b7f77621a --include-expirations --page-size 50`

### group_member.remove

Remove direct membership edges for the user or group IDs in the `--principal-ids` JSON array. A user may still inherit the group through another nested path or retain access through a separate grant. Check all relevant paths before treating this as a full access revocation.

Required input: `group_id`, `--principal-ids` as a JSON array. Success is HTTP 204 with no resource body. Run `group-member list` to verify direct removal; use `group-membership list <USER_ID> --transitive` when nested groups may still confer membership. An unknown group or principal, insufficient permission, or CLI access policy can reject removal.

**Example:** `pal-found-admin group-member remove 0950264e-01c8-4e83-81a9-1a6b7f77621a --principal-ids '["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]'`

### group_membership.list

List groups containing a given user to explain access inherited through group grants. By default, only direct memberships appear; `--transitive` also follows nested groups. Results are paged; continue with returned `nextPageToken` even if the current page is short.

Required input: `user_id`. By default, the response lists direct group memberships. `--transitive` also follows nested groups: if the user is in A and A is in B, both A and B appear. The SDK returns `ListGroupMembershipsResponse` without changing membership. An empty response means no visible matches; page forward when a continuation token is returned. Authentication or permission errors stop the read.

**Example:** `pal-found-admin group-membership list f05f8da4-b84c-4fca-9c77-8af0b13d11de`

### group_membership_expiration_policy.get

Read the group's membership expiration policy before adding temporary members. `maximum_duration` limits how far into the future an expiration may be, in seconds from the time a member is added. `maximum_value` is an absolute latest expiration timestamp. These are constraints on additions to the group, not expiration dates assigned by this read.

Required input: `group_id`. The SDK returns `GroupMembershipExpirationPolicy` without changing the group. An unknown group or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin group-membership-expiration-policy get 0950264e-01c8-4e83-81a9-1a6b7f77621a`

### group_membership_expiration_policy.replace

Replace the policy that limits future group membership expirations. `--maximum-duration` is a number of seconds measured from each new member's addition; `--maximum-value` is an absolute latest expiration timestamp. New member expirations must satisfy the configured limits. For example, 86400 seconds limits a temporary addition to less than one day into the future. Read the current policy first so the requested replacement keeps every limit you intend.

Required input: `group_id`; optional limits are `--maximum-duration` and `--maximum-value`. The SDK returns the updated `GroupMembershipExpirationPolicy`. Confirm it with `get` before adding members. An invalid duration or timestamp, unknown group, or insufficient permission can reject the change.

**Example:** `pal-found-admin group-membership-expiration-policy replace 0950264e-01c8-4e83-81a9-1a6b7f77621a --maximum-duration 86400 --maximum-value 2027-01-31T00:00:00.000Z`

### group_provider_info.get

Read the external identity-provider ID associated with a Foundry group. Use the mapping when reconciling a group returned by Foundry with the corresponding group in the external directory; `group get` supplies its Foundry-facing details.

Required input: `group_id`. The SDK returns `GroupProviderInfo`, including the ID used by the external authentication provider, without changing the mapping. An unknown group or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin group-provider-info get 0950264e-01c8-4e83-81a9-1a6b7f77621a`

### group_provider_info.replace

Change the external provider ID mapped to this Foundry group. Supply the provider's stable group ID through `--provider-id`, then read the mapping back before relying on synchronization.

Required input: `group_id` and `--provider-id`, the group's ID in the external authentication provider. The SDK returns the updated `GroupProviderInfo`. A provider ID can identify at most one group in a realm; a duplicate mapping or insufficient permission can reject the replacement. Read the mapping afterward to verify it.

**Example:** `pal-found-admin group-provider-info replace 0950264e-01c8-4e83-81a9-1a6b7f77621a --provider-id external-id-123`

### role.get

Read a role by ID to inspect the permissions it groups before assigning that role at enrollment or organization scope. A role definition does not say which principals have it; use the corresponding role-assignment list for that.

Required input: `role_id`. The SDK returns `Role` on success. The operation does not change Foundry state.  An unknown ID or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin role get 8bf49052-dc37-4528-8bf0-b551cfb71268`

### role.get_batch

Resolve multiple role IDs in a single request, such as those in an assignment list. The positional `body` is a JSON array of `roleId` requests; compare returned IDs with the input before treating the lookup as complete.

Required input: `body`. The SDK returns `GetRolesBatchResponse` on success. The operation does not change Foundry state. Compare returned IDs with requested IDs; some endpoints omit unknown or inaccessible records.  An unknown ID or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin role get-batch '[{"roleId":"8bf49052-dc37-4528-8bf0-b551cfb71268"}]'`
