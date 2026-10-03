# Admin identity: authentication providers, enrollment, and users

This part documents the Admin identity operations that manage authentication
providers, enrollment and its role assignments, users, and user provider
information (15 operations). Read [identifiers, auth, and access
control](../pal-found/references/02-identifiers-auth-access.md) from the
general skill first if you are new to Admin.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/admin/scripts/pal_found_admin_cli.py`;
SDK `foundry_sdk/v2/admin/{authentication_provider,enrollment,enrollment_role_assignment,user,user_provider_info}.py`
at the pinned commit `2da67907`. Reviewer architect (CODEREVIEW-042),
2026-10-03. QA baseline TESTCASE-009.

## Workflow

1. Read an enrollment to learn its providers and scope (`enrollment.get`).
2. List authentication providers (`authentication_provider.list`) and manage
   preregistration (`authentication_provider.preregister_group` /
   `preregister_user`) so users and groups can be provisioned.
3. Create/read/search users (`user.create` has no CLI entry here; use
   `user.get`/`user.list`/`user.search`), and manage their provider info and
   tokens.
4. Assign or remove enrollment roles (`enrollment_role_assignment`).

## Common rules

All commands: `--timeout`, `--format json|toon|auto`, `--pretty`. Get-batch
commands take a positional JSON `body` (list of RIDs) and return a batch of
records. Reads never write state. Deletes are destructive and immediate; a
zero exit means the subject was removed, but confirm with a follow-up `get`
if the platform allows late propagation.

## Operation records

### authentication_provider.get

- **Class**: read. Affects no enrollment state.
- **Preconditions**: you can read the enrollment and the provider.
- **Effect**: returns the named authentication provider's configuration for
  the enrollment.
- **Inputs**: positional `enrollment_rid`, `authentication_provider_rid`;
  optional `--preview`.
- **Success**: returns the authentication provider record. Empty is not
  expected for an existing provider.
- **Failure**: exit 4 (not found) if enrollment/provider RID is wrong; exit 3
  if you lack read permission; exit 2 if auth is bad.
- **Example**: `pal-found-admin authentication-provider get <ENROLLMENT_RID> <PROVIDER_RID>`.

### authentication_provider.list

- **Class**: read. Lists providers for an enrollment.
- **Preconditions**: read on the enrollment.
- **Effect**: returns the enrollment's authentication providers.
- **Inputs**: positional `enrollment_rid`; optional `--preview`.
- **Success**: a list of providers; empty means none configured.
- **Failure**: exit 4 if enrollment RID is wrong; exit 3 permission; exit 2 auth.
- **Example**: `pal-found-admin authentication-provider list <ENROLLMENT_RID>`.

### authentication_provider.preregister_group

- **Class**: change. Preregisters a group so it can be provisioned later.
- **Preconditions**: enrollment write access and a group identifier.
- **Effect**: marks a group as preregistered in the enrollment.
- **Inputs**: positional `enrollment_rid`, `group_id`; optional `--preview`.
- **Success**: returns the preregistered group reference.
- **Failure**: exit 1 invalid input; exit 8 if CLI access control blocks;
  exit 3 permission.
- **Example**: `pal-found-admin authentication-provider preregister-group <ENROLLMENT_RID> <GROUP_ID>`.

### authentication_provider.preregister_user

- **Class**: change. Preregisters a user for enrollment provisioning.
- **Preconditions**: enrollment write access and a user identifier.
- **Effect**: marks a user as preregistered.
- **Inputs**: positional `enrollment_rid`, `user_id`; optional `--preview`.
- **Success**: returns the preregistered user reference.
- **Failure**: same as preregister_group.
- **Example**: `pal-found-admin authentication-provider preregister-user <ENROLLMENT_RID> <USER_ID>`.

### enrollment.get

- **Class**: read. Returns an enrollment.
- **Preconditions**: enrollment read access.
- **Effect**: returns the enrollment's configuration and realm.
- **Inputs**: positional `enrollment_rid`; optional `--preview`.
- **Success**: the enrollment record.
- **Failure**: exit 4 if RID wrong; exit 3 permission.
- **Example**: `pal-found-admin enrollment get <ENROLLMENT_RID>`.

### enrollment.get_current

- **Class**: read. Returns the enrollment that governs the caller's realm.
- **Preconditions**: a valid AuthenticatedUserId.
- **Effect**: returns the current enrollment without needing its RID.
- **Inputs**: none positional; optional `--preview`.
- **Success**: the enrollment record for the current identity.
- **Failure**: exit 2 if no authenticated identity.
- **Example**: `pal-found-admin enrollment get-current`.

### enrollment_role_assignment.add

- **Class**: change. Assigns a role to a principal within the enrollment.
- **Preconditions**: enrollment write access and a valid role.
- **Effect**: grants the role.
- **Inputs**: positional `enrollment_rid`; `--principal-ids` and
  `--role-role-rid`/role identifiers.
- **Success**: returns the created assignment.
- **Failure**: exit 1 invalid role/principal; exit 3 permission.
- **Example**: `pal-found-admin enrollment-role-assignment add <ENROLLMENT_RID> --principal-ids '["ri.principal.user.abc"]' --role-rid <ROLE_RID>`.

### enrollment_role_assignment.list

- **Class**: read. Lists role assignments in the enrollment.
- **Preconditions**: enrollment read access.
- **Effect**: returns assignments, paged.
- **Inputs**: positional `enrollment_rid`; paging options.
- **Success**: list of assignments; empty means none.
- **Failure**: exit 4/3 as above.
- **Example**: `pal-found-admin enrollment-role-assignment list <ENROLLMENT_RID> --page-size 100`.

### enrollment_role_assignment.remove

- **Class**: change. Removes a role assignment.
- **Preconditions**: enrollment write access.
- **Effect**: revokes the role.
- **Inputs**: positional `enrollment_rid`; principal and role identifiers.
- **Success**: returns the updated enrollment.
- **Failure**: exit 4 if assignment not found; exit 3 permission.
- **Example**: `pal-found-admin enrollment-role-assignment remove <ENROLLMENT_RID> --principal-id <PID> --role-rid <ROLE_RID>`.

### user.get

- **Class**: read. Returns a single user.
- **Preconditions**: can read the user.
- **Effect**: returns user attributes.
- **Inputs**: positional `user_id`; optional `--preview`.
- **Success**: the user record.
- **Failure**: exit 4 if unknown user; exit 3 permission.
- **Example**: `pal-found-admin user get <USER_ID>`.

### user.get_batch

- **Class**: read. Returns several users in one call.
- **Preconditions**: read on each requested user.
- **Effect**: returns a batch of user records.
- **Inputs**: positional JSON `body` (list of user IDs); optional `--preview`.
- **Success**: a list of user records for the requested IDs.
- **Failure**: exit 1 malformed body.
- **Example**: `pal-found-admin user get-batch --body '["u1","u2"]'`.

### user.get_current

- **Class**: read. Returns the calling user.
- **Preconditions**: a valid token.
- **Effect**: returns the current user without knowing the user ID.
- **Inputs**: none; optional `--preview`.
- **Success**: the current user record.
- **Failure**: exit 2 if no valid identity.
- **Example**: `pal-found-admin user get-current`.

### user.get_markings

- **Class**: read. Returns the markings granted to a user.
- **Preconditions**: can read the user.
- **Effect**: returns the user's markings.
- **Inputs**: positional `user_id`; optional `--preview`.
- **Success**: a list of markings (may be empty).
- **Failure**: exit 4 if unknown user.
- **Example**: `pal-found-admin user get-markings <USER_ID>`.

### user.list

- **Class**: read. Lists users matching the enrollment scope.
- **Preconditions**: can read the enrollment's users.
- **Effect**: returns a page of users; use paging to get more.
- **Inputs**: optional `--page-size`, `--page-token`, `--batch-pages`.
- **Success**: a list of users; empty if no users are visible.
- **Failure**: exit 3 permission; exit 2 auth.
- **Example**: `pal-found-admin user list --page-size 100`.

### user.delete

- **Class**: delete. Removes a user.
- **Preconditions**: write access; confirm the user has no dependent grants
  you still need.
- **Effect**: permanently deletes the user. Returns the deleted user.
- **Inputs**: positional `user_id`; optional `--preview`.
- **Success**: the deleted user record; deletion is immediate.
- **Failure**: exit 4 if unknown user; exit 3 permission.
- **Example**: `pal-found-admin user delete <USER_ID>`.

### user.profile_picture

- **Class**: read (binary download). Retrieves a user's profile picture.
- **Preconditions**: can read the user.
- **Effect**: writes a binary file through the download handler; returns a
  metadata envelope (file path, size, checksums).
- **Inputs**: positional `user_id`; `--output` for the destination.
- **Success**: metadata envelope; download bound applies
  (`FOUNDRY_AGENTIC_CLI_MAX_DOWNLOAD_BYTES`).
- **Failure**: exit 8 if content read blocked in metadata-only mode.
- **Example**: `pal-found-admin user profile-picture <USER_ID> --output picture.png`.

### user.revoke_all_tokens

- **Class**: change. Invalidates all tokens for a user.
- **Preconditions**: write access on the user.
- **Effect**: revokes the user's tokens; any session using them breaks.
- **Inputs**: positional `user_id`.
- **Success**: returns the updated user.
- **Failure**: exit 3 permission; exit 4 unknown user.
- **Example**: `pal-found-admin user revoke-all-tokens <USER_ID>`.

### user.search

- **Class**: read. Searches users by query.
- **Preconditions**: can read users.
- **Effect**: returns matching users.
- **Inputs**: `--where`/query plus paging options.
- **Success**: a list of matches; empty means no match.
- **Failure**: exit 1 invalid query.
- **Example**: `pal-found-admin user search --query 'alice'`.

### user_provider_info.get

- **Class**: read. Returns a user's provider info.
- **Preconditions**: read on the user.
- **Effect**: returns the provider-specific identity for the user.
- **Inputs**: positional `user_id`.

### user_provider_info.replace

- **Class**: change. Replaces a user's provider info.
- **Preconditions**: write access on the user.
- **Effect**: updates the user's provider identity; previous provider info is
  replaced.
- **Inputs**: positional `user_id` plus provider fields.

## Evidence and review

Each record above was reviewed against the installed `pal-found-admin`
parser/dispatch and the pinned SDK sources (commit `2da67907`). Read-class
operations never write; change/delete class operations write and may be
destructive. No unsupported operation is presented as callable.
