# Production operations

[Development guide](../SKILL.md) · [Pipeline development](pipelines.md)

Production operation connects source freshness, build execution, committed output,
application consumption and incident ownership. A successful old job can coexist with
stale output; a passing intermediate job does not establish success for its whole schedule.
Use exact branches and transaction times when diagnosing results.

| Task | Local guide |
| --- | --- |
| Trace input versions, branch resolution and downstream impact | [Trace branch and build provenance](operations/lineage.md) |
| Configure evaluated checks, subscriptions and alert ownership | [Checks, monitoring and alert ownership](operations/monitoring.md) |
| Investigate stale/failed outputs and verify recovery | [Diagnose, recover and verify pipelines](operations/support.md) |

For snapshot/incremental decisions use [transaction behavior](pipelines/transactions.md).
For build versus code delivery use [release procedure](pipelines/releases.md).
External integrations use [REST request/error contracts](rest-api.md); Compute processing
has its own [mode and resource-effects contract](compute/execution.md).
