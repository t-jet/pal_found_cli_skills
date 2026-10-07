# Repository authoring and review

[Pipeline guide](../pipelines.md) | [Development guide](../../SKILL.md)

## Concept and lifecycle

Code Repositories holds source and its Git history. A transform definition
declares data dependencies; pipeline registration makes it discoverable to
Foundry. A commit records code. Checks, a reviewed merge, artifact publication
and an output build are separate steps with different evidence.

| Repository area | Use it to establish |
| --- | --- |
| Code | File/package location, source changes and selected branch. |
| Branches | Base and working branches; identify the intended merge target. |
| Tags | Named code revisions used by the repository's release convention. |
| Pull Requests | Proposed comparison, reviewer discussion and merge decision. |
| Checks | Build/test/check results for the relevant commit. |
| Settings | Applicable branch protections, repository configuration and artifacts. |

## Prerequisites

Obtain a repository, intended base/target branch, authorized input datasets and
output location, schema examples, prepared Python environment and permission
to edit that repository and create/update its output. Branch protection and
review policy may restrict merge or release to designated identities.
Local fixtures and source editing need only prepared tools. Repository UI,
tenant preview, checks, merge, publication and builds need enrollment access.
Administrator-controlled configuration must be confirmed by its owner.

## Procedure

1. Open Code and verify the displayed branch. Open Branches to create or select
   a working branch based on the intended target; record its exact name.
2. Identify the Python package and registration entry point from the existing
   template. Keep transform modules, shared business logic and tests separate.
3. Add declared inputs/outputs and the transform implementation. Register its
   module through `Pipeline.discover_transforms` or explicit `add_transforms`.
   Discovery imports modules, so keep external calls and other side effects
   inside the compute function rather than at module import time.
4. Preview the selected transform on the intended branch/context. Inspect
   schema and sample results; record limits and resolved inputs. Continue with
   [tests and expectations](testing.md) before production release.
5. Commit the change. In Checks, inspect results for that exact commit rather
   than an older successful revision. Resolve failed checks before proposing
   release.
6. Open a pull request against the intended target. Review code, dataset
   contracts, tests, security effects and migration/recompute needs. Apply
   branch protections from Settings and obtain required approvals.
7. Merge only the reviewed revision. Follow the repository's artifact/tag
   convention and [production release](releases.md), then inspect output builds.

## Worked example

Illustrative package layout:

```text
myproject/
  pipeline.py
  datasets/
    __init__.py
    orders.py
  rules.py
tests/
  test_orders.py
```

`orders.py` defines the transform. `rules.py` holds the tested business
function. A registration file for module-level transform discovery is:

```python
from transforms.api import Pipeline
import myproject.datasets

my_pipeline = Pipeline()
my_pipeline.discover_transforms(myproject.datasets)
```

`myproject` is an illustrative package name. Preserve the entry-point naming
and configuration supplied by the repository template. Adapt the
[complete transform example](python-transforms.md) to those package paths.
For a working branch `feature/order-quality` based on the actual production
target, record the commit, passing checks, reviewed pull request, merged
revision and resulting output build ID. Do not assume `master` is the target.

## Expected result and checks

The transform is discoverable with the intended dependencies, tests cover its
business rules, and checks reference the proposed revision. Merge evidence
identifies the reviewed target. Delivery evidence additionally identifies the
produced output, branch, committed data and successful build. A tag or merge
alone does not prove fresh production data.

## Failures and recovery

If a transform is missing, check package/module registration, imports and
duplicate output declarations. If discovery causes a network call or writes a
resource, move that effect out of module import. A protected branch rejection
requires the configured review/check process, not a force push. A successful
preview with a failed check blocks release until the underlying failure is
understood. If merge succeeds but output remains stale, investigate release
selection and the output build using [production operations](../operations.md).

Optional sources: [repository navigation](https://www.palantir.com/docs/foundry/code-repositories/navigation),
[pipeline registration](https://www.palantir.com/docs/foundry/transforms-python/pipelines),
[branch settings](https://www.palantir.com/docs/foundry/code-repositories/branch-settings),
[transform preview](https://www.palantir.com/docs/foundry/code-repositories/preview-transforms).
