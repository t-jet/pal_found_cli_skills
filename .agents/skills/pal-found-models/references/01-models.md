# Model and experiment operations

This part documents the `model` (3), `model_version` (3), `experiment` (2),
`experiment_artifact_table` (2), `experiment_series` (2), and
`live_deployment` (1) resource clients (13 operations).

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/models/scripts/pal_found_models_cli.py`;
SDK `foundry_sdk/v2/models/{model,model_version,experiment,experiment_artifact_table,experiment_series,live_deployment}.py`
at pinned commit `2da67907`. Reviewer architect (CODEREVIEW-050), 2026-10-03.
QA baseline TESTCASE-013.

## Operation records

### model.create

- **Class**: create (write). Registers a new ML model.
- **Preconditions**: can create models.
- **Effect**: creates a model artifact.
- **Inputs**: required name/api; `--model-api-json` for full definition.
- **Success**: the created model, including its RID.
- **Failure**: exit 8 readonly block; exit 1 invalid definition.

### model.get

- **Class**: read. Returns a model.
- **Preconditions**: can read the model.
- **Effect**: returns the model record.
- **Inputs**: positional `model_rid`.
- **Success**: the model.
- **Failure**: exit 4 if missing.

### model.promote_version

- **Class**: change (write). Promotes a model version to live.
- **Preconditions**: can write the model; the version exists.
- **Effect**: makes a model version the promoted/live one; affects consumers
  and deployments.
- **Inputs**: positional `model_rid`, `model_version_rid`.
- **Success**: returns the updated model/promoted version.
- **Example**: `pal-found-models model promote-version <MODEL_RID> <VERSION_RID>`.

### model_version.create

- **Class**: create (write). Registers a model version.
- **Preconditions**: can write the model; a version payload.
- **Effect**: adds a version to a model.
- **Inputs**: positional `model_rid`; version definition.
- **Success**: the created version (RID).

### model_version.get / list

- **Class**: read. Returns a version or pages versions of a model.
- **Preconditions**: can read the model.
- **Effect**: returns version metadata.
- **Inputs**: `get` positional `model_rid`, `model_version_rid`; `list`
  positional `model_rid` + paging.

### experiment.get / search

- **Class**: read. Returns an experiment or searches experiments.
- **Preconditions**: can read experiments.
- **Effect**: `get` returns one experiment; `search` returns matches.
- **Inputs**: `get` positional `experiment_rid`; `search` uses criteria/paging.

### experiment_artifact_table.json / parquet

- **Class**: read (binary/stream download). Reads an experiment artifact table
  as JSON or Parquet.
- **Preconditions**: can read the experiment/artifact.
- **Effect**: downloads the artifact table in the requested format; may be
  large.
- **Inputs**: positional `experiment_rid`, artifact/table ids; `--output`.
- **Success**: a streamed artifact (bounded/download).
- **Failure**: exit 8 if read blocked; exit 5 on large/failed download.

### experiment_series.json / parquet

- **Class**: read (binary/stream download). Reads an experiment series as JSON
  or Parquet.
- **Preconditions**: can read the experiment/series.
- **Effect**: downloads the series data in the requested format.
- **Inputs**: positional `experiment_rid`, series id; `--output`.
- **Success**: a streamed series (bounded).

### live_deployment.transform_json

- **Class**: execute (read/inference). Runs a live deployment transform.
- **Preconditions**: a live deployment you can invoke.
- **Effect**: applies the deployment to the input and returns the transform
  result; consumes model inference.
- **Inputs**: positional `live_deployment_rid`; input payload.
- **Success**: the transform result.

## Evidence and review

Reviewed against the installed `pal-found-models` parser and pinned SDK
sources (commit `2da67907`). `model.create/promote_version` and
`model_version.create` write and affect consumers; `live_deployment.transform_json`
consumes inference (AC-D-013-09). Artifact/series reads stream large data and
are bounded. No unsupported operation is documented as callable.
