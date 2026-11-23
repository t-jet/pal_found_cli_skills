# v2 orchestration: Build

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

A Build groups orchestration work performed by jobs. Submission, job execution and
cancellation acknowledgement are separate states. A successful cancellation request does
not immediately change build status and cannot undo jobs that finished before
cancellation.

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

## Wait for a submitted build

Once `client.orchestration.Build.create` returns a build RID for the intended
target and branch, use the public `client.orchestration.Build.get` route to
observe the terminal result. The caller must construct the `BuildTarget`
variant from the linked create contract; a dataset transaction commit alone
does not imply a Build was submitted. The status enum is `RUNNING`,
`SUCCEEDED`, `FAILED`, or `CANCELED`.

```python
from time import monotonic, sleep

deadline = monotonic() + 120
while True:
    remaining = deadline - monotonic()
    if remaining <= 0:
        raise TimeoutError(f"Build {build_rid} status remains uncertain")
    build = client.orchestration.Build.get(
        build_rid, request_timeout=min(10, max(1, int(remaining))),
    )
    if build.status == "SUCCEEDED":
        break
    if build.status in {"FAILED", "CANCELED"}:
        raise RuntimeError(f"Build {build_rid} ended {build.status}; inspect jobs")
    sleep(min(2, max(0, deadline - monotonic())))
```

`FAILED` and `CANCELED` are unsuccessful terminal results. Record the build
RID and status, then check the selected dataset branch before correcting and
resubmitting. Job diagnostics are a separate optional step. Read at most five
pages and 500 jobs when investigating a failed or canceled build:

```python
jobs = []
page_token = None
seen_tokens = set()
for _ in range(5):
    page = client.orchestration.Build.jobs(
        build_rid, page_size=100, page_token=page_token, request_timeout=30,
    )
    jobs.extend(page.data)
    if len(jobs) > 500:
        raise RuntimeError(f"Build {build_rid} job count exceeds the review limit")
    next_token = page.next_page_token
    if not next_token:
        break
    if next_token in seen_tokens:
        raise RuntimeError(f"Build {build_rid} repeated a jobs page token")
    seen_tokens.add(next_token)
    page_token = next_token
else:
    raise RuntimeError(f"Build {build_rid} has more jobs pages than the review limit")
```

Read the returned `ResourceIterator` page through `.data` and
`.next_page_token`; iterating it would fetch more pages outside these bounds.
The build status check above does not need jobs. A timeout means the outcome is unknown;
read the same build RID later instead of creating a duplicate. Per-call
timeouts are positive integers in SDK 1.101.0, so a final call can exceed
the application deadline by less than one second. The two-second poll interval
stays under the documented four-requests-per-second limit. The
[staged dataset procedure](../datasets/Transaction.md) separately verifies
file visibility before and after commit. Its
[offline composed fixture](../../../../examples/rest/074/v2/datasets/staged_commit_journey.py)
checks `SUCCEEDED`, `FAILED`, `CANCELED`, two-poll exhaustion and lost upload or
commit replies with a synthetic transport. Those checks do not submit a tenant build.

### cancel

Request cancellation of unfinished jobs, then inspect build/job state within a finite
deadline. Acknowledgement is asynchronous and the build may already have finished or
finish before cancellation takes effect.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/Build/cancel.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/Build/cancel.py):

```bash
python -B examples/rest/075/v2/orchestration/Build/cancel.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CancelBuildPermissionDenied | Could not cancel the Build. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### create

Construct a build request for the intended resources and configuration, then preserve
the returned build identity. Inspect jobs and status with finite polling; submission is
not completion.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/Build/create.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/Build/create.py):

```bash
python -B examples/rest/075/v2/orchestration/Build/create.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CreateBuildPermissionDenied | Could not create the Build. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get

Inspect the selected build state. Respect the documented maximum of four requests per
second and 25 concurrent requests; bounded polling must also remain below these limits.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/Build/get.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/Build/get.py):

```bash
python -B examples/rest/075/v2/orchestration/Build/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| BuildNotFound | The given Build could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_batch

Read up to 100 builds per batch. Respect four requests per second and 25 concurrent
requests, then match returned identities to requested builds.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/Build/get_batch.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/Build/get_batch.py):

```bash
python -B examples/rest/075/v2/orchestration/Build/get_batch.py
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

### jobs

Enumerate jobs belonging to the selected build. Inspect each returned job state and
preserve partial continuation rather than declaring the build successful from job
presence.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/Build/jobs.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/Build/jobs.py):

```bash
python -B examples/rest/075/v2/orchestration/Build/jobs.py
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

### search

Search builds using the complete source-defined query model and bounded pages. Correlate
returned identities with the intended resources before using a candidate as submission
reconciliation.

[Exact parameters, request, result and error models](../../contracts/v2/orchestration/Build/search.md).

[Executable SDK example](../../../../examples/rest/075/v2/orchestration/Build/search.py):

```bash
python -B examples/rest/075/v2/orchestration/Build/search.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| SearchBuildsPermissionDenied | Could not search the Build. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
