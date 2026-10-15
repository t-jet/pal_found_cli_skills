# TrendConfig

[Configuration guide](../check-config.md)

Configuration for trend-based validation with severity settings. At least one of trendType or differenceBounds must be specified. Both may be provided to validate both the trend pattern and the magnitude of change.

| JSON field | Required | Contract |
| --- | --- | --- |
| `trendType` | No | `NON_INCREASING`, `NON_DECREASING`, `STRICTLY_INCREASING`, `STRICTLY_DECREASING`, `CONSTANT` or null; default `null` |
| `differenceBounds` | No | [NumericBounds](NumericBounds.md) or null; default `null` |
| `severity` | Yes | `MODERATE`, `CRITICAL` |

## Example JSON

```json
{
  "trendType": "NON_INCREASING",
  "differenceBounds": {
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
