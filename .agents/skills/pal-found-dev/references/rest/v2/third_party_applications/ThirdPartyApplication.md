# ThirdPartyApplication: third party applications operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

Use an approved application RID to select version or Website operations. `ThirdPartyApplication.get` returns only `rid`; its response contains no application configuration or child-membership list. Retain the selected application RID as request context for later calls.

Prepare SDK 1.101.0 and an identity authorized for the exact tenant resource. Check each contract for its API stage and endpoint-specific restrictions. No universal role or retry guarantee is implied by these operations. For an uncertain write, read the exact RID and effect before repeating it.

## Python client route

With a configured `FoundryClient` named `client`, use `client.third_party_applications.ThirdPartyApplication` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.

## Operations

### get

Read the application and compare the returned `rid` with the requested application RID. This response does not identify versions, Website configuration or child membership. Pass the retained application RID to the separate version and Website operations. Read [Website.get](Website.md#get) when `deployed_version` or `subdomains` are needed; those fields come from the Website response, not the application response.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/third_party_applications/ThirdPartyApplication/get.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/third_party_applications/ThirdPartyApplication/get.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.
