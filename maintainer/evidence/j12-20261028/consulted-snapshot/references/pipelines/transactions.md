# Transactions and incremental execution

[Pipeline guide](../pipelines.md) | [Development guide](../../SKILL.md)

## Concept and lifecycle

Dataset transactions describe changes to versioned files. A branch selects
their history. A committed transaction changes the visible dataset state;
an open write is not a committed output. Foundry transform execution opens
output transactions and commits them when its job succeeds. A whole pipeline
can contain multiple jobs, so do not treat the entire build as one atomic write.

| Transaction form | Data interpretation |
| --- | --- |
| SNAPSHOT | Defines a replacement view of current files. |
| APPEND | Adds files; strict append rejects overwriting an existing file. |
| UPDATE | Can replace files while retaining others. |
| DELETE | Removes files and changes what downstream consumers can read. |

Incremental execution uses supported changes relative to earlier successful
state. Its validity depends on input histories, transform configuration and
output state. The initial output build and an explicit semantic-version change
can require a snapshot even when incremental execution is otherwise required.

Code Repositories Preview always runs nonincrementally, even with
`require_incremental=True`. VS Code Preview honors v1/v2 incremental semantics
for Spark and lightweight transforms. Validate actual accumulated state there
or in an authorized build, alongside the local business fixtures.

## Prerequisites

Fallback configured in a Code Repository applies to builds and actions inside
that repository. It does not set resolution rules for other applications or
externally triggered builds such as scheduled builds. Check the actual build's
context; do not transfer a repository Preview's fallback result to a schedule.

Identify input/output datasets and their branches, previous output state,
actual input changes, prepared transform runtime, schema/business rules and
authorized write context. For an incremental transform, decide which inputs
are snapshots, whether unsupported change must fail or trigger full recompute,
and what semantic-version changes mean to the algorithm.

Local fixtures can test an algorithm and derive state decisions. Actual input
transaction histories, fallback resolution, writes and builds need enrollment
access and permission. Current single-node and Spark engines both support
incremental transforms, but their APIs and output/schema behavior differ.

## Procedure

1. Inspect the requested branch and actual resolved input history. If it lacks
   data, inspect fallback rather than assuming an empty input. A dataset
   branch does not merge data like a Git merge combines source changes.
2. Compare current schema, input transaction types and previous successful
   output with the algorithm's incremental assumptions. Decide snapshot versus
   incremental handling explicitly.
3. Declare the incremental configuration with `@incremental` when supported by
   the prepared runtime. Parameters include `require_incremental`,
   `semantic_version`, `snapshot_inputs` and `strict_append`. A changed
   semantic version requests a new nonincremental run. Required-incremental
   mode can fail when incremental computation is impossible, with documented
   first-output/semantic-version exceptions.
4. In the compute function, use the selected runtime's incremental input/output
   APIs and the run's actual incremental state. Validate accumulated state
   and schema; do not append blindly after a changed reference snapshot.
5. Write output and let failures propagate. Confirm the job/build, committed
   transaction and resulting content, then compare it with full computation
   on the same small fixture inputs.

## Worked example

The [incremental transform](../../examples/pipelines/incremental_transform.py)
uses `@incremental(semantic_version=1, snapshot_inputs=["customers"])` above
`@transform.using`. Its shared
[reconciliation function](../../examples/pipelines/order_rules.py) keeps raw
order fields from previous output, adds new orders and joins the complete
customer snapshot again. `ctx.is_incremental` determines whether previous
output is read with `output.pandas(mode="previous")`. In snapshot execution,
the prior list is empty and orders supplies the full input. `set_mode("replace")`
writes the full reconciled output, so previous rows are not appended twice.

Initial inputs contain `o1/c1/1200` and customer `c1/Ada`. Later orders append
`o2/c1/500` while the customer snapshot stays unchanged. Full computation on
both orders yields two rows. An incremental algorithm may process only the new
order if it keeps the prior accepted row and uses the same reference state.
Test that its combined result equals full recomputation, including unique IDs.

If the customer name changes to `Grace`, the example recomputes both names
from the current snapshot, producing `o1/Grace/1200` and `o2/Grace/500`.
Customers is declared a snapshot input; it is read in full during incremental
execution. Orders must remain compatible with append-only processing. A
changed order schema or history needs a supported recompute decision; compare
schema before accepting the output, and bump semantic version when changing
the algorithm. Do not recover by blindly replaying already accumulated orders:
the duplicate-key business rule rejects that replay.

Run `python -B examples/pipelines/fixture_run.py` from this skill directory.
It verifies append/full equivalence, changed customer names, snapshot-style
recompute and duplicate replay rejection using the same reconciliation helper
as the transform. It does not execute Foundry's incremental planner, decorators
or transaction writes. Prepared runtime/enrollment verification must separately
show actual `ctx.is_incremental`, resolved histories, output schema and commit.

A PySpark implementation reading previous output must supply its exact schema
when previous data may be absent, with nullable fields matching Foundry's stored
schema. Schema mismatch fails the read; adding nullable fields or changing types
requires a planned full recompute/migration rather than ignoring the error.
The lifecycle choice below is application planning, not an SDK request schema:

```text
No prior output                 -> snapshot initialization
Compatible new orders only      -> incremental candidate, compare full result
Changed reference/schema/history -> recompute or supported explicit reconciliation
Required incremental impossible -> fail and investigate; do not hide a snapshot
```

For direct REST writes, navigate the [local SDK contracts](../rest-api.md) for
create, upload, commit, inspect and abort. Retain the actual transaction ID after
creation; a timed-out commit must be reconciled by reading that known
transaction, not by blindly creating another write. Method inputs and status
values belong to those local version-specific contracts.

## Expected result and checks

The plan identifies selected and resolved branches, input histories and the
reason for the computation mode. Output state matches full fixture computation
where required, preserves intended keys and uses current reference/schema
rules. A job's success is checked alongside transaction visibility and content;
swallowed write errors or no output write can produce an unintended empty
snapshot despite a successful job.

## Failures and recovery

If an incremental run cannot proceed, inspect driver logs and input/output
histories before changing configuration. Unsupported deletes, retention or
snapshot changes require a supported policy; enabling flags without checking
their runtime restrictions is unsafe. Duplicate append output requires correcting
state handling or a controlled snapshot recompute. An uncertain direct write
requires bounded status/effect reconciliation using its known identity. A
successful rebuild does not prove that unrelated downstream effects were undone.

Optional sources: [incremental usage](https://www.palantir.com/docs/foundry/transforms-python/incremental-usage),
[transform transactions](https://www.palantir.com/docs/foundry/transforms-python/transforms),
[dataset concepts](https://www.palantir.com/docs/foundry/data-integration/datasets),
[branching](https://www.palantir.com/docs/foundry/data-integration/branching).
