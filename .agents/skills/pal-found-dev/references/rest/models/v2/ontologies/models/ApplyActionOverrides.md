# foundry_sdk.v2.ontologies.models.ApplyActionOverrides


ApplyActionOverrides

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| unique_identifier_link_id_values | uniqueIdentifierLinkIdValues | typing.Dict[UniqueIdentifierLinkId, UniqueIdentifierValue] | required; no default | No additional field description in SDK source. |
| action_execution_time | actionExecutionTime | typing.Optional[ActionExecutionTime] | default None | No additional field description in SDK source. |

```python
class ApplyActionOverrides(core.ModelBase):
    """ApplyActionOverrides"""

    unique_identifier_link_id_values: typing.Dict[UniqueIdentifierLinkId, UniqueIdentifierValue] = pydantic.Field(alias=str("uniqueIdentifierLinkIdValues"))  # type: ignore[literal-required]
    action_execution_time: typing.Optional[ActionExecutionTime] = pydantic.Field(alias=str("actionExecutionTime"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.ActionExecutionTime](ActionExecutionTime.md)
- [foundry_sdk.v2.ontologies.models.UniqueIdentifierLinkId](UniqueIdentifierLinkId.md)
- [foundry_sdk.v2.ontologies.models.UniqueIdentifierValue](UniqueIdentifierValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ApplyActionOverrides.md)
