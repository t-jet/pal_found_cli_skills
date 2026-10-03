# Admin governance

This part documents the Admin governance operations: CBAC banner and marking
restrictions, hosts, markings, marking categories, marking members and role
assignments, organizations, guest members, and organization role assignments
(28 operations). It is owned by DEV-STORY-043.

Read the general [identifiers, auth, and access
control](../pal-found/references/02-identifiers-auth-access.md) part and the
[Admin entry](SKILL.md) first. Governance writes change who can see or act on
resources; they are not reversible by the CLI and affect access immediately.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/admin/scripts/pal_found_admin_cli.py`;
SDK `foundry_sdk/v2/admin/{cbac_banner,cbac_marking_restrictions,host,marking,marking_category,marking_member,marking_role_assignment,organization,organization_guest_member,organization_role_assignment}.py`
at pinned commit `2da67907`. Reviewer architect (CODEREVIEW-043), 2026-10-03.
QA baseline TESTCASE-009.

## Workflow

1. Read governance context: `cbac_banner.get`, `cbac_marking_restrictions.get`,
   `host.list`.
2. Manage markings for resource classification (`marking` create/get/get-batch/
   list/replace) and their categories (`marking_category`).
3. Grant and revoke access via `marking_member.add`/`list`/`remove` and
   `marking_role_assignment.add`/`list`/`remove`.
4. Manage organizations (`organization` create/get/list-available-roles/replace),
   guest members, and role assignments.

## Operation records

### cbac_banner.get

- **Class**: read. Returns the CBAC banner text shown in the platform.
- **Preconditions**: can read governance settings.
- **Effect**: returns the banner; no state change.
- **Inputs**: none positional.

### cbac_marking_restrictions.get

- **Class**: read. Returns cross-organization marking restrictions.
- **Preconditions**: can read governance settings.
- **Effect**: returns restrictions; no state change.
- **Inputs**: none positional.

### host.list

- **Class**: read. Lists hosts.
- **Preconditions**: can read hosts.
- **Effect**: returns a page of hosts.
- **Inputs**: paging options.
- **Success**: list of hosts; empty if none.

### marking.create

- **Class**: create. Creates a marking.
- **Preconditions**: write access to governance.
- **Effect**: creates a marking for classifying resources by access.
- **Inputs**: required name and category; attributes JSON (`--attributes`).
- **Success**: the new marking, including its RID.
- **Failure**: exit 1 invalid input; exit 8 readonly block; exit 3 permission.

### marking.get / marking.get_batch / marking.list / marking.replace

- **get**: read a marking by RID.
- **get_batch**: read several markings by a JSON `body` list of RIDs.
- **list**: page through markings.
- **replace**: replace a marking's definition (write; affects who can use it).

### marking_category.create / get / list / replace

- **create**: create a marking category (write).
- **get**: read a category by RID.
- **list**: page categories.
- **replace**: replace a category's definition (write).

### marking_member.add / list / remove

- **add**: grant a principal membership to a marking (write, changes access).
- **list**: page a marking's members.
- **remove**: revoke a principal's membership in a marking (write, changes
  access).

### marking_role_assignment.add / list / remove

- **add**: assign a role on a marking to a principal (write).
- **list**: page role assignments on a marking.
- **remove**: remove a role assignment (write).

### organization.create / get / list_available_roles / replace

- **create**: create an organization (write).
- **get**: read an organization by RID.
- **list_available_roles**: read the roles available to assign in an
  organization.
- **replace**: replace an organization's definition (write).

### organization_guest_member.add / list / remove

- **add**: grant guest membership in an organization to a principal (write).
- **list**: page guest members of an organization.
- **remove**: revoke guest membership (write).

### organization_role_assignment.add / list / remove

- **add**: assign a role within an organization (write).
- **list**: page organization role assignments.
- **remove**: remove an organization role assignment (write).

## Effects and permissions

Membership and role-assignment writes immediately change who can access
resources governed by the marking or organization. Deletes are not available
for markings here; use `replace` to update. A zero exit confirms the change was
accepted; verify with a read (`get`/`list`) when the platform may propagate
late. Never present a governance change as done without confirming the read
result matches intent.

## Evidence and review

Each record was reviewed against the installed `pal-found-admin`
parser/dispatch and pinned SDK sources (commit `2da67907`). Writes alter
access and are flagged; reads never write. No unsupported operation is
documented as callable.
