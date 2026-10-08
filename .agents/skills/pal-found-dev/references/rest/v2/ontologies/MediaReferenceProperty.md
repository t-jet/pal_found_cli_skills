# MediaReferenceProperty operations

[REST development](../../../rest-api.md) | [Ontology service](index.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

A media reference property points to media stored in its backing Media Set. Metadata, bytes and upload are separate operations; upload requires an unambiguous single backing set and branch.

## Prerequisites

Use the frozen Foundry Python SDK 1.101.0 and an authorized Ontology, branch, resource identifier, acting identity and exact type/parameter names from the enrollment. Prepare the linked local models before a live request. Synthetic examples run offline with the prepared SDK and mock transport; real reads or writes require enrollment access, resource permissions and any listed beta enablement. An administrator or resource owner supplies missing grants and capability access.

## Procedure and operation choices

Select the operation below, read its exact request/response/error model, then adapt the linked SDK fixture with authorized resource values. The fixture uses synthetic identifiers and checks serialized transport; it does not assert tenant behavior. Record branch, version, page/snapshot context, response and named errors for the actual call.

### `MediaReferenceProperty.get_media_content`

Stage: Public Beta. Required SDK arguments: `ontology`, `object_type`, `primary_key`, `property`.

Gets the content of a media item referenced by this property.

Read [exact contract](../../contracts/v2/ontologies/MediaReferenceProperty/get_media_content.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/MediaReferenceProperty/invoke_get_media_content.py): `python -B examples/rest/083/v2/ontologies/MediaReferenceProperty/invoke_get_media_content.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `MediaReferenceProperty.get_media_metadata`

Stage: Private Beta. Required SDK arguments: `ontology`, `object_type`, `primary_key`, `property`.

Gets metadata about the media item referenced by this property.

Read [exact contract](../../contracts/v2/ontologies/MediaReferenceProperty/get_media_metadata.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/MediaReferenceProperty/invoke_get_media_metadata.py): `python -B examples/rest/083/v2/ontologies/MediaReferenceProperty/invoke_get_media_metadata.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `MediaReferenceProperty.upload`

Stage: Public Beta. Required SDK arguments: `ontology`, `object_type`, `property`, `body`.

Uploads a media item to the media set which backs the specified property. The property must be backed by a single media set and branch, otherwise an error will be thrown. The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.

Read [exact contract](../../contracts/v2/ontologies/MediaReferenceProperty/upload.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/MediaReferenceProperty/invoke_upload.py): `python -B examples/rest/083/v2/ontologies/MediaReferenceProperty/invoke_upload.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

## Worked example

Resolve an approved object's media property, inspect metadata before downloading bounded content, or upload a small test item through the configured backing set. Record the returned reference and verify the object's intended binding separately.

```python
ontology = "dispatch"  # authorized Ontology identifier
api = client.ontologies.MediaReferenceProperty
media = api.upload(
    ontology=ontology,
    object_type="Asset",
    property="inspectionPhoto",
    body=b"synthetic image payload",
    preview=True,
)
assert media.reference and media.mime_type

# After the authorized Action binds `media` to Asset A-1:
metadata = api.get_media_metadata(
    ontology=ontology,
    object_type="Asset",
    primary_key="A-1",
    property="inspectionPhoto",
    preview=True,
)
print(metadata)
```

`upload` requires a property backed by one Media Set and branch. Supply
`media_item_path` when that backing set requires paths. Upload returns a
`MediaReference`; it does not edit the object by itself. The metadata read above
is valid only after an authorized binding step, and `get_media_content` needs
its own bounded byte/stream handling. Public Beta upload and Private Beta
metadata retrieval may have different availability in an enrollment.

The linked operation fixtures show actual SDK method invocation, serialized request and decoded response/error using a local mock transport. Their synthetic values are test data. Replace them with authorized identifiers and typed payloads from each linked contract; verify the live result under the intended identity before asserting a platform effect.

## Expected result and checks

Record exact operation ID, API version, release stage, branch, requested IDs, returned IDs, page/snapshot token, response mode and decoded result. For effectful calls, inspect validation/commit state and fresh target data; a successful HTTP response alone may not establish the business result. For lists, finish pagination before claiming completeness.

## Failures and recovery

On a missing or filtered result, verify Ontology/type/API names, branch and effective caller permissions. On schema rejection, compare payload fields, requiredness, aliases and discriminator values with the linked models. On a timeout after an effectful call, reconcile target or transaction state before retrying. Bound pages, streamed bytes and time windows; close streaming/raw responses according to [client lifetimes](../../client-behavior.md). Missing beta enablement is a prerequisite to resolve with the enrollment owner.
