# v1 ontologies: Attachment

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Attachments hold binary content for use in actions. Uploaded attachments must be
connected to an object through an action within one hour or they are removed. Previously
mapped attachments that no longer connect to an object are also removed on a biweekly
basis.

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

Read attachment metadata by its RID before connecting it to an action or downloading
content. Confirm the expected attachment identity and lifecycle.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/Attachment/get.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/Attachment/get.py):

```bash
python -B examples/rest/077/v1/ontologies/Attachment/get.py
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

### read

Read attachment content as bytes and close the response. Confirm content metadata
separately rather than inferring it from a generic byte stream.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/Attachment/read.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/Attachment/read.py):

```bash
python -B examples/rest/077/v1/ontologies/Attachment/read.py
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

### upload

The endpoint documentation requires binary bytes with `Content-Type:
application/octet-stream`. SDK 1.101.0 has a conflicting implementation: its upload
header dictionary assigns `Content-Type` twice, so the final `*/*` overwrites the
supplied `content_type`. Both synchronous and asynchronous upload paths have this
behavior. Passing `content_type='application/octet-stream'` does not send that MIME
type on the wire. The example checks the actual `*/*` header and leaves the SDK intact;
its mocked success does not prove that an enrollment accepts that request.

Before a live upload, use an approved client/version whose serialized header meets
the endpoint contract, and verify it against a controlled transport. Do not infer a
working live upload from this frozen SDK example. A failed or ambiguous upload needs
reconciliation before another attempt. Retain the returned attachment RID and connect
it through an action within one hour. Unlinked new uploads are removed; previously
mapped but disconnected attachments are removed biweekly.

The synthetic file is `inspection.txt`, containing 19 bytes (`Inspection evidence`).
Returned metadata uses `mediaType='text/plain'`, the file's media type; it is separate
from the upload transport header. Compare filename and size with the submitted bytes,
and compare a metadata-read RID with the requested RID. The read example returns the
same content. An upload creates its RID, so no caller-provided RID exists to compare.

Source: SDK 1.101.0 `v1/ontologies/attachment.py`, `AttachmentClient.upload` and
`AsyncAttachmentClient.upload`; local [upload contract](../../contracts/v1/ontologies/Attachment/upload.md)
records the frozen request shape.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/Attachment/upload.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/Attachment/upload.py):

```bash
python -B examples/rest/077/v1/ontologies/Attachment/upload.py
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
