---
name: pal-found-third-party-applications
description: Inspect Developer Console applications and manage their static website versions and deployment through 9 CLI operations.
---

# Foundry Third-Party Applications CLI

## Capability and lifecycle

Use nine API v2 operations to read an existing Developer Console application,
upload static website assets, inspect versions and select or remove deployment.
Application creation, application search, OAuth grants and sharing changes are
outside this command. Version discovery uses `version list` for a known
application. Upload stores a version; `website deploy` selects it for hosting.
`website undeploy` clears deployment while preserving uploaded versions.
Snapshot uploads are temporary: the SDK states deletion after two days.

Static assets contain the frontend; server functionality requires API calls.
The frozen API defines upload and deployment contracts, but does not establish
tenant hosting availability, visitor login rules, client-facing eligibility,
Sharing & Tokens UI steps or asset-scan readiness. Obtain those requirements
from the application's owner or administrator before production release.
Deployment success does not demonstrate that intended visitors can open it.

## Prepared runtime and identity

Have the installed `pal-found-third-party-applications` executable, its Python
environment and compatible `foundry-platform-sdk` dependencies prepared. These
pages are instructions, not executable wrappers. Run the command with `--help`
to check availability without a tenant call. An offline test also needs supplied
fake transport, response fixtures and non-secret credentials; it cannot prove a
live enrollment accepted deployment.

For tenant operations, obtain the target enrollment hostname, permitted bearer
token and existing Developer Console application RID from an authorized owner.
The CLI constructs SDK `UserTokenAuth(FOUNDRY_TOKEN)`. It has no client-ID/secret
OAuth grant, interactive login or token-refresh command. For automation, arrange
an enrollment-approved token acquisition and renewal process outside this CLI.
Do not infer service-account support from possession of client credentials.
The frozen operation sources name permission-denied errors but do not specify
universal OAuth scopes or IAM grants; ask the enrollment administrator which
identity and application permissions are required for the intended operation.

Set credentials in the invoking process or an approved `.env` file. For example,
these Bash assignments use placeholders that must be replaced:

```bash
export FOUNDRY_HOSTNAME="https://<your-enrollment-host>"
export FOUNDRY_TOKEN="<authorized-bearer-token>"
export APP_RID="<existing-Developer-Console-application-RID>"
pal-found-third-party-applications third-party-application get "$APP_RID"
```

Keep tokens out of source control and captured output. In PowerShell, assign
`$env:FOUNDRY_HOSTNAME`, `$env:FOUNDRY_TOKEN` and `$APP_RID` instead.
Config loading chooses the first available file: explicit
`FOUNDRY_AGENTIC_CLI_ENV_FILE`, Git root `.env`, then current-directory `.env`;
otherwise it uses environment variables alone. An explicit missing file fails.
Existing process environment values take precedence over file values. No home
directory search occurs. Check inherited environment values when a file change
appears ineffective.

## Target and archive prerequisites

Obtain the RID from an existing Developer Console application's details or
supplied owner records; ask the owner to identify the application if no RID is
available. This command cannot create or list applications. `APP_RID` is a shell
variable, not a CLI configuration key. Run application `get` above and compare
its returned application RID with the owner's target before any write. A
website version label such as `1.2.0` is a semantic version, not an application
RID. Verify uploaded labels with `version get` or `version list`.

Prepare a production build using the application's supplied source, dependencies,
build command and environment configuration. Review the resulting static assets
locally; exclude secrets and development-only files. Zip build directory contents
with `index.html` at archive root, rather than an enclosing `dist/` directory.
Both upload commands require an existing `--file` no larger than 16 MiB
(16,777,216 bytes) and `--version`. The CLI reads bounded bytes after policy
approval; it does not validate ZIP structure or build the frontend. Foundry may
reject an invalid archive or semantic version.

Local build/archive inspection needs no enrollment. Upload, reads of tenant
state, deploy, undeploy and delete require authorized enrollment access. Hosting
availability, identity grants and visitor access are controlled outside this CLI.

## Local policy and recovery

An exit 8 is a local policy refusal, evaluated before client creation or upload
file reads. Inspect the error's blocked rule and the effective process/file
configuration with the policy owner. `FOUNDRY_AGENTIC_CLI_ENABLED=false` blocks
all operations. Namespace and operation `ENABLED` controls can also disable
access. `FOUNDRY_AGENTIC_CLI_READONLY=true` blocks writes; an approved namespace
`FOUNDRY_AGENTIC_CLI_THIRD_PARTY_APPLICATIONS_READONLY=false` or operation override
such as `FOUNDRY_AGENTIC_CLI_THIRD_PARTY_APPLICATIONS_WEBSITE_DEPLOY_READONLY=false`
can permit that write. An override cannot bypass an `ENABLED=false` decision.
`METADATA_ONLY` policies can restrict content reads. Change policy only with its
owner's authorization; local permission never grants tenant permission.

| Failure | Recovery |
| --- | --- |
| Exit 9, configuration | Supply non-empty hostname/token, correct explicit env-file path, or restore prepared SDK environment. |
| Exit 1, input/file | Correct arguments, semantic version and file path/size; use `--timeout` 1..3600 seconds and positive paging values. |
| HTTP 401 / exit 2 | Check hostname and replace expired/invalid token using approved identity process, then repeat read-only target check. |
| HTTP 403 / exit 3 | Ask application owner/admin for required operation access; local flags cannot grant it. |
| HTTP 404 / exit 4 | Verify enrollment, RID and version with owner; resource may be absent or access concealed. |
| Conflict or uncertain write | Read and reconcile existing version and deployed state before any retry; compare intended label/build and choose an approved unused version if needed. Do not infer absence or success, or blindly upload/redeploy. |
| Paging/server/timeout error | Retain last successful cursor and batch; retry the read, deduplicate version labels, and confirm terminal cursor. |

Native SDK `ConflictError` maps to exit 1 and may omit `http_status`. Inspect
`exception_type`, available structured context and stderr diagnostics to identify
the conflict; exit 1 alone does not establish invalid input. Failed commands emit
a structured error on stdout and diagnostics on stderr. Do not treat error
envelopes as successful resource records.

## Usage, results and navigation

```bash
pal-found-third-party-applications <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`. Version
listing additionally supports `--page-size`, `--page-token`, `--all`, `--max-pages`.
Default list output is one page of Version records on stdout; pagination
metadata including `next_page_token` goes to stderr. Resume with that token.
`--max-pages N` bounds a batch; `--all` ignores it and uses at most 40 pages
(or a lower configured cap). A remaining token means discovery is incomplete.

Website results contain optional `deployedVersion` plus a `subdomains` list. After
deploy, use `website get` and compare the selected version. After undeploy,
check that no deployed version remains. Version results contain `version`;
they do not prove visitor access or scan completion. Successful delete returns
no API body, represented as `null` in JSON CLI output. Verify deletion with
`version get` returning missing, while confirming application access still
works; a 404 alone can conceal a permission failure.

| Local guide | Resource clients | Operations |
| --- | --- | ---: |
| [Application, website, and version operations](references/01-applications.md) | `third_party_application`, `website`, `version` | 9 |

Contracts follow Palantir Python SDK 1.101.0. Optional background:
[Host an OSDK application](https://www.palantir.com/docs/foundry/developer-console/deploy-custom-application-on-foundry).
