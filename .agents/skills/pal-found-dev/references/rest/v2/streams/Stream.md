# Stream branches, records and views

[Streams operations](index.md) | [Subscriber consumption](Subscriber.md)

## Concept and prerequisites

A Stream is attached to a branch of a streaming dataset. Its schema validates records, and its partitions carry offsets. A branch can have a new stream view after a reset; retain `viewRid` when consistent reads matter. Prepare dataset RID, branch, schema and write permissions for live operations. The local SDK fixtures use synthetic values and require no enrollment.

## Procedure and operations

| Operation | Use and check |
| --- | --- |
| [create](../../contracts/v2/streams/Stream/create.md) ([fixture](../../../../examples/rest/089/v2/streams/Stream/invoke_create.py)) | Create a new branch on the backing dataset with its own stream. Verify branch, schema and returned view RID before publishing. |
| [get](../../contracts/v2/streams/Stream/get.md) ([fixture](../../../../examples/rest/089/v2/streams/Stream/invoke_get.py)) | Resolve a branch's stream. A 404 may mean branch absent, no stream or lack of access; do not infer which from status alone. |
| [get_end_offsets](../../contracts/v2/streams/Stream/get_end_offsets.md) ([fixture](../../../../examples/rest/089/v2/streams/Stream/invoke_get_end_offsets.py)) | Read each partition's next-write offset. This is a boundary, not the last record's offset. Preserve the view RID used for the read. |
| [get_records](../../contracts/v2/streams/Stream/get_records.md) ([fixture](../../../../examples/rest/089/v2/streams/Stream/invoke_get_records.py)) | Read a bounded batch from one partition and start offset. Offsets may be sparse, so advance from returned record offsets rather than `start + count`. Decode binary fields from base64. |
| [publish_record](../../contracts/v2/streams/Stream/publish_record.md) ([fixture](../../../../examples/rest/089/v2/streams/Stream/invoke_publish_record.py)) | Publish one schema-valid JSON record. Confirm the returned write result; a rejected record does not enter the stream. |
| [publish_records](../../contracts/v2/streams/Stream/publish_records.md) ([fixture](../../../../examples/rest/089/v2/streams/Stream/invoke_publish_records.py)) | Publish a batch. If one record violates schema, the batch is rejected; inspect each item before retrying. A transport timeout leaves delivery uncertain, so reconcile consumer-visible records before replay. |
| [publish_binary_record](../../contracts/v2/streams/Stream/publish_binary_record.md) ([fixture](../../../../examples/rest/089/v2/streams/Stream/invoke_publish_binary_record.py)) | Send binary bytes only when the stream schema has a single binary field. The wire body is binary, not a JSON string or local filename. |
| [reset](../../contracts/v2/streams/Stream/reset.md) ([fixture](../../../../examples/rest/089/v2/streams/Stream/invoke_reset.py)) | Clear existing records and apply new stream configuration. Reset creates a new view RID; downstream readers and subscribers must reconcile their state. Use an in-platform settings change when records must remain. |

## Worked example and checks

Each operation links an exact local SDK contract. Its [offline fixture](../../../../examples/rest/089/v2/streams/Stream/invoke_get_records.py) verifies request serialization, decoded response and named errors. Run `python -B examples/rest/089/v2/streams/Stream/invoke_get_records.py` from the skill root to inspect bounded read parameters. For a live flow, create or get the branch, publish a schema-valid record, then read from its partition using a finite record and time budget. Compare the returned view RID with the writer's view and report a reset rather than merging records from different views silently.

## Failures and recovery

Schema validation failures call for correcting the record or stream schema. A missing stream needs branch, resource and access checks. Failed binary writes require checking the single-binary-field constraint. Do not blindly replay a timed-out publish: records can be duplicated. A reset is destructive to previous stream records and should follow the application's retention decision; keep old view identity in diagnostics.

## Access boundary

Fixtures run offline through a mock transport. Live branch creation, reads, publishes and reset require authorized enrollment access and can change production data.
