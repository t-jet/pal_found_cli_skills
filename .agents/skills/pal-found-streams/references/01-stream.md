# Stream operations

This part documents the `dataset` (1) and `stream` (8) resource clients (9
operations). A stream is created on a stream dataset; records are published to
it.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/streams/scripts/pal_found_streams_cli.py`;
SDK `foundry_sdk/v2/streams/{dataset,stream,subscriber}.py` at pinned commit
`2da67907`. Reviewer architect (CODEREVIEW-052), 2026-10-03. QA baseline
TESTCASE-016. Uses the ADR-003 batch-response pattern.

## Operation records

### dataset.create

- **Class**: create (write). Creates a stream dataset.
- **Preconditions**: can create datasets/streams.
- **Effect**: creates a dataset that holds a stream.
- **Inputs**: required `--schema-json` (stream schema); parent/name fields.
- **Success**: the created stream dataset (RID).
- **Failure**: exit 1 invalid schema; exit 8 readonly block.
- **Example**: `pal-found-streams dataset create --schema-json '{"fieldSchemaList":[]}'`.

### stream.create

- **Class**: create (write). Creates a stream on a stream dataset.
- **Preconditions**: a stream dataset you can write.
- **Effect**: creates a stream and returns it (RID).
- **Inputs**: positional `stream_dataset_rid`; stream name.
- **Success**: the created stream.
- **Example**: `pal-found-streams stream create <STREAM_DATASET_RID> --name "events"`.

### stream.get

- **Class**: read. Returns a stream.
- **Preconditions**: can read the stream.
- **Effect**: returns the stream record.
- **Inputs**: positional `stream_rid`.
- **Success**: the stream.
- **Failure**: exit 4 if missing.

### stream.get_end_offsets

- **Class**: read. Returns the current end offsets of a stream's partitions.
- **Preconditions**: can read the stream.
- **Effect**: returns the end offset per partition.
- **Inputs**: positional `stream_rid`.
- **Success**: the end-offset map.

### stream.get_records

- **Class**: read. Reads records from a stream.
- **Preconditions**: can read the stream.
- **Effect**: returns a batch of records up to `--max-records` (default 100).
- **Inputs**: positional `stream_rid`; `--max-records`, `--start-offset`,
  `--end-offset` where supported.
- **Success**: a batch of records (bounded by `--max-records`).
- **Failure**: exit 5 on stream timeout.
- **Example**: `pal-found-streams stream get-records <STREAM_RID> --max-records 100`.

### stream.publish_binary_record

- **Class**: execute (write). Publishes a binary record.
- **Preconditions**: can write the stream.
- **Effect**: publishes the binary record to the stream (material shell).
- **Inputs**: positional `stream_rid`; `--file` (bounded 16 MiB read).
- **Success**: publishes the record; returns publication metadata.
- **Failure**: exit 1 file too large; exit 8 readonly block.

### stream.publish_record

- **Class**: execute (write). Publishes a JSON record.
- **Preconditions**: can write the stream.
- **Effect**: publishes the record to the stream.
- **Inputs**: positional `stream_rid`; `--records-json` (record).
- **Success**: publishes the record.

### stream.publish_records

- **Class**: execute (write). Publishes a batch of records.
- **Preconditions**: can write the stream.
- **Effect**: publishes multiple records in one call.
- **Inputs**: positional `stream_rid`; `--records-json` (list).
- **Success**: publishes the batch.

### stream.reset

- **Class**: change (write). Resets a stream's state.
- **Preconditions**: can write the stream.
- **Effect**: resets the stream (e.g. clears offsets/published state); affects
  consumers.
- **Inputs**: positional `stream_rid`.
- **Success**: returns the reset stream.

## Evidence and review

Reviewed against the installed `pal-found-streams` parser and pinned SDK
sources (commit `2da67907`). `create`/`publish_*`/`reset` are write with
material publication/state effects; `get_records` is bounded by `--max-records`
(AC-D-013-09); binary publish has a 16 MiB bound. No unsupported operation is
documented as callable.
