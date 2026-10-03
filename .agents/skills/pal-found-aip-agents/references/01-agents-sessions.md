# Agent and session operations

This part documents the `agent` (2), `agent_version` (2), and `session` (9)
resource clients (13 operations). An agent is a conversational entry point; a
session carries a conversation; sessions are created, continued, and canceled.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/aip_agents/scripts/pal_found_aip_agents_cli.py`;
SDK `foundry_sdk/v2/aip_agents/{agent,agent_version,session}.py` at pinned
commit `2da67907`. Reviewer architect (CODEREVIEW-049), 2026-10-03. QA
baseline TESTCASE-011.

## Operation records

### agent.all_sessions

- **Class**: read. Returns all sessions for an agent.
- **Preconditions**: can read the agent's sessions.
- **Effect**: returns sessions, paged.
- **Inputs**: positional `agent_rid`; paging options.
- **Success**: sessions; empty if none.
- **Example**: `pal-found-aip-agents agent all-sessions <AGENT_RID>`.

### agent.get

- **Class**: read. Returns an agent's metadata.
- **Preconditions**: can read the agent.
- **Effect**: returns the agent record (configuration, versions).
- **Inputs**: positional `agent_rid`.
- **Success**: the agent record.
- **Failure**: exit 4 if missing.

### agent_version.get / list

- **Class**: read. Returns agent version metadata.
- **Preconditions**: can read the agent.
- **Effect**: `get` returns one version; `list` pages versions.
- **Inputs**: `get` positional `agent_rid`, `version`; `list` positional
  `agent_rid` + paging.
- **Success**: the version record(s).

### session.blocking_continue

- **Class**: execute (write). Continues a session and waits for the response.
- **Preconditions**: a valid session; user input supplied.
- **Effect**: sends the turn and returns the agent's response (blocks until
  complete).
- **Inputs**: positional `session_rid`; `--user-input-json`,
  `--contexts-override-json`.
- **Success**: the agent's message/result.
- **Failure**: exit 5 on timeout; session may still be pending server-side.
- **Example**: `pal-found-aip-agents session blocking-continue <SESSION_RID> --user-input-json '{"input":"summarize"}'`.

### session.cancel

- **Class**: change (write). Cancels an in-flight session turn.
- **Preconditions**: a session with an active turn.
- **Effect**: cancels the running turn.
- **Inputs**: positional `session_rid`.
- **Success**: returns the canceled session.

### session.create

- **Class**: create (write). Creates a new agent session.
- **Preconditions**: an agent you can start a session with.
- **Effect**: creates a session (empty until continued).
- **Inputs**: positional `agent_rid`; initial title/inputs.
- **Success**: the created session, including its RID.
- **Example**: `pal-found-aip-agents session create <AGENT_RID>`.

### session.delete

- **Class**: delete (write). Deletes a session (and its content).
- **Preconditions**: can delete the session.
- **Effect**: permanently deletes the session.
- **Inputs**: positional `session_rid`.
- **Success**: returns the deleted session.
- **Failure**: exit 8 readonly block.

### session.get

- **Class**: read. Returns a session.
- **Preconditions**: can read the session.
- **Effect**: returns the session record.
- **Inputs**: positional `session_rid`.
- **Success**: the session.
- **Failure**: exit 4 if missing.

### session.list

- **Class**: read. Lists sessions.
- **Preconditions**: can read sessions.
- **Effect**: returns sessions, paged.
- **Inputs**: paging options.
- **Success**: sessions; empty if none.

### session.rag_context

- **Class**: read. Returns retrieval-augmented context for a session turn input.
- **Preconditions**: a session; a RAG-enabled flow.
- **Effect**: returns the retrieved context the agent would use.
- **Inputs**: positional `session_rid`; input JSON.

### session.streaming_continue

- **Class**: execute (write, streaming). Continues a session and streams the
  response.
- **Preconditions**: a valid session and user input.
- **Effect**: sends the turn and streams tokens; a zero exit means the CLI
  stream ended, not that the platform finished.
- **Inputs**: positional `session_rid`; `--user-input-json`, `--stream-format`.
- **Success**: a stream of response tokens.
- **Failure**: exit 5 on timeout mid-stream; do not assume a saved final state.

### session.update_title

- **Class**: change (write). Updates a session's title.
- **Preconditions**: can write the session.
- **Effect**: sets the session title.
- **Inputs**: positional `session_rid`; `--title`.
- **Success**: the updated session.

## Evidence and review

Reviewed against the installed `pal-found-aip-agents` parser and pinned SDK
sources (commit `2da67907`). `session.create/continue/cancel/delete` and
`update_title` are execute/write with side effects; session content is not
logged. Blocking/streaming continuations return only after the CLI's own wait;
do not assume a server-side final state on timeout (AC-D-013-05). No
unsupported operation is documented as callable.
