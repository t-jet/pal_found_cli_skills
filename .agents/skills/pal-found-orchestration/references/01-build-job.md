# Build and job operations

This part documents the `build` (6) and `job` (2) resource clients (8
operations). A build processes targets; a build's work runs as jobs.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/orchestration/scripts/pal_found_orchestration_cli.py`;
SDK `foundry_sdk/v2/orchestration/{build,job}.py` at pinned commit
`2da67907`. Reviewer architect (CODEREVIEW-051), 2026-10-03. QA baseline
TESTCASE-014.

## Operation records

### build.cancel

- **Class**: change (write). Cancels a running build.
- **Preconditions**: a build you can cancel.
- **Effect**: cancels the build; a zero exit means the cancel was accepted.
- **Inputs**: positional `build_rid`.
- **Success**: returns the canceled build.
- **Failure**: exit 1 if build not cancellable.

### build.create

- **Class**: execute (write, async). Creates and starts a build.
- **Preconditions**: valid targets and permissions.
- **Effect**: starts a build over the targets; acceptance is not proof it
  finished.
- **Inputs**: `--target-json` (targets/branches).
- **Success**: the created build reference (Brid). Check `build.get`/`jobs`
  for status.
- **Failure**: exit 5 on timeout; build may still run.
- **Example**: `pal-found-orchestration build create --target-json '{"datasetRids":["ri.foundry.main.dataset.d1"]}'`.

### build.get

- **Class**: read. Returns a build's status.
- **Preconditions**: can read the build.
- **Effect**: returns the build and its state.
- **Inputs**: positional `build_rid`.
- **Success**: the build record; use its status to confirm completion.

### build.get_batch

- **Class**: read. Returns several builds.
- **Preconditions**: can read each.
- **Effect**: returns a batch of build records.
- **Inputs**: positional JSON body list of build RIDs.
- **Success**: list of builds.

### build.jobs

- **Class**: read. Lists a build's jobs.
- **Preconditions**: can read the build.
- **Effect**: returns jobs, paged.
- **Inputs**: positional `build_rid`; paging options.
- **Success**: jobs; empty if none.

### build.search

- **Class**: read. Searches builds by criteria.
- **Preconditions**: can read builds.
- **Effect**: returns matching builds, paged.
- **Inputs**: `--where-json`, paging options.
- **Success**: matches; empty if none.

### job.get

- **Class**: read. Returns a job.
- **Preconditions**: can read the job.
- **Effect**: returns the job record.
- **Inputs**: positional `job_rid`.
- **Success**: the job and its status.
- **Failure**: exit 4 if missing.

### job.get_batch

- **Class**: read. Returns several jobs.
- **Preconditions**: can read each.
- **Effect**: returns a batch of job records.
- **Inputs**: positional JSON body list of job RIDs.
- **Success**: list of jobs.

## Evidence and review

Reviewed against the installed `pal-found-orchestration` parser and pinned SDK
sources (commit `2da67907`). `build.create`/`cancel` are write/execute with
compute cost; a zero exit approves the request, not the finished build. Always
confirm with `build.get`/`job.get` (AC-D-013-05). No unsupported operation is
documented as callable.
