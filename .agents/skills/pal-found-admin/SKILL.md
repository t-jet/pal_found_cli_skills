---
name: pal-found-admin
description: Understand Foundry identity and security administration, then use 66 CLI operations to inspect or change users, groups, roles, markings, and organizations.
---

# Foundry Admin CLI

## Capability and source

Foundry administration connects authentication to authorization. An
authentication provider verifies identity. Users and groups represent the
people and teams receiving grants. Roles collect permissions; project and
administrative role assignments decide what those principals may do.
Organizations, markings, and classification controls add mandatory access
requirements. They can restrict access even when a user has a project role,
and mandatory controls can follow data through derivation. Enrollment
administrators manage the broad platform scope, while organization roles
delegate responsibilities within an organization. The CLI exposes 66 Admin
API v2 operations for these controls; invoking a command still requires
credentials and the relevant Foundry permission.

Source: [Palantir administration](https://www.palantir.com/docs/foundry/administration/overview), [security model](https://www.palantir.com/docs/foundry/security/overview), and SDK `docs/v2/Admin`.

66 Foundry Admin API v2 operations are available through the installed `pal-found-admin` command.

## Usage

```bash
pal-found-admin <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, and `--pretty`.
Paginated operations also accept `--page-size`, `--page-token`, and
`--batch-pages`.

The CLI uses the shared config loader, ADMIN access control guard, retry
handler, pagination helper, structured error serializer, output formatter,
and SDK-native B3 tracing scope.

## Operation index

Choose the reference page for the subject you are investigating or changing.
Each operation has its own inputs, result, and example.

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Identity: authentication, enrollment, users](references/01-identity-auth-users.md) | `authentication_provider`, `enrollment`, `enrollment_role_assignment`, `user`, `user_provider_info` | 20 |
| [Identity: groups, memberships, roles](references/02-identity-groups-roles.md) | `group`, `group_member`, `group_membership`, `group_membership_expiration_policy`, `group_provider_info`, `role` | 18 |
| [Governance: classifications and markings](references/03-governance.md) | `cbac_banner`, `cbac_marking_restrictions`, `host`, `marking`, `marking_category` | 12 |
| [Governance: membership and organizations](references/04-governance-access.md) | `marking_member`, `marking_role_assignment`, `organization`, `organization_guest_member`, `organization_role_assignment` | 16 |

The `pal-found-audit` skill documents the two `audit log_file` operations
separately.

## Parameters and JSON

Every operation accepts `--timeout` (request timeout in seconds), `--format
json|toon|auto` (output encoding), and `--pretty` (indented output). Paged
operations accept `--page-size` (requested items per page), `--page-token`
(continuation token returned by the preceding page), and `--batch-pages`
(maximum pages fetched in one call). A short page is not proof that the list
has ended; check the continuation token.

The references explain each operation's required inputs. These names recur
across operations:

| Input | Meaning |
| --- | --- |
| `enrollment_rid`, `--enrollment-rid` | Enrollment containing the provider, host, or new organization. |
| `--organization`, `--organizations` | One primary organization RID, or a JSON array of organization RIDs whose members can see a group. |
| `--name`, `--description`, `--host` | Resource display name, explanatory text, or organization host address. |
| `--attributes` | JSON map of identity attributes to arrays of values; `multipass:` keys are reserved and must be preserved on group replacement. |
| `--administrators`, `--initial-members`, `--principal-ids` | JSON arrays of user or group principal IDs receiving organization administration, initial marking membership, or a requested membership change. |
| `--initial-role-assignments`, `--role-assignments` | JSON arrays pairing principal IDs with role IDs or marking role names. |
| `--initial-permissions` | JSON object defining a marking category's organization visibility, public visibility, and administrator roles. |
| `--marking-ids`, `--category-id` | JSON array of marking IDs for classification queries, or one category ID for a new marking. |
| `--display-type` | Classification banner style: short `PORTION_MARKING` or longer `BANNER_LINE`. |
| `--where` | Typed JSON search filter, such as `{"type":"queryString","value":"Data"}`. |
| `body` | Positional JSON array of ID requests for a `get-batch` operation. |
| `--username`, `--email`, `--given-name`, `--family-name` | Provider username and optional identity details for preregistering a user. |
| `--provider-id` | Stable identifier assigned by an external identity provider to a user or group. |
| `--status`, `--include` | User status requested by `get`, or extra statuses included by `list`, such as `DELETED`. |
| `--expiration`, `--maximum-value`, `--maximum-duration` | Member expiry timestamp, latest allowed expiry timestamp, or maximum lifetime in seconds. |
| `--include-expirations`, `--transitive` | Show direct membership expiry or follow nested group membership; these cannot both be true for `group-member list`. |
| `--preview` | Opt in to preview behavior on operations that support it. |

Other positional IDs name the resource shown in `--help`. Use IDs returned by
read commands rather than display names where a command asks for an ID.

## Install requirement

`pal-found-admin` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

```bash
# conda (t-jet channel)
conda install -c t-jet pal_found_cli

# PyPI / pip
pip install pal_found_cli

# uv
uv tool install pal_found_cli
```
