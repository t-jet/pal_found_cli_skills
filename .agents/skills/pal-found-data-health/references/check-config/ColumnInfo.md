# ColumnInfo

[Configuration guide](../check-config.md)

Information about a column including its name and type.

| JSON field | Required | Contract |
| --- | --- | --- |
| `name` | Yes | string |
| `columnType` | No | `ARRAY`, `BINARY`, `BOOLEAN`, `BYTE`, `DATE`, `DECIMAL`, `DOUBLE`, `FLOAT`, `INTEGER`, `LONG`, `MAP`, `SHORT`, `STRING`, `STRUCT`, `TIMESTAMP` or null; default `null` |

## Example JSON

```json
{
  "name": "status",
  "columnType": "STRING"
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
