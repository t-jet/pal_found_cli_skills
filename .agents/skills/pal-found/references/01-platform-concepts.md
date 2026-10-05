# Platform concepts and resources

This part defines the Foundry resources the CLI works with and how a task maps
to a resource and its owning namespace skill. Read it from the general
`pal-found` skill before opening a namespace; each namespace skill also states
its own lifecycle and starting conditions.

## How the platform fits together

Data Connection and dataset uploads bring source data into Foundry. A dataset
stores files and records changes as transactions, so a pipeline can read a
specific branch or view rather than an unversioned file location. Build jobs
apply transformation logic and write new dataset versions; schedules decide
when builds should be attempted. Projects organize these resources and
control who can work on them, subject to markings and organization rules.

The Ontology turns selected data into business objects and links and brings
logic and actions alongside it. Applications and agents can then read those
objects and invoke governed actions. This is why a dataset, an Ontology
object type, and an action are related but distinct resources: loading files
does not by itself create an object type or expose an action. See the
[platform overview](https://www.palantir.com/docs/foundry/platform-overview/overview)
for the data, logic, and action model.

## Core resource model

| Concept | What it is | Owning namespace |
| --- | --- | --- |
| Project | A top-level container that groups folders and resources under a user-visible name. | `pal-found-filesystem` |
| Folder | A container inside a project that organizes resources by path. | `pal-found-filesystem` |
| Space | A scope for projects, their organization access, deletion policy, and defaults for storage and roles. | `pal-found-filesystem` |
| Resource | A general roll-up category that includes projects, folders, datasets, and documents exposed through `resource` operations. | `pal-found-filesystem` |
| Dataset | A versioned collection of files, either tabular with a schema or unstructured; branches refer to transaction history. | `pal-found-datasets` |
| Branch | A named pointer to dataset transaction history; the default is `master` in most enrollments. Branches do not merge. | `pal-found-datasets` |
| Transaction | A grouped set of changes to a dataset (created, then `commit` or `abort`). | `pal-found-datasets` |
| Schema | Column and type definitions applied to a dataset. | `pal-found-datasets` |
| File | A named binary blob stored inside a dataset's branch. | `pal-found-datasets` |
| View | A union of backing datasets evaluated when read, without storing their data files; optional primary key supports deduplication. | `pal-found-datasets` |
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
| Schedule / build | A schedule decides when to run; a build computes new dataset versions through jobs. A started run is not proof of a successful build. | `pal-found-orchestration` |
| SQL query | An ad-hoc SQL query with Arrow result downloads and lifecycle operations. | `pal-found-sql-queries` |
| Enrollment | The broad scope under which groups, organizations, and roles are governed. | `pal-found-admin` |
| Group / user / role | Identity subjects and the roles assigned to them. | `pal-found-admin` |
| Marking / organization | Governance constructs that control who can see or act on resources. | `pal-found-admin` |
| Audit log | A log file listing platform events; content can be downloaded. | `pal-found-audit` |
| Checkpoint | A justification prompt for a sensitive Foundry interaction; its submitted answer becomes a reviewable record. | `pal-found-checkpoints` |
| Data health check | A check and its latest report on data quality. | `pal-found-data-health` |
| Connection / import | An external source configuration and file or table sync definitions that write into datasets when executed. | `pal-found-connectivity` |
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
- **Media sets**: work with an existing set, use `create` to open a transaction,
  `upload` media, then `commit` (or `abort`) the transaction. `clear` removes
  media by path where the selected set and transaction policy allow it.
- **Streams**: create the dataset/stream, publish records, and have a
  subscriber read at committed offsets.
- **Orchestration**: a schedule `run` starts a build; a build processes
  jobs. Accepting a run/build is not proof it finished; check status.

Each namespace skill restates and extends this with the operations that
advance or read the resource.

## Cross-capability examples

A full task usually spans several resources. For example, to "load a file into
a dataset, compute a derived dataset, and expose it in the Ontology":

1. Upload a file into a dataset branch (`pal-found-datasets`).
2. Run a build or an existing schedule for the derived dataset
   (`pal-found-orchestration`); its transformation logic must already exist.
3. Once the dataset holds rows, its object type presents them to users
   (`pal-found-ontologies`).

A single CLI operation does not perform the whole workflow; each step is its
own record.
