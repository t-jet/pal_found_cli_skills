# Agent version operations

These records describe the `agent_version` commands in `pal-found-aip-agents`. Each record gives inputs, behavior, results, and examples.

### agent_version.get

- **Purpose and behavior:** Get version details for an AIP Agent.
- **CLI inputs:** positionals `agent_rid`, `agent_version_string`.
- **Input meaning:** `agent_rid`: Resource identifier (RID) of the named Foundry resource. `agent_version_string`: The semantic version of the Agent, formatted as "majorVersion.minorVersion".
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The local alias must resolve to a session the caller can access.
- **Result:** Returns `AgentVersion` for the selected agent version.
- **Failure:** An unknown agent version identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-aip-agents agent-version get ri.aip-agents..agent.732cd5b4-7ca7-4219-aabb-6e976faf63b1 1.0`

### agent_version.list

- **Purpose and behavior:** List all versions for an AIP Agent. Versions are returned in descending order, by most recent versions first.
- **CLI inputs:** positionals `agent_rid`.
- **Input meaning:** `agent_rid`: Resource identifier (RID) of the named Foundry resource.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The agent RID identifies an accessible agent; `get` also needs a published version string.
- **Result:** Returns `ListAgentVersionsResponse` containing the visible matching agent version entries; an empty page means none matched that page.
- **Failure:** Invalid filters or a denied scope produce a structured error; an empty successful page is not an error.
- **Example:** `pal-found-aip-agents agent-version list ri.aip-agents..agent.732cd5b4-7ca7-4219-aabb-6e976faf63b1`
