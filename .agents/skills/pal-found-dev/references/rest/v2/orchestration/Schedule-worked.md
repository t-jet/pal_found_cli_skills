# Schedules and explicit runs

[Operation catalog](../../catalog.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

A Schedule describes recurring orchestration work. Its configuration, versions,
pause state and execution runs are separate concerns. An explicit run returns a
ScheduleRun; receiving that record does not establish that resulting builds or
jobs have finished successfully.

## Start one explicit run

1. Resolve the schedule RID and inspect its intended resources and configuration.
   Confirm that initiating its work is authorized and appropriate now.
2. Call [run](../../contracts/v2/orchestration/Schedule/run.md) with that RID.
   Preserve the returned ScheduleRun and its identifiers for follow-up.
3. Read runs and associated build/job state using their local contracts. If the
   application waits, use a finite poll count and deadline. Report pending work
   separately from success. The run method's SDK source does not describe a
   universal terminal-state or completion guarantee.

Run from the skill directory:

```bash
python -B examples/rest/075/v2/orchestration/Schedule/run.py
```

The example makes an actual SDK call through a synthetic transport. It asserts
the POST path, decodes the ScheduleRun and verifies the named
`RunSchedulePermissionDenied` exception. Its output confirms request/result/error
handling; no schedule executes in an enrollment.

For `RunSchedulePermissionDenied`, verify application grants and permission to
run the intended schedule. SDK source gives no universal OAuth scope or exact
role name for this operation. Confirm those requirements in the authorized
tenant. If the response is lost after submission, inspect schedule run history
and correlate available identities and times before considering another run.
The SDK does not promise an idempotency key or that repeating `run` avoids
duplicate work. Escalate an ambiguous submission rather than starting another
run automatically.

## Execution boundary

Prepared SDK 1.101.0 and httpx suffice for the offline fixture. Live schedule runs
can initiate resource work and need enrollment connectivity and authorized
identity. Fixture success establishes neither authorization nor build success.
