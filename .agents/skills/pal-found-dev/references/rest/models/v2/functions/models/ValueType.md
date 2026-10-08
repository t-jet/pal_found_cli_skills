# foundry_sdk.v2.functions.models.ValueType


ValueType

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | ValueTypeRid | required; no default | No additional field description in SDK source. |
| version | version | ValueTypeVersion | required; no default | No additional field description in SDK source. |
| version_id | versionId | ValueTypeVersionId | required; no default | No additional field description in SDK source. |
| api_name | apiName | ValueTypeApiName | required; no default | No additional field description in SDK source. |
| display_name | displayName | core_models.DisplayName | required; no default | No additional field description in SDK source. |
| description | description | typing.Optional[ValueTypeDescription] | None | No additional field description in SDK source. |
| base_type | baseType | typing.Optional[ValueTypeDataType] | default None | No additional field description in SDK source. |
| constraints | constraints | typing.List[ValueTypeConstraint] | required; no default | No additional field description in SDK source. |

```python
class ValueType(core.ModelBase):
    """ValueType"""

    rid: ValueTypeRid
    version: ValueTypeVersion
    version_id: ValueTypeVersionId = pydantic.Field(alias=str("versionId"))  # type: ignore[literal-required]
    api_name: ValueTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[ValueTypeDescription] = None
    base_type: typing.Optional[ValueTypeDataType] = pydantic.Field(alias=str("baseType"), default=None)  # type: ignore[literal-required]
    constraints: typing.List[ValueTypeConstraint]
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.DisplayName](../../core/models/DisplayName.md)
- [foundry_sdk.v2.functions.models.ValueTypeApiName](ValueTypeApiName.md)
- [foundry_sdk.v2.functions.models.ValueTypeConstraint](ValueTypeConstraint.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataType](ValueTypeDataType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDescription](ValueTypeDescription.md)
- [foundry_sdk.v2.functions.models.ValueTypeRid](ValueTypeRid.md)
- [foundry_sdk.v2.functions.models.ValueTypeVersion](ValueTypeVersion.md)
- [foundry_sdk.v2.functions.models.ValueTypeVersionId](ValueTypeVersionId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ValueType.md)
