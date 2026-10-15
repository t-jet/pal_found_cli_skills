# DateBounds

[Configuration guide](../check-config.md)

The range of date values a check is expected to be within.

| JSON field | Required | Contract |
| --- | --- | --- |
| `lowerBound` | No | string (date-time) or null; default `null` |
| `upperBound` | No | string (date-time) or null; default `null` |

## Example JSON

```json
{
  "lowerBound": "2026-10-01T00:00:00Z",
  "upperBound": "2026-10-01T00:00:00Z"
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
