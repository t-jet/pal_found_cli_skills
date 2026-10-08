# PercentageBounds

[Configuration guide](../check-config.md)

The configuration for the range of percentage values between which the health check is expected to succeed.

| JSON field | Required | Contract |
| --- | --- | --- |
| `lowerBoundPercentage` | No | number or null; default `null` |
| `upperBoundPercentage` | No | number or null; default `null` |

## Example JSON

```json
{
  "lowerBoundPercentage": 0,
  "upperBoundPercentage": 10
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
