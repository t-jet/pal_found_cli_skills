# Application, website, and version operations

[Return to skill entry](../SKILL.md)

## Prerequisites and identity

Use a prepared `pal-found-third-party-applications` executable with its Python
runtime and compatible `foundry-platform-sdk`; `--help` checks availability.
For offline execution tests, supply fake transport, fixtures and fake credentials.
Local production build/archive preparation can be offline; tenant reads and
writes need authorized enrollment access. Application creation, application
search, identity grants and sharing changes are outside these nine operations.

The CLI uses `UserTokenAuth` with `FOUNDRY_TOKEN`, a bearer token for the
`FOUNDRY_HOSTNAME` enrollment. Obtain both from the approved enrollment/identity
process. There is no client-ID/secret OAuth grant flow, interactive login or
refresh command. Automation and any permitted service-account use require
external approved token acquisition/renewal; client credentials alone cannot
be used as this CLI's token. SDK permission error names do not specify exact
OAuth scopes or IAM grants. Ask the administrator which identity and application
access is required; do not invent scope strings.

Configuration chooses explicit `FOUNDRY_AGENTIC_CLI_ENV_FILE`, Git root `.env`,
then current-directory `.env`, taking the first existing choice; otherwise only
environment variables apply. An explicit missing file fails instead of falling
back. Existing process values override file values; no home-directory lookup.
Set credentials in the process or an approved file and keep tokens out of logs
and source control. Bash setup (replace placeholders):

```bash
export FOUNDRY_HOSTNAME="https://<your-enrollment-host>"
export FOUNDRY_TOKEN="<authorized-bearer-token>"
export APP_RID="<existing-Developer-Console-application-RID>"
pal-found-third-party-applications third-party-application get "$APP_RID"
```

For PowerShell use `$env:FOUNDRY_HOSTNAME`, `$env:FOUNDRY_TOKEN` and `$APP_RID`.
Obtain application RID from existing Developer Console application details or
owner-supplied records; request it from the owner if unavailable. This CLI has
no application list or search. Compare returned application RID with the intended
owner-supplied target before writing. `APP_RID` is only an example shell variable.
A website version is a semantic label such as `1.2.0`, not a RID.

Prepare the frontend from supplied source, dependencies, build command and build
environment. Review production static assets locally, exclude secrets, and zip
build directory contents so `index.html` sits at archive root. Both upload paths
need `--version` and an existing `--file` no larger than 16 MiB (16,777,216 bytes).
The CLI reads bounded bytes after its local guard; it does not build the site or
validate ZIP contents. Server-side archive/version rejection remains possible.

Hosting availability, visitor login, client-facing eligibility, sharing UI and
asset-scan readiness are not established by the frozen API contracts. Have the
owner/admin provide applicable tenant requirements and access checks. Static
assets need API calls for server functionality; successful deployment alone does
not verify visitor access. Optional background:
[Host an OSDK application](https://www.palantir.com/docs/foundry/developer-console/deploy-custom-application-on-foundry).

## Procedure and operation contracts

Typical release: verify application, inspect current website and versions,
upload unused production label, confirm Version, deploy, then read Website.
Use `--format json` for JSON examples; `--format toon|auto` and `--pretty` are
also supported. `--timeout` is per-request seconds, 1..3600.

### third_party_application.get

Reads an existing Developer Console application by positional RID. Response
contains its application RID. Compare it with the intended target before website
operations. Missing resource or read permission prevents lookup.

**Example:** `pal-found-third-party-applications third-party-application get "$APP_RID"`

### website.deploy

Selects uploaded semantic `--version` for application RID. Requires authorized
deployment permission. Response is Website with optional `deployedVersion` and
`subdomains`, the hostnames associated with the website. First inspect intended
version using `version get`. Then deploy and use `website get` to confirm
`deployedVersion` equals the intended label. Missing version or permission can
fail. Reconcile read state after an uncertain response before retrying a write.

**Example:** `pal-found-third-party-applications website deploy "$APP_RID" --version 1.2.0`

### website.get

Reads Website by positional application RID. `deployedVersion` is optional;
absent/null means the result identifies no deployed version. `subdomains` lists
associated website hostnames and does not prove reachability or visitor access.
Use after deploy/undeploy to check state. A missing website or access failure
requires target and permissions checks.

**Example:** `pal-found-third-party-applications website get "$APP_RID"`

### website.undeploy

Removes current deployment; uploaded versions remain available. Response is
Website. Requires deployment permission. Follow with `website get` and confirm
`deployedVersion` is absent/null. Confirm the application target before retrying
if the website is missing or the response is uncertain.

**Example:** `pal-found-third-party-applications website undeploy "$APP_RID"`

### version.delete

Deletes the positional semantic version from application website. Check current
`deployedVersion` and obtain approval for deletion first; use an approved
replacement deployment or undeploy if needed. Do not assume deletion of a live
version is permitted. API success has no body, so JSON CLI result is `null`.
Verify `version get` reports missing and `version list` no longer includes the
label across all pages. Confirm application access still works because a 404
alone can also conceal denial. Retain needed build artifacts before deletion.

**Example:** `pal-found-third-party-applications version delete "$APP_RID" 1.2.0`

### version.get

Reads Version by positional application RID and semantic label. Response
contains `version`; compare with requested label before deployment or deletion.
It supplies no archive checksum, scan status or visitor-access proof. Missing
version or permission prevents lookup; verify target/application access first.

**Example:** `pal-found-third-party-applications version get "$APP_RID" 1.2.0`

### version.list

Discovers versions for one known application, with no search operation. stdout
contains a list of Version records; stderr carries pagination metadata including
`next_page_token` and diagnostics. Capture streams separately. Default is one
page. Server may return fewer or more records than requested `--page-size`.
Omit `--page-token` first; pass the returned stderr token unchanged to resume.
`--max-pages N` bounds one batch; `--all` ignores `--max-pages` and fetches up to
40 pages, or the lower `FOUNDRY_AGENTIC_CLI_MAX_BATCH_PAGES` cap. A remaining token
means more results; even `--all` can be incomplete. No next token means end.
Page size and batch counts must be positive integers; default page size is 100
unless `FOUNDRY_AGENTIC_CLI_DEFAULT_PAGE_SIZE` configures it.

**Example:** `pal-found-third-party-applications version list "$APP_RID" --page-size 50`

Resume using the actual token, replacing the placeholder:

```bash
pal-found-third-party-applications version list "$APP_RID" --page-size 50 --page-token "<next_page_token>"
pal-found-third-party-applications version list "$APP_RID" --max-pages 2
```

On paging failure, keep the last successful batch and its cursor, inspect exit
code and error envelope, and retry the read from that cursor. An unsuccessful
batch does not establish completeness. If server rejects an expired/invalid
cursor, restart without a token and deduplicate by version label. Keep application
and page options consistent; inspect terminal cursor before declaring absence.

### version.upload

Uploads zip bytes under semantic `--version`. Requires upload permission. Use
existing bounded production `--file` described above. Response is Version;
compare returned `version`, then verify with `version get`. Upload stores assets;
explicit deploy selects a production version. The CLI does not accept a JSON
body in place of `--file` and never forwards the local filename to the SDK.
On conflict, read and reconcile existing version and deployed state before any
retry or selection of an approved unused version. Do not infer absence or success,
or blindly upload/redeploy. Do not assume an existing archive can be overwritten
or infer byte equality
from the label. On uncertain upload, check version state before retrying.

**Example:** `pal-found-third-party-applications version upload "$APP_RID" --version 1.2.0 --file ./website.zip`

### version.upload_snapshot

Uploads temporary zip bytes for preview, with required semantic `--version`
and bounded `--file`. SDK states automatic deletion after two days. Optional
`--snapshot-identifier` associates the snapshot with a preview. The documented
`foundry.v1@<repositoryRid>@<pullRequestRid>@<commitHash>` format connects PR
preview in Foundry Code Repositories; `review-42` below is only a custom label.
Response is Version; compare `version` and use `version get` while it exists.
A snapshot upload does not itself select production deployment. Expired snapshot
must be uploaded again under an approved label if still needed.

**Example:** `pal-found-third-party-applications version upload-snapshot "$APP_RID" --version 1.2.0-snapshot.1 --file ./website.zip --snapshot-identifier review-42`

## Failures and recovery

| Failure | Action |
| --- | --- |
| Exit 9, config/runtime | Set non-empty hostname/token; fix explicit env-file path or prepare missing SDK dependencies. Check inherited process values overriding files. |
| Exit 1, arguments/file | Supply required RID/version/file; fix absent/oversized file, correct production ZIP contents, use valid format/timeout and positive paging values. Server validates archive/version semantics. |
| HTTP 401, exit 2 | Verify enrollment hostname; replace expired or invalid bearer token through approved identity process. Repeat application `get`. |
| HTTP 403, exit 3 | Ask owner/admin for intended operation permission for this identity/application; do not change local flags to solve tenant denial. |
| HTTP 404, exit 4 | Confirm hostname and RID, then version using known accessible application. Ask owner about deletion or concealed access denial. |
| Conflict or rejected version | Native SDK `ConflictError` maps to exit 1 and may omit `http_status`; inspect `exception_type`, available structured context and stderr diagnostics. Read and reconcile existing version and deployed state before any retry. Do not infer absence or success, or blindly upload/redeploy. Correct the build/label or choose an approved unused semantic version after reconciliation. |
| Exit 8, local policy | Inspect blocked rule and effective environment/file config with policy owner before an approved change. No request or upload file read has occurred. |
| Other server/timeout failure | Preserve call ID and HTTP status without secrets. Read version/website state before repeating writes; retry paged reads from last successful cursor. |

Local controls include `FOUNDRY_AGENTIC_CLI_ENABLED`, namespace
`FOUNDRY_AGENTIC_CLI_THIRD_PARTY_APPLICATIONS_ENABLED` and operation keys such as
`FOUNDRY_AGENTIC_CLI_THIRD_PARTY_APPLICATIONS_WEBSITE_DEPLOY_ENABLED`; a false
value disables access. `FOUNDRY_AGENTIC_CLI_READONLY=true` blocks writes. An
approved namespace `FOUNDRY_AGENTIC_CLI_THIRD_PARTY_APPLICATIONS_READONLY=false`
or operation `FOUNDRY_AGENTIC_CLI_THIRD_PARTY_APPLICATIONS_WEBSITE_DEPLOY_READONLY=false`
override can permit writes under a parent read-only policy, but cannot bypass
disabled access. `METADATA_ONLY` can restrict content reads. Policy owners decide
permitted changes; these controls do not create tenant permissions, enable
hosting, grant visitor access or acquire credentials.

Errors are structured stdout envelopes, with diagnostics on stderr. Check
process exit before parsing stdout as Version/Website/list output. Offline
fixtures verify request/result handling only; deployment and visitor-access
claims need separate authorized enrollment checks. Contracts follow SDK 1.101.0.
