# PercentageBoundsConfig

[Configuration guide](../check-config.md)

Configuration for percentage bounds check with severity settings.

| JSON field | Required | Contract |
| --- | --- | --- |
| `percentageBounds` | Yes | [PercentageBounds](PercentageBounds.md) |
| `severity` | Yes | `MODERATE`, `CRITICAL` |

## Example JSON

```json
{
  "percentageBounds": {
    "lowerBoundPercentage": 0,
    "upperBoundPercentage": 10
  },
  "severity": "MODERATE"
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
