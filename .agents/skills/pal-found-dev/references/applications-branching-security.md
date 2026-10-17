# Applications, branching, and security

[Development guide](../SKILL.md) · [Ontology and Compute](ontology-compute.md)

Developer Console defines a custom application's OAuth client, selected resources
and generated OSDK. React clients query operational objects and invoke governed
Actions. Workshop custom widgets embed prepared components through a Widget Set,
with declared parameters and events connecting them to the surrounding module.
Source compilation, hosted assets, authentication and authorized business effects
must each be verified before delivery.

## Application and widget procedures

| Task | Guide |
| --- | --- |
| Register an application, prepare generated bindings and authentication | [Application registration and generated SDK](applications/osdk.md) |
| Query/edit objects and release a React client | [React query and release lifecycle](applications/react.md) |
| Create a Widget Set and release assets | [Widget Set creation and releases](widgets/lifecycle.md) |
| Test a component in Playground and Workshop | [Playground and Workshop previews](widgets/testing.md) |
| Connect Workshop data and events | [Parameters and events](widgets/integration.md) |
| Share widgets and deliver reusable products | [Widget and Marketplace distribution](widgets/distribution.md) |

## Branch and authorization procedures

Git source branches, dataset transaction branches and global configuration branches
have different scopes. Name each context and inspect resolved inputs/outputs rather
than inferring isolation from a shared name. Project roles, mandatory controls, OAuth
restrictions, object policies and execution identities also govern separate boundaries.

| Task | Guide |
| --- | --- |
| Coordinate supported resources and merge a proposal | [Global branch lifecycle](branching/global.md) |
| Review source and protect repository branches | [Git review and branch settings](branching/git.md) |
| Distinguish Git/global/build/data contexts | [Select and verify branch contexts](branching/contexts.md) |
| Resolve dataset histories and fallback inputs | [Dataset branches and fallbacks](branching/datasets.md) |
| Coordinate application-specific branch/release behavior | [Resource integration boundaries](branching/integrations.md) |
| Prepare projects, references and resource grants | [Projects and resource boundaries](security/platform.md) |
| Diagnose application scopes and Ontology access | [Application and Ontology permission checks](security/applications.md) |
| Verify Compute identities and branch permissions | [Execution identity and branch authorization](security/compute-branches.md) |

The local guides include prerequisites, worked examples, expected states and recovery.
Public links within them serve only as source attribution. Live Foundry operations need
authorized enrollment access even when public internet is unavailable.
