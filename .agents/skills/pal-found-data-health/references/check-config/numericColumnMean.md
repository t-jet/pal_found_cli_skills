# numericColumnMean

[Configuration guide](../check-config.md)

Checks the mean value of a numeric column.

## Create fields

| JSON field | Required | Contract |
| --- | --- | --- |
| `subject` | Yes | [DatasetSubject](DatasetSubject.md) |
| `numericColumnCheckConfig` | Yes | [NumericColumnCheckConfig](NumericColumnCheckConfig.md) |
| `type` | No | `numericColumnMean`; default `"numericColumnMean"` |

## Replace fields

| JSON field | Required | Contract |
| --- | --- | --- |
| `numericColumnCheckConfig` | Yes | [ReplaceNumericColumnCheckConfig](ReplaceNumericColumnCheckConfig.md) |
| `type` | No | `numericColumnMean`; default `"numericColumnMean"` |

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
  "numericColumnCheckConfig": {
    "columnName": "status",
    "numericBounds": {
      "numericBounds": {
        "lowerBound": 0,
        "upperBound": 100
      },
      "severity": "MODERATE"
    },
    "trend": {
      "trendType": "NON_INCREASING",
      "differenceBounds": {
        "lowerBound": 0,
        "upperBound": 100
      },
      "severity": "MODERATE"
    }
  },
  "type": "numericColumnMean"
}
```

## Complete replacement example

```json
{
  "numericColumnCheckConfig": {
    "numericBounds": {
      "numericBounds": {
        "lowerBound": 0,
        "upperBound": 100
      },
      "severity": "MODERATE"
    },
    "trend": {
      "trendType": "NON_INCREASING",
      "differenceBounds": {
        "lowerBound": 0,
        "upperBound": 100
      },
      "severity": "MODERATE"
    }
  },
  "type": "numericColumnMean"
}
```

These synthetic examples demonstrate typed payload shape for prepared SDK
1.101.0. Replace dataset/branch, column names and policy values using the actual
resource schema and monitoring requirement. Local validation does not save a
check, evaluate a dataset or prove authorization.
