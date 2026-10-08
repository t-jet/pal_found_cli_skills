# Foundry Platform REST operation catalog


Choose the API version and capability, then a resource and method. Each method links exact inputs, return modes and complete local model/error definitions. v1 and v2 identities are separate contracts; a release stage is an availability decision, not permission.

## Services

- [v1.datasets](v1/datasets/index.md)
- [v1.ontologies](v1/ontologies/index.md)
- [v2.admin](v2/admin/index.md)
- [v2.aip_agents](v2/aip_agents/index.md)
- [v2.audit](v2/audit/index.md)
- [v2.checkpoints](v2/checkpoints/index.md)
- [v2.connectivity](v2/connectivity/index.md)
- [v2.data_health](v2/data_health/index.md)
- [v2.datasets](v2/datasets/index.md)
- [v2.filesystem](v2/filesystem/index.md)
- [v2.functions](v2/functions/index.md)
- [v2.language_models](v2/language_models/index.md)
- [v2.media_sets](v2/media_sets/index.md)
- [v2.models](v2/models/index.md)
- [v2.ontologies](v2/ontologies/index.md)
- [v2.orchestration](v2/orchestration/index.md)
- [v2.sql_queries](v2/sql_queries/index.md)
- [v2.streams](v2/streams/index.md)
- [v2.third_party_applications](v2/third_party_applications/index.md)
- [v2.widgets](v2/widgets/index.md)

## Task selection

Governance applications start with Filesystem projects, folders and resources, then Admin identity/role/marking contracts where the task requires them. AIP applications select Agents/session or Models/language-model contracts; dataset pipelines select Datasets, Orchestration, health and checkpoint resources. Ontology applications choose the matching version's schema, objects, Actions and Queries. Connectivity, streams, SQL, Media Sets, Widgets, audit and application registration have their own services.

[Authentication](authentication.md) | [Response modes and finite work](client-behavior.md) | [REST authoring procedure](../rest-api.md)

[Part 1](catalog.md)
