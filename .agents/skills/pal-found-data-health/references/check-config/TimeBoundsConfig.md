# TimeBoundsConfig

[Configuration guide](../check-config.md)

Configuration for time bounds check with severity settings.

| JSON field | Required | Contract |
| --- | --- | --- |
| `timeBounds` | Yes | [TimeBounds](TimeBounds.md) |
| `severity` | Yes | `MODERATE`, `CRITICAL` |

## Example JSON

```json
{
  "timeBounds": {
    "lowerBoundInSeconds": 0,
    "upperBoundInSeconds": 3600
  },
  "severity": "MODERATE"
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
