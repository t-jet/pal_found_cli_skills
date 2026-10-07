# v2 datasets: View

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Views compose backing datasets and branches. Backing membership and primary-key
configuration determine how that composition is interpreted. Removing a backing dataset
can trigger a SNAPSHOT transaction on the next update; this is a data lifecycle change
rather than a metadata-only edit.

## Prepare the application

Use prepared SDK 1.101.0 and an authorized identity for the intended enrollment. Resolve
the resource identities and complete request models linked below before calling a
method. Offline fixtures use synthetic identities and an actual SDK HTTP transport; they
need prepared Python, SDK and httpx and contact no enrollment.

Verify the application grants, resource permissions and capability enablement in the
tenant. SDK source does not enumerate a universal role or scope for every operation;
operation-specific documented requirements below take precedence. Source does not
provide a universal idempotency guarantee. For uncertain writes, retain request identity
and reconcile through authorized reads before repeating.

## Operations and outcome checks

### add_backing_datasets

Add backing dataset/branch pairs and verify the resulting composition. Duplicate pairs
with the same dataset RID and branch name are ignored.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/View/add_backing_datasets.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/View/add_backing_datasets.py):

```bash
python -B examples/rest/074/v2/datasets/View/add_backing_datasets.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| AddBackingDatasetsPermissionDenied | Could not addBackingDatasets the View. |
| InputBackingDatasetNotInOutputViewProject | One or more backing datasets do not live in the same project as the view. Add the missing datasets as project resource references to the view's project using the Filesystem API, or move them into the view's project, and then retry. |
| InvalidViewBackingDataset | Either you do not have access to one or more of the backing datasets or it does not exist. |
| NotAuthorizedToDeclassifyMarkings | The caller does not have DECLASSIFY permission on these markings or the markings do not exist. |
| ViewNotFound | The requested View could not be found. Either the view does not exist, the branch is not valid or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### add_primary_key

Add a primary key only to a view without one. The key is a guarantee supplied by the
dataset creator; verify its uniqueness semantics before declaring that guarantee.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/View/add_primary_key.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/View/add_primary_key.py):

```bash
python -B examples/rest/074/v2/datasets/View/add_primary_key.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| AddPrimaryKeyPermissionDenied | Could not addPrimaryKey the View. |
| InvalidViewPrimaryKeyColumnType | The type of each referenced column in the primary key must be one of the following: BYTE, SHORT, DECIMAL, INTEGER, LONG, STRING, BOOLEAN, TIMESTAMP or DATE. |
| InvalidViewPrimaryKeyDeletionColumn | The deletion column must be a boolean. |
| NotAllColumnsInPrimaryKeyArePresent | Not all columns in the View's primary key are present in the dataset(s). |
| ViewNotFound | The requested View could not be found. Either the view does not exist, the branch is not valid or the client token does not have access to it. |
| ViewPrimaryKeyCannotBeModified | A primary key already exits. |
| ViewPrimaryKeyDeletionColumnNotInDatasetSchema | The deletion column is not present in the dataset. |
| ViewPrimaryKeyMustContainAtLeastOneColumn | No columns were provided as part of the primary key |
| ViewPrimaryKeyRequiresBackingDatasets | Cannot add a primary key to a View that does not have any backing datasets. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### create

Create the view using explicitly selected backing datasets and configuration. Verify
metadata and intended composition before using it as an application data source.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/View/create.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/View/create.py):

```bash
python -B examples/rest/074/v2/datasets/View/create.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CreateDatasetPermissionDenied | The provided token does not have permission to create a dataset in this folder. |
| CreateViewPermissionDenied | Could not create the View. |
| FolderNotFound | The given Folder could not be found. |
| InputBackingDatasetNotInOutputViewProject | One or more backing datasets do not live in the same project as the view. Add the missing datasets as project resource references to the view's project using the Filesystem API, or move them into the view's project, and then retry. |
| InvalidDisplayName | The display name of a resource should not be exactly `.` or `..`, contain a forward slash `/` and must be less than or equal to 700 characters. |
| InvalidViewBackingDataset | Either you do not have access to one or more of the backing datasets or it does not exist. |
| InvalidViewPrimaryKeyColumnType | The type of each referenced column in the primary key must be one of the following: BYTE, SHORT, DECIMAL, INTEGER, LONG, STRING, BOOLEAN, TIMESTAMP or DATE. |
| InvalidViewPrimaryKeyDeletionColumn | The deletion column must be a boolean. |
| NotAllColumnsInPrimaryKeyArePresent | Not all columns in the View's primary key are present in the dataset(s). |
| NotAuthorizedToDeclassifyMarkings | The caller does not have DECLASSIFY permission on these markings or the markings do not exist. |
| ResourceNameAlreadyExists | The provided resource name is already in use by another resource in the same folder. |
| ViewDatasetCleanupFailed | Failed to delete dataset following View creation failure. |
| ViewNotFound | The requested View could not be found. Either the view does not exist, the branch is not valid or the client token does not have access to it. |
| ViewPrimaryKeyDeletionColumnNotInDatasetSchema | The deletion column is not present in the dataset. |
| ViewPrimaryKeyMustContainAtLeastOneColumn | No columns were provided as part of the primary key |
| ViewPrimaryKeyRequiresBackingDatasets | Cannot add a primary key to a View that does not have any backing datasets. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get

Read view metadata to inspect composition and primary-key configuration. Use the
dedicated View contract rather than assuming ordinary dataset export supports virtual
views.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/View/get.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/View/get.py):

```bash
python -B examples/rest/074/v2/datasets/View/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| ViewNotFound | The requested View could not be found. Either the view does not exist, the branch is not valid or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### remove_backing_datasets

Remove selected backing pairs and verify composition. A nonexistent specified dataset
produces no error. Removal triggers a SNAPSHOT transaction on the next update; plan that
data effect.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/View/remove_backing_datasets.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/View/remove_backing_datasets.py):

```bash
python -B examples/rest/074/v2/datasets/View/remove_backing_datasets.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| InputBackingDatasetNotInOutputViewProject | One or more backing datasets do not live in the same project as the view. Add the missing datasets as project resource references to the view's project using the Filesystem API, or move them into the view's project, and then retry. |
| InvalidViewBackingDataset | Either you do not have access to one or more of the backing datasets or it does not exist. |
| RemoveBackingDatasetsPermissionDenied | Could not removeBackingDatasets the View. |
| ViewNotFound | The requested View could not be found. Either the view does not exist, the branch is not valid or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### replace_backing_datasets

Replace the backing composition and compare the complete intended pairs. Removing any
prior backing dataset triggers a SNAPSHOT transaction when the view next updates.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/View/replace_backing_datasets.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/View/replace_backing_datasets.py):

```bash
python -B examples/rest/074/v2/datasets/View/replace_backing_datasets.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| InputBackingDatasetNotInOutputViewProject | One or more backing datasets do not live in the same project as the view. Add the missing datasets as project resource references to the view's project using the Filesystem API, or move them into the view's project, and then retry. |
| InvalidViewBackingDataset | Either you do not have access to one or more of the backing datasets or it does not exist. |
| NotAuthorizedToDeclassifyMarkings | The caller does not have DECLASSIFY permission on these markings or the markings do not exist. |
| ReplaceBackingDatasetsPermissionDenied | Could not replaceBackingDatasets the View. |
| ViewNotFound | The requested View could not be found. Either the view does not exist, the branch is not valid or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
