# Projects, organization boundaries and role grants

[REST development](../../../rest-api.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

A project groups resources within a Space and carries organization and role
configuration. Project metadata, organization markings, role grants and references
to resources from another project are separate records. A successful metadata read
does not establish permission to change those records or to read every contained
resource. Retain project and Space RIDs throughout a governance workflow.

## Prerequisites

Use the prepared SDK 1.101.0 and the intended Space's role set. For creation,
resolve organization RIDs and ensure their organization markings are on the Space.
Supply an owner-like grant: its role must include `compass:edit-project`. The common
default role set uses `compass:manage`, but a custom Space requires its actual role
IDs. `default_roles` and explicit `role_grants` are distinct inputs.

An OAuth application creating projects through this endpoint cannot be associated
with an OSDK whose restrictions confine operations to selected existing projects.
The SDK instructs that application to choose no OSDK on its Resources page. Obtain
an authorized application configuration; do not broaden a restricted application's
access silently. Grant and Space capability checks still apply.

## Procedure

| Operation | Decision and effect |
| --- | --- |
| [get](../../contracts/v2/filesystem/Project/get.md) | Read the project by RID and confirm Space, identity and resource-level role-grant setting. |
| [create](../../contracts/v2/filesystem/Project/create.md) | Create with display name, Space, organization RIDs, default roles and explicit grants. Keep an owner-like principal grant so an administrator retains control. |
| [create_from_template](../../contracts/v2/filesystem/Project/create_from_template.md) | Create from the selected template using its complete request schema. Template identity and input configuration require verification before submission. |
| [replace](../../contracts/v2/filesystem/Project/replace.md) | Replace project metadata using the supported replacement fields; read first and compare intended identity/name afterward. |
| [organizations](../../contracts/v2/filesystem/Project/organizations.md) | Read directly applied organizations. The list is normally small; the SDK does not require paging parameters here. |
| [add_organizations](../../contracts/v2/filesystem/Project/add_organizations.md) | Add the explicitly approved organization identities; check their Space markings before submission and verify the resulting list. |
| [remove_organizations](../../contracts/v2/filesystem/Project/remove_organizations.md) | Remove the intended direct organization relationships, then verify remaining identities and reassess resulting visibility. |

To reference existing resources, use [ProjectResourceReference](../../contracts/v2/filesystem/ProjectResourceReference/add.md).
A reference is distinct from moving a resource or creating another project. Read
the existing reference inventory before adding or removing intended relationships.

## Worked example

Run from this skill directory:

```bash
python -B examples/rest/073/v2/filesystem/Project/invoke_create.py
```

The fixture calls the actual SDK with display name `Governance review`, a synthetic
Space/organization, default viewer role and a synthetic user explicitly granted
`compass:manage`. Its principal contains `principalId`, `principalType: USER` and
`type: principalWithId`. This is the common role-set example, not a universal tenant
role definition. The response has `NOT_TRASHED` status. The mock verifies wire aliases,
typed result and each declared named error; it does not evaluate real authorization.

Adapt the identifiers and role set using approved Space metadata. The display name
cannot be `.` or `..`, contain `/`, or exceed 700 characters. An omitted
`resource_level_role_grants_allowed` defaults to true at the operation level.
Decide whether individual resource grants should be permitted before creation.

## Expected result and checks

Retain the returned project RID and verify its display name, path, Space and
resource-level grant policy. Enumerate directly applied organizations independently.
For an authorized enrollment check, compare the intended owner's access and a
deliberately denied identity; fake success proves serialization and handling only.
Local definitions linked from each contract explain all request fields, aliases,
typed responses and named-error parameter models.

## Failures and recovery

`CreateProjectNoOwnerLikeRoleGrant` requires correcting actual owner-like grants,
not adding a guessed user role. `InvalidRoleIds` requires the Space's role set.
`OrganizationMarkingNotOnSpace` requires an authorized Space/organization decision.
`ProjectCreationNotSupported` cannot be repaired through request retries alone.
A name conflict requires inspecting the existing project and deciding whether to
reuse it; a matching name alone does not identify the original request.

After an uncertain create or organization mutation, inspect the intended project
and relationship state through permitted reads before replaying it. Preserve the
request context and report an unresolved outcome. This SDK documents no universal
idempotency guarantee for these operations.

## Access boundary

Synthetic SDK fixtures require prepared local libraries. Actual grants, project
creation, organization changes and custom role-set verification require enrollment
connectivity and authorized administration. Each contract preserves its release
stage and supported sync, async, raw and streaming result handling.

## Python client route

With a configured `FoundryClient` named `client`, use `client.filesystem.Project` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.
