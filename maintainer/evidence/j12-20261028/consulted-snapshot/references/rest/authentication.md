# REST identity and effective access

[REST development](../rest-api.md) | [Operation catalog](catalog.md)

## Credentials and acting identity

Every live request needs the target enrollment hostname and an authorized
identity. The SDK adds a Bearer authorization header using its authentication
object. Pass `UserTokenAuth`, `PublicClientAuth`, or `ConfidentialClientAuth`
as `auth`; passing a token string directly to `FoundryClient` is invalid.

| Identity path | Intended interaction | Values to obtain before coding |
| --- | --- | --- |
| Temporary user token | Development call with the issuing user's access | Token from the authorized user and exact enrollment hostname. |
| Public OAuth client | Interactive application acting for a user | Registered client ID, redirect URI, authorized scopes and user authorization flow. |
| Confidential OAuth client | Backend application/service identity | Registered client ID/secret and permitted scopes; keep the secret outside browser code. |

An application's scope request and the identity's resource permission are
separate requirements. A successful login does not authorize a project move,
Ontology edit, model deployment or agent invocation. Application restrictions,
organizational policy and enabled capabilities can further limit execution.
Use the declared application registration and identity for the task.

## Prepared client

With prepared SDK 1.101.0 and authorized values, this constructs a v2 client.
Construction alone does not prove enrollment connectivity or resource access.

```python
import os
from foundry_sdk import Config, FoundryClient, UserTokenAuth

client = FoundryClient(
    auth=UserTokenAuth(token=os.environ["FOUNDRY_TOKEN"]),
    hostname=os.environ["FOUNDRY_HOSTNAME"],
    config=Config(timeout=30, max_retries=1,
                  propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
)
```

Keep tokens out of source, logs and fixture responses. Fixture examples use
a synthetic credential and a fake transport. They do not authenticate to a
real enrollment. A prepared OAuth client or token supplied by your organization
is a prerequisite; no public package or documentation retrieval is needed.

## Interactive OAuth callback

The public client performs authorization-code exchange with PKCE. Keep the
same authentication object across authorization and its callback; it retains
the generated state and code verifier. SDK 1.101.0 constructor arguments are
`client_id`, `redirect_url`, optional `hostname`, `scopes`, `should_refresh`
and keyword-only `config`. The redirect URL must match the registered value.

```python
from foundry_sdk import FoundryClient, PublicClientAuth

# Values come from the authorized registration, not guessed scope names.
auth = PublicClientAuth(
    client_id=registered_client_id,
    redirect_url=registered_redirect_url,
    hostname=enrollment_hostname,
    scopes=approved_scopes,
    should_refresh=True,
)
authorization_url = auth.sign_in()
# Redirect the user to authorization_url. In this same user's callback:
auth.set_token(code=callback_code, state=callback_state)
client = FoundryClient(auth=auth, hostname=enrollment_hostname)
```

The variables above are values your application's registration and callback
handler supply. Bind each authentication object to its own authorization
session; do not share one pending login between unrelated users. `set_token`
requires an earlier `sign_in` and rejects a mismatched state before exchange.
Do not log callback codes, state/verifier material or token contents. A callback
failure is not a completed login. The flow needs enrollment connectivity even
when the authored application and all reference material are local.

## Confidential OAuth and token lifetime

SDK 1.101.0 `ConfidentialClientAuth` takes `client_id`, `client_secret`, optional
`hostname`, `scopes`, `should_refresh` and keyword-only `config`. It has no
interactive `sign_in` method. Its `get_token()` obtains a token when missing
or expired; SDK requests use this authentication object to obtain their header.

```python
from foundry_sdk import ConfidentialClientAuth, FoundryClient

auth = ConfidentialClientAuth(
    client_id=registered_client_id,
    client_secret=secret_from_authorized_store,
    hostname=enrollment_hostname,
    scopes=approved_scopes,
    should_refresh=True,
)
client = FoundryClient(auth=auth, hostname=enrollment_hostname)
```

Public-client `get_token()` rejects an unauthenticated client. On expiration it
attempts refresh and raises `NotAuthenticated` if refresh fails. Automatic
refresh runs when enabled; it does not grant additional scopes or resource
permissions. `sign_out()` revokes the current token and stops automatic refresh.
Choose session/logout ownership deliberately, and handle authorization denial,
expired credentials and unavailable token endpoints separately from a resource
operation's named errors. Synthetic API transport fixtures do not verify real
OAuth exchange, refresh or revocation.

## Resolve authorization prerequisites locally

1. Identify the intended user/service identity and application registration.
2. Read the local operation contract and resource workflow. Note its release
   stage, named access errors and capability prerequisites.
3. Compare the supplied application's authorized scopes/restrictions with
   organizational registration metadata. If the source does not specify a
   scope, ask the registration owner to confirm it; do not invent a scope name.
4. Check the acting identity's permission on the exact resource and relevant
   ancestors, branch or Ontology objects. Use supplied access metadata or
   authorized enrollment administration tooling.
5. Verify a permitted read using the same identity before an intended mutation
   when the resource workflow supports it. A failed read cannot be replaced by
   assuming a broader identity is available.

The frozen SDK does not enumerate every operation's complete OAuth policy.
That absence is explicit; supplied registration and enrollment policy determine
live permission. Offline authoring uses declared policy fixtures. It cannot
prove that an identity has production access.

## Failures and recovery

For `401`, check expiry, enrollment and authentication configuration. For
`403`, inspect the acting identity, authorized scope, resource permissions and
application restrictions. A resource `404` can reflect absence or access rules;
use its named error contract and permitted metadata to distinguish the cause.
An empty `404` response can indicate an unavailable API in that enrollment.
Do not replay a denied mutation while changing identities without authorization.

Private Beta/Public Beta operations remain in the local catalog. Their release
stage does not prove enablement. Identify the capability administrator and
confirm availability before live use; recorded fixture outcomes prove only
the declared scenario.

## Access boundary

Client code, request validation and fixture handling work locally with prepared
tools. Token issuance, OAuth authorization, registration changes and live API
calls require authorized enrollment connectivity. Administrative permission
and capability enablement are prerequisites where the selected operation needs
them. Missing credentials or tenant metadata identify a blocked step.

Optional attribution: [API authentication](https://www.palantir.com/docs/foundry/api/general/overview/authentication).
