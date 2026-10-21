# v2 data_health: CheckReport

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

A CheckReport is an evaluation result for a health check. A particular report and the
latest reports answer different questions. Read the result and its evaluation context
before deciding whether current data meets application requirements.

## Prepare the application

Use prepared SDK 1.101.0 and an authorized identity for the intended enrollment. Resolve
the resource identities and complete request models linked below before calling a
method. Offline fixtures use synthetic identities and an actual SDK HTTP transport; they
need prepared Python, SDK and httpx and contact no enrollment.

Verify the application grants, resource permissions and capability enablement in the
tenant. SDK source does not enumerate a universal role or scope for every operation;
operation-specific documented requirements below take precedence. Source does not
provide a universal idempotency guarantee. For uncertain writes, retain request identity
and reconcile through authorized reads before repeating.

## Operations and outcome checks

### get

Read a report by RID and inspect its evaluation result and context. Distinguish a
historical report from the latest assessment.

[Exact parameters, request, result and error models](../../contracts/v2/data_health/CheckReport/get.md).

[Executable SDK example](../../../../examples/rest/075/v2/data_health/CheckReport/get.py):

```bash
python -B examples/rest/075/v2/data_health/CheckReport/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CheckReportNotFound | The given CheckReport could not be found. |
| CheckTypeNotSupported | The type of the requested check is not yet supported in the Platform API. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_latest

Read recent reports for the selected check in reverse chronological order. Bound
retrieval and compare evaluation context before using the latest report for a decision.

[Exact parameters, request, result and error models](../../contracts/v2/data_health/CheckReport/get_latest.md).

[Executable SDK example](../../../../examples/rest/075/v2/data_health/CheckReport/get_latest.py):

```bash
python -B examples/rest/075/v2/data_health/CheckReport/get_latest.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CheckNotFound | The given Check could not be found. |
| CheckTypeNotSupported | The type of the requested check is not yet supported in the Platform API. |
| GetLatestCheckReportsPermissionDenied | Could not getLatest the CheckReport. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
