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

Use an authorized identity with enrollment access and an owner-confirmed exact RID,
parent and path. Read that RID before deciding whether to restore it. The local
[Resource model](../../models/v2/filesystem/models/Resource.md) exposes `rid`,
`trash_status`, `parent_folder_rid` and `path`; the
[TrashStatus definition](../../models/v2/filesystem/models/TrashStatus.md) distinguishes:

- `DIRECTLY_TRASHED`: the resource was specifically trashed and can be restored directly.
- `ANCESTOR_TRASHED`: restoration requires restoring the original containing folder.
  Stop and have an authorized owner reconcile that folder and its hierarchy;
  this example does not select or mutate ancestors.
- `NOT_TRASHED`: if identity, parent and path match the approved desired state,
  record that observation and skip the mutation.

SDK 1.101.0 provenance: the linked contract reproduces the SDK prose,
"If the resource is not trashed, this operation will be ignored."
The same method declares `ResourceNotDirectlyTrashed` (the resource is not directly
trashed). This is a task-critical source disagreement. Live server policy is
unverified; neither the prose nor synthetic HTTP responses establish an
active-resource no-op, idempotency, or a universal ancestor-state outcome.

An ordinary success returns `None` (synthetic HTTP 204 in the fixture), which
contains no restored state. Perform one authorized exact-RID read afterward;
check RID, `trash_status`, `parent_folder_rid` and path against the approved
expectations. A matching `NOT_TRASHED` read establishes only the observed desired
state at read time, not which changes this attempt caused or the state of every
ancestor. Read any required ancestor context separately with authorization.

The exact declared errors are `ResourceNotDirectlyTrashed`, `ResourceNotFound`,
and `RestoreResourcePermissionDenied`; each carries `parameters['resourceRid']`.
For `ResourceNotDirectlyTrashed` or a timeout with unknown write outcome, stop
replay and reconcile once using the same RID. A matching `NOT_TRASHED` state needs
no replay; `ANCESTOR_TRASHED` needs original-folder reconciliation; a still
`DIRECTLY_TRASHED` resource or conflicting state needs authorized owner review
of outcome and policy. `ResourceNotFound`, restore permission denial, unavailable
or denied reads, unknown status, or changed identity/parent/path stop this flow.
Retain the error and observed state for that owner; do not switch identity,
substitute a RID found at the old path, mutate arbitrary ancestors, or retry
blindly. Resolve access and policy before planning any further write.

The fixture's adaptable `restore_once(client.filesystem.Resource, resource_rid,
expected_parent_rid=approved_parent_rid, expected_path=approved_path)` uses at most
one restore and two reads with 30-second request timeouts. Its client must have
an explicitly bounded retry policy (the fixture uses `Config(max_retries=1)`).
Read exceptions propagate and stop; fixture outcomes demonstrate client decisions
only. Confirm scope/permission and tenant state with the authorized owner before
using tenant values.

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
parent before calling, then read trash status if access permits. For `restore`,
follow the state decision and source-conflict limits in [restore](#restore).
`permanently_delete` requires
the resource to be directly trashed and has no restore route. If a delete or
restore response is uncertain, read the exact RID and status before repeating
it. Do not substitute a resource found at the old path; path lookup can now
resolve to a different RID. [Role assignments](ResourceRole.md) and
[project references](ProjectResourceReference.md) need separate checks.
