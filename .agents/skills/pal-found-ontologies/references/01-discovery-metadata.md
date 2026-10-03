# Discovery: ontology metadata and model

This part documents the Ontology discovery operations that read the ontology
model and its metadata (DEV-046): `ontology` (4), `ontology_value_type` (2),
`object_type` (7), `action_type` (4), `action_type_full_metadata` (2), and
`query_type` (2) = 21 operations. Read the
[Ontologies entry](SKILL.md) first.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/ontologies/scripts/pal_found_ontologies_cli.py`;
SDK `foundry_sdk/v2/ontologies/{ontology,ontology_value_type,object_type,action_type,action_type_full_metadata,query_type}.py`
at pinned commit `2da67907`. Reviewer architect (CODEREVIEW-046), 2026-10-03.
QA baseline TESTCASE-006.

All operations in this part are **read-class**: they never write ontology
state. A zero exit means the read completed; an empty result means no matching
entries in the requested scope.

## Operation records

### ontology.get / ontology.get_full_metadata / ontology.list / ontology.load_metadata

- **Class**: read. Returns ontology metadata.
- **Preconditions**: can read the ontology.
- **Effect**: `get` returns the ontology record (RID, api-name);
  `get_full_metadata` returns the full metadata including object types,
  interfaces, and shared properties; `list` pages visible ontologies;
  `load_metadata` returns a metadata handle/summary used for discovery.
- **Inputs**: `get`/`get_full_metadata`/`load_metadata` take positional
  `ontology_rid`; `list` takes paging options.
- **Success**: the ontology record/metadata; `list` empty if none visible.
- **Failure**: exit 4 if ontology RID wrong.
- **Example**: `pal-found-ontologies ontology get <ONTOLOGY_RID>`.

### ontology_value_type.get / list

- **Class**: read. Returns a value type used in the ontology.
- **Preconditions**: can read the ontology.
- **Effect**: `get` returns one value type; `list` pages value types.
- **Inputs**: `get` positional `ontology_rid`, `value_type_api_name`;
  `list` paging.
- **Success**: the value type record(s).
- **Example**: `pal-found-ontologies ontology-value-type get <ONTOLOGY_RID> <VALUE_TYPE_NAME>`.

### object_type.get / get_by_rid_batch / get_edits_history / get_full_metadata / get_outgoing_link_type / list / list_outgoing_link_types

- **Class**: read. Returns object type metadata.
- **Preconditions**: can read the ontology/object type.
- **Effect**:
  - `get`: returns one object type by its API name.
  - `get_by_rid_batch`: returns several object types by RID.
  - `get_edits_history`: returns the edit history of an object type.
  - `get_full_metadata`: returns full object type metadata (properties, links).
  - `get_outgoing_link_type`: returns one outgoing link type of an object type.
  - `list`: pages the object types in an ontology.
  - `list_outgoing_link_types`: pages the outgoing link types.
- **Inputs**: positional `ontology_rid`, `object_type_api_name` (and link type
  where relevant); batch uses a JSON `body`; `list` variants take paging.
- **Success**: the object type/link records; empty list when none.
- **Failure**: exit 4 if object type missing.
- **Example**: `pal-found-ontologies object-type get <ONTOLOGY_RID> Customer`.

### action_type.get / get_by_rid / get_by_rid_batch / list

- **Class**: read. Returns action type metadata.
- **Preconditions**: can read the ontology.
- **Effect**: `get`/`get_by_rid` return one action type (by api-name/RID);
  `get_by_rid_batch` returns several by RID; `list` pages action types.
- **Inputs**: positional `ontology_rid`, `action_type_api_name` (or RID);
  batch JSON `body`; `list` paging.
- **Success**: the action type record(s) describing its parameters.
- **Example**: `pal-found-ontologies action-type get <ONTOLOGY_RID> create-order`.

### action_type_full_metadata.get / list

- **Class**: read. Returns extended action type metadata.
- **Preconditions**: can read the ontology.
- **Effect**: returns action type metadata including parameter/interface detail.
- **Inputs**: `get` positional `ontology_rid`, `action_type_api_name`/RID;
  `list` paging.
- **Success**: full metadata records.

### query_type.get / list

- **Class**: read. Returns query type metadata.
- **Preconditions**: can read the ontology.
- **Effect**: `get` returns one query type; `list` pages them.
- **Inputs**: `get` positional `ontology_rid`, `query_type_api_name`; `list`
  paging.
- **Success**: the query type record(s) describing parameters and return type.
- **Example**: `pal-found-ontologies query-type get <ONTOLOGY_RID> top-customers`.

## Evidence and review

All records above are read-class and were reviewed against the installed
`pal-found-ontologies` parser and pinned SDK sources (commit `2da67907`).
Reads never write ontology state. No unsupported operation is documented as
callable.
