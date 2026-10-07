# Resource integration boundaries

[Branching and security](../applications-branching-security.md) · [Development guide](../../SKILL.md)

## Concept and lifecycle

Global branching coordinates supported resource configurations; each owning application
supplies its editing, rebase, approval and publication behavior. Supported integrations
include Workshop, Ontology, Functions, AIP Logic, Automate, Code Repositories, Pipeline
Builder, Restricted Views and lineage tools. Generated external OSDKs are not themselves
branchable. A global branch therefore does not automatically isolate all application code.

## Prerequisites

Prepare the affected resource types, dependency graph and supported templates. Function
branch development requires TypeScript v1 child template >=0.903.0, TypeScript v2 parent
>=0.1299.0 or Python parent >=0.724.0. TypeScript v2/Python additionally need a local
Ontology SDK. An environment owner prepares upgrades/dependencies; authorization and
branch-aware preview require enrollment. Local fixtures exercise business logic only.

## Procedure

1. List resource types and choose supported branch controls in each application. Use
   [global lifecycle](global.md) to create/select the shared branch and inspect its list.
2. In Ontology Manager save entity changes to the branch. Protected resources require
   a branch/proposal; migrations to project permissions may precede protection.
3. In Workshop save before rebase. Open Changelog when out-of-date, Start rebasing,
   inspect main/current branch/current session alternatives, resolve fields and Save.
4. For Functions publish an unstable branched version with a stable version target.
   Select that branched preview in Workshop/AIP Logic/function-backed Actions on the
   same branch. If the target changes, update all dependents before proposal checks.
5. In Pipeline Builder choose Global versus pipeline-local branch explicitly. When
   coordinating with repository data, configure matching build branch names/fallbacks.
6. Review each resource's checks and approvals. After merge inspect stable Function
   versions, application configurations and actual production builds separately.

## Worked example

Illustrative coordinated change: Shipment.priority is used by a Python Function and
Workshop display. Prepare a branch-capable Python repository with local bindings; save
priority in branched Ontology, regenerate local bindings and publish Function target
`1.4.0`. Choose its Branched pre-release in the same branch's Workshop module.

If main publishes 1.4.0 first, choose an unused target, update Workshop's function binding,
and rerun checks. At merge the selected target becomes a stable main Function. Other
historical preview versions are not also delivered. An external React application using
its generated OSDK needs its own supported SDK/release path and separate verification.

## Expected result and checks

Every dependency is either a supported branch resource or has a named independent delivery
step. Confirm main remains unchanged before merge, branch preview uses correct bindings,
and merged consumers use the stable target. Branched query Functions cannot currently be
depended on from TypeScript v1/v2 or Python repositories; redesign that dependency.
Pipeline Builder-created object types are not modifiable in Ontology Manager on a branch.

## Failures and recovery

| Observation | Recovery |
| --- | --- |
| Branched schema unavailable | Check template minimum/local Ontology SDK and regenerate branch imports. |
| Workshop edits lost on rebase | Save before rebase; recover through available change history rather than overwriting main. |
| Function target conflict | Choose unused target and update every dependent's binding. |
| External OSDK still uses old schema | Generate its approved new SDK/version and follow its independent release path. |
| Resource unsupported | Keep its release separate and verify cross-resource compatibility explicitly. |

Optional source attribution: [integration inventory](https://www.palantir.com/docs/foundry/global-branching/integrations),
[Function branch contract](https://www.palantir.com/docs/foundry/functions/branching-functions),
[Workshop rebase](https://www.palantir.com/docs/foundry/workshop/branching-integration),
[Ontology branches](https://www.palantir.com/docs/foundry/ontologies/branching-ontology),
[Pipeline Builder branches](https://www.palantir.com/docs/foundry/pipeline-builder/branches-overview).
