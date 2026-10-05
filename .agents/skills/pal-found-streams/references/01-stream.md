# Stream operations

Streams belong to datasets and branches. Use dataset RID and branch name in
every `stream` command. Examples assume `DATASET_RID` and `FOLDER_RID` shell
variables hold real RIDs. Change sample schema and records together for your
data. CLI input errors exit 1; SDK permission denials exit 3, missing
resources exit 4, and read-only policy blocks writes (8). A stream `get`
may return 404 for missing branch, stream, or concealed access denial.

### dataset.create

Creates streaming dataset and first stream on `master` unless
`--branch-name` selects another initial branch. `--name` names dataset within
`--parent-folder-rid`; `--schema-json` defines fields and key names. Example
schema has non-null timestamp and string fields; timestamp records use epoch
milliseconds. `--partitions-count` defaults to 1, gives parallel throughput,
and cannot change after dataset creation. `--compressed` enables compression;
`--stream-type` selects `LOW_LATENCY` (default) or `HIGH_THROUGHPUT`.
Response is dataset RID, name, and parent folder RID. Invalid schema,
duplicate name, or missing folder permission can prevent creation.

**Example:** `pal-found-streams dataset create --name sensor-events --parent-folder-rid "$FOLDER_RID" --schema-json '{"fields":[{"name":"timestamp","schema":{"nullable":false,"dataType":{"type":"timestamp"}}},{"name":"value","schema":{"nullable":false,"dataType":{"type":"string"}}}],"keyFieldNames":["timestamp"]}' --partitions-count 2`

### stream.create

Creates new branch and stream on existing streaming dataset. Positional RID
identifies dataset; `--branch-name` names new branch; `--schema-json` supplies
its field and key schema. `--partitions-count` defaults to 1 for throughput;
`--compressed` enables compression; `--stream-type` chooses
`LOW_LATENCY` (default) or `HIGH_THROUGHPUT`. Response contains branch name,
schema, view RID, partition count, stream type, and compression setting.
Existing branch, invalid schema, or missing dataset access can reject request.

**Example:** `pal-found-streams stream create "$DATASET_RID" --branch-name experiment --schema-json '{"fields":[{"name":"value","schema":{"nullable":false,"dataType":{"type":"string"}}}],"keyFieldNames":[]}'`

### stream.get

Looks up stream on positional dataset RID and branch name. Returns schema,
view RID, partition count, stream type, and compression setting.
SDK returns 404 when branch or stream is absent or access denied; response
cannot distinguish these conditions.

**Example:** `pal-found-streams stream get "$DATASET_RID" master`

### stream.get_end_offsets

Reads map from partition ID to end offset, position of its *next* write. Use
to measure arrivals or choose starting position; no records are returned.
Optional `--view-rid` pins one stream view. Absent branch or inaccessible
view can fail.

**Example:** `pal-found-streams stream get-end-offsets "$DATASET_RID" master`

### stream.get_records

Reads one partition selected by string `--partition-id` from inclusive
`--start-offset` (beginning if omitted). `--max-records` bounds one response:
default 100, CLI range 1–10,000. Result is list of records with offsets;
fewer than requested may arrive. Offsets may have gaps; binary values arrive
base64 encoded. Optional `--view-rid` pins branch's underlying view. Invalid
partition or offset can fail; empty list can mean no records yet.

**Example:** `pal-found-streams stream get-records "$DATASET_RID" master --partition-id 0 --start-offset 50 --max-records 100`

### stream.publish_binary_record

Writes bytes from existing `--file` as one record. Stream schema must have a
single binary field. Optional `--view-rid` pins target view; otherwise latest
on branch receives bytes. CLI rejects files over 16 MiB; server rejects
incompatible schema. Successful call returns no response body.

**Example:** `pal-found-streams stream publish-binary-record "$DATASET_RID" master --file ./payload.bin`

### stream.publish_record

Validates one object from `--record-json` against branch schema, then
publishes it. Field names must match schema; timestamp example uses epoch
milliseconds. Optional `--view-rid` targets one view instead of latest.
Mismatched types or missing required fields fail validation. Success has no
response body.

**Example:** `pal-found-streams stream publish-record "$DATASET_RID" master --record-json '{"timestamp":1731426022784,"value":"ready"}'`

### stream.publish_records

Publishes array from `--records-json` in one request. Optional `--view-rid`
pins stream view. Foundry rejects whole batch if any record fails schema
validation; no partial records are published. Success has no response body.

**Example:** `pal-found-streams stream publish-records "$DATASET_RID" master --records-json '[{"timestamp":1731426022784,"value":"ready"},{"timestamp":1731426082784,"value":"running"}]'`

### stream.reset

Clears records on positional dataset RID and branch, then creates new stream
view. `--schema-json`, `--compressed`, `--partitions-count`, and
`--stream-type` configure replacement. Omitted schema, compression, and
stream type, and partition count reuse branch's prior settings; reset permits
changing partition count. Response is new Stream with changed `viewRid`. Downstream consumers
see new view and lost old records; check branch before running. Missing write
permission blocks reset.

**Example:** `pal-found-streams stream reset "$DATASET_RID" experiment --schema-json '{"fields":[{"name":"value","schema":{"nullable":false,"dataType":{"type":"string"}}}],"keyFieldNames":[]}'`
