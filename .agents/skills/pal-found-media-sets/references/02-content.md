# Item reads and downloads

Examples use `MEDIA_SET_RID`, `MEDIA_ITEM_RID`, and `JOB_ID` shell variables.
Downloads save bytes through CLI's bounded handler and return path, size,
checksum, and `truncated` metadata. `--output` is a **basename**, never a path:
the handler saves it under configured download directory. Omit it for
generated name. Default limit is 1.5 MiB; larger content is saved as a
truncated prefix and marked `truncated: true`. Read token options apply to
individual items where SDK supports them. `--read-token` applies to item
reads; transformation status/result use `--token`. `--preview` enables beta
endpoint behavior where accepted. Input errors exit 1; SDK permission denials
exit 3, missing items exit 4, and metadata-only policy may block binary reads
(8). Server may conceal a denial as 404.

### media_set.get

Returns set RID, media schema, default branch name, transaction policy,
and `pathsRequired`. Use policy before opening transaction and path rule
before upload. Requires set RID. Missing set or read permission fails;
no item bytes are returned.

**Example:** `pal-found-media-sets media-set get "$MEDIA_SET_RID"`

### media_set.get_rid_by_path

Resolves current item at `--media-item-path` to its RID. Defaults to set's
default branch; choose `--branch-name`, `--branch-rid`, or `--view-rid`, one
at a time, to scope lookup. Response has optional `mediaItemRid`; absent path
may yield null. Denied branch access fails. Older direct reference can still
point to an overwritten item at same path.

**Example:** `pal-found-media-sets media-set get-rid-by-path "$MEDIA_SET_RID" --media-item-path reports/q3.pdf --branch-name master`

### media_set.info

Returns item information: view RID, optional path, logical timestamp,
original/upload MIME type, current MIME type, and size when available.
Optional `--read-token` authorizes item read. Use `metadata` for extracted
type-specific details. Missing item or read permission fails.

**Example:** `pal-found-media-sets media-set info "$MEDIA_SET_RID" "$MEDIA_ITEM_RID"`

### media_set.metadata

Returns detailed extracted metadata for item RID: image dimensions,
audio/video duration, document page count, or other type-specific fields
when available. Optional `--read-token` authorizes item read. Missing item
or read permission fails; extracted fields depend on item format.

**Example:** `pal-found-media-sets media-set metadata "$MEDIA_SET_RID" "$MEDIA_ITEM_RID"`

### media_set.reference

Returns media reference for item RID. Reference lets Ontology or another
Foundry workflow point to item without downloading bytes. This is a read;
it does not add item to transaction. Optional `--read-token` authorizes item
read; missing item or read permission fails. Response is `MediaReference`.

**Example:** `pal-found-media-sets media-set reference "$MEDIA_SET_RID" "$MEDIA_ITEM_RID"`

### media_set.read

Downloads current content of item RID, saving bounded bytes under `--output`
basename or generated name. Optional `--read-token` grants item read. Response
gives local path, size, checksum, and truncation flag. Missing item or read
denial fails; content over configured bound is truncated. Use `read-original`
when upload converted its format.

**Example:** `pal-found-media-sets media-set read "$MEDIA_SET_RID" "$MEDIA_ITEM_RID" --output q3.pdf`

### media_set.read_original

Downloads original uploaded file even when media set transformed additional
input format on upload. `--read-token` can grant item access and `--output`
chooses basename. Missing original or read permission fails. Result reports
local path, saved size, checksum, and truncation status.

**Example:** `pal-found-media-sets media-set read-original "$MEDIA_SET_RID" "$MEDIA_ITEM_RID" --output q3-original.docx`

### media_set.get_status

Returns `jobId` and status for transformation identified by set RID, item
RID, and job ID. Optional `--token` supplies media item read token. Use after
`transform`; `PENDING` means wait, `FAILED` needs handling, and `SUCCESSFUL`
allows `get-result`. Unknown job or missing read access fails.

**Example:** `pal-found-media-sets media-set get-status "$MEDIA_SET_RID" "$MEDIA_ITEM_RID" "$JOB_ID"`

### media_set.get_result

Downloads transformed bytes after job succeeded. Requires set RID, item RID,
job ID; `--output` selects basename and optional `--token` grants item read.
Pending or failed job returns error; read denial also fails. Oversize result
is truncated and marked in envelope;
download does not create a new media item in set.

**Example:** `pal-found-media-sets media-set get-result "$MEDIA_SET_RID" "$MEDIA_ITEM_RID" "$JOB_ID" --output resized.webp`

### media_set.retrieve

Downloads successfully calculated 200-pixel WebP thumbnail for image item.
First call `calculate` and confirm `successful` status. Optional
`--read-token` grants item read; `--preview` enables beta endpoint where
needed. Missing thumbnail, non-image item, or read denial fails. Result is
local file metadata with truncation status.

**Example:** `pal-found-media-sets media-set retrieve "$MEDIA_SET_RID" "$MEDIA_ITEM_RID" --output thumbnail.webp`
