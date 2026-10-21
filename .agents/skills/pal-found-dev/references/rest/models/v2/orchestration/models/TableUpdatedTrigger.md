# foundry_sdk.v2.orchestration.models.TableUpdatedTrigger


Trigger whenever a new transaction is committed to the
table on the target branch.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| table_rid | tableRid | core_models.TableRid | required; no default | No additional field description in SDK source. |
| branch_name | branchName | core_models.BranchName | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['tableUpdated'] | 'tableUpdated' | No additional field description in SDK source. |

```python
class TableUpdatedTrigger(core.ModelBase):
    """
    Trigger whenever a new transaction is committed to the
    table on the target branch.
    """

    table_rid: core_models.TableRid = pydantic.Field(alias=str("tableRid"))  # type: ignore[literal-required]
    branch_name: core_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    type: typing.Literal["tableUpdated"] = "tableUpdated"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.core.models.TableRid](../../core/models/TableRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TableUpdatedTrigger.md)
