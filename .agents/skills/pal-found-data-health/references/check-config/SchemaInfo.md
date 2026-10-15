# SchemaInfo

[Configuration guide](../check-config.md)

Information about a dataset schema including all columns.

| JSON field | Required | Contract |
| --- | --- | --- |
| `columns` | Yes | array of [ColumnInfo](ColumnInfo.md) |

## Example JSON

```json
{
  "columns": [
    {
      "name": "status",
      "columnType": "STRING"
    }
  ]
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
