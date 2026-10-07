# Projects and resource boundaries

[Branching and security](../applications-branching-security.md) · [Development guide](../../SKILL.md)

## Concept and lifecycle

Projects organize collaboration and discretionary role grants. Resource operations still
need applicable mandatory controls: organizations, markings and classifications. Those
controls remain relevant through derivation. Project roles alone do not make protected
data distributable. A project reference exposes an upstream dependency to work in another
project; it does not relocate ownership or universally grant direct upstream access.

Pipeline logic and output belong together in their project. To consume resources in a
different project, use an approved reference. Keep project-level grants in groups where
possible; inspect actual role operations because administrators can customize role sets.

## Prerequisites

Prepare source/destination project RIDs, resource RIDs, desired readers/editors, applicable
mandatory controls and approved groups. Obtain IDs from Compass resource/project details.
Project creation requires Editor or Owner on its space. Permission or mandatory-control
changes require authorized owners/administrators. Local architecture/fixture work can
plan access; real resource operations and effective access need enrollment checks.

## Procedure

1. In Compass open the intended project and inspect Sharing & permissions, inherited
   roles, organization/marking/classification requirements and group membership.
2. Place logic and output in the correct project. For an upstream dependency, use the
   source resource's reference/share action and choose the approved destination project.
   Typically source Viewer and destination Editor are needed; verify enabled operations.
3. Grant the intended group the minimum role operations on the project. Check resource
   inheritance/custom settings; a role label alone is not proof of effective access.
4. Verify a read/build using the actual developer/job identity, then verify downstream
   readers against output controls. Test a deliberately denied reader as well.
5. Record resource ownership and access requests. Users lacking access can select Request
   access/Request additional access and specify the approved role/group with justification.

## Worked example

Illustrative split: Raw Logistics holds sensitive orders; Dispatch Analytics holds its
repository and totals output. A pipeline developer needs the approved raw read and
analytics write/build operations. Create a reference to orders inside Analytics and
register it as a transform input. A dashboard viewer reads totals in Analytics.

Test the viewer's output access separately from opening raw orders. An output project
role does not grant raw-project Viewer. Conversely an inherited mandatory marking can
still deny totals despite its Viewer grant. Confirm whether the approved aggregation
may retain or alter controls through the organization's authorized security workflow.
Do not remove controls merely to make a preview pass.

## Expected result and checks

Capture project/resource IDs, reference target, acting identities, effective operations,
mandatory controls and allowed/denied results. A build success must identify the expected
output owner/project. Navigation that lists a folder proves discovery only; test the
specific requested read/edit/build. [REST governance contracts](../rest-api.md) cover
folder navigation/moves/references with exact request/result/error models.

## Failures and recovery

| Observation | Recovery |
| --- | --- |
| Resource visible but read denied | Inspect mandatory controls and actual read operation, not only discovery. |
| Cross-project build denied | Verify reference, source read and destination write/build rights under job identity. |
| User can read output but not raw | Compare separate project grants; grant raw access only if authorized. |
| New folder silently changes access | Inspect inherited controls before moving dependent resources. |
| Access request pending | Identify project/group/marking approver and retain the existing authorized scope. |

Optional source attribution: [project roles and references](https://www.palantir.com/docs/foundry/security/projects-and-roles).
