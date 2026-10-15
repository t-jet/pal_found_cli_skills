# StatusCheckConfig

[Configuration guide](../check-config.md)

StatusCheckConfig

| JSON field | Required | Contract |
| --- | --- | --- |
| `severity` | Yes | `MODERATE`, `CRITICAL` |
| `escalationConfig` | No | [EscalationConfig](EscalationConfig.md) or null; default `null` |

## Example JSON

```json
{
  "severity": "MODERATE",
  "escalationConfig": {
    "failuresToCritical": 3,
    "timeIntervalInSeconds": 3600
  }
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
