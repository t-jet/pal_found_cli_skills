# NumericBoundsConfig

[Configuration guide](../check-config.md)

Configuration for numeric bounds check with severity settings.

| JSON field | Required | Contract |
| --- | --- | --- |
| `numericBounds` | Yes | [NumericBounds](NumericBounds.md) |
| `severity` | Yes | `MODERATE`, `CRITICAL` |

## Example JSON

```json
{
  "numericBounds": {
    "lowerBound": 0,
    "upperBound": 100
  },
  "severity": "MODERATE"
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
