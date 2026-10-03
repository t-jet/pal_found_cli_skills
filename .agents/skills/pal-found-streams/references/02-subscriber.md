# Subscriber operations

This part documents the `subscriber` resource client (6 operations). A
subscriber consumes records from a stream and commits offsets so delivery is
tracked.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/streams/scripts/pal_found_streams_cli.py`;
SDK `foundry_sdk/v2/streams/subscriber.py` at pinned commit `2da67907`.
Reviewer architect (CODEREVIEW-052), 2026-10-03. QA baseline TESTCASE-016.

## Operation records

### subscriber.create

- **Class**: create (write). Creates a subscriber on a stream.
- **Preconditions**: can write subscriptions to the stream.
- **Effect**: creates a subscriber that will read from the stream.
- **Inputs**: positional `stream_rid`; `--subscriber-name`,
  `--schema-json` (where needed).
- **Success**: the created subscriber (RID).
- **Example**: `pal-found-streams subscriber create <STREAM_RID> --subscriber-name "processor"`.

### subscriber.commit_offsets

- **Class**: execute (write). Commits processed offsets for a subscriber.
- **Preconditions**: can write to the subscription.
- **Effect**: advances the subscriber's committed offsets; affects what it
  reads next.
- **Inputs**: positional `stream_rid`, `subscriber_rid`; `--offsets-json`.
- **Success**: commits the offsets; returns the updated position.
- **Example**: `pal-found-streams subscriber commit-offsets <STREAM_RID> <SUBSCRIBER_RID> --offsets-json '{}'`.

### subscriber.delete

- **Class**: delete (write). Deletes a subscriber.
- **Preconditions**: can delete the subscription.
- **Effect**: removes the subscriber; its offsets are removed.
- **Inputs**: positional `stream_rid`, `subscriber_rid`.
- **Success**: returns the deleted subscriber.

### subscriber.get_read_position

- **Class**: read. Returns a subscriber's read position.
- **Preconditions**: can read the subscription.
- **Effect**: returns the subscriber's current read offsets per partition.
- **Inputs**: positional `stream_rid`, `subscriber_rid`.
- **Success**: the read-position map.

### subscriber.read_records

- **Class**: read. Reads unprocessed records for a subscriber.
- **Preconditions**: can read the subscription.
- **Effect**: returns a batch of records up to `--max-records` (default 100).
- **Inputs**: positional `stream_rid`, `subscriber_rid`; `--max-records`.
- **Success**: a batch of records; empty if none pending.
- **Failure**: exit 5 on timeout.
- **Example**: `pal-found-streams subscriber read-records <STREAM_RID> <SUBSCRIBER_RID> --max-records 100`.

### subscriber.reset_offsets

- **Class**: change (write). Resets a subscriber's offsets.
- **Preconditions**: can write the subscription.
- **Effect**: resets offsets so the subscriber re-reads from a position.
- **Inputs**: positional `stream_rid`, `subscriber_rid`; `--offsets-json` or a
  reset target.
- **Success**: returns the reset position.

## Evidence and review

Reviewed against the installed `pal-found-streams` parser and pinned SDK
sources (commit `2da67907`). `create`/`commit_offsets`/`delete`/`reset_offsets`
are write with material offset/subscription effects; `read_records` is bounded
by `--max-records` (AC-D-013-09). Committing offsets changes what a subscriber
reads next. No unsupported operation is documented as callable.
