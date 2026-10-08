# primaryKey

[Configuration guide](../check-config.md)

Checks the uniqueness and non-null values of one or more columns (primary key constraint).

## Create fields

| JSON field | Required | Contract |
| --- | --- | --- |
| `subject` | Yes | [DatasetSubject](DatasetSubject.md) |
| `primaryKeyConfig` | Yes | [PrimaryKeyConfig](PrimaryKeyConfig.md) |
| `type` | No | `primaryKey`; default `"primaryKey"` |

## Replace fields

| JSON field | Required | Contract |
| --- | --- | --- |
| `primaryKeyConfig` | Yes | [ReplacePrimaryKeyConfig](ReplacePrimaryKeyConfig.md) |
| `type` | No | `primaryKey`; default `"primaryKey"` |

Replacement retains the original subject and type. Fields absent from the
replace table cannot be changed through this replacement contract. Use get to
inspect the saved rule before choosing replacement values. Include `type`
explicitly when constructing CLI JSON even though individual models default it.

## Complete create example

```json
{
  "subject": {
    "datasetRid": "ri.foundry.main.dataset.a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "branchId": "master"
  },
  "primaryKeyConfig": {
    "columnNames": [
      "order_id"
    ],
    "severity": "MODERATE"
  },
  "type": "primaryKey"
}
```

## Complete replacement example

```json
{
  "primaryKeyConfig": {
    "severity": "MODERATE"
  },
  "type": "primaryKey"
}
```

These synthetic examples demonstrate typed payload shape for prepared SDK
1.101.0. Replace dataset/branch, column names and policy values using the actual
resource schema and monitoring requirement. Local validation does not save a
check, evaluate a dataset or prove authorization.
