# Output, success, and failure

This part explains how the CLI formats results, what each exit code means, and
how to tell whether a Foundry change actually happened. Use it when you
interpret the result of any command.

## Output format: TOON vs JSON

`--format` accepts `json`, `toon`, or `auto`; `FOUNDRY_AGENTIC_CLI_DEFAULT_FORMAT`
(default `auto`) sets the same choice. Under `auto`:

- **TOON** is used only when the top-level result is a list **and** every item
  is a dict with the identical field set.
- **JSON** is used for everything else: errors, single objects, empty lists,
  mixed-type arrays, heterogeneous-field arrays, binary download envelopes,
  and pagination metadata.

Data goes to stdout. Metadata (pagination, retry info) goes to stderr,
preceded by the separator line `# ---metadata-start---`. TOON rendering uses
`toon-python`; data is on stdout, metadata on stderr.

JSON formatting has no connection to a Foundry state change. The output shape
only reflects what the API returned and how the CLI rendered it.

## Exit codes

| Code | Meaning | Typical recovery |
| --- | --- | --- |
| 0 | Success | — |
| 1 | User input error (bad args, validation) | Fix the command line |
| 2 | Authentication error (missing/invalid token or hostname) | Check `FOUNDRY_TOKEN`/`FOUNDRY_HOSTNAME` |
| 3 | Permission denied (API 403) | Request access in Foundry |
| 4 | Not found (API 404) | Check RIDs/paths |
| 5 | Timeout (`asyncio.wait_for` exceeded) | Raise `FOUNDRY_AGENTIC_CLI_TIMEOUT_S` |
| 6 | Server error (API 5xx, excluding retried 503) | Retry later |
| 7 | Rate limit exhausted (HTTP 429 after retries) | Back off, reduce concurrency |
| 8 | Access control block (readonly/metadata-only/disabled) | Adjust ACL env vars |
| 9 | Configuration error (missing env var, bad `.env` path) | Fix configuration |

All failures also emit a JSON error object on stdout.

## Retries and timeouts

Exponential backoff with jitter, max 4 total attempts (1 + 3 retries), per-call
timeout 30 s by default (`FOUNDRY_AGENTIC_CLI_TIMEOUT_S`, range 1–3600). The
Streams namespace uses `FOUNDRY_AGENTIC_CLI_STREAMS_TIMEOUT_S` (default 120 s)
for long-lived record connections.

A nonzero exit from a timeout or retry means the CLI did not get a conclusive
response. Do **not** assume the intended Foundry change happened. Use a status
or read operation to check.

## Logs

NDJSON structured logs go to stderr. Required fields: `ts`, `level`,
`logger`, `msg`; context fields (`op`, `call_id`, `attempt`, `delay_ms`,
`access_decision`, `http_status`) appear when relevant.
`FOUNDRY_AGENTIC_CLI_LOG_LEVEL` (default `WARNING`) controls verbosity.

## Paging

A paged operation returns a page of results and, when another page exists, a
page token (possibly inside metadata on stderr). To fetch all results, pass the
returned token to `--page-token`. An empty result set is a valid outcome and is
not an error; it means no records matched the scope. Confirm whether the result
list is empty or truncated before concluding.

## Common failure modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| Exit 9 at startup | `FOUNDRY_TOKEN`/`FOUNDRY_HOSTNAME` missing, or `FOUNDRY_AGENTIC_CLI_ENV_FILE` points to a missing file | Set both variables; fix the env-file path |
| Exit 2 on a call | Token rejected by Foundry at request time | Replace `FOUNDRY_TOKEN` |
| Exit 8 on a write in read-only mode | `READONLY=true` active | Set `_READONLY=false` or remove the global flag |
| Exit 8 in metadata-only mode | Operation blocked by allow-list | Disable metadata-only or use a permitted operation |
| Binary download fails | Over 1.5 MiB bound (`FOUNDRY_AGENTIC_CLI_MAX_DOWNLOAD_BYTES`) | Stream the content outside the CLI |
| Binary upload fails | Over 16 MiB bound | Split or transfer large media outside the CLI |
| Exit 7 under load | HTTP 429 after retries | Back off and retry later |
| Exit 1 on a `-json` flag | Invalid JSON argument | Validate the JSON locally and re-run |

## Interpreting a result

1. A zero exit with a data body means the request completed and the platform
   answered. Read the returned identifiers and fields.
2. An empty result means no matching records for that scope; it is not a
   failure.
3. A page token means more results may exist; continue paging or note the
   partial view.
4. A nonzero exit has a specific meaning from the table above. Read the JSON
   error body for the server-provided detail.
5. For operations that start asynchronous work (a run, a build, a session, a
   transform), a zero exit confirms the request was accepted, not that the
   work finished. Check status before claiming completion.
