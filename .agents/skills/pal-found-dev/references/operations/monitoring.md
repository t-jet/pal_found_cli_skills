# Checks, monitoring and alert ownership

[Production operations](../operations.md) · [Development guide](../../SKILL.md)

## Concept and lifecycle

Health checks evaluate resource conditions and retain results. Configuration, latest
evaluation, failure notification and recovery establish separate states. Schedule status
covers the scheduled build. Job status covers its target job and can pass when a later
downstream job fails. Upstream cancellation can leave a target's job check unevaluated.

Freshness measures differ. Time since last updated measures time from the last committed
transaction, including empty transactions. Data freshness compares that commit time with
the maximum timestamp column value and evaluates on commit. Sync freshness compares sync
time with data timestamps. Select the measure matching the business requirement.

## Prerequisites

Prepare resource/schedule IDs, timestamp semantics/time zone, normal cadence, moderate and
critical thresholds, support hours, primary/backup owner and isolated failure test. Check
configuration and subscription require enrollment access and appropriate resource rights.
Local calculations validate thresholds; live evaluations/notifications need actual checks.
Administrators prepare permitted email or external integrations where needed.

## Procedure

1. Open Dataset Preview > Health, or Data Lineage schedule > Metrics > Health. Add a
   resource-supported check. To apply one to multiple datasets, select graph nodes and
   right-click Add health check.
2. Configure rule, thresholds and severity from the business contract. Add schedule status
   for the whole schedule and output freshness/content checks where status misses old data.
3. Choose automatic or manual evaluation. Automatic time checks evaluate at updates and
   their threshold; manual schedules evaluate at the configured interval.
4. Expand the check and Watch: All failures, Only critical or Nothing. Enable email through
   Profile > Settings > Notifications > Builds where permitted. Name the responder;
   creating a check does not subscribe that person.
5. Where useful, enable Automatically create an issue when this check fails and assign
   the authorized owner. For many resources use a monitoring view/subscription and agreed
   routing instead of maintaining individual watches.
6. Trigger an isolated failure. Inspect evaluation timestamp/value and actual notification
   or issue. Restore good data and verify a new passing evaluation and business result.

## Worked example

Illustrative totals updates every 15 minutes; critical deadline is 60 minutes since commit.
Configure an automatic Time Since Last Updated check at 60 minutes, watch All failures
on a test dataset and record its last commit as 09:00 UTC.

A 09:58 commit refreshes the evaluated condition and next deadline. If none arrives,
inspect the threshold evaluation around 10:00 and its failure/notification. After a 10:02
repair commit, inspect the passing evaluation. Service processing can add delay; record
actual timestamps instead of assuming punctual email delivery. An empty transaction resets
update freshness without proving fresh business rows. Also verify timestamp/content
under a separate check where the output contract requires it.

## Expected result and checks

Record rule, severity, evaluation mode, owner/watch preferences, observed value, failure
delivery and recovery result. Check the destination under authorized test conditions.
Pausing snoozes all watchers; deleting removes configuration and schedule. Record approved
maintenance and restore monitoring afterward. A check's last result can precede the
incident; always compare its evaluation time with the relevant build/commit.

## Failures and recovery

| Observation | Recovery |
| --- | --- |
| No alert despite failure | Inspect evaluation time, Watch severity, pause state and notification preferences. |
| Old passing result | Check trigger semantics; upstream cancellation can prevent target evaluation. |
| Recent commit but old rows | Inspect business timestamps/content in addition to update freshness. |
| Excess alerts | Reconcile cadence/severity and routing with the SLA; retain a responsible owner. |
| Recovery banner, unresolved incident | Verify business output and new check evaluation before closing. |

Optional source attribution: [configuration](https://www.palantir.com/docs/foundry/health-checks/overview),
[semantics](https://www.palantir.com/docs/foundry/health-checks/check-types),
[evaluation](https://www.palantir.com/docs/foundry/health-checks/check-evaluation),
[watching](https://www.palantir.com/docs/foundry/health-checks/watching-checks),
[notifications/issues](https://www.palantir.com/docs/foundry/health-checks/notifications).
