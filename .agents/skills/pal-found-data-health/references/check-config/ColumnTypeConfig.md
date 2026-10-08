# ColumnTypeConfig

[Configuration guide](../check-config.md)

Configuration for column type validation with severity settings.

| JSON field | Required | Contract |
| --- | --- | --- |
| `columnName` | Yes | string |
| `expectedType` | No | `ARRAY`, `BINARY`, `BOOLEAN`, `BYTE`, `DATE`, `DECIMAL`, `DOUBLE`, `FLOAT`, `INTEGER`, `LONG`, `MAP`, `SHORT`, `STRING`, `STRUCT`, `TIMESTAMP` or null; default `null` |
| `severity` | Yes | `MODERATE`, `CRITICAL` |

## Example JSON

```json
{
  "columnName": "status",
  "expectedType": "STRING",
  "severity": "MODERATE"
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
