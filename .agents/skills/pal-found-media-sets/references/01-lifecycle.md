# Transactions and writes

Media set must already exist. `media-set create` opens a transaction on it;
it does not create a new set. Examples use `MEDIA_SET_RID`, `MEDIA_ITEM_RID`,
and `TRANSACTION_ID` shell variables. For transactional sets, pass transaction
ID to uploads, register, and clear, then commit. Select at most one branch
name, branch RID, or view RID. CLI input errors exit 1 and read-only policy
blocks writes (8); server can reject schema, permission, or state errors.
`--preview` enables preview features on operations that accept it. A
`--read-token` or `--token` can supply item-level read access on supported
transform and thumbnail calls; the flag spelling depends on endpoint.

### media_set.create

Opens transaction on existing media set, optionally on `--branch-name`.
Without branch, SDK uses default (`master` for most enrollments). Response is
transaction ID for later upload and commit. Use `get` first to inspect
`transactionPolicy` and default branch. Missing set or permission fails.

**Example:** `pal-found-media-sets media-set create "$MEDIA_SET_RID" --branch-name master`

### media_set.commit

Commits open transaction. Uploaded or cleared items become visible on its
branch. Requires media set RID and transaction ID; server returns no body on
success. Invalid, aborted, or already committed transaction fails.

**Example:** `pal-found-media-sets media-set commit "$MEDIA_SET_RID" "$TRANSACTION_ID"`

### media_set.abort

Aborts open transaction and deletes items uploaded within it. Requires set
RID and transaction ID; server returns no body. This discards unpublished
work. Unknown or closed transaction fails.

**Example:** `pal-found-media-sets media-set abort "$MEDIA_SET_RID" "$TRANSACTION_ID"`

### media_set.clear

Soft-deletes item at `--media-item-path`, making it and older items at that
path unretrievable. Defaults to set's default branch. `--branch-name`,
`--branch-rid`, or `--view-rid` chooses target, one at a time. Transactional
sets require `--transaction-id`; change becomes visible on commit. Server
returns no body; conflicting branch selectors or missing permission fail.

**Example:** `pal-found-media-sets media-set clear "$MEDIA_SET_RID" --media-item-path reports/q3.pdf --transaction-id "$TRANSACTION_ID"`

### media_set.upload

Uploads file bytes into existing set. `--file` is required and limited by CLI
to 16 MiB. `--media-item-path` is required when backing set's
`pathsRequired` is true. Optional `--media-item-rid` chooses client-controlled
RID, otherwise server generates it; custom RID must use media set instance
and unused UUID. Supply at most one branch name/RID or view RID; default
branch applies otherwise. Transactional sets require transaction ID. Response
contains new item RID and media set view RID. Schema mismatch, malformed or
duplicate custom RID, or denied write fails. Upload to existing path makes
new item current at that path while direct old references still identify old
item.

**Example:** `pal-found-media-sets media-set upload "$MEDIA_SET_RID" --file ./q3.pdf --media-item-path reports/q3.pdf --transaction-id "$TRANSACTION_ID"`

### media_set.upload_media

Uploads temporary item outside a specified set and returns media reference.
Requires `--file` (16 MiB maximum) and `--filename` logical label; no media
set RID or transaction is accepted. Optional `--media-item-rid` supplies a
client RID, usually best omitted. Item expires after one hour unless
persisted. Useful for Functions or Ontology workflows. Invalid file,
duplicate custom RID, or missing upload permission fails.

**Example:** `pal-found-media-sets media-set upload-media --file ./preview.png --filename preview.png`

### media_set.register

Registers file already in federated media store into federated media set.
`--physical-item-name` is path relative to store; optional
`--media-item-path` sets logical path in set. `--branch-name` or `--view-rid`
selects target. Registration validates schema and extracts initial metadata.
Transactional sets require transaction ID. Response contains item RID and
media type. Ordinary stored sets or missing physical item reject operation.

**Example:** `pal-found-media-sets media-set register "$MEDIA_SET_RID" --physical-item-name camera/frame-001.jpg --media-item-path frames/frame-001.jpg --transaction-id "$TRANSACTION_ID"`

### media_set.transform

Starts asynchronous transformation of existing item; read access or media
read token is required. Supply SDK transformation object with
`--transformation-json`; example resizes image to 800 by 600 WebP. Optional
`--token` passes media read token. Response includes job ID and status
(`PENDING`, `FAILED`, or `SUCCESSFUL`). Accepted request may still be pending;
poll `get-status`, then `get-result`. Unsupported transformation or missing
read permission fails.

**Example:** `pal-found-media-sets media-set transform "$MEDIA_SET_RID" "$MEDIA_ITEM_RID" --transformation-json '{"type":"image","encoding":{"type":"webp"},"operations":[{"type":"resize","width":800,"height":600}]}'`

### media_set.calculate

Starts calculation of 200-pixel WebP thumbnail for image item. This GET
endpoint can start work; response is tracked state (`successful`, `pending`,
or `failed`) rather than image bytes. Optional `--read-token` can grant item
access; `--preview` enables beta endpoint where required. Non-image item,
failed calculation, or missing read permission prevents usable thumbnail.
Call `retrieve` once state is successful.

**Example:** `pal-found-media-sets media-set calculate "$MEDIA_SET_RID" "$MEDIA_ITEM_RID"`
