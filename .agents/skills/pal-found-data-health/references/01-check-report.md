# Data Health checks and reports

Data Health monitors individual resources with checks for status, freshness, size, content, and schema. For example, a build status check asks whether the most recent build of a dataset succeeded. A check is the saved rule; each evaluation produces a check report with a result and a snapshot of the rule at that time. Time-based checks can evaluate on dataset updates, at configured thresholds, or on a regular schedule. Creation alone need not produce a report, so `get-latest` may return an empty collection until evaluation occurs. A failed check reports unhealthy data, while an API failure means the request itself could not complete. See [Health checks](https://www.palantir.com/docs/foundry/health-checks/overview), [check evaluation](https://www.palantir.com/docs/foundry/health-checks/check-evaluation), the [checks reference](https://www.palantir.com/docs/foundry/health-checks/checks-reference), and SDK `docs/v2/DataHealth/{Check,CheckReport}.md`.

The examples assume valid Foundry credentials and the required dataset or check permissions. Replace sample RIDs. A `buildStatus` rule uses a dataset RID, branch, and severity (`MODERATE` or `CRITICAL`). Other rule types have different configuration fields; inspect their SDK model before editing the JSON.

### check.create

Create a check on a dataset. `--config-json` is a required, typed rule definition; `--intent` explains why the rule exists. The returned `Check` contains its RID and saved configuration. Creation does not mean that a report has already been produced. Invalid rule fields, a missing dataset, or insufficient write permission prevent creation.

**Example:**
```bash
pal-found-data-health check create --config-json '{"type":"buildStatus","subject":{"datasetRid":"ri.foundry.main.dataset.a1b2c3d4-e5f6-7890-abcd-ef1234567890","branchId":"master"},"statusCheckConfig":{"severity":"CRITICAL"}}' --intent 'Alert when the orders build fails'
```

### check.get

Read one saved rule by `check_rid` without changing it. Use this before replacing a check to confirm its type and current fields. An unknown or inaccessible RID fails instead of returning a rule.

**Example:** `pal-found-data-health check get ri.data-health.main.check.8e27b13a-e21b-4232-ae1b-76ccf5ff42b3`

### check.replace

Replace an existing check's configuration and optional intent. The JSON is a `ReplaceCheckConfig`; it omits the subject because the check keeps its existing target. Foundry does not support changing a check's type after creation. The response is the updated `Check`. Use `get` first and preserve its type; wrong type, invalid fields, missing check, or insufficient permission fails.

**Example:**
```bash
pal-found-data-health check replace ri.data-health.main.check.8e27b13a-e21b-4232-ae1b-76ccf5ff42b3 --config-json '{"type":"buildStatus","statusCheckConfig":{"severity":"MODERATE"}}' --intent 'Monitor the orders build'
```

### check.delete

Delete the check definition identified by RID. This stops future evaluation of that rule and returns no resource body (HTTP 204). It does not repair the dataset. Confirm the RID and downstream alerting expectations before running; an unknown RID or insufficient delete permission fails.

**Example:** `pal-found-data-health check delete ri.data-health.main.check.8e27b13a-e21b-4232-ae1b-76ccf5ff42b3`

### check_report.get

Read one historical report using both its check RID and report RID. The report includes its result and a snapshot of the check configuration from evaluation time; later check edits do not rewrite it. An unknown check/report pair or inadequate read access fails.

**Example:** `pal-found-data-health check-report get ri.data-health.main.check.8e27b13a-e21b-4232-ae1b-76ccf5ff42b3 ri.data-health.main.check-report.a1b2c3d4-e5f6-7890-abcd-ef1234567890`

### check_report.get_latest

Read recent reports for one check in reverse chronological order. `--limit` defaults to 10 and has a maximum of 100. The response is a collection, so a never-evaluated check can yield no reports. Use the newest report's result to understand current observed health, and retain its RID if you need to retrieve that exact report later.

**Example:** `pal-found-data-health check-report get-latest ri.data-health.main.check.8e27b13a-e21b-4232-ae1b-76ccf5ff42b3 --limit 5`

An invalid limit, unknown check, or insufficient read permission fails. Reading reports does not run a check.
