# Application, website, and version operations

Developer Console application RID identifies website and all its versions.
`version` is a semantic version string, not a RID. Examples use shell variable
`APP_RID` holding real third-party application RID. Input errors exit 1;
SDK permission denials exit 3, missing resources exit 4, and read-only policy
blocks writes (8). Server may conceal a denial as 404.
SDK: `docs/v2/ThirdPartyApplications/`.

### third_party_application.get

Retrieves Developer Console application by positional RID. Response contains
its application RID, which also identifies website and versions in this CLI.
Use before website operations to confirm target. Unknown RID or missing read
permission prevents lookup.

**Example:** `pal-found-third-party-applications third-party-application get "$APP_RID"`

### website.deploy

Selects uploaded website version served to users. Requires application RID,
`--version` semantic version, and deployment permission. Response is Website
with `deployedVersion` and served `subdomains`; all users on those subdomains
see selected build. Absent version or incomplete asset scan can prevent
deployment. Site visitors also need Foundry login and hosted website access;
deployment alone does not grant it. Check version first, then inspect
`website get`.

**Example:** `pal-found-third-party-applications website deploy "$APP_RID" --version 1.2.0`

### website.get

Reads Website for positional application RID. Response gives optional
`deployedVersion` and `subdomains` currently serving it; absent deployed
version means no version is live. Missing website or access permission can
fail. Use after deploy or undeploy to verify state.

**Example:** `pal-found-third-party-applications website get "$APP_RID"`

### website.undeploy

Removes currently deployed version from application. Response is Website;
`deployedVersion` becomes absent. Previously uploaded versions remain
available for later deployment. Requires deployment permission; missing
application or website can fail. Verify with `website get`.

**Example:** `pal-found-third-party-applications website undeploy "$APP_RID"`

### version.delete

Deletes named semantic version of application website. Supply application
RID and version as positional arguments. Successful deletion has no response
body. Confirm current `deployedVersion` before deleting an asset; missing
version or delete permission fails.

**Example:** `pal-found-third-party-applications version delete "$APP_RID" 1.2.0`

### version.get

Retrieves uploaded Version by positional application RID and semantic version
string. Response includes its `version`; use to check asset before deploy or
delete. Missing version or read permission prevents lookup.

**Example:** `pal-found-third-party-applications version get "$APP_RID" 1.2.0`

### version.list

Lists versions for application. Response has `data` array of Version records
and optional `nextPageToken`. `--page-size` requests page size but server may
return fewer or more records. Omit `--page-token` on first call; reuse returned
token on next call. `--all --max-pages` gives bounded traversal. Missing
application or read permission fails.

**Example:** `pal-found-third-party-applications version list "$APP_RID" --page-size 50`

### version.upload

Uploads zipped static website assets under `--version` for later preview or
deployment. Requires website upload permission. `--file` must name existing
zip no larger than 16 MiB. Put build directory **contents** at archive root
(`index.html`, assets), not an enclosing `dist/` directory. CLI rejects
absent or oversized file, while
Foundry can reject invalid archive or version conflict. Response is Version
with semantic `version`. Upload stores asset; `website deploy` makes it live.

**Example:** `pal-found-third-party-applications version upload "$APP_RID" --version 1.2.0 --file ./website.zip`

### version.upload_snapshot

Uploads temporary zipped snapshot for preview. SDK states snapshots are
automatically deleted after two days. `--version` and bounded `--file` remain
required. Optional `--snapshot-identifier` associates build with preview;
the SDK's `foundry.v1@<repositoryRid>@<pullRequestRid>@<commitHash>` form
connects PR preview in Foundry Code Repositories. Response is Version.
Invalid archive or denied upload fails; snapshot stays off production until
explicit deployment.

**Example:** `pal-found-third-party-applications version upload-snapshot "$APP_RID" --version 1.2.0-snapshot.1 --file ./website.zip --snapshot-identifier review-42`
