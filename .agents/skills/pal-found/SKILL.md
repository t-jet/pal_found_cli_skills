---
name: pal-found
description: Offline entry point for Palantir Foundry knowledge shared by all pal-found-* CLI skills: platform concepts, the 18-namespace operation inventory, UserTokenAuth + .env setup, the access-control model, TOON vs JSON output rules, exit-code troubleshooting, retries/timeouts, and relative-link navigation to local reference parts.
---

# Foundry Platform Primer and Navigation

This skill is the offline entry point for the `pal-found-*` namespace skills.
Read it to learn what Foundry is, which resources and identifiers the CLI uses,
how authorization and access control work, and how to interpret output and
failures. Then open the namespace skill for the capability you have been asked
to act on. Each namespace folder is independently usable: it carries the
concepts, prerequisites, inputs, effects, outputs, and failure rules it needs.

This skill holds only the general knowledge the namespace skills share. It
cannot substitute for a namespace's operational guidance, and it never grants
access.

## Platform description

Palantir Foundry is a data operations platform for managing data, developing
an Ontology, and building analytics, workflows, and applications on top of
those layers. The `pal-found-*` CLI exposes selected Foundry API v2 clients;
it does not replace Foundry applications or change platform permissions.

Source: [Palantir, integrated platforms](https://www.palantir.com/docs/foundry/architecture-center/platforms); reviewed 2026-08-13. This source link is maintenance evidence for maintainers; it is not needed to use the skill offline.

## 1. Read the shared foundations first

| Part | What it covers |
| --- | --- |
| [Platform concepts and resources](references/01-platform-concepts.md) | Projects, datasets, branches, transactions, Ontology objects and actions, models, streams, media, administration, and how a task maps to a resource. |
| [Identifiers, auth, and access control](references/02-identifiers-auth-access.md) | RIDs, paths, names, tokens, hostname, `.env` setup, and the access-control precedence model. |
| [Output, success, and failure](references/03-output-success-failure.md) | TOON vs JSON, exit codes, retries, timeouts, paging, and how to avoid claiming an unproven Foundry change. |
| [Shared command options](references/04-shared-options.md) | `--timeout`, `--format`, `--pretty`, paging, and batch flags where the namespace parser supports them. |

The four parts above repeat a small amount of vocabulary on purpose so a
namespace can be read alone. If a claim here conflicts with a namespace part,
the namespace part wins for that namespace.

## 2. Namespace navigation map

The installed CLI exposes 18 namespace commands. Each has a skill folder.
Start from a task's Foundry resource and desired outcome, then open the
namespace skill for the capability that owns it.

| If the task is about | Open this skill | Installed command | Operations |
| --- | --- | --- | ---: |
| Enrollment, groups, roles, users, authentication providers | `pal-found-admin` | `pal-found-admin` | 66 |
| Markings, CBAC, organizations, hosts (governance) and audit log files | `pal-found-admin`, `pal-found-audit` | `pal-found-admin`, `pal-found-audit` | 28+2 |
| Datasets, branches, files, transactions, views | `pal-found-datasets` | `pal-found-datasets` | 33 |
| Projects, folders, resources, roles, spaces | `pal-found-filesystem` | `pal-found-filesystem` | 31 |
| Ontology object types, actions, attachments, time series | `pal-found-ontologies` | `pal-found-ontologies` | 67 |
| AIP agents, sessions, functions, language models | `pal-found-aip-agents`, `pal-found-functions`, `pal-found-language-models` | matching commands | 24 |
| ML models, experiments, model studio | `pal-found-models` | `pal-found-models` | 23 |
| Builds, schedules, SQL query lifecycle | `pal-found-orchestration`, `pal-found-sql-queries` | matching commands | 25 |
| Records, offsets, subscription | `pal-found-streams` | `pal-found-streams` | 15 |
| Media lifecycle and transactions | `pal-found-media-sets` | `pal-found-media-sets` | 19 |
| Connections, checkpoints, data quality checks | `pal-found-connectivity`, `pal-found-checkpoints`, `pal-found-data-health` | matching commands | 29 |
| Third-party apps, websites, widget-sets | `pal-found-third-party-applications`, `pal-found-widgets` | matching commands | 17 |

The implemented total is **351** operations across 18 namespace skills.
`geo` and `core` are SDK namespaces with no public CLI-callable operations and
no skill folders. Four legacy Widgets design-catalogue entries are not in the
installed runtime and are documented as unsupported, never callable.

## 3. End-to-end map: task to resource to operation

1. Name the Foundry resource the task targets (for example, a dataset, an
   ontology object type, a schedule, a stream).
2. Find the resource in the navigation map above and open the owning namespace
   skill.
3. The namespace skill lists its resource clients and operations and links
   each to a local operation record.
4. Read the record's preconditions, inputs, effect, and result rules before
   invoking the installed command.
5. Invoke `pal-found-<namespace> <resource> <operation> [options]`.
6. Interpret the result or failure using the shared output and exit-code
   rules in [Output, success, and failure](references/03-output-success-failure.md).

No namespace is callable unless it has a reachable, documented operation
record. If the namespace skill does not describe the operation you need,
stop and ask rather than guessing a command.

## Install requirement

`pal-found-*` commands are provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

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
.agents/skills/pal-found/
├── SKILL.md
└── references/
    ├── 01-platform-concepts.md
    ├── 02-identifiers-auth-access.md
    ├── 03-output-success-failure.md
    └── 04-shared-options.md
```

Copy the entire `pal-found` folder, including `references/`, so the relative
links above resolve offline.
