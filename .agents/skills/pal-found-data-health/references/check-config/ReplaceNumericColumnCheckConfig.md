# ReplaceNumericColumnCheckConfig

[Configuration guide](../check-config.md)

ReplaceNumericColumnCheckConfig

| JSON field | Required | Contract |
| --- | --- | --- |
| `numericBounds` | No | [NumericBoundsConfig](NumericBoundsConfig.md) or null; default `null` |
| `trend` | No | [TrendConfig](TrendConfig.md) or null; default `null` |

## Example JSON

```json
{
  "numericBounds": {
    "numericBounds": {
      "lowerBound": 0,
      "upperBound": 100
    },
    "severity": "MODERATE"
  },
  "trend": {
    "trendType": "NON_INCREASING",
    "differenceBounds": {
      "lowerBound": 0,
      "upperBound": 100
    },
    "severity": "MODERATE"
  }
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
