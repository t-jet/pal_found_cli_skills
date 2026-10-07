# Ontology and Compute Modules

[Development guide](../SKILL.md) · [Applications and security](applications-branching-security.md)

The Ontology maps operational data into objects, properties and links. Interfaces
let related object types share a contract. Queries retrieve object sets; Functions
provide typed logic; Actions validate and apply operational edits. Type configuration,
object visibility and permission to submit edits are separate controls.

Compute Modules host prepared containers. Function mode serves registered calls;
Pipeline mode supports autonomous processing with declared resources and job access.
Container readiness, a successful invocation and durable resource writes establish
different outcomes. Use the execution identity and explicit resource protocol for the task.

## Local procedures

| Task | Guide |
| --- | --- |
| Model objects, primary keys, properties, links and datasources | [Object modeling](ontology/modeling.md) |
| Share contracts across types | [Interfaces](ontology/interfaces.md) |
| Query object sets and verify results | [Queries](ontology/queries.md) |
| Validate and apply operational changes | [Actions](ontology/actions.md) |
| Choose a Function runtime, preview and publish | [Function runtimes and publication](ontology/functions.md) |
| Distinguish configuration, object and Action access | [Object and Action authorization](ontology/security.md) |
| Build, configure and deploy a container | [Container configuration and lifecycle](compute/lifecycle.md) |
| Select Function/Pipeline modes and verify provenance | [Execution modes and provenance](compute/execution.md) |
| Register SDK functions, authenticate and configure Sources | [SDK integration and Sources](compute/integration.md) |

For coordinated schema/Function/application changes use [resource integration boundaries](branching/integrations.md).
For generated application bindings use [Developer Console and OSDK](applications/osdk.md).
Platform REST clients use the [complete local REST contracts](rest-api.md).
