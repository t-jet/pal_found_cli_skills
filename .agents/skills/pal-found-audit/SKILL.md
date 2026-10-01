---
name: pal-found-audit
description: List Foundry Audit log files and download bounded log-file content through Audit API v2.
---

# Foundry Audit CLI

## Capability and source

Audit API v2 lists organization log files and retrieves one bounded log-file
content stream. The CLI exposes only those two SDK operations.

Source: [Palantir Foundry documentation](https://www.palantir.com/docs/foundry); reviewed 2026-08-13.

Use `pal-found-audit` for two Audit API v2 operations:

| Command | Required arguments | Options |
|---|---|---|
| `log-file list` | `organization_rid`; `--start-date YYYY-MM-DD` for an initial request | `--end-date`, `--page-size`, `--page-token`, `--batch-pages`, `--timeout`, `--format`, `--pretty` |
| `log-file content` | `organization_rid`, `log_file_id` | `--output-filename`, `--timeout`, `--format`, `--pretty` |

Run it with:

```bash
pal-found-audit log-file list <organization_rid> --start-date 2026-08-01
pal-found-audit log-file content <organization_rid> <log_file_id>
```

`list` returns metadata records. It fetches one server page by default and writes continuation metadata to stderr. A continuation request with `--page-token` may omit `--start-date`; batches are capped at 40 pages.

`content` never writes audit content to stdout or logs. It streams into the configured bounded download directory and returns a JSON metadata envelope, even when `--format toon` is supplied. The access guard runs before client creation or filesystem access. Metadata-only mode permits `list` and blocks `content`.

The command uses shared retry, error, output, logging, and SDK-native B3 tracing components. It does not add W3C tracing headers. Exit codes follow ADR-001: user input 1, authentication 2, permission 3, not found 4, timeout or cancellation 5, server failure 6, exhausted rate limit 7, access control 8, and configuration 9.

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
