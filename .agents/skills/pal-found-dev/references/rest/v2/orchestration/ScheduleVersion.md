# v2 orchestration: ScheduleVersion

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

A ScheduleVersion identifies a version of schedule configuration. Use it to understand
which schedule definition a workflow refers to. Retrieving the associated schedule is
different from retrieving the version record.

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

Read a specific schedule-version record and inspect its configuration identity. Use it
when explaining which version a workflow references.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/ScheduleVersion/get.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/ScheduleVersion/get.py):

```bash
python -B examples/rest/075/v2/orchestration/ScheduleVersion/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| ScheduleVersionNotFound | The given ScheduleVersion could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### schedule

Retrieve the schedule associated with the selected version. Compare identities with the
intended schedule before acting on its current configuration.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/ScheduleVersion/schedule.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/ScheduleVersion/schedule.py):

```bash
python -B examples/rest/075/v2/orchestration/ScheduleVersion/schedule.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

No named operation failures are declared by this frozen SDK method. Generic API,
authentication, transport and decoding failures remain possible; preserve the error
envelope and request identity rather than inventing a domain-specific exception.

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
