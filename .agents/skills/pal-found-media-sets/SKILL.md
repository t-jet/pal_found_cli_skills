---
name: pal-found-media-sets
description: Work with Foundry media items, transactions, references, transformations, and bounded binary transfers through 19 CLI operations.
---

# Foundry Media Sets CLI

## Capability and source

Media sets collect unstructured items such as documents, images, audio, and
video under a shared schema and primary format. An item has a path and RID;
uploading to an existing path changes the item shown at that path, while an
older direct media reference can still identify the earlier item. Media
references let other Foundry workflows use the item without copying its bytes.
Transactional sets require `create` to open a transaction and `commit` to
expose uploaded items; `abort` discards that transaction's uploads. The CLI's
`create` operation does **not** create a media set. `transform` starts an
asynchronous job; use `get-status` and then `get-result`. `calculate` and
`retrieve` specifically produce and read 200-pixel WebP thumbnails.

Source: [Media sets](https://www.palantir.com/docs/foundry/media-sets-advanced-formats),
[importing media](https://www.palantir.com/docs/foundry/media-sets-advanced-formats/importing-media).

19 Foundry Media Sets API v2 operations are available through the installed `pal-found-media-sets` command.

## Usage

```bash
pal-found-media-sets media-set <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`.

Downloads use the shared `BinaryDownloadHandler` and return a JSON/TOON
metadata envelope (file path, size, checksums, truncation status); the download
bound applies. Oversized responses yield truncated files, so inspect envelope
before using saved content.
Uploads read a bounded file (16 MiB).

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope. Attribution is applied per FR-ATTR-4.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Transactions and writes](references/01-lifecycle.md) | `media_set` | 9 |
| [Item reads and downloads](references/02-content.md) | `media_set` | 10 |

## Parameters and JSON

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`. Use exactly one of `--branch-name`, `--branch-rid`, or `--view-rid`
when selecting a branch or view. `--media-item-path` selects an item by path
for upload, clear, or RID lookup; `--media-item-rid` can choose a client RID
on upload. `--transaction-id` binds changes to an open transaction.
`--physical-item-name` names a file within a federated store for `register`.
`upload-media` uses `--filename` as the temporary item's label. `transform`
requires `--transformation-json`; `--token` or `--read-token` can grant
item read access on supported calls. Binary downloads take optional
`--output` basename, saved under configured download directory. The CLI
enforces its download bound. Files uploaded with `--file` are limited to 16 MiB.

## Install requirement

`pal-found-media-sets` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

```bash
# conda (t-jet channel)
conda install -c t-jet pal_found_cli

# PyPI / pip
pip install pal_found_cli

# uv
uv tool install pal_found_cli
```
