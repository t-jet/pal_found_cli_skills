# Local Python development

[Pipeline guide](../pipelines.md) | [Development guide](../../SKILL.md)

## Concept and lifecycle

Local source editing, local fixture tests, local real-data preview and hosted
preview are different operations. Local preview can stream authorized Foundry
inputs into local memory. A hosted VS Code workspace keeps computation on
Palantir infrastructure, apart from displayed preview results. Both require
the relevant prepared environment; a local editor alone cannot provide tenant
execution, credentials or missing runtime packages.

Code Repositories Preview always runs a transform nonincrementally, including
when `require_incremental=True`. VS Code Preview respects incremental behavior
with v1/v2 semantics for Spark and lightweight transforms. Choose VS Code
Preview or authorized builds when validating actual incremental state; a
repository snapshot preview cannot establish incremental correctness.

## Prerequisites

Use an already prepared repository checkout, interpreter, dependency set and
Palantir VS Code tooling. Confirm the runtime APIs used by the source example.
For local real-data preview, administrators must enable local preview and the
caller needs download operations `s3-proxy:datasets-read` and
`api:datasets-read` on every input. Hosted Code Workspaces must be enabled and
the identity needs access to the repository and data. Organizational rules
determine whether data may leave the platform.

Pure business fixtures can run without public or enrollment connectivity.
Tenant-backed preview, repository synchronization, remote checks and builds
need authorized enrollment access. Missing tools, credentials, bindings or
enabled capabilities block their particular steps and have provisioning owners.

## Procedure

1. Verify the checkout/repository, working Git branch and intended dataset
   context. Record interpreter and dependencies; compare them with the
   repository environment rather than using an unrelated system interpreter.
2. Author the transform and shared tests. Run deterministic local fixtures
   without reaching public endpoints or reading live data unexpectedly.
3. If real-data preview is permitted, open the prepared Palantir preview
   tooling for the selected transform and verify its resolved input resources
   and sample. Confirm the data handling boundary before local execution.
4. If local download is prohibited, use the enabled hosted workspace or
   tenant repository Preview path. In Code Repositories, choose Preview from
   the code editor options or helper panel. For file inputs, choose the sample
   files initially; inputs can be reconfigured before another preview.
5. Inspect output/schema and logs. Preview does not commit datasets or run
   checks. Commit and perform [tests](testing.md) and [release](releases.md)
   separately through the authorized repository workflow.

## Worked example

An analyst has the prepared source, interpreter and synthetic tables for
`orders_clean`, but no enrollment connection. Run:

```bash
python -B examples/pipelines/fixture_run.py
```

from this skill's root. The output confirms the shared join rules and four
rejected inputs. Record those fixture results and the version of the prepared
interpreter. Actual preview, repository checks and output build remain pending.

Later, enrollment access becomes available but input download is prohibited.
Open the repository in the enabled hosted environment; select the intended
branch and transform, run tenant Preview and inspect the customer join. Then
run the configured repository checks and authorized release/build steps.
The hosted path does not grant data access that the identity lacks.

## Expected result and checks

The plan names the local interpreter, dependencies, branch and data boundary.
Its evidence distinguishes fixture output, tenant sample output, check results
and committed production output. A missing tool or denied download is recorded
as a prerequisite/permission failure, rather than replaced by public reading
or reported as a successful preview.

## Failures and recovery

If a library/API is absent, compare the prepared runtime with the declared
template and identify the missing artifact/version. If tenant preview is
denied, distinguish authentication, resource permission and local-download
enablement. If local tests pass but a tenant build fails, compare actual
schemas, branch fallback, dependencies, identity and compute resources before
altering business logic. Reuse permitted fixtures while the live step is
blocked; they cannot demonstrate production execution.

Optional sources: [local Python development](https://www.palantir.com/docs/foundry/transforms-python/local-development),
[local versus hosted VS Code](https://www.palantir.com/docs/foundry/vs-code/local-vs-workspace-guide),
[repository Preview](https://www.palantir.com/docs/foundry/code-repositories/preview-transforms).
