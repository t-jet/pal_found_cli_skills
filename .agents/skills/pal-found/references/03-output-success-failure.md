# Output, success, and failure

This part explains how the CLI formats results, what each exit code means, and
how to tell whether a Foundry change actually happened. Use it when you
interpret the result of any command.

## Output format: TOON vs JSON

`--format` accepts `json`, `toon`, or `auto`. The shared formatter reads
`FOUNDRY_AGENTIC_CLI_DEFAULT_FORMAT` when no format setting is supplied to it.
Some namespace parsers, including Filesystem, pass their default `auto` even
when the flag is omitted, masking that environment setting. Pass `--format`
explicitly when the selected output format matters. Under `auto`:

- **TOON** is used only when the top-level result is a list **and** every item
  is a dict with the identical field set.
- **JSON** is used for everything else: errors, single objects, empty lists,
  mixed-type arrays, heterogeneous-field arrays, binary download envelopes,
  and pagination metadata.

Data goes to stdout. Pagination metadata goes to stderr, preceded by the
separator line `# ---metadata-start---`. Retry events are separate NDJSON logs
on stderr and do not use that separator. The pinned CLI renders
`toon` with its own aligned-column table formatter, not the `toon-python` codec.
Use JSON when a machine consumer requires a defined JSON representation.

JSON formatting has no connection to a Foundry state change. The output shape
only reflects what the API returned and how the CLI rendered it.

## Exit codes

| Code | Meaning | Typical recovery |
| --- | --- | --- |
| 0 | Success | — |
| 1 | User input error (bad args, validation) | Fix the command line |
| 2 | Runtime authentication error; some namespace parsers also use 2 for usage errors | Inspect JSON error or stderr usage, then fix credentials or arguments |
| 3 | Permission denied (API 403) | Request access in Foundry |
| 4 | Not found (API 404) | Check RIDs/paths |
| 5 | Timeout (`asyncio.wait_for` exceeded) | Raise `FOUNDRY_AGENTIC_CLI_TIMEOUT_S` |
| 6 | Server error (API 5xx, including 503 after retries) | Retry later |
| 7 | Rate limit exhausted (HTTP 429 after retries) | Back off, reduce concurrency |
| 8 | Access control block (readonly/metadata-only/disabled) | Adjust ACL env vars |
| 9 | Configuration error (missing env var, bad `.env` path) | Fix configuration |

Handled runtime failures emit a JSON error object on stdout. Parser behavior
differs: Filesystem's argparse usage failures exit 2 with usage on stderr and
no JSON stdout; Data Health converts invalid input to exit 1 with JSON.

## Retries and timeouts

Exponential backoff uses jitter. The pinned default `RetryHandler` value 4 is
used as four retries after the initial call, allowing five calls in total.
The default outer per-call timeout is 30 s. `RetryHandler` reads
`FOUNDRY_AGENTIC_CLI_TIMEOUT_S` directly as a float without clamping;
`ConfigLoader` separately bounds the SDK configuration timeout to 1–3600 s. The
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
returned token to `--page-token`. An empty page is valid, even when a next-page
token exists. Continue until no token remains before concluding that no records
matched the scope.

## Common failure modes

| Symptom | Cause | Fix |
| --- | --- | --- |
| Exit 9 at startup | `FOUNDRY_TOKEN`/`FOUNDRY_HOSTNAME` missing, or `FOUNDRY_AGENTIC_CLI_ENV_FILE` points to a missing file | Set both variables; fix the env-file path |
| Exit 2 on a call | Token rejected by Foundry at request time | Replace `FOUNDRY_TOKEN` |
| Exit 8 on a write in read-only mode | `READONLY=true` active | Set `_READONLY=false` or remove the global flag |
| Exit 8 in metadata-only mode | Operation blocked by allow-list | Disable metadata-only or use a permitted operation |
| Binary download fails | Over 1.5 MiB bound (`FOUNDRY_AGENTIC_CLI_MAX_DOWNLOAD_BYTES`) | Stream the content outside the CLI |
| Binary upload fails in a namespace with an upload cap | Local upload cap, often 16 MiB; check the namespace record | Split the payload or use another supported transfer method |
| Exit 7 under load | HTTP 429 after retries | Back off and retry later |
| Exit 1 on a `-json` flag | Invalid JSON argument | Validate the JSON locally and re-run |

## Interpreting a result

1. A zero exit with a data body means the request completed and the platform
   answered. Read the returned identifiers and fields.
2. An empty page is not a failure. Check for a next-page token before concluding
   that no records matched the scope.
3. A page token means more results may exist; continue paging or note the
   partial view.
4. A nonzero exit has a meaning from the table above. Read the JSON error body
   when present; parser usage failures may instead provide stderr usage.
5. For operations that start asynchronous work (a run, a build, a session, a
   transform), a zero exit confirms the request was accepted, not that the
   work finished. Check status before claiming completion.
