# Content: aip agents operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

Session content contains exchanges between the calling user and an Agent. Read it to reconcile a continued, cancelled or uncertain exchange.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Python client route

With a configured `FoundryClient` named `client`, use `client.aip_agents.Agent.Session.Content` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.

## Operations

### get

Read all content for one session after a continuation or cancellation. Inspect each exchange's user input, contexts and result, including `interrupted_output` and `session_trace_id`, to reconcile the visible outcome before deciding whether to retry. Exchanges do not return the streaming message ID; retain that ID from the stream when cancellation is needed.

Read the [exact SDK/HTTP contract](../../contracts/v2/aip_agents/Content/get.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/aip_agents/Content/get.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
