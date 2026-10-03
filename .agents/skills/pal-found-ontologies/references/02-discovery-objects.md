# Discovery: linked objects and ontology objects

This part documents the Ontology discovery operations that return object and
link data (DEV-046): `linked_object` (2) and `ontology_object` (5) = 7
operations. Read the [Ontologies entry](SKILL.md) first.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/ontologies/scripts/pal_found_ontologies_cli.py`;
SDK `foundry_sdk/v2/ontologies/{linked_object,ontology_object}.py` at pinned
commit `2da67907`. Reviewer architect (CODEREVIEW-046), 2026-10-03. QA
baseline TESTCASE-006.

All operations in this part are **read/query-class**: they never write
ontology state.

## Operation records

### linked_object.get_linked_object

- **Class**: read. Returns the object(s) linked to a source object across a
  link type.
- **Preconditions**: can read the source object and link type.
- **Effect**: returns the linked objects of one object across one link type.
- **Inputs**: positional `ontology_rid`, `object_type_api_name`,
  `object_rid`, `link_type_api_name`; optional `--select`.
- **Success**: a list of linked objects; empty if none.
- **Example**: `pal-found-ontologies linked-object get-linked-object <ONTOLOGY_RID> Order O1 order-items Item`.

### linked_object.list_linked_objects

- **Class**: read. Returns an object set of linked objects across a link type
  (paged).
- **Preconditions**: can read the source objects and link type.
- **Effect**: returns linked objects for a set of source objects.
- **Inputs**: positional `ontology_rid`, `object_type_api_name`,
  `object_rid`, `link_type_api_name`; paging and `--select` options.
- **Success**: a page of linked objects; empty if none.

### ontology_object.aggregate

- **Class**: read/query. Aggregates ontology objects by grouping and metrics.
- **Preconditions**: can read the object type; the aggregation is allowed.
- **Effect**: returns aggregated groups/metrics over the object set.
- **Inputs**: positional `ontology_rid`, `object_type_api_name`;
  `--aggregation`, `--group-by`, `--select` where shown.
- **Success**: aggregation result; empty groups when no matches.
- **Example**: `pal-found-ontologies ontology-object aggregate <ONTOLOGY_RID> Order --group-by '["status"]'`.

### ontology_object.count

- **Class**: read/query. Counts ontology objects matching a criteria.
- **Preconditions**: can read the object type.
- **Effect**: returns the count of objects matching the criteria.
- **Inputs**: positional `ontology_rid`, `object_type_api_name`;
  `--where`/filters.
- **Success**: a count; zero means no matches.
- **Example**: `pal-found-ontologies ontology-object count <ONTOLOGY_RID> Order --where '{"status":"OPEN"}'`.

### ontology_object.get

- **Class**: read. Returns a single ontology object by its primary key.
- **Preconditions**: can read the object.
- **Effect**: returns the object and its selected properties.
- **Inputs**: positional `ontology_rid`, `object_type_api_name`,
  `object_primary_key`; `--select`, `--branch` options.
- **Success**: the object record.
- **Failure**: exit 4 if the object is missing.
- **Example**: `pal-found-ontologies ontology-object get <ONTOLOGY_RID> Order O1 --select '["orderId","amount"]'`.

### ontology_object.list

- **Class**: read. Pages ontology objects (optionally on an object set).
- **Preconditions**: can read the object type.
- **Effect**: returns a page of objects.
- **Inputs**: positional `ontology_rid`, `object_type_api_name`; `--object-set`,
  filters, `--select`, paging.
- **Success**: objects; empty if none.
- **Example**: `pal-found-ontologies ontology-object list <ONTOLOGY_RID> Order --page-size 100`.

### ontology_object.search

- **Class**: read/query. Searches ontology objects by text/`where` criteria.
- **Preconditions**: can read and search the object type.
- **Effect**: returns objects matching the query/criteria.
- **Inputs**: positional `ontology_rid`, `object_type_api_name`;
  `--where`/query, `--order-by`, paging.
- **Success**: matching objects; empty if none.
- **Example**: `pal-found-ontologies ontology-object search <ONTOLOGY_RID> Order --where '{"amount":{"$gt":100}}'`.

## Evidence and review

All records above are read/query-class and were reviewed against the
installed `pal-found-ontologies` parser and pinned SDK sources (commit
`2da67907`). Reads never write ontology state; query operations may consume
compute per the aggregation/count scope (AC-D-013-09). No unsupported
operation is documented as callable.
