# Schedule and schedule version operations

A build computes selected dataset targets through jobs. A schedule records what to build and when; a
schedule run may only start a build, so inspect the build and its jobs to determine completion. The
trigger controls when a schedule fires; its action and scope determine targets and which resources
can be built.

Platform context: [Palantir
documentation](https://www.palantir.com/docs/foundry/data-integration/schedules). The behavior below
describes the installed CLI commands. Replace
example identifiers and configuration values with values from your Foundry enrollment.

## Operation records

### schedule.create

- **Behavior:** Creates a Schedule whose action names the build targets and build options, whose
  trigger decides when it runs, and whose scope decides which outputs it may build. A user-scoped
  schedule can change behavior if the owner's permissions change.
- **Before use:** Choose accessible build targets, a valid action and trigger, and a scope that can
  build those outputs.
- **Inputs:** positional none; required `--action-json`, `--trigger-json`, `--scope-mode-json`;
  optional `--display-name`, `--description`. `trigger`: The schedule trigger. If the requesting
  user does not have permission to see the trigger, this will be empty.
- **Parameter notes:** `--display-name` labels the schedule; `--description` stores its explanatory text.
- **Result:** `Schedule`.
- **Failure or follow-up:** An invalid configuration or insufficient permission rejects schedule
  creation; use the returned RID for later calls.
- **Example:** `pal-found-orchestration schedule create --action-json '{"abortOnFailure":false,"forceBuild":false,"retryBackoffDuration":{"unit":"SECONDS","value":30},"retryCount":1,"fallbackBranches":[],"branchName":"master","notificationsEnabled":false,"target":{"type":"manual","targetRids":["ri.foundry.main.dataset.b737e24d-6b19-43aa-93d5-da9fc4073f6e","ri.foundry.main.dataset.d2452a94-a755-4778-8bfc-a315ab52fc43"]}}' --trigger-json '{"type":"time","cronExpression":"0 0 * * *","timeZone":"UTC"}' --scope-mode-json '{"type":"user"}'`

### schedule.delete

- **Behavior:** Delete the Schedule with the specified rid.
- **Before use:** The schedule must exist and be accessible; state-changing calls also require
  schedule management permission.
- **Inputs:** positional `schedule_rid`; required none; optional none.
- **Result:** `None`.
- **Failure or follow-up:** A missing schedule, invalid target, or insufficient permission rejects
  the removal. Confirm the resulting state with a read operation.
- **Example:** `pal-found-orchestration schedule delete SCHEDULE_RID`

### schedule.get

- **Behavior:** Get the Schedule with the specified rid.
- **Before use:** The schedule must exist and be accessible; state-changing calls also require
  schedule management permission.
- **Inputs:** positional `schedule_rid`; required none; optional none.
- **Result:** `Schedule`.
- **Failure or follow-up:** A missing or inaccessible schedule returns an error, except where the
  SDK declares an optional result.
- **Example:** `pal-found-orchestration schedule get SCHEDULE_RID`

### schedule.get_affected_resources

- **Behavior:** Returns the resources affected by the schedule's action, so you can inspect its
  build scope before running or editing it.
- **Before use:** The schedule must exist and be accessible; state-changing calls also require
  schedule management permission.
- **Inputs:** positional `schedule_rid`; required none; optional none.
- **Result:** `AffectedResourcesResponse`.
- **Failure or follow-up:** Invalid input or insufficient access to the schedule is returned through
  the CLI error envelope.
- **Example:** `pal-found-orchestration schedule get-affected-resources SCHEDULE_RID`

### schedule.get_batch

- **Behavior:** Fetch multiple schedules in a single request. Schedules not found or inaccessible to
  the user will be omitted from the response. The maximum batch size for this endpoint is 1000.
- **Before use:** The schedule must exist and be accessible; state-changing calls also require
  schedule management permission.
- **Inputs:** positional none; required `--schedule-rids-json`; optional none.
- **Result:** `GetSchedulesBatchResponse`.
- **Failure or follow-up:** Check the returned entries: batch endpoints may omit missing or
  inaccessible resources, so compare the result with requested RIDs.
- **Example:** `pal-found-orchestration schedule get-batch --schedule-rids-json '["SCHEDULE_RID"]'`

### schedule.pause

- **Behavior:** Pauses the schedule's trigger so future automatic runs are not started until it is
  unpaused.
- **Before use:** The schedule must exist and be accessible; state-changing calls also require
  schedule management permission.
- **Inputs:** positional `schedule_rid`; required none; optional none.
- **Result:** `None`.
- **Failure or follow-up:** The API response acknowledges the request; read the resource again to
  confirm its subsequent state.
- **Example:** `pal-found-orchestration schedule pause SCHEDULE_RID`

### schedule.replace

- **Behavior:** Replaces the Schedule with the specified rid.
- **Before use:** The schedule must exist and be editable; provide its complete replacement action,
  trigger, and scope.
- **Inputs:** positional `schedule_rid`; required `--action-json`, `--trigger-json`,
  `--scope-mode-json`; optional `--display-name`, `--description`. `trigger`: The schedule trigger.
  If the requesting user does not have permission to see the trigger, this will be empty.
- **Parameter notes:** `--display-name` replaces the schedule label; `--description` replaces its explanatory text.
- **Result:** `Schedule`.
- **Failure or follow-up:** An invalid replacement payload or insufficient permission leaves the
  schedule unchanged; read it again after success.
- **Example:** `pal-found-orchestration schedule replace SCHEDULE_RID --action-json '{"abortOnFailure":false,"forceBuild":false,"retryBackoffDuration":{"unit":"SECONDS","value":30},"retryCount":1,"fallbackBranches":[],"branchName":"master","notificationsEnabled":false,"target":{"type":"manual","targetRids":["ri.foundry.main.dataset.b737e24d-6b19-43aa-93d5-da9fc4073f6e","ri.foundry.main.dataset.d2452a94-a755-4778-8bfc-a315ab52fc43"]}}' --trigger-json '{"type":"time","cronExpression":"0 0 * * *","timeZone":"UTC"}' --scope-mode-json '{"type":"user"}'`

### schedule.run

- **Behavior:** Starts a run of this schedule now. The run may start a build, be ignored because
  nothing needs building, or fail before a build starts.
- **Before use:** The schedule must exist and be accessible; state-changing calls also require
  schedule management permission.
- **Inputs:** positional `schedule_rid`; required none; optional none.
- **Result:** `ScheduleRun`.
- **Failure or follow-up:** A successful request starts a schedule run; inspect `schedule runs` and
  the resulting build for completion or failure.
- **Example:** `pal-found-orchestration schedule run SCHEDULE_RID`

### schedule.runs

- **Behavior:** Get the most recent runs of a Schedule. If no page size is provided, a page size of
  100 will be used.
- **Before use:** The schedule must exist and be accessible; state-changing calls also require
  schedule management permission.
- **Inputs:** positional `schedule_rid`; required none; optional none.
- **Result:** `ListRunsOfScheduleResponse`.
- **Failure or follow-up:** An empty page is not proof there are no more results; follow the
  returned page token when present.
- **Example:** `pal-found-orchestration schedule runs SCHEDULE_RID`

### schedule.unpause

- **Behavior:** Resumes a paused schedule so its trigger can start future automatic runs again.
- **Before use:** The schedule must exist and be accessible; state-changing calls also require
  schedule management permission.
- **Inputs:** positional `schedule_rid`; required none; optional none.
- **Result:** `None`.
- **Failure or follow-up:** The API response acknowledges the request; read the resource again to
  confirm its subsequent state.
- **Example:** `pal-found-orchestration schedule unpause SCHEDULE_RID`

### schedule_version.get

- **Behavior:** Get the ScheduleVersion with the specified rid.
- **Before use:** The schedule version must exist and be readable.
- **Inputs:** positional `schedule_version_rid`; required none; optional none.
  `schedule_version_rid`: The RID of a schedule version
- **Result:** `ScheduleVersion`.
- **Failure or follow-up:** A missing or inaccessible schedule version returns an error, except
  where the SDK declares an optional result.
- **Example:** `pal-found-orchestration schedule-version get SCHEDULE_VERSION_RID`

### schedule_version.schedule

- **Behavior:** Looks up the Schedule associated with this ScheduleVersion. The response may be
  empty if the version is no longer linked to an accessible schedule.
- **Before use:** The schedule version must exist and be readable.
- **Inputs:** positional `schedule_version_rid`; required none; optional none.
  `schedule_version_rid`: The RID of a schedule version
- **Result:** `Optional[Schedule]`.
- **Failure or follow-up:** A missing or inaccessible schedule version returns an error, except
  where the SDK declares an optional result.
- **Example:** `pal-found-orchestration schedule-version schedule SCHEDULE_VERSION_RID`
