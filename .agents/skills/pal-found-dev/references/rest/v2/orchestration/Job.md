# v2 orchestration: Job

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

A Job is execution work associated with orchestration. Read job metadata and returned
status to distinguish submitted, running and completed work. Job retrieval is
observational and does not start, retry or cancel a job.

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

Read the intended job and inspect its status/result. Respect four requests per second
and 25 concurrent requests when polling.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/Job/get.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/Job/get.py):

```bash
python -B examples/rest/075/v2/orchestration/Job/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| JobNotFound | The given Job could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_batch

Read up to 500 jobs per batch, within four requests per second and 25 concurrent
requests. Match returned IDs before summarizing build outcomes.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/Job/get_batch.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/Job/get_batch.py):

```bash
python -B examples/rest/075/v2/orchestration/Job/get_batch.py
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
