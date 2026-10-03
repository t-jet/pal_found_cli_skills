---
name: pal-found-admin
description: Offline entry point for Foundry Admin API v2 CLI operations. Covers enrollment, authentication providers, groups, roles, users, markings, organizations, CBAC, hosts, and their membership/role assignments. Navigation + index to the local identity and governance reference parts; never grants access.
---

# Foundry Admin CLI

## Capability and source

Foundry administration exposes enrollment, identity (authentication
providers, groups, roles, users), and governance (markings, organizations,
CBAC, hosts). The `pal-found-admin` command maps those controls to 66 CLI
operations. This skill documents each operation's precondition, effect,
inputs, result, and failure mode offline; it does not grant access by itself.

Source: [Palantir Foundry security and governance](https://www.palantir.com/docs/foundry/security/overview); reviewed 2026-08-13. This source link is maintenance evidence for maintainers; it is not needed to use the skill offline.

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

The Admin operations are grouped into two disjoint reference parts. Read the
index below, pick the resource client for the subject you are acting on, then
open the part and the operation record.

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Identity: authentication, enrollment, users](references/01-identity-auth-users.md) | `authentication_provider`, `enrollment`, `enrollment_role_assignment`, `user`, `user_provider_info` | 15 |
| [Identity: groups, memberships, roles](references/02-identity-groups-roles.md) | `group`, `group_member`, `group_membership`, `group_membership_expiration_policy`, `group_provider_info`, `role` | 23 |
| [Governance](references/03-governance.md) | `cbac_banner`, `cbac_marking_restrictions`, `host`, `marking`, `marking_category`, `marking_member`, `marking_role_assignment`, `organization`, `organization_guest_member`, `organization_role_assignment` | 28 |

The `pal-found-audit` skill documents the two `audit log_file` operations
separately.

## Parameters and JSON

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`; paged operations add `--page-size`, `--page-token`, and
`--batch-pages`. JSON values use `--attributes`, `--administrators`,
`--initial-members`, `--initial-permissions`, `--initial-role-assignments`,
`--marking-ids`, `--organizations`, `--principal-ids`, `--role-assignments`,
and `--where` where help shows them; `body` is the positional JSON batch form
on get-batch commands. Scalar or list variants include `--category-id`,
`--description`, `--display-type`, `--email`, `--enrollment-rid`,
`--expiration`, `--family-name`, `--given-name`, `--host`,
`--maximum-duration`, `--maximum-value`, `--name`, `--organization`,
`--provider-id`, `--status`, `--username`, and `--include`. Other positional
variants are the resource RIDs shown by `--help`. Boolean flags are
`--include-expirations`, `--preview`, and `--transitive`.

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

## File layout

```
.agents/skills/pal-found-admin/
├── SKILL.md
└── references/
    ├── 01-identity-auth-users.md
    ├── 02-identity-groups-roles.md
    └── 03-governance.md
```

Copy the entire `pal-found-admin` folder, including `references/`, so the
relative links above resolve offline. `references/03-governance.md` is owned
by DEV-STORY-043 and documented with the Audit skill.
