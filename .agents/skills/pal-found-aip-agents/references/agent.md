# Agent operations

These records describe the `agent` commands in `pal-found-aip-agents`. Each record gives inputs, behavior, results, and examples.

### agent.all_sessions

- **Purpose and behavior:** List all conversation sessions between the calling user and all accessible Agents that were created by this client. Sessions are returned in order of most recently updated first.
- **CLI inputs:** .
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The agent RID identifies an accessible AIP agent where the command asks for one.
- **Result:** Returns `AgentsSessionsPage` containing the visible matching agent entries; an empty page means none matched that page.
- **Failure:** Invalid filters or a denied scope produce a structured error; an empty successful page is not an error.
- **Example:** `pal-found-aip-agents agent all-sessions`

### agent.get

- **Purpose and behavior:** Get details for an AIP Agent.
- **CLI inputs:** positionals `agent_rid`; optional `--version`.
- **Input meaning:** `agent_rid`: Resource identifier (RID) of the named Foundry resource. `--version`: The version of the Agent to retrieve. If not specified, the latest published version will be returned.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The local alias must resolve to a session the caller can access.
- **Result:** Returns `Agent` for the selected agent.
- **Failure:** An unknown agent identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-aip-agents agent get ri.aip-agents..agent.732cd5b4-7ca7-4219-aabb-6e976faf63b1`
