# Read a saved Model Studio configuration version

[Operation catalog](../../catalog.md) | [REST development](../../../rest-api.md)

## Concept and lifecycle

A Model Studio configuration version identifies saved training configuration.
Its response includes trainer identity/version, worker input/output
configuration, requested resources and creation metadata. Retrieving it reads
that configuration; it does not launch a training run or demonstrate that its
dependencies and resources are available for execution.

The exact [get contract](../../contracts/v2/models/ModelStudioConfigVersion/get.md)
requires a Model Studio RID and integer configuration version. Other resource
methods create configurations, discover latest versions and enumerate them;
their separate catalog contracts govern those operations.

## Prerequisites

Use prepared SDK 1.101.0, Python and httpx. Live work needs an authorized
enrollment hostname/token, actual accessible studio RID and selected version.
The frozen operation is Public Beta; confirm capability enablement and preview
policy. The example sends `preview=True` explicitly. Scope and resource access
come from the supplied application/identity metadata, not a guessed grant.

## Procedure and frozen SDK limitation

SDK 1.101.0 exposes `get(studio_rid, version)` with an integer version. Its
transport passes that integer directly to URL quoting, which raises
`quote_from_bytes() expected bytes` before sending HTTP. Providing a decimal
string to the decorated method is not a reliable bridge: its integer validator
can convert the string back into the same failing value.

For this specific frozen-version limitation, use the example's public HTTP
adapter rather than patching the SDK or reporting a successful native call:

1. Verify the studio/version and authorization prerequisites.
2. Construct the frozen GET route using an encoded RID and encoded decimal
   version. Include the actual preview query and Bearer header.
3. Use a bounded streamed response with explicit timeout, byte and chunk
   budgets. Close the response even when decoding or a budget check fails.
4. Validate success JSON with the SDK's `ModelStudioConfigVersion` model.
5. Preserve named error parameters and error instance ID. Unknown structured
   API errors use `PalantirRPCException`; non-JSON/malformed HTTP failures stay
   HTTP errors. Distinguish those failures from the native SDK encoding defect.

The direct route is:

```text
GET /api/v2/models/modelStudios/{modelStudioRid}/configVersions/{modelStudioConfigVersionVersion}
Accept: application/json
Authorization: Bearer <authorized-token>
```

The response and error models remain fully available through the local contract.
This workaround is confined to this operation and SDK version; it does not
establish a general rule for bypassing SDK validation.

## Worked example

Run from this skill directory:

```bash
python -B examples/rest/087/model_studio_config_version.py
```

The file preserves the native SDK failure and asserts that no HTTP request
occurred. Its separate direct GET verifies the exact path/query/header and
decodes a synthetic configuration. It verifies both declared named errors,
an unknown structured API error and byte-budget exhaustion. Adapt
`get_config_version`'s supplied public HTTP client, authorized values and
application budgets for live use. Its caller owns that client's lifecycle.

## Expected result and checks

The runner prints `Native SDK integer-path regression and bounded direct REST/model/error fixtures passed`.
Check returned version and trainer identity against the selected configuration.
Keep the native failure distinct from direct-adapter success. The synthetic
worker/resource values validate response shape; they do not establish that a
real training configuration can execute or that an identity has access.

## Failures and recovery

`ModelStudioConfigVersionNotFound` carries `studioRid` and integer
`configVersion`; `ModelStudioNotFound` carries `studioRid`. Verify identifiers,
visibility and version selection before another request. A denied identity
requires correcting declared access, not broadening an unrelated role. A
response budget failure requires a deliberate budget/representation decision.
HTTP timeout, invalid JSON and model-validation failures retain their distinct
diagnostics. This example performs one read and contains no automatic retry.

## Access boundary

Synthetic HTTP/SDK-model fixtures work without public or enrollment access.
Live GET needs enrollment connectivity and an authorized identity. Training,
deployment and other mutations have separate prerequisites and effects.

### create

Create a configuration version for the selected Studio. Validate trainer and inputs, then read the returned version identifier.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelStudioConfigVersion/create.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelStudioConfigVersion/create.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### latest

Read the latest configuration version and retain its number when preparing a launch.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelStudioConfigVersion/latest.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelStudioConfigVersion/latest.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

### list

List configuration versions with finite paging and choose an existing version by its returned number.

Read the [exact SDK/HTTP contract](../../contracts/v2/models/ModelStudioConfigVersion/list.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/models/ModelStudioConfigVersion/list.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.

## Python client route

With a configured `FoundryClient` named `client`, use `client.models.ModelStudio.ConfigVersion` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.
