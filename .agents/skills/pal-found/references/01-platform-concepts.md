# Platform concepts and resources

This part defines the Foundry resources the CLI works with and how a task maps
to a resource and its owning namespace skill. Read it from the general
`pal-found` skill before opening a namespace; each namespace skill also states
its own lifecycle and starting conditions.

## Core resource model

| Concept | What it is | Owning namespace |
| --- | --- | --- |
| Project | A top-level container that groups folders and resources under a user-visible name. | `pal-found-filesystem` |
| Folder | A container inside a project that organizes resources by path. | `pal-found-filesystem` |
| Space | A named container that scopes resource creation, often used to isolate work. | `pal-found-filesystem` |
| Resource | A general roll-up category that includes projects, folders, datasets, and documents exposed through `resource` operations. | `pal-found-filesystem` |
| Dataset | Tabular data stored in named branches; each branch holds an ordered set of transactions. | `pal-found-datasets` |
| Branch | A named line of dataset history; a dataset usually has a default branch (for example `main`). | `pal-found-datasets` |
| Transaction | A grouped set of changes to a dataset (created, then `commit` or `abort`). | `pal-found-datasets` |
| Schema | Column and type definitions applied to a dataset. | `pal-found-datasets` |
| File | A named binary blob stored inside a dataset's branch. | `pal-found-datasets` |
| View | A derived dataset backed by one or more source datasets. | `pal-found-datasets` |
| Ontology | The semantic layer over datasets: object types, object sets, links, action types, query types. | `pal-found-ontologies` |
| Object type | A typed view of dataset rows; each row becomes an object. | `pal-found-ontologies` |
| Object set | A collection of objects, possibly filtered or derived. | `pal-found-ontologies` |
| Action type | A declared change an agent or user can apply to objects, with parameters. | `pal-found-ontologies` |
| Query type | A declared read/function over the ontology with typed parameters. | `pal-found-ontologies` |
| Function | A server-side query (with value types and versioning) callable from the CLI. | `pal-found-functions` |
| AIP agent | A conversational Foundry agent with sessions, content, and traces. | `pal-found-aip-agents` |
| Language model | An inference endpoint; the CLI exposes Anthropic messages and OpenAI embeddings. | `pal-found-language-models` |
| Media set | A store for unstructured binary media with a transaction lifecycle. | `pal-found-media-sets` |
| Stream | A time-ordered record stream; subscribers consume records at committed offsets. | `pal-found-streams` |
| Model | An ML model artifact, its versions, live deployments, experiments, and Model Studio resources. | `pal-found-models` |
| Schedule / build | Orchestration resources: scheduled runs, builds, jobs, and their versions. | `pal-found-orchestration` |
| SQL query | An ad-hoc SQL query with Arrow result downloads and lifecycle operations. | `pal-found-sql-queries` |
| Enrollment | The broad scope under which groups, organizations, and roles are governed. | `pal-found-admin` |
| Group / user / role | Identity subjects and the roles assigned to them. | `pal-found-admin` |
| Marking / organization | Governance constructs that control who can see or act on resources. | `pal-found-admin` |
| Audit log | A log file listing platform events; content can be downloaded. | `pal-found-audit` |
| Checkpoint | A named record holding external system state. | `pal-found-checkpoints` |
| Data health check | A check and its latest report on data quality. | `pal-found-data-health` |
| Connection / import | An external data source (connection) and the file/table imports from it. | `pal-found-connectivity` |
| Third-party application | A website/app that can be deployed and versioned through the CLI. | `pal-found-third-party-applications` |
| Widget set | A collection of Foundry widgets managed in a repository, with releases. | `pal-found-widgets` |

## From task to resource

When you receive a task:

1. Identify the resource the task names or implies. Resource names in a task
   (for example "the `orders` dataset" or "the `Customer` object type") map to
   the concepts above.
2. For analytics over tabular data, the resource is usually a dataset (or a
   derived view). For semantic access, it is an ontology object type or object.
3. For automation or governance, the resource is a schedule, a build, an
   enrollment subject, or a marking.
4. Once you know the resource, open the owning namespace skill from the
   navigation map in the general skill.

## Lifecycle and state

Resources are not all static. Several namespaces model a lifecycle:

- **Datasets**: `create` the dataset, work on a `branch`, open a
  `transaction`, `commit` or `abort` it.
- **Ontology actions**: `apply` an action to change objects; the result may
  depend on the object's current state.
- **Media sets**: `create` the set, `create` a transaction, `upload` media,
  `commit` (or `abort`/`clear`) the transaction.
- **Streams**: create the dataset/stream, publish records, and have a
  subscriber read at committed offsets.
- **Orchestration**: a schedule `run` starts a build; a build processes
  jobs. Accepting a run/build is not proof it finished; check status.

Each namespace skill restates and extends this with the operations that
advance or read the resource.

## Cross-capability examples

A full task usually spans several resources. For example, to "load a file into
a dataset, build an image from it, and expose it in the ontology":

1. Upload a file into a dataset branch (`pal-found-datasets`).
2. Configure a transformer or schedule to build an updated dataset
   (`pal-found-orchestration`).
3. Once the dataset holds rows, its object type presents them to users
   (`pal-found-ontologies`).

A single CLI operation does not perform the whole workflow; each step is its
own record.
