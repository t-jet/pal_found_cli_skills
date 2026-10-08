# DateBoundsConfig

[Configuration guide](../check-config.md)

Configuration for date bounds check with severity settings.

| JSON field | Required | Contract |
| --- | --- | --- |
| `dateBounds` | Yes | [DateBounds](DateBounds.md) |
| `severity` | Yes | `MODERATE`, `CRITICAL` |

## Example JSON

```json
{
  "dateBounds": {
    "lowerBound": "2026-10-01T00:00:00Z",
    "upperBound": "2026-10-01T00:00:00Z"
  },
  "severity": "MODERATE"
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
