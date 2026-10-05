# Session operations

These records describe the `session` commands in `pal-found-aip-agents`. Each record gives inputs, behavior, results, and examples.

### session.blocking_continue

- **Purpose and behavior:** Continue a conversation session with an Agent, or add the first exchange to a session after creation. Adds a new exchange to the session with the provided inputs, and generates a response from the Agent. Blocks on returning the result of the added exchange until the response is fully generated. Streamed responses are also supported; see `streamingContinue` for details. Concurrent requests to continue the same session are not supported. Clients should wait to receive a response before sending the next message.
- **CLI inputs:** required `--alias`, `--parameter-inputs-json`, `--user-input-json`; optional `--contexts-override-json`, `--session-trace-id`.
- **Input meaning:** `--alias`: Local name bound to the server session RID. `--parameter-inputs-json`: Any supplied values for application variables to pass to the Agent for the exchange. `--user-input-json`: The user message for the Agent to respond to. `--contexts-override-json`: If set, automatic context retrieval is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session. `--session-trace-id` sets a trace ID to correlate this agent exchange with trace records.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The local alias must resolve to an accessible session; continue calls require valid application variables and user text.
- **Result:** Returns `SessionExchangeResult` after the agent finishes generating the exchange; inspect the response and trace ID.
- **Failure:** Concurrent continues on one session are unsupported. On timeout or interrupted stream, reload the session before sending another turn.
- **Example:** `pal-found-aip-agents session blocking-continue --alias order-help --parameter-inputs-json '{"currentCustomerOrders":{"type":"objectSet","ontology":"example-ontology","objectSet":{"type":"filter","objectSet":{"type":"base","objectType":"customerOrder"},"where":{"type":"eq","field":"customerId","value":"123abc"}}}}' --user-input-json '{"text":"What is the status of my order?"}'`

### session.cancel

- **Purpose and behavior:** Cancel an in-progress streamed exchange with an Agent which was initiated with `streamingContinue`. Canceling an exchange allows clients to prevent the exchange from being added to the session, or to provide a response to replace the Agent-generated response. Note that canceling an exchange does not terminate the stream returned by `streamingContinue`; clients should close the stream on triggering the cancellation request to stop reading from the stream.
- **CLI inputs:** required `--alias`, `--message-id`; optional `--response`.
- **Input meaning:** `--alias`: Local name bound to the server session RID. `--message-id`: The identifier for the in-progress exchange to cancel. This should match the `messageId` which was provided when initiating the exchange with `streamingContinue`. `--response` supplies replacement text for a canceled streamed agent response.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The local alias must resolve to a session the caller can access.
- **Result:** Returns `CancelSessionResponse`; close the client stream separately because cancel does not terminate it.
- **Failure:** Cancel requires the active streamed message ID. Closing the stream is a separate client step.
- **Example:** `pal-found-aip-agents session cancel --alias order-help --message-id 00f8412a-c29d-4063-a417-8052825285a5`

### session.create

- **Purpose and behavior:** Create a new conversation session between the calling user and an Agent. Use `blockingContinue` or `streamingContinue` to start adding exchanges to the session.
- **CLI inputs:** required `--alias`, `--agent-rid`; optional `--agent-version`.
- **Input meaning:** `--alias` is a local name stored by this CLI for the newly returned session RID. `--agent-rid` identifies the agent to converse with; optional `--agent-version` pins a published version instead of using the default.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The agent RID identifies an agent the caller may use; the local alias is available.
- **Result:** Returns the new `Session` and records its RID under the supplied local alias for later commands.
- **Failure:** Invalid session inputs or insufficient permission produce a structured error. After a timeout, read current state before retrying.
- **Example:** `pal-found-aip-agents session create --alias order-help --agent-rid ri.aip-agents..agent.732cd5b4-7ca7-4219-aabb-6e976faf63b1`

### session.delete

- **Purpose and behavior:** Delete a conversation session between the calling user and an Agent. Once deleted, the session can no longer be accessed and will not appear in session lists.
- **CLI inputs:** required `--alias`.
- **Input meaning:** `--alias`: Local name bound to the server session RID.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The local alias must resolve to a session the caller can access.
- **Result:** Returns no body. A zero exit confirms the session delete request completed.
- **Failure:** Invalid session inputs or insufficient permission produce a structured error. After a timeout, read current state before retrying.
- **Example:** `pal-found-aip-agents session delete --alias order-help`

### session.get

- **Purpose and behavior:** Get the details of a conversation session between the calling user and an Agent.
- **CLI inputs:** required `--alias`.
- **Input meaning:** `--alias`: Local name bound to the server session RID.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The local alias must resolve to a session the caller can access.
- **Result:** Returns `Session` for the selected session.
- **Failure:** An unknown session identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-aip-agents session get --alias order-help`

### session.list

- **Purpose and behavior:** List all conversation sessions between the calling user and an Agent that was created by this client. This does not list sessions for the user created by other clients. For example, any sessions created by the user in AIP Agent Studio will not be listed here. Sessions are returned in order of most recently updated first.
- **CLI inputs:** positionals `agent_rid`.
- **Input meaning:** `agent_rid` identifies the agent whose sessions to list. This endpoint returns only sessions that the calling user created through this client.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The agent exists and the caller can list their sessions for it. No local session alias is needed.
- **Result:** Returns `ListSessionsResponse` containing the visible matching session entries; an empty page means none matched that page.
- **Failure:** Invalid filters or a denied scope produce a structured error; an empty successful page is not an error.
- **Example:** `pal-found-aip-agents session list ri.aip-agents..agent.732cd5b4-7ca7-4219-aabb-6e976faf63b1`

### session.rag_context

- **Purpose and behavior:** Retrieve relevant context for a user message from the data sources configured for the session. This allows clients to pre-retrieve context for a user message before sending it to the Agent with the `contextsOverride` option when continuing a session, to allow any pre-processing of the context before sending it to the Agent.
- **CLI inputs:** required `--alias`, `--parameter-inputs-json`, `--user-input-json`.
- **Input meaning:** `--alias`: Local name bound to the server session RID. `--parameter-inputs-json`: Any values for application variables to use for the context retrieval. `--user-input-json`: The user message to retrieve relevant context for from the configured Agent data sources.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The local alias resolves to an accessible session, and application variables and user text match the agent configuration. This retrieval call does not continue the conversation.
- **Result:** Returns `AgentSessionRagContextResponse` with retrieved context for the supplied message; it does not add a conversation exchange.
- **Failure:** Unknown alias, invalid application variables, or unavailable retrieval source returns an error; no exchange is added by this call.
- **Example:** `pal-found-aip-agents session rag-context --alias order-help --parameter-inputs-json '{"customerName":{"type":"string","value":"Titan Technologies"}}' --user-input-json '{"text":"What is the status of my order?"}'`

### session.streaming_continue

- **Purpose and behavior:** Continue a session or add its first exchange. The SDK endpoint produces response text as a stream, but this CLI waits for the SDK bytes and saves them as a bounded download. It does not print tokens as they arrive. Reload session content after completion to inspect the saved exchange. Concurrent continue requests on one session are unsupported; `cancel` can target an in-progress exchange.
- **CLI inputs:** required `--alias`, `--parameter-inputs-json`, `--user-input-json`; optional `--contexts-override-json`, `--message-id`, `--session-trace-id`, `--output-filename`.
- **Input meaning:** `--alias`: Local name bound to the server session RID. `--parameter-inputs-json`: Any supplied values for application variables to pass to the Agent for the exchange. `--user-input-json`: The user message for the Agent to respond to. `--contexts-override-json`: If set, automatic context retrieval is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session. `--message-id` identifies the streamed exchange; reuse its ID to cancel that exchange; `--output-filename` chooses a basename for the downloaded content in the CLI download directory; `--session-trace-id` sets a trace ID to correlate this agent exchange with trace records.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The local alias must resolve to an accessible session; continue calls require valid application variables and user text.
- **Result:** Prints a JSON download envelope with saved path, byte count, checksums, and truncation status. `--output-filename` selects a basename inside the configured download directory. Open that file to read the response text; reload session content for full exchange details.
- **Failure:** Concurrent continues on one session are unsupported. On timeout or interrupted stream, reload the session before sending another turn.
- **Example:** `pal-found-aip-agents session streaming-continue --alias order-help --parameter-inputs-json '{"currentCustomerOrders":{"type":"objectSet","ontology":"example-ontology","objectSet":{"type":"filter","objectSet":{"type":"base","objectType":"customerOrder"},"where":{"type":"eq","field":"customerId","value":"123abc"}}}}' --user-input-json '{"text":"What is the status of my order?"}'`

### session.update_title

- **Purpose and behavior:** Update the title for a session. Use this to set a custom title for a session to help identify it in the list of sessions with an Agent.
- **CLI inputs:** required `--alias`, `--title`.
- **Input meaning:** `--alias`: Local name bound to the server session RID. `--title`: The new title for the session. The maximum title length is 200 characters. Titles are truncated if they exceed this length.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The local alias must resolve to a session the caller can access.
- **Result:** Returns no body. A zero exit confirms the session update title request completed.
- **Failure:** Invalid session inputs or insufficient permission produce a structured error. After a timeout, read current state before retrying.
- **Example:** `pal-found-aip-agents session update-title --alias order-help --title 'Order status 02/01'`
