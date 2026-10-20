# Shared command options

This part explains the options most namespace parsers share. Namespace parsers
differ: support for a flag is per operation and per namespace. A record in a
namespace skill tells you which flags that operation accepts. Do not assume a
flag works everywhere.

## Timeout, format, and pretty

| Option | Meaning |
| --- | --- |
| `--timeout <seconds>` | Integer seconds from 1 through 3600, applied to both SDK requests and the outer timeout for each attempt. |
| `--format json\|toon\|auto` | Explicit output format. Use this flag when deterministic selection is required. |
| `--pretty` | Pretty-print JSON output when JSON is selected. |

An explicit `--timeout` overrides the environment for both timeout layers.
For example, `--timeout 120` gives each attempt 120 seconds even when the
environment default is 3 seconds. Without the flag, ordinary namespaces use
`FOUNDRY_AGENTIC_CLI_TIMEOUT_S` (default 30); Streams uses its separate
`FOUNDRY_AGENTIC_CLI_STREAMS_TIMEOUT_S` (default 120). Environment integers are
clamped to 1 through 3600; malformed values use the relevant default. Invalid
CLI values are input errors. Retries and backoff can extend total duration.

When `--format` is omitted, `FOUNDRY_AGENTIC_CLI_DEFAULT_FORMAT` selects output,
falling back to `auto`. An explicit flag overrides it, including explicit `auto`.

## Paging options

These appear where the parser supports pagination:

| Option | Meaning |
| --- | --- |
| `--page-size <n>` | Number of items per page. A larger page transfers more data. |
| `--page-token <token>` | Resume from a token returned by a previous page. |
| `--batch-pages <n>` | Fetch one batch of up to `n` pages in a single call in some namespaces. |

Naming varies: some namespaces use `--batch-pages`, others use a `--all`
or `--max-pages` style. Read the namespace record.

## Positional identifiers and bodies

Most commands take a positional resource identifier (for example a RID) right
after the operation name:

```bash
pal-found-datasets dataset get <DATASET_RID>
```

Some commands take a positional JSON `body` for batch or replacement payloads,
or a `--body-file` for a JSON file. Operation records name the positional and
flag inputs the local parser accepts. JSON flag inputs are usually passed with
a `-json` suffix (for example `--where-json`, `--parameters-json`); their
exact names are per namespace.

## Where format and state differ

- The `--format` choice changes how the response is rendered on stdout; it
  does not change what happens in Foundry.
- Metadata such as page tokens is printed to stderr. stdout carries data.
- A nonzero exit signals a CLI, auth, access, or server problem; a zero exit
  signals the request completed. For asynchronous work, check status
  separately.

## When a flag is absent

Use the operation record to select meaningful options. A common parser can
accept a flag that an operation ignores: Filesystem `project get` accepts
`--page-size` even though it is not paginated. A truly unknown flag fails as
input error: exit 1 with JSON stdout. `--help` remains successful usage output.
Do not infer operation support from parser acceptance alone.
