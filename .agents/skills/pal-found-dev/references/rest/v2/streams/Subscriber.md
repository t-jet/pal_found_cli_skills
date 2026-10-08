# Subscriber offsets and replay

[Streams operations](index.md) | [Stream records](Stream.md)

## Concept and prerequisites

A Subscriber stores a server-side read position for one stream. Its ID must be unique for that stream; reusing it on another stream is an error. Choose automatic commit only when acknowledging at fetch time is acceptable. For processing that must finish before acknowledgement, use manual commits and make the handler tolerate repeated records. Prepare dataset, branch and subscriber identity with the required stream permissions.

## Procedure and operations

| Operation | Use and check |
| --- | --- |
| [create](../../contracts/v2/streams/Subscriber/create.md) ([fixture](../../../../examples/rest/089/v2/streams/Subscriber/invoke_create.py)) | Register an ID and initial read position. Recreating the same ID on the same stream returns its existing registration; inspect its position rather than assuming a fresh start. |
| [get_read_position](../../contracts/v2/streams/Subscriber/get_read_position.md) ([fixture](../../../../examples/rest/089/v2/streams/Subscriber/invoke_get_read_position.py)) | Read each partition's next-read position. Record it before replay or troubleshooting. |
| [read_records](../../contracts/v2/streams/Subscriber/read_records.md) ([fixture](../../../../examples/rest/089/v2/streams/Subscriber/invoke_read_records.py)) | Fetch a bounded set grouped by partition. With `auto_commit=True`, retrieval advances server position immediately; with `False`, process records before explicit commit. |
| [commit_offsets](../../contracts/v2/streams/Subscriber/commit_offsets.md) ([fixture](../../../../examples/rest/089/v2/streams/Subscriber/invoke_commit_offsets.py)) | For manual consumption, commit the last processed offset per partition. Processing offset 50 and committing `{"0": 50}` makes the next read start at 51. Never commit a record the handler has not durably processed. |
| [reset_offsets](../../contracts/v2/streams/Subscriber/reset_offsets.md) ([fixture](../../../../examples/rest/089/v2/streams/Subscriber/invoke_reset_offsets.py)) | Choose `earliest`, `latest` or `specific` position for intentional replay/skip. Verify new read position before resuming processing. |
| [delete](../../contracts/v2/streams/Subscriber/delete.md) ([fixture](../../../../examples/rest/089/v2/streams/Subscriber/invoke_delete.py)) | Remove subscriber and its committed offset state. Its ID can then be reused; capture needed audit state first. |

## Worked example and expected result

The [offline subscriber fixtures](../../../../examples/rest/089/v2/streams/Subscriber/invoke_commit_offsets.py) verify each SDK request and named errors. Run `python -B examples/rest/089/v2/streams/Subscriber/invoke_commit_offsets.py` from the skill root for the manual-commit shape. In a live worker, create or find the subscriber, read a finite batch with `auto_commit=False`, process each record, then commit the last successful offset per partition. Verify the read position after commit. Sparse stream offsets mean the committed value comes from actual returned records.

## Failures, recovery and access boundary

If processing fails, leave unprocessed offsets uncommitted and expect at-least-once delivery on retry. A timed-out commit is uncertain: read the position before committing again. Resetting to `latest` skips existing records, while `earliest` replays them; require an explicit business decision. Local fixtures cannot establish live subscriber state or processing durability. Live reads and mutations require authorized enrollment access.
