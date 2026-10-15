# SchemaComparisonConfig

[Configuration guide](../check-config.md)

Configuration for schema comparison validation with severity settings.

| JSON field | Required | Contract |
| --- | --- | --- |
| `expectedSchema` | Yes | [SchemaInfo](SchemaInfo.md) |
| `schemaComparisonType` | Yes | `EXACT_MATCH_ORDERED_COLUMNS`, `EXACT_MATCH_UNORDERED_COLUMNS`, `COLUMN_ADDITIONS_ALLOWED`, `COLUMN_ADDITIONS_ALLOWED_STRICT` |
| `severity` | Yes | `MODERATE`, `CRITICAL` |

## Example JSON

```json
{
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
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
