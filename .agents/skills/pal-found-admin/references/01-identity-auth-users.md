# Identity: authentication, enrollment, users

Authentication verifies users through configured providers. Enrollment roles delegate broad administrative powers; organization, group, and marking controls still affect access. User provider records map external identities to Foundry users. See [administration overview](https://www.palantir.com/docs/foundry/administration/overview) and [users and groups](https://www.palantir.com/docs/foundry/security/users-and-groups). Commands here use the installed Admin CLI. Example identifiers and names are illustrative; replace them with values from your enrollment.

## Operation records

### authentication_provider.get

Read one authentication provider in an enrollment by RID. Its configuration identifies the external identity source used for sign-in and preregistration. Use `list` first when you do not know the provider RID.

Required input: `enrollment_rid`, `authentication_provider_rid`. The SDK returns `AuthenticationProvider` on success. The operation does not change Foundry state.  An unknown ID or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin authentication-provider get ri.multipass..enrollment.example ri.control-panel.main.saml.3faf689c-eaa1-4137-851f-81d58afe4c86`

### authentication_provider.list

List authentication providers configured for an enrollment. Use the returned provider RIDs to inspect a provider or preregister an externally managed user or group. An empty list means no providers are visible to this caller.

Required input: `enrollment_rid`. The SDK returns `ListAuthenticationProvidersResponse` on success. The operation does not change Foundry state. An empty response means no visible matches; page forward when a continuation token is returned.  Authentication or permission errors stop the read; an empty visible result is not an API failure.

**Example:** `pal-found-admin authentication-provider list ri.multipass..enrollment.example`

### authentication_provider.preregister_group

Preregister an externally managed group before its members first sign in. `--name` must match the group name supplied by the selected provider; `--organizations` is a JSON array of organizations whose members can see the new group. The returned principal ID can receive grants before the provider adds members at sign-in.

Required input: `enrollment_rid`, `authentication_provider_rid`, `--name`, `--organizations`. The SDK returns `PrincipalId` on success. This changes identity or access state. Read the affected resource afterward to verify the intended result. The group can receive permissions before a matching provider login creates membership. Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin authentication-provider preregister-group ri.multipass..enrollment.example ri.control-panel.main.saml.3faf689c-eaa1-4137-851f-81d58afe4c86 --name 'Data Source Admins' --organizations '["ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa"]'`

### authentication_provider.preregister_user

Preregister an externally managed user before first sign-in so the returned principal ID can receive groups and roles in advance. `--username` must match a pattern supported by the provider. `--organization` is the intended primary organization RID, which sign-in assignment rules may later change. Optional `--attributes` is a JSON map of additional identity values; `--email`, `--given-name`, and `--family-name` provide contact and profile details.

Required input: `enrollment_rid`, `authentication_provider_rid`, `--organization`, `--username`. Optional: `--attributes`, `--email`, `--family-name`, `--given-name`. The SDK returns `PrincipalId` on success. This changes identity or access state. Read the affected resource afterward to verify the intended result. The user can receive group and role assignments before first login. Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin authentication-provider preregister-user ri.multipass..enrollment.example ri.control-panel.main.saml.3faf689c-eaa1-4137-851f-81d58afe4c86 --organization ri.multipass..organization.c30ee6ad-b5e4-4afe-a74f-fe4a289f2faa --username jsmith`

### enrollment.get

Read an enrollment by RID to inspect the top-level identity and organization boundary before assigning enrollment roles or configuring providers. This does not enumerate its users or grant access.

Required input: `enrollment_rid`. The SDK returns `Enrollment` on success. The operation does not change Foundry state.  An unknown ID or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin enrollment get ri.multipass..enrollment.example`

### enrollment.get_current

Discover the enrollment attached to the authenticated user's primary organization. Use its returned RID with enrollment-scoped commands such as `authentication-provider list` and `enrollment-role-assignment list`.

Required input: no required operation arguments. The SDK returns `Enrollment` on success. The operation does not change Foundry state.  Authentication or permission errors stop the read; an empty visible result is not an API failure.

**Example:** `pal-found-admin enrollment get-current`

### enrollment_role_assignment.add

Assign enrollment-wide roles to users or groups. `--role-assignments` is a JSON array of `roleId` and `principalId` pairs, with at most 100 pairs per request. Read available role definitions before constructing the array, then list assignments to verify the result.

Required input: `enrollment_rid`, `--role-assignments`. The SDK returns no resource body after success. This changes identity or access state. Read the affected resource afterward to verify the intended result. The endpoint accepts at most 100 assignments per request. Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin enrollment-role-assignment add ri.multipass..enrollment.example --role-assignments '[{"roleId":"8bf49052-dc37-4528-8bf0-b551cfb71268","principalId":"f05f8da4-b84c-4fca-9c77-8af0b13d11de"}]'`

### enrollment_role_assignment.list

Enrollment roles delegate platform-wide administrative permissions to users or groups. List all principals who are assigned a role for the given Enrollment.

Required input: `enrollment_rid`. The SDK returns `ListEnrollmentRoleAssignmentsResponse` on success. The operation does not change Foundry state. An empty response means no visible matches; page forward when a continuation token is returned.  Authentication or permission errors stop the read; an empty visible result is not an API failure.

**Example:** `pal-found-admin enrollment-role-assignment list ri.multipass..enrollment.example`

### enrollment_role_assignment.remove

Remove enrollment-wide roles from users or groups. `--role-assignments` is a JSON array of the exact `roleId` and `principalId` pairs to remove, with at most 100 pairs per request. Check `list` afterward because other assignments may still grant administrative access.

Required input: `enrollment_rid`, `--role-assignments`. The SDK returns no resource body after success. This changes identity or access state. Read the affected resource afterward to verify the intended result. The endpoint accepts at most 100 assignments per request. Invalid identifiers or payloads, insufficient administration rights, and CLI access policy can reject the change.

**Example:** `pal-found-admin enrollment-role-assignment remove ri.multipass..enrollment.example --role-assignments '[{"roleId":"8bf49052-dc37-4528-8bf0-b551cfb71268","principalId":"f05f8da4-b84c-4fca-9c77-8af0b13d11de"}]'`

### user.delete

Delete the user identified by `user_id`. Foundry represents deleted users with status `DELETED`, so this operation changes the identity's status rather than returning a deleted user record. Check the target ID before running because this CLI has no restore-user operation. Later, `user get --status DELETED` targets that status, while `user list --include DELETED` includes deleted accounts in an inventory.

Required input: `user_id`. Success is HTTP 204 with no resource body. To inspect the resulting status, use `user get <USER_ID> --status DELETED` or `user list --include DELETED`. A missing user, already deleted user, insufficient permission, or CLI access policy can reject the request.

**Example:** `pal-found-admin user delete f05f8da4-b84c-4fca-9c77-8af0b13d11de`

### user.get

Read one Foundry user by principal ID. The response contains identity details and status; `--status` selects the status to retrieve, including `DELETED` when investigating a removed account. The call does not show every group or marking membership; use the corresponding membership commands for those.

Required input: `user_id`. Optional: `--status`. The SDK returns `User` on success. The operation does not change Foundry state.  An unknown ID or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin user get f05f8da4-b84c-4fca-9c77-8af0b13d11de`

### user.get_batch

Resolve several user IDs in one request, for example the principals returned by a role assignment list. The positional `body` is a JSON array of requests with `userId` and optional status. The endpoint accepts at most 500 requests; compare returned IDs with input IDs before assuming every user was found.

Required input: `body`. The SDK returns `GetUsersBatchResponse` on success. The operation does not change Foundry state. Compare returned IDs with requested IDs; some endpoints omit unknown or inaccessible records. The endpoint accepts at most 500 user IDs. An unknown ID or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin user get-batch '[{"userId":"0d1fe74e-2b70-4a93-9b1a-80070637788b","status":"ACTIVE"}]'`

### user.get_current

Read the user represented by the CLI credential. Use its principal ID to check group membership, marking membership, or whether an administrative role assignment names the right account.

Required input: no required operation arguments. The SDK returns `User` on success. The operation does not change Foundry state.  Authentication or permission errors stop the read; an empty visible result is not an API failure.

**Example:** `pal-found-admin user get-current`

### user.get_markings

List markings of which the specified user is currently a member. Marking membership can satisfy a mandatory access requirement, but it does not by itself grant a project role or access to every resource carrying that marking.

Required input: `user_id`. The SDK returns `GetUserMarkingsResponse` on success. The operation does not change Foundry state.  An unknown ID or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin user get-markings f05f8da4-b84c-4fca-9c77-8af0b13d11de`

### user.list

List users visible to the caller. Use `--include DELETED` when reviewing deleted accounts; the default view is for active users. Results are paged, and a short page is not the last page when `nextPageToken` is present.

Required input: no required operation arguments. Optional: `--include`. The SDK returns `ListUsersResponse` on success. The operation does not change Foundry state. An empty response means no visible matches; page forward when a continuation token is returned.  Authentication or permission errors stop the read; an empty visible result is not an API failure.

**Example:** `pal-found-admin user list`

### user.profile_picture

Fetch the user's profile picture bytes when one exists. This endpoint is for profile media, not user metadata; use `user get` for names and status. The CLI reports byte count rather than saving an image, so this command cannot be used to recover the picture file.

Required input: `user_id`. The SDK returns `Optional[bytes]` on success. The result is binary profile-picture content represented by byte count in CLI JSON output; this CLI has no `--output` argument here.  An unknown ID or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin user profile-picture f05f8da4-b84c-4fca-9c77-8af0b13d11de`

### user.revoke_all_tokens

User records represent identities that sign in and receive group, organization, and marking access. Revoke all active authentication tokens for the user including active browser sessions and long-lived development tokens. If the user has active sessions in a browser, this will force re-authentication. The caller must have permission to manage users for the target user's organization.

Required input: `user_id`. Success is HTTP 204 with no resource body. Active browser sessions must authenticate again, and long-lived development tokens stop working. The caller must be able to manage users in the target organization. This CLI has no token-status read operation to confirm each revocation separately; the successful response confirms that Foundry accepted the request.

**Example:** `pal-found-admin user revoke-all-tokens f05f8da4-b84c-4fca-9c77-8af0b13d11de`

### user.search

Search active users by a case-insensitive prefix of username, given name, or family name. `--where` takes a typed JSON filter such as `{"type":"queryString","value":"jsmith"}`. Deleted accounts do not appear in search; use `user list --include DELETED` to inspect those.

Required input: `--where`. The SDK returns `SearchUsersResponse` on success. The operation does not change Foundry state. An empty response means no visible matches; page forward when a continuation token is returned. The API performs a case-insensitive prefix search on active users’ username, given name, and family name. Use `user.list --include DELETED` to find deleted users. Authentication or permission errors stop the read; an empty visible result is not an API failure.

**Example:** `pal-found-admin user search --where '{"type":"queryString","value":"jsmith"}'`

### user_provider_info.get

Provider information links a Foundry user to an externally managed identity. Get user provider info.

Required input: `user_id`. The SDK returns `UserProviderInfo`, including the external provider's ID for this user, without changing the mapping. An unknown user or insufficient read permission prevents a usable response.

**Example:** `pal-found-admin user-provider-info get f05f8da4-b84c-4fca-9c77-8af0b13d11de`

### user_provider_info.replace

Change the user's mapping to an external identity provider. `--provider-id` is that provider's stable identifier for the user; it must not already belong to another user in the realm. Read the mapping afterward to verify it.

Required input: `user_id` and `--provider-id`, the user's ID in the external authentication provider. The SDK returns the updated `UserProviderInfo`. A provider ID can identify at most one user in a realm; a duplicate mapping or insufficient permission can reject replacement. Read the mapping afterward to verify it.

**Example:** `pal-found-admin user-provider-info replace f05f8da4-b84c-4fca-9c77-8af0b13d11de --provider-id external-id-123`
