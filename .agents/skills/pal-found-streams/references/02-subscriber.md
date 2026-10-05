# Subscriber operations

Subscriber ID belongs to stream's dataset and branch. It stores read
positions by partition. Examples use `DATASET_RID` and `SUBSCRIBER_ID` shell
variables. Reads with `--auto-commit` advance stored position when fetched;
otherwise commit after processing.
Input errors exit 1, SDK permission denials exit 3, missing resources exit 4,
and read-only policy can block writes (8). Some server 404s can conceal denial.

### subscriber.create

Registers consumer identified by `--subscriber-id` on positional dataset
RID and branch. `--read-position-json` chooses `{"type":"earliest"}`
(default), `{"type":"latest"}`, or `{"type":"specific","offsets":{"0":50}}`.
Earliest replays retained history; latest starts after current records;
specific uses valid partition offsets. Result includes subscriber ID, dataset
RID, branch, current view RID, and starting offsets. Same ID on same stream
returns existing registration; ID bound to different stream fails.

**Example:** `pal-found-streams subscriber create "$DATASET_RID" master --subscriber-id events-worker --read-position-json '{"type":"earliest"}'`

### subscriber.commit_offsets

Stores **last processed** offset per partition when auto commit is off.
Committing `{"0":50}` makes next read of partition 0 start at 51. Required
`--offsets-json` maps string partition IDs to numeric offsets. Optional
`--view-rid` commits for a specific view; default is latest branch view.
Result is partition-to-next-read-offset map. Invalid partitions, stale views,
or missing write permission can reject request.

**Example:** `pal-found-streams subscriber commit-offsets "$DATASET_RID" master "$SUBSCRIBER_ID" --offsets-json '{"0":50}'`

### subscriber.delete

Deletes subscriber and committed offset state; response has no body. ID can
then be registered again, perhaps at different start. Confirm no consumer
relies on checkpoint; nonexistent ID or insufficient permission fails.

**Example:** `pal-found-streams subscriber delete "$DATASET_RID" master "$SUBSCRIBER_ID"`

### subscriber.get_read_position

Returns map of string partition IDs to next read offsets. Optional
`--view-rid` targets a specific stream view; default is latest branch view.
Use after commit or reset to inspect checkpoint. Absent subscriber or
inaccessible view can fail.

**Example:** `pal-found-streams subscriber get-read-position "$DATASET_RID" master "$SUBSCRIBER_ID"`

### subscriber.read_records

Fetches records from stored position, grouped by partition ID in
`recordsByPartition`. `--max-records` bounds total across partitions (default
100, CLI range 1–1,000). `--partition-ids-json` accepts array of string IDs;
omitting it reads all partitions. Default `auto_commit` is false, so call
`commit-offsets` after processing for at-least-once behavior. With
`--auto-commit`, fetching advances position before process handles records.
Optional `--view-rid` pins one view. Missing subscriber or view fails.

**Example:** `pal-found-streams subscriber read-records "$DATASET_RID" master "$SUBSCRIBER_ID" --max-records 100 --partition-ids-json '["0"]'`

### subscriber.reset_offsets

Moves this subscriber's position without changing stream data. Supply
`--position-json` with earliest, latest, or specific per-partition offsets.
Earliest replays retained records; latest skips existing records. Specific
offsets must be nonnegative and no later than each partition's end. Result
maps partitions to new next-read offsets; malformed position or missing
permission rejects change.

**Example:** `pal-found-streams subscriber reset-offsets "$DATASET_RID" master "$SUBSCRIBER_ID" --position-json '{"type":"earliest"}'`
