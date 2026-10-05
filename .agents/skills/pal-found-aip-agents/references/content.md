# Content operations

These records describe the `content` commands in `pal-found-aip-agents`. Each record gives inputs, behavior, results, and examples.

### content.get

- **Purpose and behavior:** Get the conversation content for a session between the calling user and an Agent.
- **CLI inputs:** required `--alias`.
- **Input meaning:** `--alias`: Local name bound to the server session RID.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The local alias must resolve to a session the caller can access.
- **Result:** Returns `Content` for the selected content.
- **Failure:** An unknown content identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-aip-agents content get --alias order-help`
