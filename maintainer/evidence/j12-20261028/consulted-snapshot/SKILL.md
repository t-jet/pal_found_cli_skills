---
name: pal-found-dev
description: Foundry development guide for choosing pipeline and application tools, building Python and SQL pipelines, modeling the Ontology, developing Compute Modules and OSDK or Workshop applications, managing branches and releases, securing resources, using Foundry REST APIs, and operating production workflows.
---

# Develop on Foundry

Use this skill when designing or changing a Foundry data pipeline, Ontology,
application, custom widget, Compute Module, or API integration. Foundry
development crosses several lifecycles: code changes, dataset transactions,
Ontology configuration, application authorization, and production builds. Read
the part that matches the task before choosing an implementation path.

Foundry ingests data into datasets and streams, transforms it in pipelines,
models operational concepts as Ontology objects and links, and makes governed
Actions and Functions available to users and applications. Pipeline Builder
provides a graph and form interface for data pipelines. Code Repositories
holds Git-versioned transforms and Functions. Workshop and Slate build Foundry
applications; Developer Console configures an application and generates an
Ontology SDK (OSDK) for custom clients. Compute Modules run containerized
compute for supported execution modes.
Start with [platform and tool selection](references/development-paths.md#platform-and-tool-selection)
and [environments and connectivity](references/development-paths.md#environments-and-connectivity).
Public links in this skill are optional source attribution. Use the local
procedures and examples for development decisions.

## Choose a development path

| Need | Start with | Why |
| --- | --- | --- |
| Shape, join, and deliver governed data with visual feedback | [Pipeline Builder](references/development-paths.md#platform-and-tool-selection) | Graph and form authoring supports previews, output checks, schedules, and collaboration. |
| Write Python, SQL, or specialized transform logic | [Code Repositories](references/pipelines.md) | Git branches, reviews, tests, and code execution support production code. |
| Explore data interactively in notebooks or an IDE | [Code Workspaces](references/pipelines/workspaces.md) | JupyterLab, RStudio, and VS Code environments integrate with Foundry data and repositories. |
| Build an operational app inside Foundry | [Workshop or Slate](references/applications-branching-security.md) | Workshop uses Ontology-backed widgets; Slate allows more UI customization. |
| Build a custom web or Python app against Ontology resources | [Developer Console and OSDK](references/applications-branching-security.md) | Configure an OAuth client and generate an application-specific SDK. |
| Embed a React component in Workshop | [Custom Widgets](references/applications-branching-security.md) | A Widget Set supplies hosted components, parameters, and events. |
| Run a custom container as a function or pipeline component | [Compute Modules](references/ontology-compute.md) | Bring containerized compute into the appropriate execution mode. |
| Integrate an external client or service through HTTP | [REST APIs](references/rest-api.md) | Select the API family and authorization model before coding requests. |
| Navigate projects/folders and perform governed resource changes | [REST governance application](references/rest-api.md) | Filesystem contracts supply resource navigation and modification; administrative contracts cover distinct identity and governance controls. |
| Develop an AIP integration using agents or model capabilities | [REST AIP application](references/rest-api.md) | Discover a supported agent/session or model operation and check its availability, inputs, result lifecycle, and execution limits. |

Pipeline Builder and Code Repositories can feed the same pipeline through
datasets. Start with Pipeline Builder for a visual pipeline; add a Code
Repositories stage when a transformation needs a custom library, an external
API call, or code-specific logic. Review branch, test, build, and release
behavior in the [pipeline guide](references/pipelines.md) before production.
The [local selection procedure](references/development-paths.md#platform-and-tool-selection)
explains these choices and their prerequisites.

## Read by task

| Task | Guide |
| --- | --- |
| Tool selection, prepared runtime, identity and connectivity boundaries | [Development paths](references/development-paths.md) |
| SQL syntax, declared datasets and output validation | [SQL transforms](references/pipelines/sql.md) |
| Notebook data preparation and publication | [Workspace exploration and publication](references/pipelines/workspaces.md) |
| Python or SQL transforms, local development, tests, builds, transactions, pipeline release | [Pipelines and development workflow](references/pipelines.md) |
| Ontology types, object sets, actions, functions, Compute Modules | [Ontology and Compute Modules](references/ontology-compute.md) |
| OSDK/React, Workshop widgets, Git/dataset/global branching, security | [Applications, branching, and security](references/applications-branching-security.md) |
| REST API and Python SDK integration | [REST API development](references/rest-api.md) |
| Schedules, lineage, observability, health checks, production support | [Production operations](references/operations.md) |

The optional `pal-found` and `pal-found-*` CLI skills cover supported command
operations. This guide also covers Foundry workflows outside that CLI surface.

## Evidence before delivery

Name the resource, identity and branch context before changing it. A passing
local test, remote preview, code release, committed dataset transaction and
completed production build establish different outcomes. Record the evidence
for the task's actual outcome and follow its local failure/recovery procedure.
Prepared Python/Node environments, generated bindings, container artifacts,
credentials and enabled platform capabilities are prerequisites where needed.
Public documentation access is unnecessary; live Foundry operations still
require authorized enrollment connectivity and permission.
