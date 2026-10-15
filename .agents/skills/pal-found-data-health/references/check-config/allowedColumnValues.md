# allowedColumnValues

[Configuration guide](../check-config.md)

Checks that values in a column are within an allowed set of values.

## Create fields

| JSON field | Required | Contract |
| --- | --- | --- |
| `subject` | Yes | [DatasetSubject](DatasetSubject.md) |
| `columnName` | Yes | string |
| `allowedValues` | Yes | array of [DateColumnValue](DateColumnValue.md) or [BooleanColumnValue](BooleanColumnValue.md) or [StringColumnValue](StringColumnValue.md) or [NumericColumnValue](NumericColumnValue.md) |
| `allowNull` | No | boolean or null; default `null` |
| `severity` | Yes | `MODERATE`, `CRITICAL` |
| `type` | No | `allowedColumnValues`; default `"allowedColumnValues"` |

## Replace fields

| JSON field | Required | Contract |
| --- | --- | --- |
| `allowedValues` | Yes | array of [DateColumnValue](DateColumnValue.md) or [BooleanColumnValue](BooleanColumnValue.md) or [StringColumnValue](StringColumnValue.md) or [NumericColumnValue](NumericColumnValue.md) |
| `severity` | Yes | `MODERATE`, `CRITICAL` |
| `allowNull` | No | boolean or null; default `null` |
| `type` | No | `allowedColumnValues`; default `"allowedColumnValues"` |

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
  "allowedValues": [
    {
      "value": "2026-10-01T00:00:00Z",
      "type": "date"
    }
  ],
  "allowNull": false,
  "severity": "MODERATE",
  "type": "allowedColumnValues"
}
```

## Complete replacement example

```json
{
  "allowedValues": [
    {
      "value": "2026-10-01T00:00:00Z",
      "type": "date"
    }
  ],
  "severity": "MODERATE",
  "allowNull": false,
  "type": "allowedColumnValues"
}
```

These synthetic examples demonstrate typed payload shape for prepared SDK
1.101.0. Replace dataset/branch, column names and policy values using the actual
resource schema and monitoring requirement. Local validation does not save a
check, evaluate a dataset or prove authorization.
