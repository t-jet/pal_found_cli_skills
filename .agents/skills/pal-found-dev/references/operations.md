# Production operations

[Foundry development guide](../SKILL.md) | [Pipelines and development workflow](pipelines.md)

## Schedule and inspect builds

A build updates target dataset outputs using the build graph and the selected
branch's inputs and transform logic. A schedule can trigger a build by time or
an upstream update. Select targets so the schedule covers the dependency path
required by consumers. A successful schedule run means a build started; inspect
the build and its jobs separately before reporting data delivery. Avoid
independent schedules that write the same output dataset. See [builds](https://www.palantir.com/docs/foundry/data-integration/builds),
[schedule run states](https://www.palantir.com/docs/foundry/data-integration/schedules),
[scheduling overview](https://www.palantir.com/docs/foundry/building-pipelines/scheduling-overview),
and [scheduling best practices](https://www.palantir.com/docs/foundry/building-pipelines/scheduling-best-practices).

When a build fails, use Data Lineage's build timeline to identify the failing
job and its upstream inputs. Inspect job logs and the selected branch, input
freshness, data schema, and compute resource use. A successful job with bad or
empty output still requires correction. See [build timeline](https://www.palantir.com/docs/foundry/data-lineage/build-timeline),
[Data Lineage navigation](https://www.palantir.com/docs/foundry/data-lineage/navigation)
and [debug a failing job](https://www.palantir.com/docs/foundry/optimizing-pipelines/debug-failing-job).

## Use lineage to understand impact

Data Lineage shows how datasets, code, builds, and schedules relate. Use it
before changing a shared output to find downstream consumers and owners;
after release, use it to inspect the build path and health of those consumers.
Branch selection and fallback affect what the graph shows, so record the
branch used for the investigation. See [Data Lineage overview](https://www.palantir.com/docs/foundry/data-lineage/overview)
and [navigation](https://www.palantir.com/docs/foundry/data-lineage/navigation).
For retention or deletion work, consult [Data Lifetime](https://www.palantir.com/docs/foundry/data-lifetime/overview)
because upstream retention choices affect derived data.

## Monitor data quality and service health

Data expectations validate output data during a build and can fail it. Health
checks monitor resource conditions after delivery, including freshness,
status, duration, schema, content, and size. Data Health presents monitored
resources and alerts. Monitoring Views can apply rules across a resource set;
observability provides logs, metrics, and traces where supported. Choose
checks from user needs: an hourly feed needs a freshness limit, while an
identifier dataset may need a uniqueness expectation. Route alerts to an
owner who can inspect the failed condition. See [data expectations](https://www.palantir.com/docs/foundry/transforms-python/data-expectations-getting-started),
[health checks](https://www.palantir.com/docs/foundry/health-checks/overview),
[checks reference](https://www.palantir.com/docs/foundry/health-checks/checks-reference),
[Data Health](https://www.palantir.com/docs/foundry/observability/data-health),
[Monitoring Views](https://www.palantir.com/docs/foundry/monitoring-views/overview),
and [observability](https://www.palantir.com/docs/foundry/observability/overview).

## Establish a support path

Production ownership includes alert recipients, support hours, escalation
contacts, upstream dependencies, and a documented response when a build or
data check fails. Keep a current lineage view and distinguish a source outage
from transform code failure before rerunning a pipeline. Review [maintaining
pipelines](https://www.palantir.com/docs/foundry/maintaining-pipelines/overview),
[recommended health checks](https://www.palantir.com/docs/foundry/maintaining-pipelines/recommended-health-checks),
[data expectations](https://www.palantir.com/docs/foundry/maintaining-pipelines/define-data-expectations),
and [support processes](https://www.palantir.com/docs/foundry/maintaining-pipelines/support-processes).
