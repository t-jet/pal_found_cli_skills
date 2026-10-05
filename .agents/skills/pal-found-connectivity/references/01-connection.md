# Connection operations

A connection stores how Foundry reaches an external source. A file import selects source files and
writes them to a dataset; a table import syncs tabular source data into a dataset. The import
definition is separate from an execution. A virtual table lets supported sources be queried without
first copying them into a Foundry dataset.

Platform context: [Palantir
documentation](https://www.palantir.com/docs/foundry/data-connection/core-concepts). The behavior
below describes the installed CLI commands and their behavior.
Replace example identifiers and configuration values with values from your Foundry enrollment.

## Operation records

### connection.create

- **Behavior:** Creates a connection in the parent folder. `configuration` selects and configures
  the source connector; `worker` chooses where its work runs. Foundry stores submitted secrets
  encrypted after processing the request.
- **Before use:** Choose a supported source configuration, a worker that can reach it, and a
  writable parent folder.
- **Inputs:** positional none; required `--configuration-json`, `--display-name`,
  `--parent-folder-rid`, `--worker-json`; optional none. `display_name`: The display name of the
  Connection. The display name must not be blank.
- **Result:** `Connection`.
- **Failure or follow-up:** An invalid configuration or insufficient permission rejects connection
  creation; use the returned RID for later calls.
- **Example:** `pal-found-connectivity connection create --configuration-json '{"type":"jdbc","url":"jdbc:postgresql://localhost:5432/test","driverClass":"org.postgresql.Driver"}' --display-name Orders --parent-folder-rid PARENT_FOLDER_RID --worker-json '{"type":"foundryWorker","networkEgressPolicyRids":[]}'`

### connection.get

- **Behavior:** Get the Connection with the specified rid.
- **Before use:** The connection must exist and be readable.
- **Inputs:** positional `connection_rid`; required none; optional none.
- **Result:** `Connection`.
- **Failure or follow-up:** A missing or inaccessible connection returns an error, except where the
  SDK declares an optional result.
- **Example:** `pal-found-connectivity connection get CONNECTION_RID`

### connection.get_configuration

- **Behavior:** Retrieves the ConnectionConfiguration of the Connection itself. This operation is
  intended for use when other Connection data is not required, providing a lighter-weight
  alternative to `getConnection` operation.
- **Before use:** The connection must exist and be readable.
- **Inputs:** positional `connection_rid`; required none; optional none.
- **Result:** `ConnectionConfiguration`.
- **Failure or follow-up:** A missing or inaccessible connection returns an error, except where the
  SDK declares an optional result.
- **Example:** `pal-found-connectivity connection get-configuration CONNECTION_RID`

### connection.get_configuration_batch

- **Behavior:** Returns a map of Connection RIDs to their corresponding configurations. Connections
  are filtered from the response if they don't exist or the requesting token lacks the required
  permissions. The maximum batch size for this endpoint is 200.
- **Before use:** The connection must exist and be readable.
- **Inputs:** positional none; required `--body-json`; optional none. `body`: Body of the request
- **Result:** `GetConfigurationConnectionsBatchResponse`.
- **Failure or follow-up:** Check the returned entries: batch endpoints may omit missing or
  inaccessible resources, so compare the result with requested RIDs.
- **Example:** `pal-found-connectivity connection get-configuration-batch --body-json '[{"connectionRid":"ri.magritte..source.c078b71b-92f9-41b6-b0df-3760f411120b"}]'`

### connection.update_export_settings

- **Behavior:** Updates the export settings on the Connection. Only users with Information Security
  Officer role can modify the export settings.
- **Before use:** The connection must exist; the SDK requires the Information Security Officer role
  to change export settings.
- **Inputs:** positional `connection_rid`; required `--export-settings-json`; optional none.
- **Result:** `None`.
- **Failure or follow-up:** Invalid input or insufficient access to the connection is returned
  through the CLI error envelope.
- **Example:** `pal-found-connectivity connection update-export-settings CONNECTION_RID --export-settings-json '{"exportsEnabled":true,"exportEnabledWithoutMarkingsValidation":false}'`

### connection.update_secrets

- **Behavior:** Replaces values for the specified secret names on the connection. Omitted secrets
  stay unchanged. The names must already be configured on that connection.
- **Before use:** The connection must exist; secret names in the request must already be configured
  on it.
- **Inputs:** positional `connection_rid`; required `--secrets-json`; optional none. `secrets`: The
  secrets to be updated. The specified secret names must already be configured on the connection.
- **Result:** `None`.
- **Failure or follow-up:** Invalid input or insufficient access to the connection is returned
  through the CLI error envelope.
- **Example:** `pal-found-connectivity connection update-secrets CONNECTION_RID --secrets-json '{"Password":"REPLACE_WITH_SECRET"}'`

### connection.upload_custom_jdbc_drivers

- **Behavior:** Upload custom jdbc drivers to an existing JDBC connection. The body of the request
  must contain the binary content of the file and the `Content-Type` header must be
  `application/octet-stream`.
- **Before use:** Use an existing JDBC connection and a readable local .jar file within the CLI
  upload size limit.
- **Inputs:** positional `connection_rid`; required `--file`, `--file-name`; optional none.
  `file_name`: The file name of the uploaded JDBC driver. Must end with .jar
- **Result:** `Connection`.
- **Failure or follow-up:** Invalid input or insufficient access to the connection is returned
  through the CLI error envelope.
- **Example:** `pal-found-connectivity connection upload-custom-jdbc-drivers CONNECTION_RID --file driver.jar --file-name driver.jar`
