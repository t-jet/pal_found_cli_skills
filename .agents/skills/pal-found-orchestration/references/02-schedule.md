# Schedule and schedule version operations

This part documents the `schedule` (10) and `schedule_version` (2) resource
clients (12 operations). A schedule triggers builds on a cadence; each run
creates a schedule run.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/orchestration/scripts/pal_found_orchestration_cli.py`;
SDK `foundry_sdk/v2/orchestration/{schedule,schedule_version}.py` at pinned
commit `2da67907`. Reviewer architect (CODEREVIEW-051), 2026-10-03. QA
baseline TESTCASE-014.

## Operation records

### schedule.create

- **Class**: create (write). Creates a schedule.
- **Preconditions**: can create schedules with the given targets.
- **Effect**: creates a schedule; it will trigger builds per its configuration.
- **Inputs**: `--display-name`, target/trigger configuration.
- **Success**: the created schedule (RID).
- **Example**: `pal-found-orchestration schedule create --display-name "Nightly" --config-json '{}'`.

### schedule.delete

- **Class**: delete (write). Deletes a schedule.
- **Preconditions**: can delete the schedule.
- **Effect**: removes the schedule; no further runs are triggered.
- **Inputs**: positional `schedule_rid`.
- **Success**: returns the deleted schedule.

### schedule.get

- **Class**: read. Returns a schedule.
- **Preconditions**: can read the schedule.
- **Effect**: returns the schedule record.
- **Inputs**: positional `schedule_rid`.
- **Success**: the schedule.
- **Failure**: exit 4 if missing.

### schedule.get_affected_resources

- **Class**: read. Returns resources a schedule affects.
- **Preconditions**: can read the schedule.
- **Effect**: returns affected resources, paged.
- **Inputs**: positional `schedule_rid`; paging options.

### schedule.get_batch

- **Class**: read. Returns several schedules.
- **Preconditions**: can read each.
- **Effect**: returns a batch of schedules.
- **Inputs**: positional JSON body list of schedule RIDs.

### schedule.pause

- **Class**: change (write). Pauses a schedule.
- **Preconditions**: can write the schedule.
- **Effect**: stops future runs while paused.
- **Inputs**: positional `schedule_rid`.
- **Success**: the updated (paused) schedule.

### schedule.replace

- **Class**: change (write). Replaces a schedule definition.
- **Preconditions**: can write the schedule.
- **Effect**: replaces the schedule's trigger/targets.
- **Inputs**: positional `schedule_rid`; replacement body/fields.
- **Success**: the updated schedule.

### schedule.run

- **Class**: execute (write, async). Triggers an immediate run.
- **Preconditions**: a schedule you can run.
- **Effect**: starts a run now; acceptance is not proof it finished.
- **Inputs**: positional `schedule_rid`.
- **Success**: the created run; check `schedule.runs`/`build.get` for status.
- **Failure**: exit 5 on timeout; schedule may still run.

### schedule.runs

- **Class**: read. Lists runs of a schedule.
- **Preconditions**: can read the schedule.
- **Effect**: returns runs, paged.
- **Inputs**: positional `schedule_rid`; paging options.
- **Success**: runs; empty if none.

### schedule.unpause

- **Class**: change (write). Unpauses a schedule.
- **Preconditions**: can write the schedule.
- **Effect**: resumes future runs.
- **Inputs**: positional `schedule_rid`.
- **Success**: the updated (unpaused) schedule.

### schedule_version.get / schedule

- **Class**: read. Returns a schedule version or the schedule bound to a
  version.
- **Preconditions**: can read the schedule/version.
- **Effect**: `get` returns a specific version; `schedule` returns the schedule
  for a version.
- **Inputs**: positional `schedule_version_id` (and `schedule_rid` where
  needed).
- **Success**: the version/schedule record.

## Evidence and review

Reviewed against the installed `pal-found-orchestration` parser and pinned SDK
sources (commit `2da67907`). `schedule.create/delete/pause/replace/run/unpause`
are write/execute with schedule-state and compute effects; `run` is async and
needs a follow-up status check (AC-D-013-05). No unsupported operation is
documented as callable.
