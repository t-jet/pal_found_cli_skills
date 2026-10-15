# DatasetSubject

[Configuration guide](../check-config.md)

A dataset resource type.

| JSON field | Required | Contract |
| --- | --- | --- |
| `datasetRid` | Yes | string; RID pattern `^ri\.[a-z][a-z0-9-]*\.([a-z0-9][a-z0-9\-]*)?\.[a-z][a-z0-9-]*\.[a-zA-Z0-9._-]+$` |
| `branchId` | Yes | string |

## Example JSON

```json
{
  "datasetRid": "ri.foundry.main.dataset.a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "branchId": "master"
}
```

Fields use JSON aliases, including case. `null` is an explicit nullable value;
an omitted optional field uses its listed default. This is a structural SDK
contract. Authorization, supported dataset types and semantic bounds are checked
by Foundry; local model validation cannot prove the rule can be saved/evaluated.
