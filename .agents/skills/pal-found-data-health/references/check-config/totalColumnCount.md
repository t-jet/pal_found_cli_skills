# totalColumnCount

[Configuration guide](../check-config.md)

Checks the total number of columns in the dataset.

## Create fields

| JSON field | Required | Contract |
| --- | --- | --- |
| `subject` | Yes | [DatasetSubject](DatasetSubject.md) |
| `columnCountConfig` | Yes | [ColumnCountConfig](ColumnCountConfig.md) |
| `type` | No | `totalColumnCount`; default `"totalColumnCount"` |

## Replace fields

| JSON field | Required | Contract |
| --- | --- | --- |
| `columnCountConfig` | Yes | [ColumnCountConfig](ColumnCountConfig.md) |
| `type` | No | `totalColumnCount`; default `"totalColumnCount"` |

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
  "columnCountConfig": {
    "expectedValue": 4,
    "severity": "MODERATE"
  },
  "type": "totalColumnCount"
}
```

## Complete replacement example

```json
{
  "columnCountConfig": {
    "expectedValue": 4,
    "severity": "MODERATE"
  },
  "type": "totalColumnCount"
}
```

These synthetic examples demonstrate typed payload shape for prepared SDK
1.101.0. Replace dataset/branch, column names and policy values using the actual
resource schema and monitoring requirement. Local validation does not save a
check, evaluate a dataset or prove authorization.
