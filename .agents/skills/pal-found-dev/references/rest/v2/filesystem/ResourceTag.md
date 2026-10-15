# ResourceTag: filesystem operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

Resource tags label a resource for organization. They do not replace access requirements or markings. Check the current tags before changing them.

Prepare SDK 1.101.0 and an identity authorized for the exact tenant resource. Check each contract for its API stage and endpoint-specific restrictions. No universal role or retry guarantee is implied by these operations. For an uncertain write, read the exact RID and effect before repeating it.

## Python client route

With a configured `FoundryClient` named `client`, use `client.filesystem.Resource.Tag` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.

## Operations

### add

Apply the requested tags to the resource. Verify the resulting direct tag list rather than assuming tags change permissions.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/ResourceTag/add.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/ResourceTag/add.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### list

List tags applied to the selected RID. Keep tag names distinct from security Markings.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/ResourceTag/list.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/ResourceTag/list.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### remove

Remove only selected tags and confirm the remaining direct tags.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/ResourceTag/remove.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/ResourceTag/remove.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.
