# Table imports

[Connectivity operations](index.md) | [Connection setup](Connection.md)

## Concept and prerequisites

A TableImport maps an upstream table through a Connection into a destination Foundry dataset. Its config, import mode and destination determine what a build reads and writes. Prepare an authorized Connection, upstream table selection and destination dataset before changing the import. Execution starts a Foundry Build asynchronously.

## Procedure and operations

| Operation | Use and check |
| --- | --- |
| [create](../../contracts/v2/connectivity/TableImport/create.md) ([fixture](../../../../examples/rest/089/v2/connectivity/TableImport/invoke_create.py)) | Supply connection, dataset, display name, import config and mode. Record returned TableImport RID; verify the upstream table and destination before execution. |
| [get](../../contracts/v2/connectivity/TableImport/get.md) ([fixture](../../../../examples/rest/089/v2/connectivity/TableImport/invoke_get.py)) | Inspect one import by Connection and TableImport RIDs. Compare the stored mapping with the intended table. |
| [list](../../contracts/v2/connectivity/TableImport/list.md) ([fixture](../../../../examples/rest/089/v2/connectivity/TableImport/invoke_list.py)) | Page through visible imports with a finite budget. Missing entries may reflect permission filtering. |
| [replace](../../contracts/v2/connectivity/TableImport/replace.md) ([fixture](../../../../examples/rest/089/v2/connectivity/TableImport/invoke_replace.py)) | Change the known import's config, display name or mode. Read it back before running a build; source or destination behavior may change. |
| [execute](../../contracts/v2/connectivity/TableImport/execute.md) ([fixture](../../../../examples/rest/089/v2/connectivity/TableImport/invoke_execute.py)) | Submit a build and retain its Build RID. Poll using [Orchestration](../orchestration/index.md), then validate destination schema and data. Submission is not completion. |
| [delete](../../contracts/v2/connectivity/TableImport/delete.md) ([fixture](../../../../examples/rest/089/v2/connectivity/TableImport/invoke_delete.py)) | Remove the import definition after confirming future refresh should stop. Existing destination dataset is not deleted. |

## Worked example and expected result

Use the [local TableImport fixtures](../../../../examples/rest/089/v2/connectivity/TableImport/invoke_execute.py) to inspect each SDK request, result and named failure without connecting to Foundry. Run `python -B examples/rest/089/v2/connectivity/TableImport/invoke_execute.py` from the skill root for the execution handle. Live success requires a terminal successful build and validation of the destination table, including expected columns and row scope.

## Failures, recovery and access boundary

Invalid upstream config, missing table, source credentials or destination grants require correcting the specific resource. An `execute` timeout leaves submission uncertain: reconcile builds and destination state before retrying. A deleted import no longer refreshes the dataset; recreate only after confirming the intended mapping. Fixtures use synthetic RIDs; live upstream reads and Foundry builds need authorized enrollment and source access.
