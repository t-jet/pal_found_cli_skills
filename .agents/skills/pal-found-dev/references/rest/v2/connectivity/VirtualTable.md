# Virtual tables

[Connectivity operations](index.md) | [Connection setup](Connection.md)

## Concept and prerequisites

A VirtualTable exposes an upstream table through Foundry data access without first defining a scheduled import. `create` places a resource in the selected parent folder and associates it with a Connection and upstream table config. Prepare an authorized Connection, parent folder, table name and supported config. Check upstream query capability and access before exposing the resource to consumers.

## Procedure and worked example

Call [VirtualTable.create](../../contracts/v2/connectivity/VirtualTable/create.md) with `connection_rid`, `config`, `name` and `parent_rid`; supply markings when the data classification requires them. Keep the returned resource RID. The [offline SDK fixture](../../../../examples/rest/089/v2/connectivity/VirtualTable/invoke_create.py) checks request serialization, decoded result and named errors. Run it from the skill root with `python -B` and the linked path. For live use, inspect the created resource in its folder and issue an authorized bounded query to verify upstream connectivity and schema.

## Expected result, failures and access boundary

The created resource should have the intended parent, name and upstream mapping. A failed query may reflect Connection credentials, upstream permissions or schema mismatch even when creation succeeded. After an uncertain create response, inspect the parent folder and verify resource identity/config before repeating a write. The fixture cannot establish tenant creation or upstream query access; those require authorized enrollment and source connectivity.
