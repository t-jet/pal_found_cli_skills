# Resource: filesystem operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

A resource RID remains the stable identity when its path changes. Read access requirements, markings, roles and tags separately. Trash and permanent deletion have different recovery paths.

Prepare SDK 1.101.0 and an identity authorized for the exact tenant resource. Check each contract for its API stage and endpoint-specific restrictions. No universal role or retry guarantee is implied by these operations. For an uncertain write, read the exact RID and effect before repeating it.

## Python client route

With a configured `FoundryClient` named `client`, use `client.filesystem.Resource` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.

## Operations

### add_markings

Add selected Markings to this resource. Read direct Markings and access requirements afterward because inherited requirements also affect visibility.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/Resource/add_markings.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/Resource/add_markings.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### delete

Move this RID to trash. Record its parent/path and check trash status; restore is possible until it is permanently deleted.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/Resource/delete.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/Resource/delete.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### get

Read one RID and check type, parent and trash status before using it as an input to another operation.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/Resource/get.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/Resource/get.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### get_access_requirements

Inspect direct and inherited Organizations and Markings required to view this resource. Use the result to diagnose access; it does not grant those requirements.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/Resource/get_access_requirements.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/Resource/get_access_requirements.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### get_batch

Fetch up to 1,000 resource RIDs. Result is a RID-to-resource map; missing, inaccessible, root-folder and space entries may be absent.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/Resource/get_batch.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/Resource/get_batch.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### get_by_path

Resolve an absolute path to a resource. Retain the returned RID for later writes because a path can change.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/Resource/get_by_path.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/Resource/get_by_path.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### get_by_path_batch

Resolve up to 1,000 absolute paths. Match each returned item by path/RID and report unresolved paths; omitted paths may be missing, inaccessible or root entries.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/Resource/get_by_path_batch.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/Resource/get_by_path_batch.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### markings

Read Markings directly applied to this RID. Compare with access requirements when inherited Markings matter.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/Resource/markings.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/Resource/markings.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### permanently_delete

Permanently remove a directly trashed RID after verifying exact identity and trash status. `ResourceNotTrashed` means the required precondition is absent.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/Resource/permanently_delete.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/Resource/permanently_delete.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### remove_markings

Remove only the named direct Markings, then reread direct and inherited requirements. Removing a direct Marking does not remove an inherited one.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/Resource/remove_markings.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/Resource/remove_markings.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### restore

Restore the RID and its directly trashed ancestors. Read its resulting parent/path and trash status; an already active resource is left as it is.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/Resource/restore.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/Resource/restore.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

## Resolve access, then change one resource

Use a prepared `FoundryClient` and a RID selected from an authorized folder or
project read. Check the returned RID before applying any change. Direct
Markings and effective access requirements answer different questions:

```python
resource = client.filesystem.Resource.get(resource_rid, request_timeout=30)
assert resource.rid == resource_rid
requirements = client.filesystem.Resource.get_access_requirements(
    resource_rid, request_timeout=30
)
effective = {item.marking_id for item in requirements.markings}
direct = {item.marking_id for item in requirements.markings
          if item.is_directly_applied}
assert direct <= effective

client.filesystem.Resource.add_markings(
    resource_rid, marking_ids=[approved_marking_id], request_timeout=30
)
checked = client.filesystem.Resource.get_access_requirements(
    resource_rid, request_timeout=30
)
assert approved_marking_id in {item.marking_id for item in checked.markings}
```

`add_markings` returns `None`; verify state with a read. A direct Marking may
affect who can see the resource, and inherited Markings remain even after a
direct Marking is removed. Resolve `approved_marking_id` through the
organization's marking policy. If a read is denied after the write, use an
authorized administrator to inspect effective requirements; do not infer that
the write failed from the caller's lost visibility.

## Trash and recovery decision

`delete(resource_rid)` moves the resource to trash. Preserve RID, path and
parent before calling, then read trash status if access permits. `restore`
restores the RID and directly trashed ancestors. `permanently_delete` requires
the resource to be directly trashed and has no restore route. If a delete or
restore response is uncertain, read the exact RID and status before repeating
it. Do not substitute a resource found at the old path; path lookup can now
resolve to a different RID. [Role assignments](ResourceRole.md) and
[project references](ProjectResourceReference.md) need separate checks.
