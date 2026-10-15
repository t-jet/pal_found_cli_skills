# DateColumnValue

[Configuration guide](../check-config.md)

A date column value.

| JSON field | Required | Contract |
| --- | --- | --- |
| `value` | Yes | string (date-time) |
| `type` | No | `date`; default `"date"` |

## Example JSON

```json
{
  "value": "2026-10-01T00:00:00Z",
  "type": "date"
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
