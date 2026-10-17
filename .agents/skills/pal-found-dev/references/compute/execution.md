# Execution modes and provenance

[Ontology and Compute topics](../ontology-compute.md) · [Development guide](../../SKILL.md)

## Concept and lifecycle

| Mode | Work and identity | Completion evidence |
| --- | --- | --- |
| Function, no platform permissions | Registered request/response logic; no Foundry API/OSDK access. External egress can be configured separately. | Invocation result under the deployed function schema. |
| Function, application permissions | Uses the application's service user; access stays the same across callers. Availability depends on enrollment. | Invocation result plus verification of intended resource effects. |
| Pipeline | Non-interactive processing; build system supplies declared inputs/outputs and scoped job access. | Job identity, declared resource provenance and independently verified resource effects. |

Pipeline supported configured resources include datasets, streaming datasets and media
sets in the module's project. Job-token and alias-map file paths arrive through
`BUILD2_TOKEN` and `RESOURCE_ALIAS_MAP`. Alias entries contain `rid` and nullable
`branch`; the documented fallback is `master`. Select branches explicitly when that
fallback is inappropriate. Pipeline mode does not receive Query calls.

## Prerequisites

Declare workload, mode, expected branch, permitted resources and durable outcome.
Prepare image/queue as in [lifecycle](lifecycle.md). For application access, identify
the service user and exact resource grants; for pipeline access, configure each input
and output alias. [Sources](integration.md) separately permit network destinations.

Locally you can validate binding maps and pure logic. Grant verification, mounted job
credentials, start/build/lineage checks and actual writes require enrollment access.
Administrators authorize service-user/OAuth restrictions and missing resource access.
Never treat the caller's successful manual read as proof of module identity access.

## Procedure

1. Choose Function mode for application calls and Pipeline mode for autonomous
   processing requiring build provenance. Capture the expected resource effects.
2. Configure Function permission mode or pipeline input/output aliases in Configure.
   Validate their RIDs/branches before execution. Do not hardcode a personal token.
3. For pipeline startup, read the token from its mounted file and parse the alias map.
   Fail on absent or malformed required bindings before making an external call.
   The [binding helper](../../examples/compute/bindings.py) accepts the runtime paths;
   its fixture uses synthetic file contents, never real credentials.
4. Set replica bounds and concurrency to expected use. Function concurrency is per
   replica; `replicas × concurrency` is simultaneous capacity, not a latency promise.
   Load thresholds and delays govern autoscaling. Pipeline modules receive no queries
   and can scale to zero; use minimum one when continuous processing must remain active.
5. Observe workload completion and output state. Batch dataset writes through REST
   require explicit transaction creation, file upload and commit using the
   [local REST contracts](../rest-api.md). Verify the transaction reports `COMMITTED`
   before accepting downstream batch consumption. Container readiness, process exit
   and stream acknowledgments establish no global dataset transaction guarantee.

## Worked example

Illustrative configuration: pipeline aliases `incoming` and `outgoing`, each pointing
to an approved project resource on branch `demo`. A mounted map is shaped as:

```json
{
  "incoming": {"rid": "ri.foundry.main.dataset.INPUT", "branch": "demo"},
  "outgoing": {"rid": "ri.foundry.main.dataset.OUTPUT", "branch": "demo"}
}
```

The RIDs are placeholders. Obtain actual values from the configuration resource picker.
`load_bindings` returns token and normalized bindings; code should pass the configured
branch to the chosen resource operation. Use [local REST contracts](../rest-api.md)
for dataset/media operations and their request/result handling. The map conveys
bindings and permission scope; it does not itself read or write records.

For a continuously running stream processor, define durable offsets/deduplication
and output reconciliation before repeating reads. A tutorial that repeatedly reads
latest records is insufficient evidence of exactly-once processing. A function-based
calculation with no resource access can use the worksheet in [lifecycle](lifecycle.md).

The [bounded stream adapter](../../examples/compute/pipeline.py) reads a `records`
array with `value.x` integers and posts `{"twice_x": x * 2}` to `jsonRecord`, following
the documented stream-proxy contract. Prepare `requests`, two streaming resources
with those schemas, the Source, mounted token/map and CA trust. Package `pipeline.py`
and `bindings.py` in the image, and choose `python pipeline.py` as its command instead
of the function worker. `FOUNDRY_URL` is the bare configured hostname;
`REQUEST_TIMEOUT` bounds each socket wait, default 30 seconds. The adapter streams
and rejects responses above 64 KiB or 100 records before writes, and checks a 60-second
elapsed budget between operations/chunks. This cooperative deadline cannot preempt
an in-progress socket operation; its timeout bounds that wait. One pass exits after
acknowledged writes; it supplies no durable cursor or exactly-once guarantee and is
for an isolated demonstration stream. Inspect partial output on any failure before
running again. Acknowledgment does not establish pipeline transaction completion.

## Expected result and checks

Fixture success establishes correct binding parsing and rejects a missing output.
Live evidence identifies input/output branch, image revision, job identity and lineage.
Running continuously is pending processing, not a completed batch transaction.
After a timeout, inspect output effects and last processed position before resuming.

Compute usage accrues while replicas start or run, including idle active replicas.
Allocation, replica count and active time affect usage; zero active/starting replicas
consume none. Minimum zero can still scale up for deployment or predicted load.
Use the enrollment's contractual rates for budgeting, not a hardcoded public price.

## Failures and recovery

| Observation | Diagnosis and next step |
| --- | --- |
| Function call expects caller-scoped access | Reassess service-user grants and application policy; do not substitute caller credentials. |
| Binding missing | Fix configured input/output alias and redeploy; never guess the RID. |
| Network denied despite resource grant | Inspect Source network policy in [integration](integration.md). |
| Continuous processor stopped | Inspect replica minimum and logs before resuming from a reconciled position. |
| Output still uncommitted | Inspect the explicit dataset transaction and commit result; preserve the previous committed output until the intended transaction is COMMITTED. |
| Unknown write outcome | Reconcile records/transaction before replay; duplicates are possible without durable protection. |

Optional source attribution: [execution modes](https://www.palantir.com/docs/foundry/compute-modules/execution-modes),
[scaling](https://www.palantir.com/docs/foundry/compute-modules/scaling),
[usage](https://www.palantir.com/docs/foundry/compute-modules/usage).
