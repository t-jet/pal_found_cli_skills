# Session trace operations

These records describe the `session_trace` commands in `pal-found-aip-agents`. Each record gives inputs, behavior, results, and examples.

### session_trace.get

- **Purpose and behavior:** Get the trace of an Agent response. The trace lists the sequence of steps that an Agent took to arrive at an answer. For example, a trace may include steps such as context retrieval and tool calls. Clients should poll this endpoint to check the realtime progress of a response until the trace is completed.
- **CLI inputs:** required `--alias`, `--session-trace-id`.
- **Input meaning:** `--alias`: Local name bound to the server session RID. `--session-trace-id`: The unique identifier for the trace.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The local alias must resolve to a session the caller can access.
- **Result:** Returns `SessionTrace` for the selected session trace.
- **Failure:** An unknown session trace identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-aip-agents session-trace get --alias order-help --session-trace-id <SESSION_TRACE_ID>`
