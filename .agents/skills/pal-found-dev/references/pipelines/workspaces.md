# Workspace exploration and publication

[Pipeline topics](../pipelines.md) · [Development guide](../../SKILL.md)

## Concept and lifecycle

Code Workspaces provide repository-backed interactive environments. A notebook's
in-memory results, an interactive dataset write, a published code revision and a
built notebook transform are different deliverables. Publish through the workspace;
its backing repository is customized infrastructure and cannot publish transforms
directly. Select [Python transforms](python-transforms.md) for distributed Spark
processing; a Jupyter workspace runs on one machine.

## Prerequisites

Prepare a Jupyter Code Workspace, its supported Python environment and readable
schema-backed input. Add input/output aliases in the Data panel and grant the author
access to the workspace, backing repository and resources. Verify branch/fallback
selection. All imported data contributes to workspace security; losing permission
to one input can remove access to the workspace. Restricted views require restricted
outputs mode, which prevents derived output publication.

Local authoring and synthetic computation need no public access. Dataset registration,
reads, writes, synchronization, CI and builds require authorized enrollment connectivity.
Administrators supply missing libraries through approved package channels, resource
capacity and permission changes. A prepared managed environment includes its manifest
and lock; its libraries are restored for notebook transforms. With older unmanaged
environments, explicitly declare the transform's dependencies through the supported
workspace library mechanism; a successful interactive import alone is insufficient.

## Procedure

1. Select the workspace branch before reading or writing. Data normally follows that
   branch, falling back to `master`; use Data > dataset options > Pin dataset branch
   for reads when a fixed input branch is required.
2. Choose Data > Add > Read data, select the input and assign alias `orders`.
   Use the generated Arrow/pandas read snippet. Reduce large inputs before loading;
   data must fit the workspace memory. An alias binds a resource, not a filename.
3. Register a tabular write destination with alias `customer_totals`, confirming its
   branch and schema. Author the complete saved notebook below. Validate keys and
   values before calling its final write cell.
4. In Data, select the output's blue Build icon. Verify inferred notebook, input and
   output bindings; edit incorrect inference. Select Sync and run to synchronize
   configuration and run publishing CI. Once CI passes, verify the transform build.
5. Inspect Source control and use Sync changes to publish other code changes. Review
   and propose branch changes through the branch manager. Publication and merge
   follow the local [release procedure](releases.md).

## Worked example

Notebook cells below assume the two registered aliases and a prepared pandas/Arrow
environment. Input rows `(customer_id,amount)` are `(c1,10.00)`, `(c1,7.50)`,
`(c2,NULL)`. Illustrative IDs must be replaced with the enrollment's registered aliases.

```python
from foundry.transforms import Dataset

orders = Dataset.get("orders").read_table(format="arrow").to_pandas()
assert set(["customer_id", "amount"]).issubset(orders.columns)
assert orders["customer_id"].notna().all()
orders["amount"] = orders["amount"].fillna(0)
totals = orders.groupby("customer_id", as_index=False)["amount"].sum()
totals = totals.rename(columns={"amount": "total_amount"})
assert totals["customer_id"].is_unique
Dataset.get("customer_totals").write_table(totals)
```

Expected rows: `(c1,17.50)`, `(c2,0.00)`. This notebook uses a sum, not currency
rounding or a universal financial calculation; preserve suitable decimal types for
production money. A registered transform's interactive write uses a
`code-workspace-sandbox/` branch; its transform run updates the current branch.
Interactive tabular writes normally create one snapshot transaction per call;
a transform execution combines script writes into one transaction, snapshot by
default or append when incremental settings are configured.

The [notebook-equivalent asset](../../examples/workspaces/transform.py) has a
[synthetic check](../../examples/workspaces/verify_fixture.py). With prepared pandas,
run `python -B verify_fixture.py` in that example directory. The Dataset substitute
tests pandas computation only; it cannot establish grants, writes or publication.

## Expected result and checks

Check the saved notebook runs from a fresh kernel in cell order, with no hidden
variables. Inspect output column names/types and the two expected rows. Then compare
the published revision, CI outcome, transform JobSpec, selected branch and build's
committed output. An interactive sandbox result does not verify production output.
CI still running is pending; failed CI leaves publication incomplete even if the
interactive write already succeeded.

## Failures and recovery

| Observation | Diagnosis and next step |
| --- | --- |
| Alias missing | Register it in Data and verify RID/branch; do not guess file paths. |
| Memory exhaustion | Push down filters or choose a distributed transform; rerunning unchanged repeats failure. |
| Input access lost | Restore appropriate input access or remove that dependency through an authorized workflow. |
| Restricted output blocked | Retain restricted outputs protection; choose an authorized supported design. |
| Build import fails | Check the transform's actual managed environment/declared dependencies. |
| Wrong output branch | Compare workspace branch, input pin and sandbox write location before rebuilding. |
| External call in notebook transform | Use supported external transforms for that pipeline; interactive Sources do not enable notebook-transform calls. |

Optional source attribution: [workspace lifecycle](https://www.palantir.com/docs/foundry/code-workspaces/getting-started/index.html),
[dataset access and writes](https://www.palantir.com/docs/foundry/code-workspaces/data),
[notebook transforms and environments](https://www.palantir.com/docs/foundry/code-workspaces/jupyterlab).
