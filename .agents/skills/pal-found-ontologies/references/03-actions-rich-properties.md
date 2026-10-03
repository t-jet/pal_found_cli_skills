# Actions and rich properties

This part documents the Ontology operations that execute actions and read or
upload attachments, media references, interfaces, object sets, time series,
and transactions (DEV-047, 39 operations). Read the [Ontologies
entry](SKILL.md) first. Many writes in this part have material effects; read
each record before invoking.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/ontologies/scripts/pal_found_ontologies_cli.py`;
SDK `foundry_sdk/v2/ontologies/*.py` at pinned commit `2da67907`. Reviewer
architect (CODEREVIEW-047), 2026-10-03. QA baseline TESTCASE-006.

## Operation records

### action.apply

- **Class**: execute (write). Applies an action to modify objects.
- **Preconditions**: the action type is valid and you can apply it; all
  required parameters are supplied.
- **Effect**: changes ontology objects per the action's logic.
- **Inputs**: positional `ontology_rid`, `action_type_api_name`;
  `--parameters` JSON (action parameters); options such as `--options`.
- **Success**: returns the action result (edited objects). The change is
  applied server-side.
- **Failure**: exit 1 invalid parameters; exit 3 permission; exit 4 if action
  missing.
- **Example**: `pal-found-ontologies action apply <ONTOLOGY_RID> create-order --parameters '{"orderId":"O1"}'`.

### action.apply_batch

- **Class**: execute (write). Applies several actions in one call.
- **Preconditions**: each action is valid.
- **Effect**: applies a batch of actions; the result reflects each.
- **Inputs**: positional `ontology_rid`, `action_type_api_name`; `--requests`
  JSON batch.
- **Success**: returns batch results per request.

### action.apply_with_overrides

- **Class**: execute (write). Applies an action with parameter/validation
  overrides.
- **Preconditions**: an action you can apply.
- **Effect**: applies the action with overridden parameters or options.
- **Inputs**: positional `ontology_rid`, `action_type_api_name`; `--parameters`,
  `--overrides`.
- **Success**: the action result.

### attachment.get

- **Class**: read (binary metadata). Returns attachment metadata.
- **Preconditions**: can read the attachment.
- **Effect**: returns attachment metadata (name, content type, size).
- **Inputs**: positional `ontology_rid`, `attachment_rid`.
- **Success**: the attachment metadata record.

### attachment.read

- **Class**: read (binary download). Downloads an attachment's bytes.
- **Preconditions**: can read the attachment.
- **Effect**: streams the attachment to a saved file; returns a metadata
  envelope.
- **Inputs**: positional `ontology_rid`, `attachment_rid`; `--output-filename`.
- **Success**: metadata envelope; download bound applies.
- **Failure**: exit 8 if content read blocked in metadata-only mode.

### attachment.upload

- **Class**: create (binary upload). Uploads an attachment.
- **Preconditions**: can write the target context.
- **Effect**: stores the attachment and returns its RID.
- **Inputs**: `--body-file`, `--content-type`, `--content-length`;
  `--sdk-package-rid`/`--sdk-version` context. Upload bound 16 MiB.
- **Success**: the uploaded attachment.
- **Failure**: exit 1 file too large; exit 8 readonly block.

### attachment.upload_with_rid

- **Class**: create (binary upload). Uploads an attachment with a caller-chosen
  RID/context.
- **Preconditions**: can write the target context.
- **Effect**: stores the attachment with the provided RID.
- **Inputs**: positional `attachment_rid`-related; `--body-file`, content
  fields.

### attachment_property.get_attachment / get_attachment_by_rid / read_attachment / read_attachment_by_rid

- **Class**: read (binary). Accesses the attachment value of a property.
- **Preconditions**: can read the object and the attachment.
- **Effect**: `get_attachment`/`get_attachment_by_rid` return attachment
  metadata for a property value; `read_attachment`/`read_attachment_by_rid`
  download the attachment bytes.
- **Inputs**: positional `ontology_rid`, `object_type_api_name`,
  `object_primary_key`/`attachment_rid`, `property_api_name`.
- **Success**: metadata or a binary envelope.

### cipher_text_property.decrypt

- **Class**: read. Decrypts a protected property value.
- **Preconditions**: you are permitted to decrypt the property.
- **Effect**: returns the decrypted value; use carefully (sensitive data).
- **Inputs**: positional `ontology_rid`, `object_type_api_name`,
  `object_primary_key`, `property_api_name`.
- **Success**: the decrypted value.

### geotemporal_series_property.get_geotemporal_series_latest_value / stream_geotemporal_series_historic_values

- **Class**: read/stream. Reads geotemporal series property values.
- **Preconditions**: can read the object and property.
- **Effect**: `get...latest_value` returns the latest value;
  `stream_geotemporal...historic_values` streams historic values.
- **Inputs**: positional `ontology_rid`, `object_type_api_name`,
  `object_primary_key`, `property_api_name`; stream options.
- **Success**: the latest value or a stream of values.

### media_reference_property.get_media_content / get_media_metadata / upload

- **Class**: read/binary. Reads media referenced by a property or uploads it.
- **Preconditions**: can read/upload media.
- **Effect**: `get_media_content` downloads media bytes;
  `get_media_metadata` returns metadata; `upload` stores media.
- **Inputs**: positional `ontology_rid`, `object_type_api_name`,
  `object_primary_key`, `property_api_name`; `--output-filename`/`--body-file`.
- **Success**: binary envelope or metadata.

### ontology_interface.aggregate / get / get_outgoing_interface_link_type / list / list_interface_linked_objects / list_objects_for_interface / list_outgoing_interface_link_types / search

- **Class**: read/query. Reads interface metadata and objects bound to
  interfaces.
- **Preconditions**: can read the interface/ontology.
- **Effect**: `aggregate`/`search`/`list_objects_for_interface` return objects
  of an interface across its bound object types; `get`/
  `get_outgoing_interface_link_type`/`list`/`list_outgoing_interface_link_types`
  return interface and link metadata.
- **Inputs**: positional `ontology_rid`, `interface_type_api_name`; filters,
  paging, `--select`, `--augmented-interface-property-types`.
- **Success**: interface metadata or objects; empty when none.
- **Example**: `pal-found-ontologies ontology-interface search <ONTOLOGY_RID> Employee --where '{}'`.

### ontology_object_set.aggregate / create_temporary / get / load / load_links / load_multiple_object_types / load_objects_or_interfaces

- **Class**: read/query or write (temporary). Reads object sets or creates a
  temporary set.
- **Preconditions**: can read the object set; `create_temporary` needs write.
- **Effect**: `create_temporary` builds a temporary object set (write);
  `aggregate`/`load`/`load_links`/`load_multiple_object_types`/
  `load_objects_or_interfaces` read the set's objects/links.
- **Inputs**: positional `ontology_rid`, `object_set`; aggregation/load
  options.
- **Success**: set results; `create_temporary` returns a temporary set RID.

### ontology_transaction.post_edits

- **Class**: execute (write). Posts ontology edits in a transaction.
- **Preconditions**: an ontology transaction context.
- **Effect**: applies edits to ontology objects.
- **Inputs**: positional `ontology_rid`, `transaction_id`; `--edits` JSON.
- **Success**: the transaction result.

### query.execute

- **Class**: execute (read). Executes a query type.
- **Preconditions**: the query type is valid and you can run it.
- **Effect**: runs the query and returns its result; consumes compute.
- **Inputs**: positional `ontology_rid`, `query_type_api_name`; `--parameters`
  JSON.
- **Success**: the query result; may be paged for list results.
- **Example**: `pal-found-ontologies query execute <ONTOLOGY_RID> top-customers --parameters '{"limit":10}'`.

### time_series_property_v2.get_first_point / get_last_point / stream_points

- **Class**: read/stream. Reads a time-series property's points.
- **Preconditions**: can read the object and property.
- **Effect**: returns the first/last point or streams points in a range.
- **Inputs**: positional `ontology_rid`, `object_type_api_name`,
  `object_primary_key`, `property_api_name`; range/stream options.
- **Success**: the point(s) or a stream.

### time_series_value_bank_property.get_latest_value / stream_values

- **Class**: read/stream. Reads value-bank time-series property values.
- **Preconditions**: can read the object and property.
- **Effect**: returns the latest value or streams values.
- **Inputs**: positional `ontology_rid`, `object_type_api_name`,
  `object_primary_key`, `property_api_name`.

## Effects and permissions

`action.apply*`/`ontology_transaction.post_edits`/`ontology_object_set.create_temporary`/
`attachment.upload*`/`media_reference_property.upload` are write or execute
operations with material effects: they change objects, store media, or consume
compute. Attachment/media reads download binaries (bounded). Time-series and
geotemporal stream operations may transfer large volumes (AC-D-013-09). Confirm
writes via a follow-up read where the platform does not return the final state.

## Evidence and review

Reviewed against the installed `pal-found-ontologies` parser and pinned SDK
sources (commit `2da67907`). Writes/executions are flagged; reads never write.
Streaming/binary volume cues are documented. No unsupported operation is
documented as callable.
