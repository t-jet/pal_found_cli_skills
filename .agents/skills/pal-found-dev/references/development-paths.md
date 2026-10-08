# Development paths

[Development guide](../SKILL.md)

## Platform and tool selection

### Concept and lifecycle

Datasets hold pipeline inputs and outputs. The Ontology represents business
entities as objects and links and exposes governed Actions and Functions.
Applications consume those resources; they do not replace data preparation or
authorization. Projects organize resources and access. A workflow can span
several tools, each with its own saved artifact and completion state.

| Outcome | Suitable tool | Artifact and local route |
| --- | --- | --- |
| Visual data preparation | Pipeline Builder | Input/transform/output graph, previews and output build; continue with [pipelines](pipelines.md). |
| Custom transform logic or reusable code | Code Repositories | Versioned source, transform registration, tests and release; [pipelines](pipelines.md). |
| Interactive analysis before production authoring | Code Workspaces | Notebook or IDE work and explicit output publication; [environment selection](#environments-and-connectivity). |
| Business model, query, Action or Function | Ontology Manager and runtime-specific development tools | Type/link/interface or published logic; [Ontology](ontology-compute.md). |
| Operational interface inside Foundry | Workshop or Slate | Application configuration and governed interactions; [applications](applications-branching-security.md). |
| Custom client for selected Ontology entities | Developer Console and generated OSDK | Application registration, OAuth configuration, generated bindings and client code; [applications](applications-branching-security.md). |
| Custom React interface embedded in Workshop | Widget Set | Widget contract, hosted version and host configuration; [widgets](applications-branching-security.md). |
| Container workload | Compute Modules | Image, execution mode, resources and invocation contract; [Compute](ontology-compute.md). |
| Platform administration or resource integration | Foundry Platform REST SDK or HTTP | Request/response contracts and code; [REST](rest-api.md). |

Pipeline Builder and Code Repositories can exchange datasets. Choose a visual
stage for maintained graph transformations, and a code stage for logic or
libraries that need explicit code. OSDK is generated for selected Ontology
entities. The platform REST SDK addresses platform resources such as folders,
datasets, builds, users and AIP services. They are separate interfaces.

### Prerequisites

Obtain the desired output, resource identifiers or approved existing paths,
data/schema examples, intended identity and environment constraints from the
task. Determine which resources that identity may read or modify. For an
application, identify the OAuth client and selected entities or API service.
For code, identify the prepared runtime and repository. For a container,
identify the prepared image and permitted resource configuration.

Tool selection and code planning work locally with supplied metadata and
fixtures. Resource creation, tenant-specific registration, preview, build and
deployment need authorized enrollment access. Administrators control available
capabilities, runtime access and organizational security policy. A missing
binding or credential is a specific prerequisite, not an invitation to guess.

### Procedure

1. State the final artifact and observable result: a dataset refresh, object
   edit, UI interaction, resource change or model/agent result.
2. Identify the resource lifecycle that produces it. Select the table row
   matching that lifecycle; split tasks crossing pipeline and application work.
3. Record identifiers, schemas, execution identity and branch context. Use
   authorized tenant metadata or supplied fixtures for values specific to the
   enrollment, rather than treating an example API name as universal.
4. Open the corresponding local guide. Verify its prerequisites and supported
   runtime/version before adapting its example.
5. Plan authoring, tests, release and result checks separately. Include the
   adverse case that would prevent the intended result.

### Worked example

Illustrative task: produce a daily `orders_clean` output, let operators approve
an order, and keep project folders organized for a governance application.

| Work item | Selection | Required evidence |
| --- | --- | --- |
| Join orders/customers and reject missing customer IDs | Python Code Repository transform | Prepared input schemas, tested join/expectation, release and successful output build. |
| Display an Order and apply an approval | OSDK React application and existing Action | Generated Order/Action bindings, OAuth configuration, permitted user, accepted validation result and verified edit. |
| Discover project/folder hierarchy and modify a folder | Platform REST SDK Filesystem contracts | Authorized project/folder IDs, traversal results, exact modification request and subsequent effect check. |
| Add agent assistance when requested | Platform REST AIP contracts | Available agent/model/version, session or request model, execution result and finite recovery limits. |

These are distinct artifacts. An approved Action does not refresh a dataset;
a successful folder change does not grant the client new resource permissions.
Open [REST development](rest-api.md) for governance and AIP method discovery,
inputs, version/stage decisions and response/error handling.

### Expected result and checks

The plan names an authoring tool, prerequisites, local guide, output artifact,
success observation and failure response for each work item. Check that every
required fact is reachable locally. A selected tool alone is not proof of a
completed pipeline, application or API operation.

### Failures and recovery

If the chosen tool cannot represent the required logic, move that stage to a
supported code or container path and retain explicit input/output contracts.
If tenant metadata, bindings or capability enablement are absent, record the
blocked operation and request the artifact from its organizational owner.
If resource access is denied, verify the acting identity and permitted scope;
do not infer access from a successful login. Reconcile uncertain writes using
the local resource-specific guide before attempting another mutation.

## Environments and connectivity

### Concept and lifecycle

Code Repositories provide a Foundry IDE with Git-backed source and checks.
Code Workspaces provide hosted JupyterLab, RStudio and VS Code environments.
A local VS Code environment runs on the developer's machine. Hosted and local
environments differ in data handling, permissions and available extensions.
Remote preview or production execution remains a Foundry service operation.

### Prerequisites

| Environment | Prepared artifacts | Access boundary |
| --- | --- | --- |
| Local fixture authoring/testing | Source, matching runtime/dependencies, data fixtures and generated bindings where used | Can run without public or enrollment access; results prove fixture behavior. |
| Local preview against Foundry | Prepared VS Code/Palantir tooling and credentials | Administrator-enabled local preview and download permissions on every input; data streams into local memory. |
| Foundry-hosted workspace | Enabled Code Workspaces, repository/resource access and chosen runtime | Needs authorized enrollment connectivity; computation/data stay on platform apart from displayed preview results. |
| Live SDK/application operation | Prepared SDK or generated client, host/client configuration and authorized identity | Needs enrollment connectivity and resource permission; private/beta capabilities may need enablement. |

For local preview, the documented download operations include
`s3-proxy:datasets-read` and `api:datasets-read`. Third-party extensions are
supported locally when organizational policy allows them; the compared hosted
VS Code workspace does not support them. A token's existence does not establish
input download permission or capability enablement.

### Procedure

1. Record whether public documentation access, enrollment access, or both are
   restricted. Do not describe these as the same condition.
2. Confirm the prepared runtime version, dependency set, bindings, image or IDE
   tooling required by the selected local procedure.
3. For real-data preview, choose hosted execution when data must remain on the
   platform. Choose local preview only when policy and input permissions allow
   it. For disconnected work, supply synthetic data or permitted fixtures.
4. Verify identity, host, selected resource and branch before a live step.
5. Run local tests first; record their scope. Perform remote preview/build or
   application publication only with enrollment access, then inspect its
   documented outcome separately.

### Worked example

Prepared task inputs: Python source and synthetic orders/customers tables,
matching Python packages, repository branch metadata and a recorded failed
expectation. Public browsing is blocked; enrollment connectivity is absent.

Author the transform and expectation, run its fixture tests, and derive a
release plan using the [pipeline guide](pipelines.md). Record the local test
result and expected remote checks. Mark remote preview, merge/release and
production build as pending enrollment steps. If real-data download permission
is unavailable later, use the enabled hosted workspace path for preview.
The record must not claim that fixture execution published code or data.

### Expected result and checks

The chosen environment satisfies data handling policy and runtime requirements.
Evidence names what ran locally, what remains an enrollment step and which
administrator-controlled prerequisite is missing. Compare preview input
context with the intended production branch before trusting its result.

### Failures and recovery

An unavailable runtime or binding blocks the step using it; name the missing
artifact and provisioning owner. A local preview denial may require input
download permission or administrator enablement, while a denied remote
operation requires its own resource/identity check. Authentication success
does not settle either case. If local tests pass but remote execution fails,
compare schemas, branch-resolved inputs, runtime dependencies, credentials and
compute configuration before changing transformation logic.

## Optional source attribution

- [Developer toolchain](https://www.palantir.com/docs/foundry/dev-toolchain)
- [Pipeline Builder and Code Repositories](https://www.palantir.com/docs/foundry/building-pipelines/considerations-pb-cr)
- [Code Workspaces](https://www.palantir.com/docs/foundry/code-workspaces)
- [Local versus hosted VS Code](https://www.palantir.com/docs/foundry/vs-code/local-vs-workspace-guide)
- [Developer Console](https://www.palantir.com/docs/foundry/developer-console/overview)

[Back to development guide](../SKILL.md)
