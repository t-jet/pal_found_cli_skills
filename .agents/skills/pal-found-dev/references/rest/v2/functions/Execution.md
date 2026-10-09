# Asynchronous Query execution

[Functions operations](index.md) | [REST client behavior](../../client-behavior.md)

## Concept and prerequisites

`Query.execute_async` can return an execution ID instead of a result. The ID names one submitted execution, not the Query definition. Keep it until that execution succeeds, fails, or is deliberately canceled. These endpoints are Private Beta in SDK 1.101.0. Confirm enablement, the calling identity's Query access and the returned ID in the authorized enrollment. Offline fixtures need the prepared SDK and `httpx` only.

## Procedure and operations

| Operation | Use and observable check |
| --- | --- |
| [get_result](../../contracts/v2/functions/Execution/get_result.md) ([fixture](../../../../examples/rest/085/v2/functions/Execution/invoke_get_result.py)) | Poll a known execution ID. The result is a discriminated union: `running` means keep the ID and poll within a finite deadline; `succeeded` carries the return value. A failed execution raises a service error. The `timeout` parameter allows server long polling; also set `request_timeout` longer than that hold interval. |
| [cancel](../../contracts/v2/functions/Execution/cancel.md) ([fixture](../../../../examples/rest/085/v2/functions/Execution/invoke_cancel.py)) | Request cancellation for a running ID when the caller no longer needs its work. This endpoint is idempotent. Read the result afterward if the outcome matters; cancellation can race with completion. |

## Worked example

The [async execution example](../../../../examples/rest/085/async_execution.py) submits a synthetic `scale(amount=2, factor=3)` Query with pinned version `1.0.0`, retains its execution ID, then receives `running` and `succeeded(value=6)` in two bounded polls through the actual SDK. Run it from the skill root with `python -B examples/rest/085/async_execution.py`. The separate [get-result fixture](../../../../examples/rest/085/v2/functions/Execution/invoke_get_result.py) and [cancel fixture](../../../../examples/rest/085/v2/functions/Execution/invoke_cancel.py) check source-declared named failures. For a live application, submit using [execute_async](../../contracts/v2/functions/Query/execute_async.md), keep its returned ID, then poll with an overall deadline and finite attempt count. Do not resubmit merely because one poll reports `running`.

## Expected result and recovery

Completion requires the `succeeded` variant and a value validated against the selected Query version. A polling deadline leaves an unresolved execution ID; preserve it for later reconciliation. A cancel response confirms the request was accepted, not that business effects were undone. Permission denial or missing execution requires checking identity and the exact ID. A transport timeout during cancellation leaves its final state uncertain; repeat the idempotent cancellation request only when that remains the intended outcome, then inspect result. No fixture proves tenant execution.

## Access boundary

These fixtures run offline. Submission, polling, cancellation and checking effects of a live Query require authorized enrollment access and any Private Beta enablement.
