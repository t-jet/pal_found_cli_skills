# MedianDeviation

[Configuration guide](../check-config.md)

The number of thresholds the build's duration differs from the median.

| JSON field | Required | Contract |
| --- | --- | --- |
| `boundsType` | No | `LOWER_BOUND`, `UPPER_BOUND`, `TWO_TAILED` or null; default `null` |
| `dataPoints` | Yes | integer |
| `deviationThreshold` | Yes | number |

## Example JSON

```json
{
  "boundsType": "LOWER_BOUND",
  "dataPoints": 5,
  "deviationThreshold": 2
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
