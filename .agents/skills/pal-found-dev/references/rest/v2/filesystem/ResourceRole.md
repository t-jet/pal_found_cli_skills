# ResourceRole: filesystem operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

Resource roles grant a principal an explicit role on one resource. Resolve the principal and role name from the enrollment, inspect existing assignments, and verify the effective assignment after a change.

Prepare SDK 1.101.0 and an identity authorized for the exact tenant resource. Check each contract for its API stage and endpoint-specific restrictions. No universal role or retry guarantee is implied by these operations. For an uncertain write, read the exact RID and effect before repeating it.

## Operations

### add

Assign a documented role to the intended principal on this resource. Verify the role list before relying on the grant.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/ResourceRole/add.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/ResourceRole/add.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### list

List the roles on the selected resource. Use this to verify specific principals and role names after a change.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/ResourceRole/list.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/ResourceRole/list.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### remove

Remove a specific role assignment from this resource and confirm it is absent from the subsequent role list.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/ResourceRole/remove.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/ResourceRole/remove.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.
