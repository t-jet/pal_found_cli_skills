# SDK integration and Sources

[Ontology and Compute topics](../ontology-compute.md) · [Development guide](../../SKILL.md)

## Concept and lifecycle

The Compute Module SDK registers/container-hosts logic. The generated Ontology SDK
provides enrollment-specific object/Action bindings. The platform REST SDK exposes
platform services. These clients serve different roles; SDK registration grants no
resource access. Function input has invocation metadata `context` and payload `event`;
ordinary results must serialize to JSON. Generators require a streaming registration.
Typed structs enable Function schema inference; imported schema must match the endpoint.

## Prerequisites

The registration API here was checked against the official `python-compute-module`
source commit `5f0850c5d10846c1dfce3f43649792379d4c60b1`. Prepare the matching
`compute-modules` package and its optional Sources dependencies before using these
imports. Package availability and installation are environment prerequisites.
For Ontology work, prepare the generated Python
OSDK package and its exported types. [Application registration](../applications/osdk.md)
explains binding generation. Application permissions require service-user resource
grants and allowed OAuth scopes/restrictions. An OSDK operation must also pass
[Ontology authorization](../ontology/security.md).

Modules have no outbound connectivity by default, including to Foundry services.
Prepare a Data Connection Source containing the specific hostname/network policy and
required secrets. It must belong to the project or be referenced into it, allow import
into Compute Modules and have an API name. Add it in Configure > Sources > Add Sources.
Local syntax/fixture tests need no network. Real credentials, grants, deployment and
resource calls need authorized enrollment access; Source/OAuth administration may
require administrators. Prepared packages and images avoid public runtime downloads.

## Procedure

1. Decide whether resource access belongs to a function application's service user
   or a pipeline's scoped job token; use [execution modes](execution.md).
2. Configure Source network access to the enrollment hostname. Independently verify
   grants and application restrictions on each resource/operation.
3. For generated OSDK application access, configure Application permissions > Use
   other app credentials using the Developer Console client ID/secret and save.
   `retrieve_third_party_id_and_creds()` reads the configured credentials. Use the
   generated package's `ConfidentialClientAuth` and `FoundryClient`, with refresh
   enabled and only the needed scopes. Never log credentials or token-bearing context.
4. For platform dataset access in application mode, `RefreshingOauthToken` supplies
   a renewable token. Obtain its current string with `get_token()`, then construct
   `UserTokenAuth(token=current_token)` and pass that authentication object to
   `FoundryClient(auth=auth, hostname=hostname)`. Never pass a bare token as `auth`.
   Refresh/reconstruct as needed for a long-lived worker. The
   [local authentication contract](../rest/authentication.md) supplies imports and
   timeout/error behavior for the prepared platform SDK.
5. Register/import the function using [lifecycle](lifecycle.md). Verify a permitted
   read, an intentional denied read and any effects under the actual module identity.

## Worked example

This adaptable OSDK example assumes a generated package named `shipment_osdk` exporting
the client/auth classes and a generated `Shipment` object collection. Substitute
actual generated names by inspecting the prepared package; `Shipment` is not a
platform-wide object type. `FOUNDRY_URL` holds the hostname expected by that package.

```python
import os
from typing import TypedDict
from compute_modules.auth import retrieve_third_party_id_and_creds
from shipment_osdk import ConfidentialClientAuth, FoundryClient

class SampleInput(TypedDict):
    limit: int

def shipment_sample(context, event: SampleInput) -> str:
    limit = event["limit"]
    if type(limit) is not int or not 1 <= limit <= 10:
        raise ValueError("limit must be an integer from 1 to 10")
    client_id, secret = retrieve_third_party_id_and_creds()
    hostname = os.environ["FOUNDRY_URL"]
    auth = ConfidentialClientAuth(
        client_id=client_id, client_secret=secret, hostname=hostname,
        scopes=["api:use-ontologies-read"], should_refresh=True,
    )
    client = FoundryClient(auth=auth, hostname=hostname)
    return str(client.ontology.objects.Shipment.take(limit))
```

This scope targets a restricted Developer Console client. Its operation and resource
restrictions must allow the requested Ontology read. Current unrestricted applications also use `api:use-*` for public APIs. Legacy
standalone OAuth clients, or authorized unrestricted clients calling underlying
service endpoints, may require `api:ontologies-read`. Select the namespace matching
the configured client-security mode, as explained in
[application registration](../applications/osdk.md). Client grants never bypass
the service user's object permissions.

Register this adapter using `add_functions(shipment_sample)` and start the SDK worker
as in the local [app](../../examples/compute/app.py). The sample returns a string for
inspection, not a stable business DTO; define an explicit result schema for consumers.
An empty permitted result differs from denied access. Use the generated package's
actual error contract to distinguish them.

For Source credentials, the mounted `SOURCE_CREDENTIALS` file contains a JSON map
indexed by Source API name and secret name. REST Source secrets can use names such
as `additionalSecretApiKey`. Inspect configured names, not guessed ones. The SDK's
`compute_modules.sources_v2.get_source(api_name)` is the supported Source helper when
its prepared optional Sources dependencies are present. Keep credentials inside the
container and pass them only to the authorized destination.

## Expected result and checks

Local tests verify logic and mounted-map handling. Enrollment checks must independently
verify network route, TLS trust, token acquisition, allowed operation and business
result. Preserve Foundry's configured CA trust; disabling TLS verification does not
repair Source policy or authorization. Set external request timeouts; the generated
SDK's prepared runtime configuration must expose the project's supported timeout.

## Failures and recovery

| Observation | Diagnosis and next step |
| --- | --- |
| Import or generated type missing | Inspect prepared package/version and exports; rebuild binding rather than inventing names. |
| `CLIENT_ID`/secret absent | Correct application credential configuration; secrets do not belong in image arguments. |
| Destination unreachable | Check Source project/reference, import allowance and exact network policy. |
| TLS failure | Verify hostname and mounted CA chain; retain certificate verification. |
| Unauthorized/forbidden | Check application identity, scope/restriction and resource/object grants separately. |
| Timed out after an effect | Inspect operation state/result before repeating the write. |

Optional source attribution: [Python contract/authentication](https://www.palantir.com/docs/foundry/compute-modules/python-sdk),
[Source contract](https://www.palantir.com/docs/foundry/compute-modules/sources),
[OSDK configuration](https://www.palantir.com/docs/foundry/compute-modules/osdk-integration).
