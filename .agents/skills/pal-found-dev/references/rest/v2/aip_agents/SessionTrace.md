# SessionTrace: aip agents operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

A trace records steps behind an Agent response, such as retrieval and tool calls. Retrieve it only for an exchange whose trace identity is known and visible to the caller.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Operations

### get

Read the trace for an Agent exchange and inspect retrieval/tool steps against that exchange ID. A trace is diagnostic data, not another generated answer.

Read the [exact SDK/HTTP contract](../../contracts/v2/aip_agents/SessionTrace/get.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/aip_agents/SessionTrace/get.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
