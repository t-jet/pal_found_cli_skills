# Media identities, transactions and transformations

[REST development](../../../rest-api.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

A media set stores typed media items with stable identities, optional paths and a
transaction policy. Its schema distinguishes imagery, audio, video, documents and
other supported media families. A media-set RID, item RID, path, transaction ID and
transformation-job ID identify different objects. Read the set's schema and policy
before uploading or changing items. `MediaSet.create` creates a transaction in an
existing set; it does not create a new media set.

## Prerequisites

With an authenticated SDK 1.101.0 `foundry_sdk.v2.FoundryClient` named
`client`, these operations are available at `client.media_sets.MediaSet`.
For example, `client.media_sets.MediaSet.get(media_set_rid)` reads the set;
`client.media_sets.MediaSet.read(media_set_rid, media_item_rid)` reads item
content. Check each linked contract for its exact arguments and response mode.

Prepare SDK 1.101.0 and an accessible media set. Inspect its `media_schema`,
`default_branch_name`, `transaction_policy` and `paths_required`. Select exactly one
supported branch name, branch RID or view RID when an operation permits that
selection; omitting them uses the default branch. Confirm supported content format
and path requirements. Binary upload bodies use `application/octet-stream`.

For transformations, SDK source requires item read access through
`api:mediasets-read` or a `MediaItemReadToken`. Temporary `upload_media` documents
`api:ontologies-read` and `api:ontologies-write` for third-party OAuth applications.
These endpoint-specific requirements do not establish a scope for every method;
verify the prepared client's security mode and resource restrictions separately.
Federated-store registration requires a federated media set and its configured
store, rather than uploading an arbitrary external URL.

## Procedure

| Operation | Purpose and lifecycle check |
| --- | --- |
| [get](../../contracts/v2/media_sets/MediaSet/get.md) | Read set schema, transaction policy, default branch and path requirement. |
| [get_rid_by_path](../../contracts/v2/media_sets/MediaSet/get_rid_by_path.md) | Resolve a path to an item identity before reading or changing that item. |
| [info](../../contracts/v2/media_sets/MediaSet/info.md) | Read item information for the intended set/item identities. |
| [metadata](../../contracts/v2/media_sets/MediaSet/metadata.md) | Read type-specific information such as image dimensions, duration or document pages. |
| [read](../../contracts/v2/media_sets/MediaSet/read.md) | Retrieve item content as bytes with a byte budget and response cleanup. |
| [read_original](../../contracts/v2/media_sets/MediaSet/read_original.md) | Retrieve the original uploaded file when upload conversion changed its representation. |
| [reference](../../contracts/v2/media_sets/MediaSet/reference.md) | Obtain the item's media-reference representation; it differs from downloading content. |
| [create](../../contracts/v2/media_sets/MediaSet/create.md) | Open a transaction; uploaded items remain invisible until commit. |
| [upload](../../contracts/v2/media_sets/MediaSet/upload.md) | Send binary content to an existing set with the intended path/branch/transaction. |
| [commit](../../contracts/v2/media_sets/MediaSet/commit.md) | Commit an open transaction, making its uploaded items available. |
| [abort](../../contracts/v2/media_sets/MediaSet/abort.md) | Abort an open transaction, deleting items uploaded in that transaction. |
| [clear](../../contracts/v2/media_sets/MediaSet/clear.md) | Soft-delete a path and make all older items at that path un-retrievable; transactional deletion becomes visible only after commit. |
| [register](../../contracts/v2/media_sets/MediaSet/register.md) | Register a federated-store item; validate schema and extract initial metadata. |
| [upload_media](../../contracts/v2/media_sets/MediaSet/upload_media.md) | Upload a temporary item that must be persisted within one hour or is deleted; multi-resource usage attribution uses the first resource. |
| [calculate](../../contracts/v2/media_sets/MediaSet/calculate.md) | Start thumbnail calculation for an image; submission is not thumbnail availability. |
| [retrieve](../../contracts/v2/media_sets/MediaSet/retrieve.md) | Retrieve a successfully calculated thumbnail: 200 pixels wide, `image/webp`. |
| [transform](../../contracts/v2/media_sets/MediaSet/transform.md) | Start an item transformation and retain the returned job ID. |
| [get_status](../../contracts/v2/media_sets/MediaSet/get_status.md) | Read transformation status using a finite polling budget. |
| [get_result](../../contracts/v2/media_sets/MediaSet/get_result.md) | Retrieve completed transformed bytes; an incomplete/unsuccessful job produces an error. |

Keep staged upload success separate from committed visibility. For transformations,
retain the job ID and inspect its supported status before reading its result. A
timeout or polling-budget exhaustion leaves a pending/uncertain outcome, rather
than permission to start another transformation. Item content and originals can
have different formats; use their actual content metadata.

## Worked example

Run from this skill directory:

```bash
python -B examples/rest/091/media_identity.py
```

The actual SDK reads synthetic imagery-set metadata with `batchTransactions` and
required paths. A second call uses the SDK's streaming `read` wrapper to consume a
small PNG under a 1,024-byte application budget; leaving the context closes the
response. The fixture checks media identity, policy and exact bytes. It performs
no upload, media transformation or authorized enrollment read.

Adapt set/item RIDs from approved metadata. The separate operation fixtures under
`examples/rest/091/v2/media_sets/MediaSet/` exercise the exact SDK arguments and
declared error contracts. Complete model and error fields remain linked from each
local operation contract; do not interpret binary responses as JSON.

## Expected result and checks

Verify set schema/policy, resolved item identity, requested representation and byte
format. Check committed visibility independently of upload acknowledgment. Preserve
the transformation job ID and verify completion before reading result bytes.
Temporary-item persistence and federated registration require their own lifecycle
checks, even when a synthetic transport returns a valid model.

## Failures and recovery

Invalid branch combinations require choosing one supported selector. Missing
paths or unsupported content require the set's schema/configuration. Denied reads
or transformations require checking effective identity, restrictions and the
documented read token. If an upload or commit times out, reconcile transaction and
item visibility before replaying it. An aborted transaction loses its uploads.
Clearing a path affects older versions too; capture the approved target and impact
before submission. Budget exhaustion closes client transport without establishing
server cancellation or transformation completion.

## Access boundary

Prepared-library/mock fixtures run offline. Actual media schema availability,
credentials, item visibility, transaction effects, federation and transformation
execution require authorized enrollment access. Local fake responses establish
request/result handling and never establish those live outcomes.
