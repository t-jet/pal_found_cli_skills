# NumericBounds

[Configuration guide](../check-config.md)

The range of numeric values a check is expected to be within.

| JSON field | Required | Contract |
| --- | --- | --- |
| `lowerBound` | No | number or null; default `null` |
| `upperBound` | No | number or null; default `null` |

## Example JSON

```json
{
  "lowerBound": 0,
  "upperBound": 100
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
