# v2 checkpoints: Record

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Checkpoint records expose processing checkpoints by identity and searchable criteria. A
governance or recovery application can inspect records without assuming that a
checkpoint record proves every downstream job succeeded. Preserve returned identities
for follow-up.

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

Read a checkpoint record by its ID and inspect its returned processing context. Preserve
record identity when correlating with application recovery state.

[Exact parameters, request, result and error models](../../contracts/v2/checkpoints/Record/get.md).

[Executable SDK example](../../../../examples/rest/075/v2/checkpoints/Record/get.py):

```bash
python -B examples/rest/075/v2/checkpoints/Record/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CheckpointRecordNotFound | The checkpoint record could not be found. |
| CheckpointRecordPermissionDenied | The caller does not have permission to access the checkpoint record. |
| RecordNotFound | The given Record could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_batch

Retrieve up to 100 checkpoint records per batch. Missing or inaccessible records are
omitted; reconcile requested IDs and explicitly report unresolved records.

[Exact parameters, request, result and error models](../../contracts/v2/checkpoints/Record/get_batch.md).

[Executable SDK example](../../../../examples/rest/075/v2/checkpoints/Record/get_batch.py):

```bash
python -B examples/rest/075/v2/checkpoints/Record/get_batch.py
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

Search with the source-defined checkpoint query model. Inspect returned records and
bounded continuation before concluding that a processing checkpoint exists or is absent.

[Exact parameters, request, result and error models](../../contracts/v2/checkpoints/Record/search.md).

[Executable SDK example](../../../../examples/rest/075/v2/checkpoints/Record/search.py):

```bash
python -B examples/rest/075/v2/checkpoints/Record/search.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| SearchRecordsPermissionDenied | Could not search the Record. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
