# Global Query execution, versions and result delivery

[REST development](../../../rest-api.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

A Query invokes published function logic through an API name. Its argument and
result schema belong to the selected function version; the REST SDK's generic
JSON value type does not define the business schema. Global Queries differ from
Ontology-scoped Queries. Ordinary `execute` uses the global endpoint, while
`execute_async` and streaming methods can receive an explicit Ontology identifier.
Select the supported endpoint instead of assuming all Query names share a scope.

## Prerequisites

Prepare SDK 1.101.0, a permitted published Query and its input/result definitions.
Check the operation's release stage, preview enablement and function/resource
access. The latest version is the most recently published version and can be a
pre-release. Pin `version` for a reproducible business contract. With `branch`,
that version must exist on the selected branch. An omitted branch uses the default.
Transactions are experimental and not supported in every workflow; a transaction
ID is not a generic request correlation identifier.

## Procedure

| Operation | Purpose and handling |
| --- | --- |
| [get](../../contracts/v2/functions/Query/get.md) ([fixture](../../../../examples/rest/085/v2/functions/Query/invoke_get.py)) | Resolve metadata by API name and selected version before constructing argument values. |
| [get_by_rid](../../contracts/v2/functions/Query/get_by_rid.md) ([fixture](../../../../examples/rest/085/v2/functions/Query/invoke_get_by_rid.py)) | Resolve the exact function identity when the caller has its RID. |
| [get_by_rid_batch](../../contracts/v2/functions/Query/get_by_rid_batch.md) ([fixture](../../../../examples/rest/085/v2/functions/Query/invoke_get_by_rid_batch.py)) | Resolve a bounded set of RID requests and match returned identities to the requested set. |
| [execute](../../contracts/v2/functions/Query/execute.md) ([fixture](../../../../examples/rest/085/v2/functions/Query/invoke_execute.py)) | Invoke a global Query and decode its complete JSON result. Validate the business result shape. |
| [execute_async](../../contracts/v2/functions/Query/execute_async.md) ([fixture](../../../../examples/rest/085/v2/functions/Query/invoke_execute_async.py)) | Submit execution; inspect whether the response is an immediate result or an execution ID. |
| [streaming_execute](../../contracts/v2/functions/Query/streaming_execute.md) ([fixture](../../../../examples/rest/085/v2/functions/Query/invoke_streaming_execute.py)) | Receive raw SSE bytes; SDK ordinary bytes buffer the result. Use the streaming wrapper for bounded incremental consumption. |
| [streaming_execute_events](../../contracts/v2/functions/Query/streaming_execute_events.md) ([fixture](../../../../examples/rest/085/v2/functions/Query/invoke_streaming_execute_events.py)) | Use its typed SSE context manager and handle each discriminated data/error event. |

After asynchronous submission, poll [Execution.get_result](../../contracts/v2/functions/Execution/get_result.md)
with an explicit deadline and attempt budget. Server asynchronous execution differs
from choosing `AsyncFoundryClient`; an asynchronous Python client can still submit
a synchronous-result operation. Preserve the returned execution identity when the
polling budget expires rather than submitting another execution automatically.

An SSE data event contains a batch of result values. A non-streaming function sends
one data event containing its entire result; a streaming function can send several
batches. An SSE error event is a typed application failure before termination and
can follow earlier data. Preserve partial results and report failure explicitly.
HTTP success or the first data batch does not prove complete Query success. Apply
the [local SSE framing/lifetime contract](../../client-behavior.md) and a finite
event/byte/deadline budget.

## Worked example

Run from this skill directory:

```bash
python -B examples/rest/085/global_query.py
```

The synthetic published `scale` Query takes integer `amount` and `factor`, returning
their integer product. The actual SDK serializes parameters `2` and `3`, pinned
version `1.0.0`, branch `master` and `preview=True`; the mock returns `value: 6`.
The named denial fixture verifies `ExecuteQueryPermissionDenied` and its Query
parameter. This schema is fully specified for the fixture and is not an existing
tenant function. Obtain a real Query's definitions through its metadata operation
before adapting these inputs or validating its result.

## Expected result and checks

Check Query identity, version/branch, complete argument schema and result shape.
For SSE, check every data/error discriminator and the terminal outcome; for
submitted execution, retain its ID until a supported completed result appears.
The local fixture proves SDK request/result/error handling and executes no business
function. Each operation contract links complete request, result and error models.

## Failures and recovery

Denied execution requires checking the calling identity and the selected function's
grants. Invalid argument/result shapes require the exact version's metadata.
Missing branch/version requires correcting that selection before invocation.
If a Query may perform effects and a call times out, reconcile those effects using
its documented business contract; this REST interface supplies no universal replay
or idempotency guarantee. An expired stream budget leaves a partial outcome.

## Access boundary

Prepared-library transport fixtures run offline. Actual Query metadata, publication,
resource permissions, execution effects and experimental transaction availability
require authorized enrollment access. No fixture establishes live execution or
compatibility with an undeclared tenant Query schema.
