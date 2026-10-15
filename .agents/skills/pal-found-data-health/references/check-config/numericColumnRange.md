# numericColumnRange

[Configuration guide](../check-config.md)

Checks that values in a numeric column fall within a specified range.

## Create fields

| JSON field | Required | Contract |
| --- | --- | --- |
| `subject` | Yes | [DatasetSubject](DatasetSubject.md) |
| `columnName` | Yes | string |
| `numericBoundsConfig` | Yes | [NumericBoundsConfig](NumericBoundsConfig.md) |
| `type` | No | `numericColumnRange`; default `"numericColumnRange"` |

## Replace fields

| JSON field | Required | Contract |
| --- | --- | --- |
| `numericBoundsConfig` | Yes | [NumericBoundsConfig](NumericBoundsConfig.md) |
| `type` | No | `numericColumnRange`; default `"numericColumnRange"` |

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
  "columnName": "status",
  "numericBoundsConfig": {
    "numericBounds": {
      "lowerBound": 0,
      "upperBound": 100
    },
    "severity": "MODERATE"
  },
  "type": "numericColumnRange"
}
```

## Complete replacement example

```json
{
  "numericBoundsConfig": {
    "numericBounds": {
      "lowerBound": 0,
      "upperBound": 100
    },
    "severity": "MODERATE"
  },
  "type": "numericColumnRange"
}
```

These synthetic examples demonstrate typed payload shape for prepared SDK
1.101.0. Replace dataset/branch, column names and policy values using the actual
resource schema and monitoring requirement. Local validation does not save a
check, evaluate a dataset or prove authorization.
