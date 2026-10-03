# Media content operations

This part documents the media-set content operations (9): get, get_result,
get_rid_by_path, get_status, info, metadata, read, read_original, and
retrieve. The download-class operations stream bounded binary content.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/media_sets/scripts/pal_found_media_sets_cli.py`;
SDK `foundry_sdk/v2/media_sets/media_set.py` at pinned commit `2da67907`.
Reviewer architect (CODEREVIEW-053), 2026-10-03. QA baseline TESTCASE-018.

## Operation records

### media_set.get

- **Class**: read. Returns a media set.
- **Preconditions**: can read the set.
- **Effect**: returns the media set record.
- **Inputs**: positional `media_set_rid`; optional `--branch-rid`/`--view-rid`.
- **Success**: the media set.
- **Failure**: exit 4 if missing.

### media_set.get_result

- **Class**: read (binary download). Downloads a media item's result.
- **Preconditions**: can read the item.
- **Effect**: saves the media content; returns a metadata envelope.
- **Inputs**: positional `media_set_rid`; `--media-item-path`/`--media-item-rid`;
  `--output` (required).
- **Success**: metadata envelope; download bound applies.
- **Failure**: exit 8 if read blocked in metadata-only mode.

### media_set.get_rid_by_path

- **Class**: read. Resolves a media item RID by its branch/path.
- **Preconditions**: can read the set.
- **Effect**: returns the item RID for a path.
- **Inputs**: positional `media_set_rid`; `--branch-rid`/`--view-rid`,
  `--media-item-path`.
- **Success**: the item RID.

### media_set.get_status

- **Class**: read. Returns a media set transaction/job status.
- **Preconditions**: can read the set.
- **Effect**: returns the status of the set or a transform.
- **Inputs**: positional `media_set_rid`; branch/transaction context.
- **Success**: the status record.

### media_set.info

- **Class**: read. Returns a media item's info.
- **Preconditions**: can read the item.
- **Effect**: returns item metadata (size, type).
- **Inputs**: positional `media_set_rid`; item selectors.
- **Success**: the item info.

### media_set.metadata

- **Class**: read. Returns media set/transaction metadata.
- **Preconditions**: can read the set.
- **Effect**: returns metadata for the set or transaction.
- **Inputs**: positional `media_set_rid`; `--transaction-id`/`--branch-name`.
- **Success**: the metadata.

### media_set.read

- **Class**: read (binary download). Reads a media item's bytes.
- **Preconditions**: can read the item.
- **Effect**: saves the media content; returns an envelope.
- **Inputs**: positional `media_set_rid`; item + `--output`.
- **Success**: metadata envelope; download bound applies.
- **Failure**: exit 8 if read blocked.

### media_set.read_original

- **Class**: read (binary download). Reads a media item's original bytes.
- **Preconditions**: can read the item.
- **Effect**: saves the original content; returns an envelope.
- **Inputs**: positional `media_set_rid`; item + `--output`.
- **Success**: metadata envelope; download bound applies.

### media_set.retrieve

- **Class**: read (binary download). Retrieves media by a read token.
- **Preconditions**: a valid read token for the item.
- **Effect**: saves the content; returns an envelope.
- **Inputs**: positional `media_set_rid`; `--read-token`, `--output`.
- **Success**: metadata envelope; download bound applies.

## Evidence and review

Reviewed against the installed `pal-found-media-sets` parser and pinned SDK
sources (commit `2da67907`). All content operations are read-class; the four
downloads (get_result, read, read_original, retrieve) use BinaryDownloadHandler
with the 1.5 MiB default bound (AC-D-013-09). No unsupported operation is
documented as callable.
