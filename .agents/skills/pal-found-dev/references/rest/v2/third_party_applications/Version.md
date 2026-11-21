# Version: third party applications operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

An application Version identifies an uploaded artifact. The returned Version model contains only `version`. Retain the application RID from the request and approved upload/release records for artifact identity and release/snapshot kind. Snapshot versions expire automatically after two days; retain upload-time provenance when reasoning about expiry, because Version responses contain no kind or expiry field. Confirm current availability through an authorized request before use.

Prepare SDK 1.101.0 and an identity authorized for the exact tenant resource. Check each contract for its API stage and endpoint-specific restrictions. No universal role or retry guarantee is implied by these operations. For an uncertain write, read the exact RID and effect before repeating it.

## Python client route

With a configured `FoundryClient` named `client`, use `client.third_party_applications.ThirdPartyApplication.Website.Version` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.

## Operations

### delete

Delete an exact application version. Check whether a Website currently uses that version before deleting it.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/third_party_applications/Version/delete.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/third_party_applications/Version/delete.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### get

Read one version under the retained application RID and compare the returned `version` with the requested version. The response contains no application RID, artifact metadata, release/snapshot kind or expiry. Use approved upload/release records or authorized verification for that provenance. Read [Website.get](Website.md#get) separately for the selected application's `deployed_version` and `subdomains`; Website state does not establish artifact contents or upload kind.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/third_party_applications/Version/get.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/third_party_applications/Version/get.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### list

Discover versions under the retained application RID with finite pagination. Each returned Version entry exposes only `version`; neither the entry nor its name establishes release/snapshot kind, artifact identity or expiry. Correlate version values with approved upload/release provenance or authorized verification before making those distinctions.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/third_party_applications/Version/list.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/third_party_applications/Version/list.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### upload

Upload a version artifact to the selected application and compare the returned `version` with the submitted value. Retain the application RID, approved artifact identity and upload/release record separately; the response does not return artifact metadata or kind. Check [Website.get](Website.md#get) separately when deployed-version or subdomain state is required.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/third_party_applications/Version/upload.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/third_party_applications/Version/upload.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### upload_snapshot

Upload a temporary snapshot artifact for preview. The pinned SDK documents automatic deletion after two days, so it is unsuitable as a durable release reference. Compare the returned `version` with the submitted value and retain the application RID, artifact identity, snapshot upload time and approved provenance separately. The returned Version carries no snapshot-kind or expiry field; do not infer either from its name.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/third_party_applications/Version/upload_snapshot.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/third_party_applications/Version/upload_snapshot.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.
