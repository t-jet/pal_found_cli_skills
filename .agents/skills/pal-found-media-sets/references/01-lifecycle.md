# Media set lifecycle

This part documents the media-set lifecycle operations (10): create, commit,
abort, clear, transform, upload, upload_media, calculate, register, and
reference. Read the [Media Sets entry](SKILL.md) first.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/media_sets/scripts/pal_found_media_sets_cli.py`;
SDK `foundry_sdk/v2/media_sets/media_set.py` at pinned commit `2da67907`.
Reviewer architect (CODEREVIEW-053), 2026-10-03. QA baseline TESTCASE-018.

## Workflow

1. `media_set.create` the set.
2. Open a transaction and upload media (`upload`, `upload_media`), or
   `register`/`reference` existing items.
3. `commit` the transaction to make media visible, or `abort`/`clear` to
   discard it.
4. Apply `transform`/`calculate` to derive content.

## Operation records

### media_set.create

- **Class**: create (write). Creates a media set.
- **Preconditions**: can create media sets.
- **Effect**: creates a media set and returns it (RID).
- **Inputs**: `--display-name`, parent/space context.
- **Success**: the created media set.
- **Failure**: exit 8 readonly block; exit 1 invalid input.

### media_set.commit

- **Class**: change (write). Commits a media set transaction.
- **Preconditions**: an open transaction on a writable set.
- **Effect**: makes the transaction's media visible.
- **Inputs**: `--branch-name`/`--transaction-id`.
- **Success**: the committed set/transaction.
- **Failure**: exit 1 invalid state.

### media_set.abort

- **Class**: change (write). Aborts a media set transaction.
- **Preconditions**: an open transaction.
- **Effect**: discards the transaction's changes.
- **Inputs**: `--branch-name`/`--transaction-id`.
- **Success**: returns the aborted transaction.

### media_set.clear

- **Class**: change (write). Clears a media set transaction.
- **Preconditions**: an open transaction.
- **Effect**: clears media in the transaction scope.
- **Inputs**: `--branch-name`/`--transaction-id`.
- **Success**: returns the cleared transaction.

### media_set.transform

- **Class**: execute (write, async). Applies a transformation.
- **Preconditions**: a valid transformation over the set.
- **Effect**: starts a transform; acceptance is not proof it finished.
- **Inputs**: `--transformation-json`; branch/transaction context.
- **Success**: a transform reference; check status for completion.
- **Failure**: exit 5 on timeout.

### media_set.upload

- **Class**: create (binary upload). Uploads a media item.
- **Preconditions**: can write the set/transaction.
- **Effect**: stores the media bytes into the set.
- **Inputs**: `--file` (bounded 16 MiB), `--media-item-path`,
  `--transaction-id`, `--branch-name`.
- **Success**: the uploaded item reference.
- **Failure**: exit 1 file too large; exit 8 readonly block.

### media_set.upload_media

- **Class**: create (binary upload). Uploads media with a filename.
- **Preconditions**: can write the set/transaction.
- **Effect**: stores media; requires `--file` + `--filename`.
- **Inputs**: `--file`, `--filename`, `--media-item-path`, transaction/branch.
- **Success**: the uploaded item.
- **Failure**: exit 1 if `--file`/`--filename` missing or too large.

### media_set.calculate

- **Class**: change (write). Recomputes derived metadata/transform output.
- **Preconditions**: can write the set.
- **Effect**: recalculates derived content for the set/transaction.
- **Inputs**: `--branch-name`/`--transaction-id`.
- **Success**: returns the updated set.

### media_set.register

- **Class**: change (write). Registers an existing item in a transaction.
- **Preconditions**: can write the set/transaction.
- **Effect**: adds an existing media item to the transaction scope.
- **Inputs**: `--media-item-rid`, `--transaction-id`, `--branch-name`.
- **Success**: returns the registered item.

### media_set.reference

- **Class**: change (write). Adds a reference to a media item in a transaction.
- **Preconditions**: can write the set/transaction.
- **Effect**: references a media item for the transaction.
- **Inputs**: `--media-item-rid`/`--physical-item-name`, branch/transaction.
- **Success**: returns the reference.

## Evidence and review

Reviewed against the installed `pal-found-media-sets` parser and pinned SDK
sources (commit `2da67907`). Lifecycle ops write material media state; `upload`
and `upload_media` are bounded 16 MiB; `transform` is async and needs a status
check (AC-D-013-05). No unsupported operation is documented as callable.
