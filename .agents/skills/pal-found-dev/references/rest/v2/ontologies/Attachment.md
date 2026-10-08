# Attachment operations

[REST development](../../../rest-api.md) | [Ontology service](index.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

An attachment upload creates an attachment for later Action use. Uploaded content not linked through an Action within one hour is removed; metadata reads and content reads have different result shapes.

## Prerequisites

Use the frozen Foundry Python SDK 1.101.0 and an authorized Ontology, branch, resource identifier, acting identity and exact type/parameter names from the enrollment. Prepare the linked local models before a live request. Synthetic examples run offline with the prepared SDK and mock transport; real reads or writes require enrollment access, resource permissions and any listed beta enablement. An administrator or resource owner supplies missing grants and capability access.

## Procedure and operation choices

Select the operation below, read its exact request/response/error model, then adapt the linked SDK fixture with authorized resource values. The fixture uses synthetic identifiers and checks serialized transport; it does not assert tenant behavior. Record branch, version, page/snapshot context, response and named errors for the actual call.

### `Attachment.get`

Stage: Stable. Required SDK arguments: `attachment_rid`.

Get the metadata of an attachment.

Read [exact contract](../../contracts/v2/ontologies/Attachment/get.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/Attachment/invoke_get.py): `python -B examples/rest/083/v2/ontologies/Attachment/invoke_get.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `Attachment.read`

Stage: Stable. Required SDK arguments: `attachment_rid`.

Get the content of an attachment.

Read [exact contract](../../contracts/v2/ontologies/Attachment/read.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/Attachment/invoke_read.py): `python -B examples/rest/083/v2/ontologies/Attachment/invoke_read.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `Attachment.upload`

Stage: Stable. Required SDK arguments: `body`, `content_length`, `content_type`, `filename`.

Upload an attachment to use in an action. Any attachment which has not been linked to an object via an action within one hour after upload will be removed. Previously mapped attachments which are not connected to any object anymore are also removed on a biweekly basis. The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.

Read [exact contract](../../contracts/v2/ontologies/Attachment/upload.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/Attachment/invoke_upload.py): `python -B examples/rest/083/v2/ontologies/Attachment/invoke_upload.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `Attachment.upload_with_rid`

Stage: Private Beta. Required SDK arguments: `attachment_rid`, `body`, `content_length`, `content_type`, `filename`.

This endpoint is identical to `/v2/ontologies/attachments/upload` but additionally accepts a previously generated `AttachmentRid`.

Read [exact contract](../../contracts/v2/ontologies/Attachment/upload_with_rid.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/Attachment/invoke_upload_with_rid.py): `python -B examples/rest/083/v2/ontologies/Attachment/invoke_upload_with_rid.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

## Worked example

Upload a small approved file with its actual media type, record the returned attachment RID, apply the intended Action before the one-hour expiry, then get metadata and read content only under authorized access.

```python
content = b"Inspection evidence"  # synthetic, 19 bytes
uploaded = client.ontologies.Attachment.upload(
    body=content,
    content_length=len(content),
    content_type="text/plain",
    filename="inspection.txt",
)
assert uploaded.rid and uploaded.size_bytes == len(content)
metadata = client.ontologies.Attachment.get(attachment_rid=uploaded.rid)
assert metadata.rid == uploaded.rid
```

The SDK sends the binary request with HTTP `Content-Type: application/octet-stream`;
the `content_type` argument records the file's media type. Pass the returned RID
to the configured Action parameter that links it to an object within one hour,
then reread the object's attachment property. Upload success alone does not
attach the file. Use `Attachment.read` with a byte budget and close raw/streaming
responses after checking metadata and the caller's permission.

The linked operation fixtures show actual SDK method invocation, serialized request and decoded response/error using a local mock transport. Their synthetic values are test data. Replace them with authorized identifiers and typed payloads from each linked contract; verify the live result under the intended identity before asserting a platform effect.

## Expected result and checks

Record exact operation ID, API version, release stage, branch, requested IDs, returned IDs, page/snapshot token, response mode and decoded result. For effectful calls, inspect validation/commit state and fresh target data; a successful HTTP response alone may not establish the business result. For lists, finish pagination before claiming completeness.

## Failures and recovery

On a missing or filtered result, verify Ontology/type/API names, branch and effective caller permissions. On schema rejection, compare payload fields, requiredness, aliases and discriminator values with the linked models. On a timeout after an effectful call, reconcile target or transaction state before retrying. Bound pages, streamed bytes and time windows; close streaming/raw responses according to [client lifetimes](../../client-behavior.md). Missing beta enablement is a prerequisite to resolve with the enrollment owner.
