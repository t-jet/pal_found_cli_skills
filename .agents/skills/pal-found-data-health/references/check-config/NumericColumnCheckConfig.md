# NumericColumnCheckConfig

[Configuration guide](../check-config.md)

Configuration for numeric column-based checks (such as mean or median). At least one of numericBounds or trend must be specified. Both may be provided to validate both the absolute value range and the trend behavior over time.

| JSON field | Required | Contract |
| --- | --- | --- |
| `columnName` | Yes | string |
| `numericBounds` | No | [NumericBoundsConfig](NumericBoundsConfig.md) or null; default `null` |
| `trend` | No | [TrendConfig](TrendConfig.md) or null; default `null` |

## Example JSON

```json
{
  "columnName": "status",
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
