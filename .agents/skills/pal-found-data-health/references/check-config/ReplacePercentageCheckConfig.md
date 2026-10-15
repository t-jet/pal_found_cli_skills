# ReplacePercentageCheckConfig

[Configuration guide](../check-config.md)

ReplacePercentageCheckConfig

| JSON field | Required | Contract |
| --- | --- | --- |
| `medianDeviation` | No | [MedianDeviationConfig](MedianDeviationConfig.md) or null; default `null` |
| `percentageBounds` | No | [PercentageBoundsConfig](PercentageBoundsConfig.md) or null; default `null` |

## Example JSON

Supply at least one of `percentageBounds` or `medianDeviation`. Both may be
provided. SDK parsing can accept an empty pair because fields are optional,
but Foundry rejects it as `InvalidPercentageCheckConfig`.

```json
{
  "medianDeviation": {
    "medianDeviation": {
      "boundsType": "LOWER_BOUND",
      "dataPoints": 5,
      "deviationThreshold": 2
    },
    "severity": "MODERATE"
  },
  "percentageBounds": {
    "percentageBounds": {
      "lowerBoundPercentage": 0,
      "upperBoundPercentage": 10
    },
    "severity": "MODERATE"
  }
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
