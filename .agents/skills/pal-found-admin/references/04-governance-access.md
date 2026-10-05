# Governance: membership and organization access

Marking membership determines who satisfies a marking requirement. Marking roles determine who can administer it. Organizations form mandatory boundaries around users and work; guests can access another organization when configured. See [organizations and spaces](https://www.palantir.com/docs/foundry/security/orgs-and-spaces) and [access control propagation](https://www.palantir.com/docs/foundry/security/access-control-propagation). Examples use the installed Admin CLI. Replace sample identifiers before running.

## Operation records

### marking_member.add

Add user or group principals named by the `--principal-ids` JSON array to a marking's member set. Membership lets those principals satisfy this marking requirement on protected resources, but other requirements and role grants still apply. The request changes access for every resource carrying the marking; inspect the marking and principal IDs before applying it.

Required input: `marking_id`, `--principal-ids`. The SDK returns no resource body after success. This changes identity or access state. Read the affected resource afterward to verify the intended result.  Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin marking-member add 0950264e-01c8-4e83-81a9-1a6b7f77621a --principal-ids '["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]'`

### marking_member.list

List principals able to satisfy the specified marking requirement. `--transitive` includes access inherited through group membership. The API ignores `pageSize` and requires `api:admin-write` because marking membership is visible only to marking administrators. Membership alone does not override other access controls.

Required input: `marking_id`. Optional: `--transitive`. The SDK returns `ListMarkingMembersResponse` on success. The operation does not change Foundry state. An empty response means no visible matches; page forward when a continuation token is returned.  Authentication or permission errors stop the read; an empty visible result is not an API failure.

**Example:** `pal-found-admin marking-member list 0950264e-01c8-4e83-81a9-1a6b7f77621a`

### marking_member.remove

Remove user or group principals named by the `--principal-ids` JSON array from a marking's direct member set. This can revoke access to resources bearing the marking, although another group path or grant may still provide membership. List members after removal and check transitive membership if nested groups are involved.

Required input: `marking_id`, `--principal-ids`. The SDK returns no resource body after success. This changes identity or access state. Read the affected resource afterward to verify the intended result.  Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin marking-member remove 0950264e-01c8-4e83-81a9-1a6b7f77621a --principal-ids '["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]'`

### marking_role_assignment.add

Assign marking roles to principals. `--role-assignments` is a JSON array of `role` and `principalId` pairs. `ADMINISTER` controls the marking; `USE` and `DECLASSIFY` have separate marking permissions. For organization markings, this endpoint supports only `USE` and `DECLASSIFY`; administer them through organization role assignments.

Required input: `marking_id`, `--role-assignments`. The SDK returns no resource body after success. This changes identity or access state. Read the affected resource afterward to verify the intended result.  Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin marking-role-assignment add 0950264e-01c8-4e83-81a9-1a6b7f77621a --role-assignments '[{"role":"ADMINISTER","principalId":"f05f8da4-b84c-4fca-9c77-8af0b13d11de"}]'`

### marking_role_assignment.list

List direct role assignments on a marking, with each principal and its marking role. Use this to check who can administer or use a marking before changing it. The API ignores `pageSize`; a small requested page size does not limit the result.

Required input: `marking_id`. The SDK returns `ListMarkingRoleAssignmentsResponse` on success. The operation does not change Foundry state. An empty response means no visible matches; page forward when a continuation token is returned.  Authentication or permission errors stop the read; an empty visible result is not an API failure.

**Example:** `pal-found-admin marking-role-assignment list 0950264e-01c8-4e83-81a9-1a6b7f77621a`

### marking_role_assignment.remove

Remove the exact `role` and `principalId` pairs in the `--role-assignments` JSON array from a marking. This can remove a principal's ability to administer, use, or declassify it; inspect existing assignments first. For organization markings, only `USE` and `DECLASSIFY` apply here; change `ADMINISTER` through organization role assignments.

Required input: `marking_id`, `--role-assignments`. The SDK returns no resource body after success. This changes identity or access state. Read the affected resource afterward to verify the intended result.  Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin marking-role-assignment remove 0950264e-01c8-4e83-81a9-1a6b7f77621a --role-assignments '[{"role":"ADMINISTER","principalId":"f05f8da4-b84c-4fca-9c77-8af0b13d11de"}]'`

### organization.create

Create an organization in the enrollment named by `--enrollment-rid`. `--administrators` is a JSON array of principal IDs receiving initial administration responsibility; `--name` identifies the organization to users. Optional `--description` explains its purpose, and `--host` sets its host address. The response supplies its organization RID for guest, role, and resource access commands.

Required input: `--administrators`, `--enrollment-rid`, `--name`. Optional: `--description`, `--host`. The SDK returns `Organization` on success. This changes identity or access state. Read the affected resource afterward to verify the intended result.  Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin organization create --administrators '["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]' --enrollment-rid ri.control-panel.main.customer.466f812b-f974-4478-9d4f-90402cd3def6 --name 'Example Organization'`

### organization.get

Read an organization by RID to confirm its name, description, and host before changing organization settings or assignments. To inspect access, also list its guest members and organization role assignments.

Required input: `organization_rid`. The SDK returns `Organization` on success. The operation does not change Foundry state.  An unknown ID or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin organization get ri.multipass..organization.example`

### organization.list_available_roles

List role definitions available for assignment at this organization's scope. Use the returned role IDs when composing `organization-role-assignment add`; this command does not list the principals currently holding those roles.

Required input: `organization_rid`. The SDK returns `ListAvailableOrganizationRolesResponse` on success. The operation does not change Foundry state.  An unknown ID or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin organization list-available-roles ri.multipass..organization.example`

### organization.replace

Replace an organization's editable metadata by RID. `--name` is its displayed name, `--description` explains its purpose, and `--host` sets its host address. Read the current organization first to preserve fields you intend to keep, then inspect the returned `Organization`. This does not change guest membership or role assignments.

Required input: `organization_rid`, `--name`. Optional: `--description`, `--host`. The SDK returns `Organization` on success. This changes identity or access state. Read the affected resource afterward to verify the intended result.  Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin organization replace ri.multipass..organization.example --name 'Example Organization'`

### organization_guest_member.add

Add the principal IDs in `--principal-ids` to another organization's guest set. Guest membership lets them participate there under that organization's access rules. Adding an existing primary member returns success without converting that principal to a guest, so verify the guest list afterward.

Required input: `organization_rid`, `--principal-ids`. The SDK returns no resource body after success. This changes identity or access state. Read the affected resource afterward to verify the intended result. Adding an existing primary member succeeds without making that principal a guest; inspect the guest list to verify the intended change. Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin organization-guest-member add ri.multipass..organization.example --principal-ids '["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]'`

### organization_guest_member.list

List principals added as guests of the specified organization. Use it after `add` or `remove` to verify the effective guest list. A primary member need not appear as a guest; adding one through the guest endpoint can return success without changing its membership kind.

Required input: `organization_rid`. The SDK returns `ListOrganizationGuestMembersResponse` on success. The operation does not change Foundry state. An empty response means no visible matches; page forward when a continuation token is returned.  Authentication or permission errors stop the read; an empty visible result is not an API failure.

**Example:** `pal-found-admin organization-guest-member list ri.multipass..organization.example`

### organization_guest_member.remove

Remove the principal IDs in `--principal-ids` from the organization's guest set. Removing an existing primary member returns success without removing primary membership, so verify the guest list afterward.

Required input: `organization_rid`, `--principal-ids`. The SDK returns no resource body after success. This changes identity or access state. Read the affected resource afterward to verify the intended result. Removing a primary member through this endpoint succeeds without removing primary membership. Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin organization-guest-member remove ri.multipass..organization.example --principal-ids '["f05f8da4-b84c-4fca-9c77-8af0b13d11de"]'`

### organization_role_assignment.add

Assign organization-scoped roles to principals. `--role-assignments` is a JSON array of `roleId` and `principalId` pairs, with at most 100 pairs per request. Use `organization list-available-roles` to find valid role IDs, then list assignments to verify.

Required input: `organization_rid`, `--role-assignments`. The SDK returns no resource body after success. This changes identity or access state. Read the affected resource afterward to verify the intended result. The endpoint accepts at most 100 assignments per request. Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin organization-role-assignment add ri.multipass..organization.example --role-assignments '[{"roleId":"8bf49052-dc37-4528-8bf0-b551cfb71268","principalId":"f05f8da4-b84c-4fca-9c77-8af0b13d11de"}]'`

### organization_role_assignment.list

Organization roles delegate administration within an organization. List all principals who are assigned a role for the given Organization.

Required input: `organization_rid`. The SDK returns `ListOrganizationRoleAssignmentsResponse` on success. The operation does not change Foundry state. An empty response means no visible matches; page forward when a continuation token is returned.  Authentication or permission errors stop the read; an empty visible result is not an API failure.

**Example:** `pal-found-admin organization-role-assignment list ri.multipass..organization.example`

### organization_role_assignment.remove

Remove organization-scoped roles from principals. `--role-assignments` is a JSON array of the exact `roleId` and `principalId` pairs to remove, with at most 100 pairs per request. List assignments afterward because other grants may still provide access.

Required input: `organization_rid`, `--role-assignments`. The SDK returns no resource body after success. This changes identity or access state. Read the affected resource afterward to verify the intended result. The endpoint accepts at most 100 assignments per request. Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin organization-role-assignment remove ri.multipass..organization.example --role-assignments '[{"roleId":"8bf49052-dc37-4528-8bf0-b551cfb71268","principalId":"f05f8da4-b84c-4fca-9c77-8af0b13d11de"}]'`
