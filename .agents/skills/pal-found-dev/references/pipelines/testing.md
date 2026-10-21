# Tests and expectations

[Pipeline guide](../pipelines.md) | [Development guide](../../SKILL.md)

## Concept and lifecycle

Unit tests assess code with controlled inputs. Data expectations assess
properties of declared inputs or outputs during supported execution. A
`FAIL` expectation can fail the build; `WARN` records a warning. Repository
Preview runs on a sample without running checks or committing data. A good
sample therefore does not prove that expectations or production checks passed.
The documented repository Python unit-test path uses pytest for batch
pipelines, and does not support streaming pipelines.

## Prerequisites

Provide the selected compute runtime, source module, prepared pytest and
engine packages, representative schemas and deterministic test data.
Separate pure business functions from decorated entry points so tests can
exercise real logic without making a live resource call. Spark DataFrame tests
require the prepared Spark test environment and fixture. Palantir expectations
require matching transforms libraries; single-node expectation support has
limits compared with Spark. The source example checks below are documented
primary-key/non-null checks; verify prepared-runtime support before execution.

Local fixtures need no enrollment access. Repository checks and actual
expectation evaluation need its configured environment and authorized tenant
execution. Keep recorded platform check results distinct from fixture output.

## Procedure

Repository pytest checks need the testing plugin in the Python subproject's
`build.gradle` (library repositories use their root project):

```groovy
apply plugin: 'com.palantir.transforms.lang.pytest-defaults'
```

Use a `test` package below `src`, for example
`transforms-python/src/test/test_orders.py`. Pytest discovers `test_*.py` or
`*_test.py` files and `test_` functions. The already prepared local environment
can expose `.maestro/bin/pytest`; run that executable from the checkout when
available. Otherwise use the prepared repository interpreter/test command,
and report a missing environment rather than claiming tests ran.

1. Test row/schema contracts, empty input, nulls, duplicates and unmatched
   references using inputs small enough to inspect completely.
2. Assert full expected results rather than only row counts. Include an input
   that fails the intended business rule and assert its specific rejection.
3. Test engine operations in that engine's prepared test environment. For
   Spark, use DataFrames with explicit schemas and normalize result ordering.
4. Attach input/output expectations to the declared resources. Use a failing
   severity where a violated property must prevent publication of bad data.
5. Run prepared local tests. Then run repository checks for the exact commit
   and a supported preview/build path. Inspect the check/expectation report
   and repair rejected data or code before release.

## Worked example

The single-node transform calls the same `build_orders` function that the
[business fixture](../../examples/pipelines/fixture_run.py) exercises. In an
illustrative repository package, a pytest test is:

```python
import pytest
from myproject.rules import build_orders

def test_customer_join_and_duplicate_rejection():
    orders = [{"order_id": "o1", "customer_id": "c1", "total_cents": 1200}]
    customers = [{"customer_id": "c1", "customer_name": "Ada"}]
    assert build_orders(orders, customers) == [
        {"order_id": "o1", "customer_id": "c1", "customer_name": "Ada", "total_cents": 1200}
    ]
    with pytest.raises(ValueError, match="duplicate order_id"):
        build_orders(orders * 2, customers)
```

Adapt `myproject.rules` to the real package holding the shared function.
From its prepared project environment, invoke `python -B -m pytest` against
the selected test module. The standalone fixture can also run from this
skill's root with `python -B examples/pipelines/fixture_run.py`.

For an actual Spark test, use the repository's prepared `spark_session`
fixture with the [undecorated `shape_orders`](../../examples/pipelines/pyspark_transform.py)
helper. Create input DataFrames with the schemas in that file, assert the
selected schema and collected small test rows, and add duplicate/unmatched
customer cases. That test requires Spark and transforms imports; the pure
Python fixture does not substitute for it.

The [transform examples](python-transforms.md) attach
`Check(E.primary_key("order_id"), "Unique order key", on_error="FAIL")`
and a non-null customer-name check. In the Spark variant, duplicate customer
rows yield duplicate output order keys; an unmatched customer yields a null
name. Both should produce failed expectations in a supported build, rather
than a silently accepted output. Correct the reference data and rerun the
affected tests and build; verify the new expectation and output results.

## Expected result and checks

Tests assert the exact joined record and intended failure behavior. Repository
checks reference the tested commit. The build report identifies the evaluated
expectations, their severity and outcome; its output contents/schema match the
contract. Preview evidence is labeled sample execution and cannot establish
passing checks, materialized data or committed production state.

## Failures and recovery

An import/fixture error requires the matching prepared runtime or test
configuration. A changed result requires comparing schemas and business rules
before rewriting the assertion. A `FAIL` expectation requires repair and
reevaluation; changing it to `WARN` changes the data acceptance policy and
needs an explicit business decision. A successful test that never used the
real compute helper provides no evidence about that transform's logic.

Optional sources: [Python unit tests](https://www.palantir.com/docs/foundry/transforms-python/unit-tests),
[expectations](https://www.palantir.com/docs/foundry/transforms-python/data-expectations-getting-started),
[preview behavior](https://www.palantir.com/docs/foundry/code-repositories/preview-transforms).
