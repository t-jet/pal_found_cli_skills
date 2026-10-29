# Conversation sessions and Agent exchanges

[Operation catalog](../../catalog.md) | [REST development](../../../rest-api.md)

## Concept and lifecycle

A session records a conversation between the calling user and an existing AIP
Agent. Creating it does not add an exchange. Creation selects an Agent version;
when omitted, the latest published version at creation time is used. That
version is recorded on the returned session. A session's RID, metadata and
Agent version are useful when resuming a conversation and diagnosing missing
tools or incompatible application variables.

## Prerequisites

Live work requires an enabled AIP Agents capability, an accessible Agent and
the prepared SDK 1.101.0. These operations are Public Beta in this frozen SDK.
Check whether preview operations are permitted in the enrollment. The example
uses `preview=True` explicitly. The SDK does not establish a universal OAuth
scope that replaces Agent, tool, Ontology or model permissions.

## Procedure

1. Choose a known accessible Agent RID and intended published version. A
   missing published version cannot be repaired by inventing a version string.
2. Read [create](../../contracts/v2/aip_agents/Session/create.md), then call
   `create(agent_rid, agent_version=..., preview=True)`. Retain the returned
   session RID and actual Agent version.
3. Retrieve it through [get](../../contracts/v2/aip_agents/Session/get.md),
   supplying both Agent and session RIDs. Check metadata and version rather
   than assuming a local conversation identifier is a valid server session.
4. Discover sessions through [list](../../contracts/v2/aip_agents/Session/list.md)
   using finite raw-page retrieval. This returns the calling user's sessions
   created by this client, ordered by most recently updated. It excludes that
   user's sessions created by other clients, including AIP Chatbot Studio.
   Preserve continuation state and distinguish partial retrieval from completion.
5. To send messages, select the catalog's `blocking_continue` or
   `streaming_continue` contract. Creation alone generates no answer. Concurrent
   continue requests on one session are unsupported; await the current result
   before sending the next message.

## Worked example

### Choose the operation by its effect

| Operation | Inputs and effect | Follow-up |
| --- | --- | --- |
| [create](../../contracts/v2/aip_agents/Session/create.md) | Agent RID and optional published version; creates a session with no exchange. | Retain returned RID/version. |
| [get](../../contracts/v2/aip_agents/Session/get.md) | Agent and session RIDs; reads session metadata. | Check identity/version before resuming. |
| [list](../../contracts/v2/aip_agents/Session/list.md) | Agent RID and optional paging inputs; discovers accessible sessions. | Bound retrieval and preserve the cursor. |
| [blocking_continue](../../contracts/v2/aip_agents/Session/blocking_continue.md) | User input and application-variable values; adds an exchange and waits for its complete generated response. | Inspect the exchange result before another continuation. |
| [streaming_continue](../../contracts/v2/aip_agents/Session/streaming_continue.md) | Same conversation inputs with optional UUID message/trace IDs; generates Markdown response text as a byte stream. | Bound consumption and reload session content after completion. |
| [rag_context](../../contracts/v2/aip_agents/Session/rag_context.md) | User input and application-variable values; retrieves configured context before continuation. | Inspect or preprocess it, then supply a compatible context override. |
| [cancel](../../contracts/v2/aip_agents/Session/cancel.md) | Agent/session RIDs and the exact in-progress streaming message UUID; cancels that exchange. | Close the stream separately and reload content after a race. |
| [update_title](../../contracts/v2/aip_agents/Session/update_title.md) | Session identity and a title; changes its label for discovery. | Read the session again and verify `metadata.title`; the title is not a unique identifier. |
| [delete](../../contracts/v2/aip_agents/Session/delete.md) | Agent and session RIDs; removes the conversation from access and listings. | Retain diagnostic IDs before deletion; deletion is not stream cancellation. |

The ordinary `streaming_continue` result in SDK 1.101.0 is `bytes`, not a
typed SSE iterator. Use `with_streaming_response.streaming_continue(...)`
and `iter_bytes()` when consuming incremental response bytes. Keep a byte
budget, deadline and context lifetime as described in
[response modes](../../client-behavior.md). Do not pass the Markdown byte
response to an SSE decoder merely because the operation is streaming.

Provide a client-generated `message_id` UUID if cancellation is needed.
`cancel(message_id=..., response=...)` stores the supplied replacement response;
omitting `response` prevents that exchange from being added. Cancellation does
not terminate the original HTTP stream. Leave its context or close it when
cancelling. `CancelSessionFailedMessageNotInProgress` can mean that the exchange
never started, already finished, was already cancelled, or has not started yet
after a race. Reload [session content](../../contracts/v2/aip_agents/Content/get.md)
and reconcile before sending another message.

`rag_context` retrieves relevant context from data sources configured for the
session. Supplying `contexts_override` to continuation skips automatic retrieval
and uses that supplied list instead. Application-variable keys and discriminated
values must match the Agent version recorded on the session. Empty parameters
are suitable only for a configured Agent requiring no application variables.
Invalid parameter/type errors require checking that version's definitions;
another session or a guessed object set does not repair a mismatch.

### Runnable creation and discovery

```bash
python -B examples/rest/087/sessions.py
```

Run from this skill directory. The prepared SDK serializes create/get/list
requests into a fake transport with no public or tenant call. The example
pins version `1.0`, verifies JSON `agentVersion`, preview query and resource
paths, decodes session metadata and bounds page retrieval. Distinct typed
`CreateSessionPermissionDenied`, `SessionNotFound` and `AgentNotFound`
fixtures include their complete required error parameters.

The session contains zero messages and an estimated expiry time. Adapt exact
method calls, identifiers, access checks and version choice to your application;
use ordinary authorized clients for live execution. Synthetic payloads prove
SDK/application handling and do not simulate model generation or tool execution.

## Expected result and checks

The runner prints `Session create/get/list request, result and error fixtures passed`.
Live checks compare returned session identity, Agent identity/version, metadata
and retrieval completeness. An estimated expiry is metadata, not a promise
that access or session state remains unchanged indefinitely.

## Failures and recovery

Create denied requires verifying calling identity and Agent access. Missing
Agent/session errors require checking both RIDs and visibility. No published
Agent version requires an authorized publication decision or a supported
explicit version. Missing Actions, Functions, Ontology entities or language
models require checking the Agent's configured tools and the caller's access;
creating another session does not grant missing access.

If create times out after submission, preserve context and reconcile bounded
session listings before retrying. Similar metadata does not establish request
identity; no universal create-idempotency guarantee is documented. Treat an
unresolved creation as uncertain rather than automatically producing another
conversation. Continuation and cancellation have separate contracts and
effects; do not infer a cancellation endpoint from generic HTTP handling.

## Access boundary

Prepared-library fixtures run offline. Live session operations need enrollment
connectivity, enabled capability and authorized Agent/tool/model access.
Model generation and real session lifecycle remain separate live checks.

### blocking_continue

Submit one exchange and wait for the complete Agent response. Check its user input and result, including `result.session_trace_id` and `result.interrupted_output`, before sending another request. The returned exchange has no exchange or streaming message ID.

Read the [exact SDK/HTTP contract](../../contracts/v2/aip_agents/Session/blocking_continue.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/aip_agents/Session/blocking_continue.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### cancel

Cancel an in-progress streaming exchange by its exact message UUID. Cancellation does not close the original HTTP stream; close that separately and reread content after a race.

Read the [exact SDK/HTTP contract](../../contracts/v2/aip_agents/Session/cancel.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/aip_agents/Session/cancel.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### delete

Delete the exact session RID. It then disappears from session reads and lists; retain diagnostic IDs before deletion.

Read the [exact SDK/HTTP contract](../../contracts/v2/aip_agents/Session/delete.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/aip_agents/Session/delete.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### rag_context

Retrieve relevant context for a prospective user message from configured data sources. Inspect context before an explicit override in a continuation.

Read the [exact SDK/HTTP contract](../../contracts/v2/aip_agents/Session/rag_context.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/aip_agents/Session/rag_context.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### streaming_continue

Start one exchange and consume Markdown response bytes under a byte/time budget. A byte stream is not a typed SSE iterator.

Read the [exact SDK/HTTP contract](../../contracts/v2/aip_agents/Session/streaming_continue.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/aip_agents/Session/streaming_continue.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### update_title

Set a session display title. This operation returns no content; call `get` afterward and verify `metadata.title`. The session RID remains its identity.

Read the [exact SDK/HTTP contract](../../contracts/v2/aip_agents/Session/update_title.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/aip_agents/Session/update_title.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

## Python client route

With a configured `FoundryClient` named `client`, use `client.aip_agents.Agent.Session` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.
