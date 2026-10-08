# Website: third party applications operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

A Website deployment selects an uploaded application version for serving. Uploading and deploying are separate actions; verify the target version and deployment state around each change.

Prepare SDK 1.101.0 and an identity authorized for the exact tenant resource. Check each contract for its API stage and endpoint-specific restrictions. No universal role or retry guarantee is implied by these operations. For an uncertain write, read the exact RID and effect before repeating it.

## Operations

### deploy

Deploy an already uploaded application version. Read Website state afterward to confirm which version is served.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/third_party_applications/Website/deploy.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/third_party_applications/Website/deploy.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### get

Read Website state and selected deployed version before changing traffic or deciding whether deployment succeeded.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/third_party_applications/Website/get.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/third_party_applications/Website/get.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### undeploy

Remove the deployed version from serving. Read Website state afterward; this does not delete the uploaded Version.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/third_party_applications/Website/undeploy.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/third_party_applications/Website/undeploy.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.
