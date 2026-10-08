# ProjectResourceReference: filesystem operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

Project resource references connect a project to resources that may live elsewhere. A reference does not copy the target or grant permission to read it. Use the project RID and target resource RID distinctly.

Prepare SDK 1.101.0 and an identity authorized for the exact tenant resource. Check each contract for its API stage and endpoint-specific restrictions. No universal role or retry guarantee is implied by these operations. For an uncertain write, read the exact RID and effect before repeating it.

## Operations

### add

Add the intended resource RIDs as references to the project. Read the project reference list afterward to confirm each association.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/ProjectResourceReference/add.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/ProjectResourceReference/add.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### list

List references held by the selected project. Bound pagination and resolve target resources separately when their details are needed.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/ProjectResourceReference/list.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/ProjectResourceReference/list.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### remove

Remove the specified associations from the project. Confirm the removed target RIDs disappear from the reference list; the resources themselves remain separate.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/ProjectResourceReference/remove.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/ProjectResourceReference/remove.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.
