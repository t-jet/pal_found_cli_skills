---
name: pal-found-third-party-applications
description: Inspect Developer Console applications and manage their static website versions and deployment through 9 CLI operations.
---

# Foundry Third-Party Applications CLI

## Capability and source

Developer Console applications can expose an OSDK frontend hosted by Foundry.
Website hosting serves static assets such as HTML, JavaScript, CSS, and images;
the frontend calls APIs for server functionality. It is available for
client-facing applications. Uploading a zipped version stores assets, while
`website deploy` selects the version served to users. A snapshot version is
temporary and is deleted after two days. Each website and version operation
uses the **third-party application RID**; versions are identified by semantic
version strings.
Zip the **contents** of production build directory, so `index.html` is at
archive root; wrapping all files in `dist/` changes served paths. Hosted sites
require Foundry login. Users with Developer Console application access can
see the site by default; grant other Foundry users hosted website access in
Sharing & Tokens. This CLI manages versions and deployment, not sharing.

Source: [Host an OSDK application](https://www.palantir.com/docs/foundry/developer-console/deploy-custom-application-on-foundry).
Operation details: SDK `docs/v2/ThirdPartyApplications/` used to author this skill.

9 Foundry Third-Party Applications API v2 operations are available through the installed `pal-found-third-party-applications` command.

## Usage

```bash
pal-found-third-party-applications <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`; version
listing also accepts `--page-size`, `--page-token`, `--all`, `--max-pages`.

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope. Version uploads are bounded zip reads.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Application, website, and version operations](references/01-applications.md) | `third_party_application`, `website`, `version` | 9 |

## Parameters and JSON

Binary version uploads require `--version` and `--file` (16 MiB maximum).
Use `version get` or `version list` to inspect uploaded versions before
changing the live deployment.

`--timeout` limits a request in seconds; `--format json|toon|auto` chooses
output encoding; `--pretty` indents it. Version listing accepts `--page-size`
as the requested number of versions, `--page-token` to resume from a returned
token, and `--all --max-pages` for bounded automatic traversal. Uploads use
`--version` as the website version label and `--file` as the local zip path.

## Install requirement

`pal-found-third-party-applications` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

```bash
# conda (t-jet channel)
conda install -c t-jet pal_found_cli

# PyPI / pip
pip install pal_found_cli

# uv
uv tool install pal_found_cli
```
