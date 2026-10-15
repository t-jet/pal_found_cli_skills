# Audit LogFile discovery

## Route and prerequisites

Use the public v2 composed client, `client.audit.Organization.LogFile.with_raw_response.list`, in `foundry-platform-sdk==1.101.0`. The SDK call needs an authorized organization RID, enrollment hostname, and an identity permitted to list that organization's audit files. A `UserTokenAuth` token, public OAuth client, or confidential OAuth client must be configured for that identity; successful authentication alone does not grant audit access. Keep credentials out of output. The operation is Stable and read only. This is the Platform SDK, not an enrollment-specific generated OSDK. Source: isolated skill **Develop with the Foundry REST API → Prerequisites**, **REST identity and effective access → Credentials and acting identity**, **LogFile: audit operations → Python client route**, and **v2.audit.LogFile.list → Public Python client route / Documented operation errors**.

## Ordered discovery

1. Fix `organization_rid` and inclusive `start_date=date(2026, 10, 1)`, `end_date=date(2026, 10, 7)`. Reject an inverted range. The first call must include `start_date`, although the Python parameter has a default. Keep both dates and organization unchanged on all pages.
2. Construct `FoundryClient` with the authorized hostname and auth object. Set `Config(timeout=10, max_retries=1, propagate_qos="PROPAGATE_429_AND_503_TO_CALLER")`. For each raw list call, use `page_size=100`, a positive `request_timeout` of at most five whole seconds, and the current opaque `page_token`; omit the token on the first page. The HTTP operation is `GET /api/v2/audit/organizations/{organizationRid}/logFiles` with `startDate`, `endDate`, `pageSize`, and optional `pageToken` query entries.
3. Decode and close each `ApiResponse`. Collect each page's `LogFile.id` values. An empty `data` page with `nextPageToken` still requires a following call. Preserve the token exactly; never derive one. Use at most five pages, 500 accepted IDs, and 30 elapsed seconds. Stop before a request if less than one whole second remains. Check the deadline again after every response.
4. Return `complete=true` only after a fixed-window response has no `nextPageToken` and the post-response deadline check passes. Return `complete=false` with a reason and cursor for a page, item, or time limit, a repeated token, a lost response, or permission denial. If the item cap splits a page, retain its unread IDs as `remaining_on_page`; consume them before following the returned next cursor. For a page cap, the cursor is the next unrequested page token. A repeated token is a partial result requiring investigation, not proof of completion.

Source: isolated skill **v2.audit.LogFile.list → Purpose and parameter meaning / SDK invocation contract / Wire request / Response modes**, **LogFile: audit operations → list**, and **SDK clients, response modes and finite work → Bounded pagination / Timeouts, throttling and uncertain writes**.

## Runnable public SDK fixture

[audit_reader_fixture.py](audit_reader_fixture.py) builds `foundry_sdk.v2.FoundryClient` and uses `httpx.MockTransport` behind the public client's HTTP session. It invokes `client.audit.Organization.LogFile.with_raw_response.list` and asserts the serialized method, path, bearer header, inclusive dates, page size, and cursor sequence. It decodes and closes each raw response. The fixture covers a populated page, an empty page with continuation, a final populated page, page and item caps, repeated tokens, deadlines before and after a response, a lost response, permission denial, and the named `MissingStartDate` error. The supplied cooperative guard blocks public DNS/socket calls and proves `PUBLIC_NETWORK_DENIED` before the fixture runs.

From repository root:

```powershell
python pal_found_cli_skills/tests/fixtures/feature015_qa/evidence/final_reader_audit_postfix/audit_reader_fixture.py
```

Observed exit code: `0`. Full captured stdout: [fixture_output.jsonl](fixture_output.jsonl). It contains ten `PASS` rows, including `public_network_guard`. The complete traversal requested cursors `[null, "A", "B"]` and returned IDs `["log-1", "log-2"]`, `complete=true`, `cursor=null`. The page cap returned `["log-1"]`, `complete=false`, `reason="page_budget"`, `cursor="B"`. The item cap returned `["log-1"]`, `remaining_on_page=["log-2"]`, `complete=false`, `cursor="A"`. The repeated token case returned `reason="repeated_token"`, `cursor="A"`. The lost response and permission cases returned partial outcomes after one request each. Source: isolated skill **LogFile: audit operations → list** and **v2.audit.LogFile.list → Complete referenced models and errors**.

## Failure handling and outcome boundary

`MissingStartDate` means correct the first request's date. `ListLogFilesPermissionDenied` means inspect the acting identity, application registration, and organization policy with an authorized owner; do not retry the same denied call in a loop. If a response is lost, retain the fixed filters, requested cursor, and accepted IDs. A later bounded read may retry that same cursor after connectivity is checked, with ID deduplication; do not claim the missing page was empty. A repeated token needs operator inspection. A page, item, or time cap requires a later run with a fresh explicit budget; process retained unread page IDs before fetching the next cursor. A request timeout cannot forcibly stop a noncooperative transport, so a response arriving after the deadline remains partial. Source: isolated skill **SDK clients, response modes and finite work → Errors and cleanup / Timeouts, throttling and uncertain writes** and **LogFile: audit operations → list**.

This evidence proves only SDK request serialization and synthetic response handling. It does not prove any real organization's files exist, tenant permission, enrollment connectivity, or complete live discovery. Source: isolated skill **Develop with the Foundry REST API → Access boundary**.

The first fixture run failed with exit code `1` in `lost_response`: `httpx.ReadTimeout: lost` was converted by installed SDK 1.101.0 into `foundry_sdk.ReadTimeout: lost`. Catching that public SDK exception made the final run pass. The consulted local headings **SDK clients, response modes and finite work → Timeouts, throttling and uncertain writes / Errors and cleanup**, **v2.audit.LogFile.list → Documented operation errors**, and **LogFile: audit operations → list** do not state this exception conversion. That is a guide gap; the recovery behavior above is grounded in the installed SDK observation and final fixture, not in those headings.

## Evidence identity

- Isolated skill snapshot: 4,439 files; manifest tree SHA-256 `790d67ad9a291e4810ad97dfdc3ad2d6c8a62fe1237b2f34a47b615dcf6adb4f`; source repository head recorded there as `633de9fea666f58d5c7b09f0cdf4bf75d2aeb20e`.
- `audit_reader_fixture.py` SHA-256: `2327ad5e5f6a2b870c9bbd6e4253400ad9a52717902c416c4111ccee720f2d7d`.
- `fixture_output.jsonl` SHA-256: `70121fcd41b6bc97a7f88f0016b7d28080d8c009698724af11618913626cf2ec`.
- Supplied guard SHA-256: `3f6152af717d97904159ba92f5907e2f3b6d879e631cd531116ea5b81c35559b`.
