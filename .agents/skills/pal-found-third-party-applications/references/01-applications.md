# Application, website, and version operations

This part documents the `third_party_application` (1), `website` (3), and
`version` (5) resource clients (9 operations). A website belongs to a
third-party application; versions hold deployable builds.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/third_party_applications/scripts/pal_found_third_party_applications_cli.py`;
SDK `foundry_sdk/v2/third_party_applications/{third_party_application,website,version}.py`
at pinned commit `2da67907`. Reviewer architect (CODEREVIEW-054), 2026-10-03.
QA baseline TESTCASE-021.

## Operation records

### third_party_application.get

- **Class**: read. Returns a third-party application.
- **Preconditions**: can read the application.
- **Effect**: returns the application record.
- **Inputs**: positional `third_party_application_rid`.
- **Success**: the application.
- **Failure**: exit 4 if missing.

### website.deploy

- **Class**: change (write). Deploys a website.
- **Preconditions**: can deploy; a website and version.
- **Effect**: makes a website version live.
- **Inputs**: positional `website_rid`; version/URL config.
- **Success**: returns the deployed website.
- **Failure**: exit 8 readonly block; exit 1 invalid version.
- **Example**: `pal-found-third-party-applications website deploy <WEBSITE_RID> --version-rid <VERSION_RID>`.

### website.get

- **Class**: read. Returns a website.
- **Preconditions**: can read the website.
- **Effect**: returns the website record.
- **Inputs**: positional `website_rid`.
- **Success**: the website.
- **Failure**: exit 4 if missing.

### website.undeploy

- **Class**: change (write). Undeploys a website.
- **Preconditions**: can undeploy.
- **Effect**: stops the website deployment.
- **Inputs**: positional `website_rid`.
- **Success**: returns the updated website.

### version.delete

- **Class**: delete (write). Deletes a website version.
- **Preconditions**: can delete the version.
- **Effect**: deletes the version.
- **Inputs**: positional `website_rid`, `version`/`version_rid`.
- **Success**: returns the deleted version.

### version.get

- **Class**: read. Returns a website version.
- **Preconditions**: can read the version.
- **Effect**: returns the version record.
- **Inputs**: positional `website_rid`, `version`.
- **Success**: the version.
- **Failure**: exit 4 if missing.

### version.list

- **Class**: read. Lists a website's versions.
- **Preconditions**: can read the website.
- **Effect**: returns versions, paged.
- **Inputs**: positional `website_rid`; paging options.
- **Success**: versions; empty if none.

### version.upload

- **Class**: create (binary upload). Uploads a new website version.
- **Preconditions**: can write the website.
- **Effect**: stores the version build (zip) for the website.
- **Inputs**: positional `website_rid`; `--file` (bounded zip), `--version`.
- **Success**: the uploaded version.
- **Failure**: exit 1 file too large or invalid zip; exit 8 readonly block.
- **Example**: `pal-found-third-party-applications version upload <WEBSITE_RID> --file ./build.zip --version "1.0.0"`.

### version.upload_snapshot

- **Class**: create (binary upload). Uploads a website version snapshot.
- **Preconditions**: can write the website.
- **Effect**: stores a snapshot build; like upload but marks it as snapshot.
- **Inputs**: positional `website_rid`; `--file`, `--version`,
  `--snapshot-identifier`.
- **Success**: the uploaded snapshot version.
- **Failure**: exit 1 invalid file; exit 8 readonly block.

## Evidence and review

Reviewed against the installed `pal-found-third-party-applications` parser and
pinned SDK sources (commit `2da67907`). `website.deploy/undeploy` and
`version.upload/upload_snapshot/delete` are write with material deploy/release
effects; uploads are bounded 16 MiB (AC-D-013-09). `get`/`list` are reads. No
unsupported operation is documented as callable.
