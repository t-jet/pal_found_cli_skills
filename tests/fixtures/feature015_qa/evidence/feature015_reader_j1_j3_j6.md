# Offline reader responses: J1, J3, J6

Reader input: isolated `pal-found-dev` skill, prepared synthetic fixtures and the J1/J3/J6 prompts. Public documentation and QA expected answers were not used. These are fixture decisions; no enrollment operation was performed.

## J1: Python orders and customers pipeline

### Capability and prerequisites

Use a Code Repository Python transform for a controlled join, tests, branch review and production build. Confirm the repository's `feature-orders` Git branch, input/output dataset RIDs and data branches, order/customer schemas, required check `ci/foundry-publish`, reviewer/owner, build context, and prepared transforms/plugin versions. `transform.using` needs `transforms >=3.68.0` and `transformsLangPythonPluginVersion >=1.978.0`; an older template needs a compatible supported API. The acting identity needs input reads, output writes and authorized merge/release/build operations. Local basis: [pipelines.md, “Follow the output through delivery”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/pipelines.md#follow-the-output-through-delivery), [python-transforms.md, “Prerequisites”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/pipelines/python-transforms.md#prerequisites), [releases.md, “Prerequisites”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/pipelines/releases.md#prerequisites).

### Ordered work and adaptable example

1. Define one output row per unique `order_id`; require a unique `customer_id` in the customer reference. Reject missing customer references, duplicate keys and negative amounts unless the business owner changes the rule. Keep output schema explicit.
2. Put reusable `build_orders` rules in the repository package and bind prepared `Input`/`Output` resources with the chosen Python transform API. For the supplied small fixture, the local `single_node_transform.py` uses `input.pandas()` and `output.write_table`. Use its declared `Check(E.primary_key("order_id"), ..., on_error="FAIL")` and non-null customer-name expectation where the prepared runtime supports them. A Spark scale choice uses the separate `transform_df` variant and Spark tests.
3. Run fixture and repository tests; preview `feature-orders` against the intended input branches, inspect schema and joined rows. Repair the failing expectation/fixture, rerun checks for the exact commit, get review, then merge or release through configured protected-branch rules.
4. Build production dataset context and inspect build/jobs, resolved upstream branches, committed output transaction, rows/schema/freshness and consumer health before declaring delivery.

Example input `o1,c1,1200` joined to `c1,Ada` yields `o1,c1,Ada,1200`. The supplied local fixture also rejects duplicate keys, missing customers and negative amounts. `python -B examples/pipelines/fixture_run.py` passed: joined row, empty input and four rejected inputs. Local basis: [python-transforms.md, “Worked example”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/pipelines/python-transforms.md#worked-example), [testing.md, “Procedure”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/pipelines/testing.md#procedure), [releases.md, “Procedure”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/pipelines/releases.md#procedure).

### Checks, recovery and boundary

Preview success is sample execution only. A `FAIL` expectation or `ci/foundry-publish` failure blocks release; neither production output nor committed visibility can be claimed. Keep the failing report tied to its revision, repair code/reference data or the expectation's real cause, rerun fixture and repository checks, obtain review and rebuild. Do not downgrade `FAIL` to `WARN` without a policy decision. Local fixture ran offline; preview, checks, merge/release and production build remain authorized enrollment steps. Local basis: [testing.md, “Expected result and checks” and “Failures and recovery”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/pipelines/testing.md#expected-result-and-checks), [releases.md, “Failures and recovery”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/pipelines/releases.md#failures-and-recovery).

## J3: Customer totals in SQL and a workspace

### Capability and prerequisites

Use a batch Spark SQL transform in a SQL Code Repository for the maintained dataset; use a Jupyter Code Workspace for interactive exploration and an explicitly published notebook transform. Record exact case-sensitive dataset paths/RIDs, data branches, readable schemas, unique customer keys, output location, workspace aliases, prepared pandas environment and authorized publishing rights. Repository SQL does not provide incremental state. A notebook's sandbox output is a separate state from CI, published transform and built branch output. Local basis: [sql.md, “Concept and lifecycle” and “Prerequisites”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/pipelines/sql.md#concept-and-lifecycle), [workspaces.md, “Concept and lifecycle” and “Prerequisites”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/pipelines/workspaces.md#concept-and-lifecycle).

### Ordered work and adaptable examples

1. Reject a duplicate customer key before either join. The prepared orders `(c1,10.00),(c1,7.50),(c2,NULL)` and customers `(c1,West),(c2,East)` require the explicit rule `NULL` amount contributes zero. Expected totals: `(c1,West,17.50,2)` and `(c2,East,0.00,1)`.
2. In the SQL repository, declare source datasets and output. Adapt exact tenant paths in this batch CTAS; omit a trailing semicolon and keep aliases/case exact:

```sql
CREATE TABLE `/Demo/customer_totals` AS
SELECT o.customer_id AS customer_id, c.region AS region,
       CAST(SUM(COALESCE(o.amount, 0)) AS DECIMAL(12,2)) AS total_amount,
       COUNT(*) AS order_count
FROM `/Demo/orders` o
JOIN `/Demo/customers` c ON o.customer_id = c.customer_id
GROUP BY o.customer_id, c.region
```

3. Preview on intended data branches; inspect values and Spark schema. Save, run repository checks, obtain review/publish, then build and verify committed output transaction and contents on the production data branch.
4. In Jupyter, register `orders`, `customers` read aliases and `customer_totals` output alias in Data. From a fresh kernel, read registered datasets through `Dataset.get(alias).read_table(format="arrow").to_pandas()`, check customer key uniqueness, join on `customer_id`, fill missing amount with zero, group by `customer_id,region`, sum amount/count rows, then `Dataset.get("customer_totals").write_table(totals)`. Inspect the sandbox result. Select the output's blue Build icon, verify inferred input/output bindings, then Sync and run; wait for publishing CI and a successful transform build on the selected branch.

The supplied SQL fixture passed arithmetic in SQLite; the workspace fixture passed pandas computation. These checks do not establish Foundry Spark grammar, workspace publication or live data permissions. Local basis: [sql.md, “Procedure,” “Worked example,” and “Expected result and checks”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/pipelines/sql.md#procedure), [workspaces.md, “Procedure,” “Worked example,” and “Expected result and checks”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/pipelines/workspaces.md#procedure).

### Checks, recovery and boundary

A duplicate `c1` customer row multiplies joined orders; reject it before aggregation rather than masking with `DISTINCT`. A visible workspace sandbox output proves only interactive computation. With publishing CI pending, notebook transform publication and production output remain pending. For wrong totals, inspect join cardinality, null policy, branches and case-sensitive paths. For a wrong workspace branch, compare branch selection, pinned inputs and sandbox path before rebuilding. Only authorized enrollment access can run repository preview/checks, workspace synchronization and production builds. Local basis: [sql.md, “Failures and recovery”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/pipelines/sql.md#failures-and-recovery), [workspaces.md, “Failures and recovery”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/pipelines/workspaces.md#failures-and-recovery).

## J6: Compute Module score operation

### Capability and prerequisites

Use Function mode with no platform permissions for pure `score(amount,factor)`; use application permissions only if calls require a service-user identity, or Pipeline mode for declared input/output processing and job provenance. Prepare a matching image architecture, cached Python base/wheels, exact `foundry-compute-modules` SDK, approved Artifact repository, resource queue, module configuration and execution identity. Function registration uses real SDK `add_functions` and `start_compute_module`; a generic HTTP server is not the worker protocol. Local basis: [compute/lifecycle.md, “Concept and lifecycle,” “Prerequisites,” and “Procedure”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/compute/lifecycle.md#concept-and-lifecycle), [compute/execution.md, “Concept and lifecycle”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/compute/execution.md#concept-and-lifecycle).

### Ordered work and adaptable example

1. Put pure score logic in `logic.py` and typed `score(context,event)` adapter in `app.py`; register it through the prepared SDK. Local fixture input `{"amount":12,"factor":3}` yields `36`; a negative value is rejected.
2. Build the provided Dockerfile locally with prepared assets (`docker build --pull=false --network=none -t compute-score:demo .` from example directory); inspect image architecture, numeric user, command and digest. Upload through the enrollment's authorized Artifact registry, create/configure Module with the exact image, resource limits and chosen Function mode, then start and inspect replicas.
3. Import the discovered `score` Function only after a responsive module. Test invocation and result schema separately from image pull, start and probe readiness. For Pipeline mode instead, declare dataset/stream/media aliases and parse the mounted `RESOURCE_ALIAS_MAP` (`rid`, nullable `branch`) and `BUILD2_TOKEN` paths. Record job identity, branch, lineage and committed output if the workload writes data.
4. Configure a Data Connection Source with project/reference, import allowance, API name and exact network policy when the module needs outbound connectivity. Confirm the acting service user or pipeline job token separately has resource permission. Run a bounded permitted read before processing; never place token/secret in image.

The supplied `python -B examples/compute/verify_fixture.py` passed pure calculation, invalid input, binding-map checks and a fake-session bounded stream adapter. It made no network call and did not build or deploy an image. Local basis: [compute/lifecycle.md, “Worked example” and “Expected result and checks”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/compute/lifecycle.md#worked-example), [compute/execution.md, “Procedure” and “Worked example”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/compute/execution.md#procedure), [compute/integration.md, “Prerequisites” and “Procedure”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/compute/integration.md#prerequisites).

### Checks, recovery and boundary

Source denial: check Source project/reference, import setting, destination hostname/network policy, TLS trust, then the module identity's grants and app restrictions. A failed readiness probe removes query routing; inspect initialization logs and probe command/timeout, while a liveness failure can restart the instance. Neither probe proves `score=36` or a durable dataset write. Bound external calls with supported timeouts; after an uncertain write, inspect effect/transaction before replay. Local authoring/fixture checks work without public internet. Image push, module deployment, Source policy, identity grants and live invocation need authorized enrollment and possibly administrator action. Local basis: [compute/lifecycle.md, “Failures and recovery”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/compute/lifecycle.md#failures-and-recovery), [compute/execution.md, “Failures and recovery”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/compute/execution.md#failures-and-recovery), [compute/integration.md, “Expected result and checks” and “Failures and recovery”](../../pal_found_cli_skills/.agents/skills/pal-found-dev/references/compute/integration.md#failures-and-recovery).
