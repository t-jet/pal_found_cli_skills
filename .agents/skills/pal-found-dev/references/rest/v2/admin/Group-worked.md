# Groups for application access administration

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md)

## Capability and lifecycle

A Group collects users for access administration. Group creation defines its
name, attributes and organization visibility; membership and role assignments
are separate operations. Creating a group does not grant it a project role.
Organization RIDs in a create request identify organizations whose members can
see the group. At least one organization is required. Attributes beginning with
`multipass:` are reserved by Foundry and can change.

## Create a review group

1. Obtain authorized organization RIDs from enrollment administration. Confirm
   the proposed group name and intended visibility with its owner.
2. Call [create](../../contracts/v2/admin/Group/create.md) with the name, a
   nonempty organization list and an attribute map. An empty map is valid when
   the application has no custom attributes. Use `description` to explain the
   group's purpose when needed.
3. Retain the returned group identifier and compare its name, attributes and
   organizations with the intended configuration. Use this identifier for
   subsequent membership work. Check the separate membership and role APIs
   before assuming anyone has access to an application.

Run the synthetic example from the skill directory:

```bash
python -B examples/rest/071/v2/admin/Group/create.py
```

The example calls the actual SDK with explicit inputs and a synthetic HTTP
transport. It checks JSON request aliases, a decoded Group response and all four
source-declared errors. It prints the operation identity and passed error count.
Its RID is deliberately synthetic; replace it with an authorized organization's
RID for enrollment execution.

`GroupNameAlreadyExists` requires inspecting the existing group before choosing
another name or using its identity. `InvalidGroupOrganizations` requires a
nonempty organization list. `OrganizationNotFound` requires checking the RID
and caller visibility. `CreateGroupPermissionDenied` requires checking the
application's grants and the caller's ability to create groups for those
organizations. The SDK does not enumerate universal OAuth scopes for this call.

If submission times out, a second create can encounter an existing name.
Reconcile the intended group through get/search before retrying. A matching name
does not establish that the first request created it. The SDK does not promise
idempotent creation; preserve uncertain results for operator review.

## Execution boundary

Offline examples require prepared Python, SDK 1.101.0 and httpx. They contact no
enrollment. Live group changes require authorized enrollment connectivity and
tenant permissions; a fixture cannot verify those permissions.
