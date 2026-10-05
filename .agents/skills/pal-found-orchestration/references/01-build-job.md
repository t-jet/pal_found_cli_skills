# Build and job operations

A build computes selected dataset targets through jobs. A schedule records what to build and when; a
schedule run may only start a build, so inspect the build and its jobs to determine completion. The
trigger controls when a schedule fires; its action and scope determine targets and which resources
can be built.

Platform context: [Palantir
documentation](https://www.palantir.com/docs/foundry/data-integration/schedules). The behavior below
describes the installed CLI commands. Replace
example identifiers and configuration values with values from your Foundry enrollment.

## Operation records

### build.cancel

- **Behavior:** Request a cancellation for all unfinished jobs in a build. The build's status will
  not update immediately. This endpoint is asynchronous and a success response indicates that the
  cancellation request has been acknowledged and the build is expected to be canceled soon. If the
  build has already finished or finishes shortly after the request and before the cancellation, the
  build will not change.
- **Before use:** The build must exist and be visible to the caller.
- **Inputs:** positional `build_rid`; required none; optional none. `build_rid`: The RID of a Build.
- **Result:** `None`.
- **Failure or follow-up:** The API response acknowledges the request; read the resource again to
  confirm its subsequent state.
- **Example:** `pal-found-orchestration build cancel BUILD_RID`

### build.create

- **Behavior:** Starts a one-time build for the datasets in `target`. Foundry resolves the build
  graph and runs the necessary jobs on the chosen branch, consulting `fallback_branches` for inputs
  when configured. `force_build` can include targets even when they are not stale.
- **Before use:** The target datasets and their dependencies must be accessible; build permissions
  must cover the target branch.
- **Inputs:** positional none; required `--target-json`, `--fallback-branches-json`; optional
  `--abort-on-failure`, `--branch-name`, `--force-build`, `--notifications-enabled`,
  `--retry-backoff-duration-json`, `--retry-count`. `target`: The targets of the schedule.
  `branch_name`: The target branch the build should run on. `retry_count`: The number of retry
  attempts for failed jobs.
- **Parameter notes:** `--branch-name` selects target branch; `--abort-on-failure` stops remaining work after failure; `--force-build` runs targets even when current; `--notifications-enabled` enables build notifications; `--retry-count` sets job retry attempts; `--retry-backoff-duration-json` supplies delay between retries.
- **Result:** `Build`.
- **Failure or follow-up:** The returned Build is a start response. Use `build get` and `build jobs`
  to check whether computation finished and whether any job failed.
- **Example:** `pal-found-orchestration build create --target-json '{"type":"manual","targetRids":["ri.foundry.main.dataset.4263bdd9-d6bc-4244-9cca-893c1a2aef62","ri.foundry.main.dataset.86939c1e-4256-41db-9fe7-e7ee9e0f752a"]}' --fallback-branches-json '[]'`

### build.get

- **Behavior:** Reads a build by RID to check its current state and targets. A started build may
  still have running jobs. The SDK documents a limit of four requests per second and 25 concurrent
  requests for this endpoint.
- **Before use:** The build must exist and be visible to the caller.
- **Inputs:** positional `build_rid`; required none; optional none. `build_rid`: The RID of a Build.
- **Result:** `Build`.
- **Failure or follow-up:** A missing or inaccessible build returns an error, except where the SDK
  declares an optional result.
- **Example:** `pal-found-orchestration build get BUILD_RID`

### build.get_batch

- **Behavior:** Fetches up to 100 builds by RID in one request, useful when checking several
  schedule runs. Compare returned entries with requested RIDs because inaccessible builds can be
  omitted. The SDK documents four requests per second and 25 concurrent requests.
- **Before use:** The build must exist and be visible to the caller.
- **Inputs:** positional none; required `--build-rids-json`; optional none.
- **Result:** `GetBuildsBatchResponse`.
- **Failure or follow-up:** Check the returned entries: batch endpoints may omit missing or
  inaccessible resources, so compare the result with requested RIDs.
- **Example:** `pal-found-orchestration build get-batch --build-rids-json '["BUILD_RID"]'`

### build.jobs

- **Behavior:** Lists jobs belonging to a build. Inspect each returned job to see which unit of
  work succeeded or failed; the build's start response alone cannot show this.
- **Before use:** The build must exist and be visible to the caller.
- **Inputs:** positional `build_rid`; required none; optional none. `build_rid`: The RID of a Build.
- **Result:** `ListJobsOfBuildResponse`.
- **Failure or follow-up:** An empty page is not proof there are no more results; follow the
  returned page token when present.
- **Example:** `pal-found-orchestration build jobs BUILD_RID`

### build.search

- **Behavior:** Searches builds visible to the caller. `--where-json` limits matches and
  `--order-by-json` controls their order; without filters, results are paginated across visible
  builds.
- **Before use:** The caller can search only builds visible to its identity; filters are optional.
- **Inputs:** positional none; required none; optional `--where-json`, `--order-by-json`.
- **Result:** `SearchBuildsResponse`.
- **Failure or follow-up:** An empty page is not proof there are no more results; follow the
  returned page token when present.
- **Example:** `pal-found-orchestration build search`

### job.get

- **Behavior:** Reads one job's status and details by RID. Use it after `build jobs` to diagnose a
  build's progress or failure. The SDK documents four requests per second and 25 concurrent
  requests for this endpoint.
- **Before use:** The job must exist and be visible to the caller.
- **Inputs:** positional `job_rid`; required none; optional none. `job_rid`: The RID of a Job.
- **Result:** `Job`.
- **Failure or follow-up:** A missing or inaccessible job returns an error, except where the SDK
  declares an optional result.
- **Example:** `pal-found-orchestration job get JOB_RID`

### job.get_batch

- **Behavior:** Fetches up to 500 jobs by RID in one request. Compare the response with requested
  RIDs because missing or inaccessible jobs can be omitted. The SDK documents four requests per
  second and 25 concurrent requests.
- **Before use:** The job must exist and be visible to the caller.
- **Inputs:** positional none; required `--job-rids-json`; optional none.
- **Result:** `GetJobsBatchResponse`.
- **Failure or follow-up:** Check the returned entries: batch endpoints may omit missing or
  inaccessible resources, so compare the result with requested RIDs.
- **Example:** `pal-found-orchestration job get-batch --job-rids-json '["JOB_RID"]'`
