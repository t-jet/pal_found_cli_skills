# foundry_sdk.v2.ontologies.models.SyncApplyActionResponseV2


SyncApplyActionResponseV2

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| operation_id | operationId | typing.Optional[core.RID] | default None | No additional field description in SDK source. |
| validation | validation | typing.Optional[ValidateActionResponseV2] | None | No additional field description in SDK source. |
| edits | edits | typing.Optional[ActionResults] | None | No additional field description in SDK source. |

```python
class SyncApplyActionResponseV2(core.ModelBase):
    """SyncApplyActionResponseV2"""

    operation_id: typing.Optional[core.RID] = pydantic.Field(alias=str("operationId"), default=None)  # type: ignore[literal-required]
    validation: typing.Optional[ValidateActionResponseV2] = None
    edits: typing.Optional[ActionResults] = None
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)
- [foundry_sdk.v2.ontologies.models.ActionResults](ActionResults.md)
- [foundry_sdk.v2.ontologies.models.ValidateActionResponseV2](ValidateActionResponseV2.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SyncApplyActionResponseV2.md)
