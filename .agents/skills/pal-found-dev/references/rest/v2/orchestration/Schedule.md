# v2 orchestration: Schedule

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Schedules define recurring orchestration work, with versions and runs. User-scoped
output discovery depends on the user's current permissions; later permission changes can
alter outputs or cause failure. Project-scoped schedules avoid that particular user-
permission dependency.

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

[Detailed worked procedure](Schedule-worked.md).

## Operations and outcome checks

### create

Create the intended recurring work with a reviewed scope and configuration. User-scoped
discovery can change when user permissions change; consider project-scoped configuration
for predictable resource boundaries.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/Schedule/create.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/Schedule/create.py):

```bash
python -B examples/rest/075/v2/orchestration/Schedule/create.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CreateSchedulePermissionDenied | Could not create the Schedule. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### delete

Confirm schedule identity and intended removal, then delete it. Review outstanding runs
separately rather than assuming deletion cancels already submitted work.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/Schedule/delete.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/Schedule/delete.py):

```bash
python -B examples/rest/075/v2/orchestration/Schedule/delete.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| DeleteSchedulePermissionDenied | Could not delete the Schedule. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get

Inspect the selected schedule's configuration before replacing, pausing or running it.
Preserve its RID for follow-up instead of selecting by name alone.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/Schedule/get.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/Schedule/get.py):

```bash
python -B examples/rest/075/v2/orchestration/Schedule/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| ScheduleNotFound | The given Schedule could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_affected_resources

Inspect affected resources for the schedule using the source response model. Compare
them with the intended orchestration boundary before initiating work.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/Schedule/get_affected_resources.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/Schedule/get_affected_resources.py):

```bash
python -B examples/rest/075/v2/orchestration/Schedule/get_affected_resources.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| GetAffectedResourcesSchedulePermissionDenied | Could not getAffectedResources the Schedule. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_batch

Read up to 1000 schedules per batch. Missing or inaccessible schedules are omitted;
reconcile requested IDs and report unknown configuration explicitly.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/Schedule/get_batch.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/Schedule/get_batch.py):

```bash
python -B examples/rest/075/v2/orchestration/Schedule/get_batch.py
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

### pause

Pause the confirmed schedule, then inspect its resulting state. Treat existing submitted
runs separately; source does not promise that pause cancels running work.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/Schedule/pause.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/Schedule/pause.py):

```bash
python -B examples/rest/075/v2/orchestration/Schedule/pause.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| PauseSchedulePermissionDenied | Could not pause the Schedule. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### replace

Read configuration and replace it with the intended schedule definition. User-scoped
discovery depends on current user permissions; verify scope, outputs and returned
configuration after replacement.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/Schedule/replace.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/Schedule/replace.py):

```bash
python -B examples/rest/075/v2/orchestration/Schedule/replace.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| ReplaceSchedulePermissionDenied | Could not replace the Schedule. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### run

Start one explicit run and retain the returned ScheduleRun identity. Read run/build/job
state within finite poll budgets; a lost submission response must be reconciled before
another run.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/Schedule/run.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/Schedule/run.py):

```bash
python -B examples/rest/075/v2/orchestration/Schedule/run.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| RunSchedulePermissionDenied | Could not run the Schedule. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

## More operations

- [Part 2](Schedule-2.md)
