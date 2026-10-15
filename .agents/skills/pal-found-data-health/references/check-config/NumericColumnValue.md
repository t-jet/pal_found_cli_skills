# NumericColumnValue

[Configuration guide](../check-config.md)

A numeric column value.

| JSON field | Required | Contract |
| --- | --- | --- |
| `value` | Yes | number |
| `type` | No | `numeric`; default `"numeric"` |

## Example JSON

```json
{
  "value": 1,
  "type": "numeric"
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
