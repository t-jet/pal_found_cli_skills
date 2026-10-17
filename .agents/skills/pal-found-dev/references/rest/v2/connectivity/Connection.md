# Direct connections and configuration

[Connectivity operations](index.md) | [REST client behavior](../../client-behavior.md)

## Concept and prerequisites

A Connection holds a configured route to an upstream source. Its RID is used by imports and virtual tables. SDK 1.101.0 creates a direct-connection runtime; choosing its configuration and worker requires knowledge of the upstream system, network route and the caller's Foundry permissions. Prepare a parent folder and keep secret values outside logs and examples. Secret fields travel over TLS and are stored encrypted by Foundry, but the service processes them temporarily in plaintext memory.

## Upstream credential boundary

Choose the configuration variant for the real upstream system before calling `create`. The [Snowflake configuration](../../models/v2/connectivity/models/SnowflakeConnectionConfiguration.md) needs an account identifier and an [authentication mode](../../models/v2/connectivity/models/SnowflakeAuthenticationMode.md). For [External OAuth](../../models/v2/connectivity/models/SnowflakeExternalOauth.md), the Snowflake security integration and trusted authorization server must already exist; issuer, audience and Connection RID subject must match their configured token claims. For [key-pair authentication](../../models/v2/connectivity/models/SnowflakeKeyPairAuthentication.md), the matching public key must already be registered to the chosen Snowflake user. Supply the private key through the declared [encrypted-property shape](../../models/v2/connectivity/models/EncryptedProperty.md), not as a public key or a value printed in a fixture. `Connection.create` consumes these values; it does not create a Snowflake security integration, user or public key.

For an AWS role-based source, [STS role configuration](../../models/v2/connectivity/models/StsRoleConfiguration.md) names the role ARN, session name and optional external ID/endpoint. The AWS trust policy and caller's ability to assume that role must already be arranged. A syntactically valid ARN does not grant access. If the required upstream identity or, for External OAuth, the matching Connection RID is unavailable, resolve that provisioning dependency before submitting a connection configuration.

## Procedure and operation choices

| Operation | When to use it and what to check |
| --- | --- |
| [create](../../contracts/v2/connectivity/Connection/create.md) ([fixture](../../../../examples/rest/089/v2/connectivity/Connection/invoke_create.py)) | Specify the parent folder, display name, connection configuration and worker. Record the returned RID and inspect the created connection before setting up imports. A timeout after submission is ambiguous: search the intended folder for a matching connection and verify its RID/configuration before considering another create. |
| [get](../../contracts/v2/connectivity/Connection/get.md) ([fixture](../../../../examples/rest/089/v2/connectivity/Connection/invoke_get.py)) | Retrieve full connection metadata by RID. Use it to confirm identity, type and the intended parent; visibility does not prove permission to change settings. |
| [get_configuration](../../contracts/v2/connectivity/Connection/get_configuration.md) ([fixture](../../../../examples/rest/089/v2/connectivity/Connection/invoke_get_configuration.py)) | Fetch configuration only when the rest of the Connection is unnecessary. Do not expect plaintext secret values in read responses. |
| [get_configuration_batch](../../contracts/v2/connectivity/Connection/get_configuration_batch.md) ([fixture](../../../../examples/rest/089/v2/connectivity/Connection/invoke_get_configuration_batch.py)) | Read up to 200 RIDs at a time. The response is a map and omits connections that are absent or invisible; compare returned keys with the requested set and report unresolved IDs. |
| [update_export_settings](../../contracts/v2/connectivity/Connection/update_export_settings.md) ([fixture](../../../../examples/rest/089/v2/connectivity/Connection/invoke_update_export_settings.py)) | Only a caller with the Information Security Officer role can change export settings. Read `Connection.get(connection_rid).export_settings`; compare `exports_enabled` and `export_enabled_without_markings_validation` with the intended values. `get_configuration` does not return these flags. |
| [update_secrets](../../contracts/v2/connectivity/Connection/update_secrets.md) ([fixture](../../../../examples/rest/089/v2/connectivity/Connection/invoke_update_secrets.py)) | Replace only named secret values in the supplied map; omitted configured secrets remain unchanged. Store the new values in an approved secret source and verify upstream connectivity through an authorized check rather than logging them. |
| [upload_custom_jdbc_drivers](../../contracts/v2/connectivity/Connection/upload_custom_jdbc_drivers.md) ([fixture](../../../../examples/rest/089/v2/connectivity/Connection/invoke_upload_custom_jdbc_drivers.py)) | Send binary driver bytes with a file name to an existing JDBC Connection. The wire body uses `application/octet-stream`; validate the returned connection and approved driver provenance. Do not encode a file path as the upload body. |

## Worked example and checks

Each operation above links its own offline SDK fixture. Run the [configuration-batch fixture](../../../../examples/rest/089/v2/connectivity/Connection/invoke_get_configuration_batch.py) from the skill root with `python -B examples/rest/089/v2/connectivity/Connection/invoke_get_configuration_batch.py` to inspect bounded batch serialization and named errors. For a live onboarding flow, create or find the Connection, read it, then configure imports using its RID. After an export update, compare both flags in `Connection.get` with the intended policy. After a secret rotation, test the authorized upstream operation that uses the secret; read APIs do not reveal plaintext values. The fixtures use synthetic IDs and do not contact upstream systems or Foundry.

Before live submission, compare the selected model's required fields and discriminator with its local type definition. Afterward, use `get` for RID/parent/export settings and `get_configuration` for non-secret source fields such as Snowflake account and authentication mode. Then run a permitted bounded upstream read or import and confirm both authentication and result shape. A local serialization fixture cannot prove a Snowflake integration, key match, STS trust policy or network route.

## Failures and recovery

Missing or hidden RIDs can be absent from batch output; resolve them individually if the distinction matters. A denied export change needs the Information Security Officer role. A rejected driver upload needs checking the JDBC connection type, binary file and permitted operation. A connection or secret mutation with an uncertain response requires read and upstream verification before retrying; no universal idempotency guarantee is declared for these writes. Never print plaintext secrets during diagnosis.

## Access boundary

Offline fixtures verify SDK serialization, decoding and named errors. Creating a live Connection, rotating secrets, changing export policy, testing an upstream route and uploading a driver require authorized enrollment and, where relevant, upstream access.
