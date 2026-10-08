# AgentVersion: aip agents operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

An Agent version fixes the definitions used by a session, including tool and application-variable inputs. Choose an accessible published version or record the version returned by the Agent API.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Operations

### get

Read one Agent version to check its application-variable and tool definitions before preparing session input.

Read the [exact SDK/HTTP contract](../../contracts/v2/aip_agents/AgentVersion/get.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/aip_agents/AgentVersion/get.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### list

Discover Agent versions newest first with a bounded page budget. Select a version by its returned identifier, not by a guessed string.

Read the [exact SDK/HTTP contract](../../contracts/v2/aip_agents/AgentVersion/list.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/aip_agents/AgentVersion/list.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
