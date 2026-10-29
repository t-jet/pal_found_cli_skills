# Folder navigation and creation

[Operation catalog](../../catalog.md) | [REST development](../../../rest-api.md)

## Concept and lifecycle

A Folder locates resources in Foundry's filesystem hierarchy. Its RID is its
identity; its display name and path describe its location. Folder children are
resources and need not all be folders. Creating a folder changes the hierarchy;
getting metadata and enumerating children read it. Project, space and root
resources have different rules, so a RID with a plausible shape does not prove
that the target supports a folder operation.

## Prerequisites

Use the prepared SDK 1.101.0, an authorized enrollment identity and an existing
parent folder inside a project for live creation. Verify the parent's identity
and the caller's ability to create resources there. The SDK does not specify a
universal OAuth scope or guarantee that visible metadata grants write access.
For the synthetic example, prepared Python, SDK and httpx suffice; no enrollment
or public connection is used.

## Procedure

1. Read [get](../../contracts/v2/filesystem/Folder/get.md) for the candidate
   parent and inspect its type, parent and path. Resolve access failures before
   choosing another target.
2. Enumerate [children](../../contracts/v2/filesystem/Folder/children.md) with
   finite raw-page budgets. Preserve partial results and continuation state;
   an empty page with a next token is not completion. Filter resource types
   explicitly when only folders are relevant.
3. Choose a display name and call
   [create](../../contracts/v2/filesystem/Folder/create.md) with
   `display_name` and `parent_folder_rid`. Names cannot be `.` or `..`, contain
   `/`, or exceed 700 characters. Another resource may already use that name.
4. Retain the returned RID and read its metadata. Compare its parent and name
   with the request; this verifies the resource the application will use next.

## Worked example

Run from this skill directory:

```bash
python -B examples/rest/073/folders.py
```

The file makes actual SDK calls through a synthetic HTTP transport. Its create
request verifies JSON aliases `displayName` and `parentFolderRid`; its get
checks decoded metadata. Children deliberately returns an empty first page
with a continuation token, then a resource. Named create-denied/get-missing/
children-missing fixtures verify typed SDK exceptions. Adapt the invocation
arguments and result checks to your authorized project; replace the fixture
transport with the ordinary client described in the REST development guide.

## Expected result and checks

The fixture prints `Folder create/get/children request, result and error fixtures passed`.
Live completion requires the returned folder, correct parent/name and an
explicitly completed or bounded child enumeration. Fixture success establishes
serialization and application handling, not actual tenant permissions.

## Failures and recovery

`CreateFolderPermissionDenied` requires checking access to the intended parent.
`FolderNotFound` requires checking identity and visibility; it does not justify
creating a replacement parent. Name conflicts require inspecting existing
resources before choosing another name. If creation times out after submission,
do not blindly repeat it: inspect the intended parent's children within a finite
budget and reconcile candidate identity/name/type. A matching name alone is
insufficient proof of which request created a resource. Escalate ambiguous state.

The local contracts enumerate other operation-specific failures and provide
complete model/error definitions. No universal idempotency guarantee is given.

## Access boundary

Offline fixtures need prepared libraries only. Reading or changing live
filesystem resources requires enrollment connectivity and authorized identity.
Creating folders is a live mutation; the fixture does not grant or simulate
approval to change production resources.

### get_batch

Fetch known folder RIDs together. Compare returned RID keys with requested IDs and treat absent entries as unresolved instead of silently matching by name.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/Folder/get_batch.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/Folder/get_batch.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### replace

Replace a folder display name or parent. Check the returned parent RID and path; reject a move that would make the folder its own ancestor.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/filesystem/Folder/replace.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/filesystem/Folder/replace.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

## Python client route

With a configured `FoundryClient` named `client`, use `client.filesystem.Folder` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.
