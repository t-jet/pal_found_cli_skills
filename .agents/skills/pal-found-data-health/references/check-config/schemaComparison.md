# schemaComparison

[Configuration guide](../check-config.md)

Checks the dataset schema against an expected schema.

## Create fields

| JSON field | Required | Contract |
| --- | --- | --- |
| `subject` | Yes | [DatasetSubject](DatasetSubject.md) |
| `schemaComparisonConfig` | Yes | [SchemaComparisonConfig](SchemaComparisonConfig.md) |
| `type` | No | `schemaComparison`; default `"schemaComparison"` |

## Replace fields

| JSON field | Required | Contract |
| --- | --- | --- |
| `schemaComparisonConfig` | Yes | [SchemaComparisonConfig](SchemaComparisonConfig.md) |
| `type` | No | `schemaComparison`; default `"schemaComparison"` |

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
  "schemaComparisonConfig": {
    "expectedSchema": {
      "columns": [
        {
          "name": "status",
          "columnType": "STRING"
        }
      ]
    },
    "schemaComparisonType": "EXACT_MATCH_ORDERED_COLUMNS",
    "severity": "MODERATE"
  },
  "type": "schemaComparison"
}
```

## Complete replacement example

```json
{
  "schemaComparisonConfig": {
    "expectedSchema": {
      "columns": [
        {
          "name": "status",
          "columnType": "STRING"
        }
      ]
    },
    "schemaComparisonType": "EXACT_MATCH_ORDERED_COLUMNS",
    "severity": "MODERATE"
  },
  "type": "schemaComparison"
}
```

These synthetic examples demonstrate typed payload shape for prepared SDK
1.101.0. Replace dataset/branch, column names and policy values using the actual
resource schema and monitoring requirement. Local validation does not save a
check, evaluate a dataset or prove authorization.
