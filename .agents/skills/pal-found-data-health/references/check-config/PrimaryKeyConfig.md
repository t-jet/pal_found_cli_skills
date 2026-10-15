# PrimaryKeyConfig

[Configuration guide](../check-config.md)

Configuration for primary key validation with severity settings.

| JSON field | Required | Contract |
| --- | --- | --- |
| `columnNames` | Yes | array of string |
| `severity` | Yes | `MODERATE`, `CRITICAL` |

## Example JSON

```json
{
  "columnNames": [
    "order_id"
  ],
  "severity": "MODERATE"
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
