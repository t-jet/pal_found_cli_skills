# TimeBounds

[Configuration guide](../check-config.md)

The configuration for the range of time between which the health check is expected to succeed.

| JSON field | Required | Contract |
| --- | --- | --- |
| `lowerBoundInSeconds` | No | integer or null; default `null` |
| `upperBoundInSeconds` | No | integer or null; default `null` |

## Example JSON

```json
{
  "lowerBoundInSeconds": 0,
  "upperBoundInSeconds": 3600
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
