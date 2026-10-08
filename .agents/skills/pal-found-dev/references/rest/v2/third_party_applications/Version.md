# Version: third party applications operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

An application Version is an uploaded artifact. Snapshot versions expire automatically after two days, while release versions require explicit lifecycle choices. Identify the application and exact version before changing it.

Prepare SDK 1.101.0 and an identity authorized for the exact tenant resource. Check each contract for its API stage and endpoint-specific restrictions. No universal role or retry guarantee is implied by these operations. For an uncertain write, read the exact RID and effect before repeating it.

## Operations

### delete

Delete an exact application version. Check whether a Website currently uses that version before deleting it.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/third_party_applications/Version/delete.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/third_party_applications/Version/delete.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### get

Read one version and verify its application identity, version and uploaded artifact metadata.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/third_party_applications/Version/get.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/third_party_applications/Version/get.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### list

Discover versions for the application with finite pagination; distinguish release and snapshot versions.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/third_party_applications/Version/list.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/third_party_applications/Version/list.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### upload

Upload a version artifact to the selected application. Inspect its returned version identity before deployment.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/third_party_applications/Version/upload.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/third_party_applications/Version/upload.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### upload_snapshot

Upload a temporary snapshot artifact for preview. It expires after two days, so it is unsuitable as a durable release reference.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/third_party_applications/Version/upload_snapshot.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/third_party_applications/Version/upload_snapshot.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.
