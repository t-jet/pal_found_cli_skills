---
name: pal-found-audit
description: Locate organization audit log files and download their event content for security review or SIEM ingestion.
---

# Foundry Audit CLI

## Capability and source

Foundry audit logs record actions taken in the platform. Security teams use
them to investigate activity, establish accountability, and send events to a
SIEM. This CLI lists log files for an organization and downloads a selected
file's event content. A log file is a delivery unit, not a single audit event;
listing returns file IDs and a continuation token while content retrieval
returns bytes.

Source: the [Palantir audit logs overview](https://www.palantir.com/docs/foundry/security/audit-logs-overview).

Use `pal-found-audit` for 2 Foundry Audit API v2 operations:

| Command | Required arguments | Options |
|---|---|---|
| `log-file list` | `organization_rid`; `--start-date YYYY-MM-DD` for an initial request | `--end-date`, `--page-size`, `--page-token`, `--batch-pages`, `--timeout`, `--format`, `--pretty` |
| `log-file content` | `organization_rid`, `log_file_id` | `--output-filename`, `--timeout`, `--format`, `--pretty` |

### log_file.list

List log files belonging to an organization. The first request requires
`--start-date`; `--end-date` is inclusive. Each returned `LogFile` contains
its ID. The response also has a `nextPageToken` when more files are available.
Page size is a hint, so
the server may return a different number of files. Continue with
`--page-token` using the returned token. Without an end date, continuing to
poll the token can discover later available logs. A wrong organization RID,
missing first-page start date, or inadequate permission fails.

**Example:** `pal-found-audit log-file list ri.multipass..organization.a1b2c3d4-e5f6-7890-abcd-ef1234567890 --start-date 2026-08-01 --end-date 2026-08-31 --page-size 100`

### log_file.content

Download one log file using its ID from `list`. The CLI streams bytes into
the configured bounded download directory and prints a metadata envelope,
even with `--format toon`; audit content is not written to stdout. Set
`--output-filename` to choose the saved filename. This reads an existing file;
an unknown ID, insufficient permission, metadata-only CLI mode, or an exceeded
download limit prevents a usable download.

**Example:** `pal-found-audit log-file content ri.multipass..organization.a1b2c3d4-e5f6-7890-abcd-ef1234567890 '<LOG_FILE_ID>' --output-filename audit-events.bin`

The two commands form this workflow:

```bash
pal-found-audit log-file list <organization_rid> --start-date 2026-08-01
pal-found-audit log-file content <organization_rid> <log_file_id>
```

`list` returns file IDs. It fetches one server page by default and writes continuation information to stderr. A continuation request with `--page-token` may omit `--start-date`; batches are capped at 40 pages.

`content` never writes audit content to stdout or logs. It streams into the configured bounded download directory and returns a JSON metadata envelope, even when `--format toon` is supplied. The access guard runs before client creation or filesystem access. Metadata-only mode permits `list` and blocks `content`.

`--timeout` limits a request in seconds; `--format json|toon|auto` chooses the
metadata encoding; `--pretty` indents structured output. For `list`,
`--page-size` requests a number of files per page and `--batch-pages` caps
automatic page traversal. `--page-token` resumes from a token returned by a
previous response. The organization RID identifies whose logs are listed;
the log file ID from that list identifies the file to download.

The command uses shared retry, error, output, logging, and SDK-native B3 tracing components. It does not add W3C tracing headers. Exit codes are: user input 1, authentication 2, permission 3, not found 4, timeout or cancellation 5, server failure 6, exhausted rate limit 7, access control 8, and configuration 9.

### Parameters and JSON

Both commands accept `--timeout`, `--format json|toon|auto`, and `--pretty`.
`log-file list` accepts positional `organization_rid`, optional `--start-date`
and `--end-date`, plus `--page-size`, `--page-token`, and `--batch-pages`.
`log-file content` accepts positional `organization_rid` and `log_file_id`,
plus `--output-filename`. This namespace has no JSON input flags; dates and
identifiers are strings.

## Install requirement

`pal-found-audit` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

```bash
# conda (t-jet channel)
conda install -c t-jet pal_found_cli

# PyPI / pip
pip install pal_found_cli

# uv
uv tool install pal_found_cli
```
