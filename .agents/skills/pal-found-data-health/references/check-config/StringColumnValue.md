# StringColumnValue

[Configuration guide](../check-config.md)

A string column value.

| JSON field | Required | Contract |
| --- | --- | --- |
| `value` | Yes | string |
| `type` | No | `string`; default `"string"` |

## Example JSON

```json
{
  "value": "ready",
  "type": "string"
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
