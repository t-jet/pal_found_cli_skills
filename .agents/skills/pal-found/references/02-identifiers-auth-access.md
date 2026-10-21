# Identifiers, authentication, and access control

This part explains the identifiers the CLI uses, how authentication is
configured, and how the CLI decides whether an operation is allowed before any
network call. Read it before invoking any command.

## Identifiers

The CLI distinguishes several kinds of identifier. Do not confuse them:

| Kind | Form | Example | Used by |
| --- | --- | --- | --- |
| Resource RID | `ri.<service>.<instance>.<resource-type>.<locator>` | `ri.foundry.main.dataset.abc123` | RID-addressed resources such as datasets, folders and projects; branch names and object primary keys are separate identifiers. |
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
   try `.env` there. If that file is absent or no `.git` is found, try `.env`
   in the current directory.
3. **Environment variables only**: if no `.env` exists, use the shell
   environment. No error.

The home directory is never searched. `python-dotenv` loads with
`override=False`, so variables already in the shell take precedence.

Setup steps: copy `.env.example` to `.env`, fill in the two variables, then run
a read-only command such as
`pal-found-filesystem project get ri.compass.main.folder.00000000-0000-0000-0000-000000000001`.
Replace this synthetic RID with a project you can read; `project_rid` is positional.
A successful result confirms auth works. Keep `.env` out of version control.

The CLI never prints tokens or secrets. It reports whether a request was
authorized; it does not grant access.

## Access control configuration

Every operation passes through an access control guard before any SDK call.
The guard applies these checks in order:

| Step | Check | If true |
| --- | --- | --- |
| 0 | Global `FOUNDRY_AGENTIC_CLI_ENABLED=false` | block; narrower settings cannot re-enable it |
| 1 | Operation `_ENABLED` | `false` → block |
| 2 | Namespace `_ENABLED` | `false` → block |
| 3 | Write with inherited read-only active: operation `_READONLY=false` | permit write immediately |
| 4 | Write with inherited read-only active: namespace `_READONLY` | `false` → permit immediately; otherwise `true` → block |
| 5 | Global `FOUNDRY_AGENTIC_CLI_READONLY` | `true` → block writes |
| 6 | Namespace `_METADATA_ONLY=false` with global metadata-only active | override global metadata-only and permit |
| 7 | Namespace or inherited global `_METADATA_ONLY=true` | block writes and require reads to be on the namespace allow-list |
| 8 | Permit | default |

The explicit write permits in steps 3 and 4 return before metadata-only checks.
They apply when inherited read-only mode is active; do not assume the same
override changes metadata-only behavior when read-only mode is off.

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
Operation-level `_METADATA_ONLY` is not evaluated; configure metadata-only at
namespace or global scope.

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
