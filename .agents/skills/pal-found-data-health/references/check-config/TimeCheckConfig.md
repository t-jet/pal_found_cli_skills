# TimeCheckConfig

[Configuration guide](../check-config.md)

TimeCheckConfig

| JSON field | Required | Contract |
| --- | --- | --- |
| `timeBounds` | No | [TimeBoundsConfig](TimeBoundsConfig.md) or null; default `null` |
| `medianDeviation` | No | [MedianDeviationConfig](MedianDeviationConfig.md) or null; default `null` |

## Example JSON

Supply at least one of `timeBounds` or `medianDeviation`. Both may be provided.
SDK parsing can accept both absent, but Foundry rejects that configuration as
`InvalidTimeCheckConfig`.

```json
{
  "timeBounds": {
    "timeBounds": {
      "lowerBoundInSeconds": 0,
      "upperBoundInSeconds": 3600
    },
    "severity": "MODERATE"
  },
  "medianDeviation": {
    "medianDeviation": {
      "boundsType": "LOWER_BOUND",
      "dataPoints": 5,
      "deviationThreshold": 2
    },
    "severity": "MODERATE"
  }
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
