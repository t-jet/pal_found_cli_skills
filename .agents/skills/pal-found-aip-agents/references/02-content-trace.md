# Session content and trace operations

This part documents the `content` (1) and `session_trace` (1) resource clients
(2 operations).

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/aip_agents/scripts/pal_found_aip_agents_cli.py`;
SDK `foundry_sdk/v2/aip_agents/{content,session_trace}.py` at pinned commit
`2da67907`. Reviewer architect (CODEREVIEW-049), 2026-10-03. QA baseline
TESTCASE-011.

## Operation records

### content.get

- **Class**: read. Fetches the content (message contents) of a session.
- **Preconditions**: can read the session.
- **Effect**: returns the session's message content.
- **Inputs**: positional `session_rid` (and content selectors).
- **Success**: the content; may be large for long sessions.
- **Failure**: exit 4 if session missing.
- **Example**: `pal-found-aip-agents content get <SESSION_RID>`.

### session_trace.get

- **Class**: read. Returns the trace of a session's turn.
- **Preconditions**: can read the session/trace.
- **Effect**: returns the execution trace for a session turn.
- **Inputs**: positional `session_rid`, `session_trace_id`.
- **Success**: the trace; includes agent reasoning/step detail.

## Evidence and review

Both operations are read-class. Reviewed against the installed
`pal-found-aip-agents` parser and pinned SDK sources (commit `2da67907`).
Traces may contain sensitive agent reasoning; handle accordingly. Reads never
write. No unsupported operation is documented as callable.
