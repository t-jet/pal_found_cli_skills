# MedianDeviationConfig

[Configuration guide](../check-config.md)

Configuration for median deviation check with severity settings.

| JSON field | Required | Contract |
| --- | --- | --- |
| `medianDeviation` | Yes | [MedianDeviation](MedianDeviation.md) |
| `severity` | Yes | `MODERATE`, `CRITICAL` |

## Example JSON

```json
{
  "medianDeviation": {
    "boundsType": "LOWER_BOUND",
    "dataPoints": 5,
    "deviationThreshold": 2
  },
  "severity": "MODERATE"
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
