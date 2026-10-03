# Model Studio operations

This part documents the `model_studio` (3), `model_studio_config_version` (4),
`model_studio_run` (1), and `model_studio_trainer` (2) resource clients (10
operations). Model Studio manages model builds, config versions, runs, and
trainers.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/models/scripts/pal_found_models_cli.py`;
SDK `foundry_sdk/v2/models/{model_studio,model_studio_config_version,model_studio_run,model_studio_trainer}.py`
at pinned commit `2da67907`. Reviewer architect (CODEREVIEW-050), 2026-10-03.
QA baseline TESTCASE-013.

## Operation records

### model_studio.create

- **Class**: create (write). Creates a Model Studio resource.
- **Preconditions**: can create model studio resources.
- **Effect**: creates a model studio model/build.
- **Inputs**: required name/config; `--model-api-json` where shown.
- **Success**: the created resource (RID).

### model_studio.get

- **Class**: read. Returns a Model Studio resource.
- **Preconditions**: can read the resource.
- **Effect**: returns the resource record.
- **Inputs**: positional `model_studio_rid`.
- **Success**: the resource.
- **Failure**: exit 4 if missing.

### model_studio.launch

- **Class**: execute (write, async). Launches a model studio session/build.
- **Preconditions**: can launch the resource.
- **Effect**: starts a session/run; acceptance is not proof it completed.
- **Inputs**: positional `model_studio_rid`; launch options.
- **Success**: a launch/session reference; check run/status for completion.
- **Failure**: exit 5 on timeout.

### model_studio_config_version.create

- **Class**: create (write). Creates a config version.
- **Preconditions**: can write the model studio resource.
- **Effect**: adds a configuration version.
- **Inputs**: positional `model_studio_rid`; config definition.
- **Success**: the created version.

### model_studio_config_version.get / latest / list

- **Class**: read. Returns a specific, latest, or paged list of config
  versions.
- **Preconditions**: can read the resource.
- **Effect**: returns config version metadata.
- **Inputs**: `get`/`latest` positional `model_studio_rid` (+ version id for
  `get`); `list` adds paging.
- **Success**: the config version(s).

### model_studio_run.list

- **Class**: read. Lists runs for a model studio resource.
- **Preconditions**: can read the resource.
- **Effect**: returns runs, paged.
- **Inputs**: positional `model_studio_rid`; paging options.
- **Success**: runs; empty if none.

### model_studio_trainer.get / list

- **Class**: read. Returns a trainer or pages trainers.
- **Preconditions**: can read the resource.
- **Effect**: returns trainer metadata.
- **Inputs**: `get` positional trainer id; `list` paging.

## Evidence and review

Reviewed against the installed `pal-found-models` parser and pinned SDK
sources (commit `2da67907`). `model_studio.create/launch` and
`config_version.create` write or start async work with pipeline cost;
`launch` requires a follow-up status check (AC-D-013-05). The rest are reads.
No unsupported operation is documented as callable.
