# v2.functions resources and operations


Use Function and Query metadata to choose a published callable version and its input/output types. Execute or stream only with arguments matching the selected version; validation or permission failures require correcting the input or access before retrying. Read the selected operation contract before invocation; stage, API version and result lifetime remain operation-specific.

| Operation | Stage |
| --- | --- |
| [v2.functions.Execution.cancel](../../contracts/v2/functions/Execution/cancel.md) | Private Beta |
| [v2.functions.Execution.get_result](../../contracts/v2/functions/Execution/get_result.md) | Private Beta |
| [v2.functions.Query.execute](../../contracts/v2/functions/Query/execute.md) | Public Beta |
| [v2.functions.Query.execute_async](../../contracts/v2/functions/Query/execute_async.md) | Private Beta |
| [v2.functions.Query.get](../../contracts/v2/functions/Query/get.md) | Public Beta |
| [v2.functions.Query.get_by_rid](../../contracts/v2/functions/Query/get_by_rid.md) | Public Beta |
| [v2.functions.Query.get_by_rid_batch](../../contracts/v2/functions/Query/get_by_rid_batch.md) | Public Beta |
| [v2.functions.Query.streaming_execute](../../contracts/v2/functions/Query/streaming_execute.md) | Public Beta |
| [v2.functions.Query.streaming_execute_events](../../contracts/v2/functions/Query/streaming_execute_events.md) | Private Beta |
| [v2.functions.ValueType.get](../../contracts/v2/functions/ValueType/get.md) | Private Beta |
| [v2.functions.VersionId.get](../../contracts/v2/functions/VersionId/get.md) | Private Beta |

[All services](../../catalog.md) | [SDK handling](../../client-behavior.md)

[Part 1](index.md)
