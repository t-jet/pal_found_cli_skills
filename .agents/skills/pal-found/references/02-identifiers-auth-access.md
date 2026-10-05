# Identifiers, authentication, and access control

This part explains the identifiers the CLI uses, how authentication is
configured, and how the CLI decides whether an operation is allowed before any
network call. Read it before invoking any command.

## Identifiers

The CLI distinguishes several kinds of identifier. Do not confuse them:

| Kind | Form | Example | Used by |
| --- | --- | --- | --- |
| Resource RID | `ri.<type>.main.resource.<key>` | `ri.foundry.main.dataset.abc123` | Most operations identify a dataset, branch, ontology object, schedule, etc. by RID. |
| Path | A `/`-separated route to a folder or resource | `/my-project/folder` | Filesystem `resource get-by-path` style operations. |
| Name | A human-friendly label, not globally unique | `My View`, `release-1.0` | Creation and display operations. |
| Branch name | A named line of dataset history | `main` | Datasets branch operations and schema reads. |
| Page token | An opaque cursor returned by a paged operation | long encoded string | Resuming pagination. |
| Object primary key | The value of an object type's primary key property | `order-001` | Identifying a single ontology object. |

Type your RIDs exactly. A wrong or missing RID is the most common cause of a
"not found" (exit 4) or "invalid input" (exit 1) result.

## Authentication

Every CLI call needs two values before it can reach Foundry:

| Variable | Required | Purpose |
| --- | --- | --- |
| `FOUNDRY_TOKEN` | yes | Palantir bearer token; the SDK builds `UserTokenAuth` from it. |
| `FOUNDRY_HOSTNAME` | yes | Foundry instance hostname, e.g. `https://pal-found.example.com`. |

Set them in the shell, or in a `.env` file. The CLI loads configuration in this order:

1. **Explicit override**: if `FOUNDRY_AGENTIC_CLI_ENV_FILE` is set, load exactly
   that file; if it is missing, fail with exit code 9 (ConfigurationError).
2. **Git-root `.env`**: walk up to the first directory containing `.git` and
   load `.env` there; if no `.git` is found, load `.env` from the current
   directory.
3. **Environment variables only**: if no `.env` exists, use the shell
   environment. No error.

The home directory is never searched. `python-dotenv` loads with
`override=False`, so variables already in the shell take precedence.

Setup steps: copy `.env.example` to `.env`, fill in the two variables, then run
a read-only command such as
`pal-found-filesystem project get --project-rid ri.project.main.project.xxx`.
A successful result confirms auth works. Keep `.env` out of version control.

The CLI never prints tokens or secrets. It reports whether a request was
authorized; it does not grant access.

## Access control configuration

Every operation passes through an access control guard before any SDK call.
The guard applies these checks in order:

| Step | Check | If true |
| --- | --- | --- |
| 1 | Operation `_ENABLED` | `false` → block |
| 2 | Namespace `_ENABLED` | `false` → block |
| 3 | Operation `_READONLY=false` | overrides a parent READONLY=true → permit write |
| 4 | Namespace `_READONLY` | `true` → block writes |
| 5 | Global `FOUNDRY_AGENTIC_CLI_READONLY` | `true` → block writes |
| 6 | Namespace `_METADATA_ONLY` | `true` → metadata-only policy applies |
| 7 | Global `FOUNDRY_AGENTIC_CLI_METADATA_ONLY` | `true` → metadata-only policy applies |
| 8 | Permit | default |

Control variables use these names:

| Scope | Pattern | Example |
| --- | --- | --- |
| Global | `FOUNDRY_AGENTIC_CLI_{KEY}` | `FOUNDRY_AGENTIC_CLI_READONLY` |
| Namespace | `FOUNDRY_AGENTIC_CLI_{NS}_{CONTROL}` | `FOUNDRY_AGENTIC_CLI_DATASETS_READONLY` |
| Operation | `FOUNDRY_AGENTIC_CLI_{NS}_{CLASS}_{OP}_{CONTROL}` | `FOUNDRY_AGENTIC_CLI_DATASETS_DATASET_GET_ENABLED` |

Control suffixes: `_ENABLED` (`true`/`false`), `_READONLY` (override only,
`false` grants write), `_METADATA_ONLY` (`true`/`false`).
Operation-level `_READONLY=true` is not supported as an independent setting;
to block a single write operation, set its `_ENABLED=false`.

Metadata-only mode permits only listed operations: only the operations on
each namespace's `metadata-allow-list.md` are permitted. A blocked operation
exits with code 8 (AccessControlError) before any network call.

## Two separate decisions

Do not confuse CLI access control with Foundry authorization:

- **CLI access control**: the guard above, evaluated locally before the
  request. It uses environment variables and can block a write or a
  metadata-only block. Exit codes 8 (access control) and 9 (configuration)
  come from this layer.
- **Foundry authorization**: the platform's own permission check when the
  request reaches the API. A rejected request returns an HTTP 403 and maps to
  exit code 3 (permission denied).

A success exit (0) means the CLI request completed and the platform accepted
it; it does not by itself prove that an asynchronous Foundry process later
finished. Check namespace-specific status operations when a task is async.
