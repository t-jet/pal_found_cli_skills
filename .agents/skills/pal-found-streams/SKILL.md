---
name: pal-found-streams
description: Create and use Foundry streaming datasets, branch streams, and subscribers through 15 CLI operations.
---

# Foundry Streams CLI

## Capability and source

Streams combine dataset features such as branches, schema, permissions, and
version control with a low latency view of incoming tabular records. Records
enter a hot buffer and can be processed by downstream streaming jobs. Partitions
allow parallel throughput; offsets identify records within each partition.
The CLI addresses a stream by **dataset RID and branch name**, not by a separate
stream RID. A subscriber tracks its own reading position and can either commit
after a read or explicitly commit each processed offset. Resetting a stream
clears its records and creates a new view; resetting a subscriber changes only
that subscriber's read position.

Source: [Streams](https://www.palantir.com/docs/foundry/data-integration/streams).

15 Foundry Streams API v2 operations are available through the installed `pal-found-streams` command.

## Usage

```bash
pal-found-streams <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`.

Long-lived record connections use `FOUNDRY_AGENTIC_CLI_STREAMS_TIMEOUT_S`
(default 120 s). The CLI uses the shared config loader, access control guard,
retry handler, pagination helper, structured error serializer, output
formatter, and SDK-native B3 tracing scope.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Stream operations](references/01-stream.md) | `dataset`, `stream` | 9 |
| [Subscriber operations](references/02-subscriber.md) | `subscriber` | 6 |

## Parameters and JSON

Use `--schema-json`, `--record-json`, `--records-json`, `--offsets-json`,
`--position-json`, and `--read-position-json` where the operation requires
structured input. `get-records` and `read-records` offer `--max-records`
(default 100) to bound one response. CLI maxima are 10,000 for stream
`get-records` and 1,000 for subscriber `read-records`. `--max-records` is a
CLI limit, not a
Foundry offset or pagination token.

Schema JSON has `fields` (each field has `name` and a `schema` with
`nullable` and `dataType`) plus `keyFieldNames`. A record uses those field
names as JSON keys. In the examples, `timestamp` values are epoch milliseconds.
`keyFieldNames` groups records sharing a key into the same partition for
ordered processing; it does not deduplicate records. `--partitions-count`
controls parallel stream throughput;
the SDK estimates about 5 MB/s per partition. `--view-rid` on supported
reads/writes pins a stream view; without it, the latest view on the branch is
used. Use it when a reset or branch change could otherwise move the target.
`LOW_LATENCY` is the usual stream type. `HIGH_THROUGHPUT` trades some latency
for more throughput and is intended for streams whose metrics show producer
batches hitting their size limit or expiring.
Read positions use `{"type":"earliest"}`, `{"type":"latest"}`, or
`{"type":"specific","offsets":{"0":50}}`. The offsets map keys are
partition IDs; values are nonnegative offsets no later than that partition's
end. For manual commits, `--offsets-json` uses the same partition-to-offset
map and represents the **last processed** record in each partition.

## Install requirement

`pal-found-streams` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

```bash
# conda (t-jet channel)
conda install -c t-jet pal_found_cli

# PyPI / pip
pip install pal_found_cli

# uv
uv tool install pal_found_cli
```
