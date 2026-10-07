# v2 orchestration: Schedule, continued

[Resource overview](Schedule.md) | [Client behavior](../../client-behavior.md)

### runs

Read recent runs for the selected schedule. Default page size is 100 when omitted; bound
pages/items independently and correlate run identities with intended submissions.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/Schedule/runs.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/Schedule/runs.py):

```bash
python -B examples/rest/075/v2/orchestration/Schedule/runs.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

No named operation failures are declared by this frozen SDK method. Generic API,
authentication, transport and decoding failures remain possible; preserve the error
envelope and request identity rather than inventing a domain-specific exception.

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### unpause

Unpause the confirmed schedule and inspect its state/configuration. Confirm that
resuming recurring work is intended; an unpause response does not prove any particular
run has completed.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/Schedule/unpause.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/Schedule/unpause.py):

```bash
python -B examples/rest/075/v2/orchestration/Schedule/unpause.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| UnpauseSchedulePermissionDenied | Could not unpause the Schedule. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
