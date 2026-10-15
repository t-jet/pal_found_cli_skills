# AgentVersion: aip agents operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

An Agent version fixes the definitions used by a session, including tool and application-variable inputs. Choose an accessible published version or record the version returned by the Agent API.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Python client route

With a configured `FoundryClient` named `client`, use `client.aip_agents.Agent.AgentVersion` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.

## Operations

### get

Read one Agent version to check its application-variable and tool definitions before preparing session input.

Read the [exact SDK/HTTP contract](../../contracts/v2/aip_agents/AgentVersion/get.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/aip_agents/AgentVersion/get.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### list

Discover Agent versions newest first with a bounded page budget. Select a version by its returned identifier, not by a guessed string.

Read the [exact SDK/HTTP contract](../../contracts/v2/aip_agents/AgentVersion/list.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/aip_agents/AgentVersion/list.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

## Select a session-compatible version

Use a prepared client and Agent RID from an authorized application. This is a
Public Beta resource in SDK 1.101.0; enable preview support in the enrollment.
The raw list wrapper returns one page with explicit continuation state.

```python
raw = client.aip_agents.Agent.AgentVersion.with_raw_response.list(
    agent_rid, page_size=100, preview=True, request_timeout=30
)
try:
    page = raw.decode()
    versions = [(item.string, item.version) for item in page.data]
    next_page = page.next_page_token
finally:
    raw.close()

selected = client.aip_agents.Agent.AgentVersion.get(
    agent_rid, chosen_version_string, preview=True, request_timeout=30
)
assert selected.string == chosen_version_string
```

Select `chosen_version_string` from a returned item. Continue with
`page_token=next_page` under a finite page budget if more versions are needed.
The `version` object contains numeric major/minor fields; `string` is the
identifier accepted by `get`. Record that string with the session RID and
validate application-variable keys and value types against the version used
by the session. A missing version or unavailable preview capability requires
checking the Agent and enrollment; inventing a version string does not help.
