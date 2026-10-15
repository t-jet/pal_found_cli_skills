# EscalationConfig

[Configuration guide](../check-config.md)

The configuration for when the severity of the failing health check should be escalated to CRITICAL – after a given number of failures, possibly within a time interval.

| JSON field | Required | Contract |
| --- | --- | --- |
| `failuresToCritical` | Yes | integer |
| `timeIntervalInSeconds` | No | integer or null; default `null` |

## Example JSON

```json
{
  "failuresToCritical": 3,
  "timeIntervalInSeconds": 3600
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
