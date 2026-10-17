# File imports

[Connectivity operations](index.md) | [Connection setup](Connection.md)

## Concept and prerequisites

A FileImport copies selected upstream files through a Connection into a destination dataset. Its definition chooses filters and an import mode; execution starts an asynchronous Foundry Build. Prepare an authorized Connection RID, destination dataset RID and supported filters before creating one. A definition alone does not populate the dataset.

## Procedure and operations

| Operation | Use and check |
| --- | --- |
| [create](../../contracts/v2/connectivity/FileImport/create.md) ([fixture](../../../../examples/rest/089/v2/connectivity/FileImport/invoke_create.py)) | Set connection, destination dataset, display name, filters and import mode. Retain returned FileImport RID; verify its destination and selection before execution. |
| [get](../../contracts/v2/connectivity/FileImport/get.md) ([fixture](../../../../examples/rest/089/v2/connectivity/FileImport/invoke_get.py)) | Read one definition by connection RID and FileImport RID. Check that both identify the intended source and import. |
| [list](../../contracts/v2/connectivity/FileImport/list.md) ([fixture](../../../../examples/rest/089/v2/connectivity/FileImport/invoke_list.py)) | Enumerate imports visible to this identity, with finite page and item budgets. Visibility filtering means an absent import may be hidden. |
| [replace](../../contracts/v2/connectivity/FileImport/replace.md) ([fixture](../../../../examples/rest/089/v2/connectivity/FileImport/invoke_replace.py)) | Replace definition fields for a known import. Re-read it before triggering a build; a replacement can change which files are selected. |
| [execute](../../contracts/v2/connectivity/FileImport/execute.md) ([fixture](../../../../examples/rest/089/v2/connectivity/FileImport/invoke_execute.py)) | Start the import; the returned Build RID is a submission handle. Use [Orchestration Build status](../orchestration/index.md) to check completion, then validate destination data. |
| [delete](../../contracts/v2/connectivity/FileImport/delete.md) ([fixture](../../../../examples/rest/089/v2/connectivity/FileImport/invoke_delete.py)) | Remove the import definition. The destination dataset remains, but future updates from this import stop. Verify that this loss of refresh is intended. |

## Worked example and expected result

The [offline FileImport examples](../../../../examples/rest/089/v2/connectivity/FileImport/invoke_execute.py) each call the pinned SDK through a synthetic transport, checking path/body serialization, decoded results and source-declared errors. From the skill root, run `python -B examples/rest/089/v2/connectivity/FileImport/invoke_execute.py` to inspect Build RID handling. A live flow succeeds only when the build reaches its supported successful terminal status and destination contents match the intended file selection. Keep the Build RID when a status check times out.

## Failures, recovery and access boundary

Check source selection, destination access and Connection permission for denied or invalid imports. A timed-out `execute` may already have started a build; inspect recent builds and the destination before submitting again. Deletion does not erase prior dataset contents. Local fixtures require no enrollment; live definitions, upstream access, builds and dataset checks require authorized access.
