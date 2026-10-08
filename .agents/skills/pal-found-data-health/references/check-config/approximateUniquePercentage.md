# approximateUniquePercentage

[Configuration guide](../check-config.md)

Checks the approximate percentage of unique values in a specific column.

## Create fields

| JSON field | Required | Contract |
| --- | --- | --- |
| `subject` | Yes | [DatasetSubject](DatasetSubject.md) |
| `percentageCheckConfig` | Yes | [PercentageCheckConfig](PercentageCheckConfig.md) |
| `type` | No | `approximateUniquePercentage`; default `"approximateUniquePercentage"` |

## Replace fields

| JSON field | Required | Contract |
| --- | --- | --- |
| `percentageCheckConfig` | Yes | [ReplacePercentageCheckConfig](ReplacePercentageCheckConfig.md) |
| `type` | No | `approximateUniquePercentage`; default `"approximateUniquePercentage"` |

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
  "percentageCheckConfig": {
    "columnName": "status",
    "percentageBounds": {
      "percentageBounds": {
        "lowerBoundPercentage": 0,
        "upperBoundPercentage": 10
      },
      "severity": "MODERATE"
    },
    "medianDeviation": {
      "medianDeviation": {
        "boundsType": "LOWER_BOUND",
        "dataPoints": 5,
        "deviationThreshold": 2
      },
      "severity": "MODERATE"
    }
  },
  "type": "approximateUniquePercentage"
}
```

## Complete replacement example

```json
{
  "percentageCheckConfig": {
    "medianDeviation": {
      "medianDeviation": {
        "boundsType": "LOWER_BOUND",
        "dataPoints": 5,
        "deviationThreshold": 2
      },
      "severity": "MODERATE"
    },
    "percentageBounds": {
      "percentageBounds": {
        "lowerBoundPercentage": 0,
        "upperBoundPercentage": 10
      },
      "severity": "MODERATE"
    }
  },
  "type": "approximateUniquePercentage"
}
```

These synthetic examples demonstrate typed payload shape for prepared SDK
1.101.0. Replace dataset/branch, column names and policy values using the actual
resource schema and monitoring requirement. Local validation does not save a
check, evaluate a dataset or prove authorization.
