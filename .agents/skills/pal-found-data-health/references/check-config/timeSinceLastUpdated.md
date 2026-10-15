# timeSinceLastUpdated

[Configuration guide](../check-config.md)

Checks the total time since the dataset has updated.

## Create fields

| JSON field | Required | Contract |
| --- | --- | --- |
| `subject` | Yes | [DatasetSubject](DatasetSubject.md) |
| `timeCheckConfig` | Yes | [TransactionTimeCheckConfig](TransactionTimeCheckConfig.md) |
| `type` | No | `timeSinceLastUpdated`; default `"timeSinceLastUpdated"` |

## Replace fields

| JSON field | Required | Contract |
| --- | --- | --- |
| `timeCheckConfig` | Yes | [TransactionTimeCheckConfig](TransactionTimeCheckConfig.md) |
| `type` | No | `timeSinceLastUpdated`; default `"timeSinceLastUpdated"` |

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
  "timeCheckConfig": {
    "timeBounds": {
      "timeBounds": {
        "lowerBoundInSeconds": 0,
        "upperBoundInSeconds": 3600
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
    },
    "ignoreEmptyTransactions": false
  },
  "type": "timeSinceLastUpdated"
}
```

## Complete replacement example

```json
{
  "timeCheckConfig": {
    "timeBounds": {
      "timeBounds": {
        "lowerBoundInSeconds": 0,
        "upperBoundInSeconds": 3600
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
    },
    "ignoreEmptyTransactions": false
  },
  "type": "timeSinceLastUpdated"
}
```

These synthetic examples demonstrate typed payload shape for prepared SDK
1.101.0. Replace dataset/branch, column names and policy values using the actual
resource schema and monitoring requirement. Local validation does not save a
check, evaluate a dataset or prove authorization.
