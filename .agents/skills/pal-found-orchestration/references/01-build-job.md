# Build and job operations

A build computes selected buildable resources through jobs. A schedule records what to build and when; a
schedule run may only start a build, so inspect the build and its jobs to determine completion. The
trigger controls when a schedule fires; its action and scope determine targets and which resources
can be built.

Platform context: [Palantir
documentation](https://www.palantir.com/docs/foundry/data-integration/schedules). The behavior below
describes the installed CLI commands. Replace
example identifiers and configuration values with values from your Foundry enrollment.

After a timeout, transport failure, or exhausted retries on a write, inspect the
build and its jobs before replaying the request. Creation or cancellation may
already have taken effect; a client failure does not establish the build state.
Reconcile the intended targets and current status to avoid duplicate work.

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

- **Behavior:** Starts a one-time build for the buildable resources in `target`, such as datasets,
  media sets, or restricted views. Foundry resolves the build
  graph and runs the necessary jobs on the chosen branch, consulting `fallback_branches` for inputs
  when configured. `force_build` can include targets even when they are not stale.
- **Before use:** The target resources and their dependencies must be accessible; build permissions
  must cover the target branch.
- **Inputs:** positional none; required `--target-json`, `--fallback-branches-json`; optional
  `--abort-on-failure`, `--branch-name`, `--force-build`, `--notifications-enabled`,
  `--retry-backoff-duration-json`, `--retry-count`. `target`: The buildable resources to build in this
  one-time request.
  `branch_name`: The target branch the build should run on. `retry_count`: The number of retry
  attempts for failed jobs.
- **Parameter notes:** `--branch-name` selects target branch; `--abort-on-failure` stops remaining work after failure; `--force-build` runs targets even when current; `--notifications-enabled` enables build notifications; `--retry-count` sets job retry attempts; `--retry-backoff-duration-json` supplies delay between retries.
- **Result:** `Build`.
- **Failure or follow-up:** The returned Build is a start response. Use `build get` and `build jobs`
  to check whether computation finished and whether any job failed.
- **Example:** `pal-found-orchestration build create --target-json '{"type":"manual","targetRids":["ri.foundry.main.dataset.4263bdd9-d6bc-4244-9cca-893c1a2aef62","ri.foundry.main.dataset.86939c1e-4256-41db-9fe7-e7ee9e0f752a"]}' --fallback-branches-json '[]'`
  This example selects datasets; `targetRids` can also identify buildable media sets or restricted
  views when the caller has access.

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
- **Inputs:** positional `build_rid`; required none; optional `--page-size`, `--page-token`,
  `--all`, `--max-pages`. `build_rid`: The RID of a Build. Use `--page-token` to resume from the
  `next_page_token` reported by a previous call; `--all` or `--max-pages` fetches more than one
  page in one invocation.
- **Parameter notes:** `--page-size` sets requested items per page (default 100 unless CLI
  configuration changes it). `--page-token` resumes at a cursor. `--max-pages` bounds pages
  fetched in this call; `--all` fetches up to the CLI page cap.
- **Result:** A list of jobs on stdout in the selected format. Page count and any
  `next_page_token` appear separately in stderr metadata.
- **Failure or follow-up:** An empty item list does not prove there are no more jobs. If stderr
  metadata contains `next_page_token`, pass it as `--page-token` to continue.
- **Example:** `pal-found-orchestration build jobs BUILD_RID`

### build.search

- **Behavior:** Searches builds visible to the caller. `--where-json` limits matches and
  `--order-by-json` controls their order; results are paginated.
- **Before use:** The caller can search only builds visible to its identity. Supply a filter;
  the CLI requires `--where-json` before configuration or SDK invocation.
- **Inputs:** positional none; required `--where-json`; optional `--order-by-json`,
  `--page-size`, `--page-token`, `--all`, `--max-pages`. Use `--page-token` to resume from the
  `next_page_token` reported by a previous call; `--all` or `--max-pages` fetches more than one
  page in one invocation.
- **Parameter notes:** `--where-json` filters builds and `--order-by-json` sorts matches.
  `--page-size` sets requested items per page (default 100 unless CLI configuration changes it).
  `--page-token` resumes at a cursor. `--max-pages` bounds pages fetched in this call; `--all`
  fetches up to the CLI page cap.
- **Result:** A list of builds on stdout in the selected format. Page count and any
  `next_page_token` appear separately in stderr metadata.
- **Failure or follow-up:** An empty item list does not prove there are no more builds. If stderr
  metadata contains `next_page_token`, pass it as `--page-token` to continue.
- **Example:** `pal-found-orchestration build search --where-json '{"type":"eq","field":"STATUS","value":"RUNNING"}'`

### job.get

The CLI sends the required `preview=true` query selector internally for both
job read operations. There is no `--preview` flag; do not add it or attempt to
disable the selector. API availability and normal authorization still apply;
the examples do not prove server access.

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
