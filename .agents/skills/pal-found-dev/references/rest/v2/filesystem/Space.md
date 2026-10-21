# Space: filesystem operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

A Space groups projects and resources. Its identity and display name differ. Empty a Space deliberately before deletion; a nonempty Space cannot be deleted through this operation.

Prepare SDK 1.101.0 and an identity authorized for the exact tenant resource. Check each contract for its API stage and endpoint-specific restrictions. No universal role or retry guarantee is implied by these operations. For an uncertain write, read the exact RID and effect before repeating it.

## Python client route

With a configured `FoundryClient` named `client`, use `client.filesystem.Space` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.

## Operations

### create

Create a Space with the chosen name and Organizations. Retain the returned RID for project creation and later updates.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/Space/create.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/Space/create.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### delete

Delete the exact Space RID only after its projects and resources have been removed. Confirm it is empty before calling.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/Space/delete.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/Space/delete.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### get

Read Space metadata by RID and verify its name and organization association.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/Space/get.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/Space/get.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### list

Discover accessible Spaces with bounded pagination. Retain the RID of the intended Space instead of selecting by name alone.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/Space/list.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/Space/list.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### replace

Update the selected Space and compare returned name/organization fields with the proposed change.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/Space/replace.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/Space/replace.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.
