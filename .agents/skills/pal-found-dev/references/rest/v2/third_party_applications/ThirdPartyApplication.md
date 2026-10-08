# ThirdPartyApplication: third party applications operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

A third-party application owns versions and may include a Website. Read its RID and configuration before selecting a version or deployment operation.

Prepare SDK 1.101.0 and an identity authorized for the exact tenant resource. Check each contract for its API stage and endpoint-specific restrictions. No universal role or retry guarantee is implied by these operations. For an uncertain write, read the exact RID and effect before repeating it.

## Operations

### get

Read the application RID and metadata to establish which Version or Website belongs to the selected application.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/third_party_applications/ThirdPartyApplication/get.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/third_party_applications/ThirdPartyApplication/get.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.
