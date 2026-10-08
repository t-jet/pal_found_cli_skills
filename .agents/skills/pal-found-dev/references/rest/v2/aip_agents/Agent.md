# Agent: aip agents operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

An Agent has a stable RID and published versions. Sessions are conversations created by a client for a caller. Check the Agent and its version before resuming or listing sessions.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Operations

### all_sessions

List this caller's sessions across accessible Agents that were created by this client. Results are newest-updated first; other clients' sessions are outside this list.

Read the [exact SDK/HTTP contract](../../contracts/v2/aip_agents/Agent/all_sessions.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/aip_agents/Agent/all_sessions.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### get

Read the Agent RID and selected or latest published version. A missing latest version requires publishing one or explicitly selecting an accessible version.

Read the [exact SDK/HTTP contract](../../contracts/v2/aip_agents/Agent/get.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/aip_agents/Agent/get.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
