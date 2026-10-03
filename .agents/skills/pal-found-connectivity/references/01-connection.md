# Connection operations

This part documents the `connection` resource client (7 operations). A
connection is the configured link to an external data source.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/connectivity/scripts/pal_found_connectivity_cli.py`;
SDK `foundry_sdk/v2/connectivity/{connection,file_import,table_import,virtual_table}.py`
at pinned commit `2da67907`. Reviewer architect (CODEREVIEW-048), 2026-10-03.
QA baseline TESTCASE-017.

## Operation records

### connection.create

- **Class**: create (write). Creates a connection.
- **Preconditions**: can create connections; a valid configuration.
- **Effect**: creates a connection to an external source and returns it.
- **Inputs**: `--display-name`, `--connection-type-name`,
  `--configuration-json`, `--runtime-google-cloud-configuration-json` (where
  applicable), `--credentials-json`.
- **Success**: the created connection, including its RID.
- **Failure**: exit 1 invalid configuration; exit 8 readonly block; exit 3
  permission.
- **Example**: `pal-found-connectivity connection create --display-name "CSV Source" --connection-type-name "s3" --configuration-json '{}'`.

### connection.get

- **Class**: read. Returns a connection.
- **Preconditions**: can read the connection.
- **Effect**: returns the connection record (without secret values).
- **Inputs**: positional `connection_rid`.
- **Success**: the connection record.
- **Failure**: exit 4 if RID wrong.

### connection.get_configuration

- **Class**: read. Returns a connection's configuration.
- **Preconditions**: can read the connection.
- **Effect**: returns the exported configuration (secrets redacted).
- **Inputs**: positional `connection_rid`.
- **Success**: the configuration.

### connection.get_configuration_batch

- **Class**: read. Returns configurations for several connections.
- **Preconditions**: can read each.
- **Effect**: returns a batch of configurations (semantic read).
- **Inputs**: required `--connection-rids` JSON list.
- **Success**: list of configurations.

### connection.update_export_settings

- **Class**: change (write). Updates a connection's export settings.
- **Preconditions**: can write the connection.
- **Effect**: changes export/settings on the connection.
- **Inputs**: positional `connection_rid`; settings fields.
- **Success**: the updated connection.

### connection.update_secrets

- **Class**: change (write). Updates a connection's secrets.
- **Preconditions**: can write the connection.
- **Effect**: updates stored secret values; affects runtime access.
- **Inputs**: positional `connection_rid`; credentials/secrets only via JSON
  flags; never echoed.
- **Success**: the updated connection.

### connection.upload_custom_jdbc_drivers

- **Class**: create (binary upload). Uploads custom JDBC drivers.
- **Preconditions**: can write the connection; the file is a `.jar`.
- **Effect**: stores the JDBC driver `.jar` for the connection.
- **Inputs**: positional `connection_rid`; `--file-name` ending `.jar`.
  Upload bound 16 MiB.
- **Success**: the uploaded driver reference.
- **Failure**: exit 1 if not a `.jar` or too large; exit 8 readonly block.

## Evidence and review

Reviewed against the installed `pal-found-connectivity` parser and pinned SDK
sources (commit `2da67907`). Writes (create/update*/upload) change the
connection and its access/runtime; secrets are input-only and never logged.
`get_configuration_batch` is a semantic read. No unsupported operation is
documented as callable.
