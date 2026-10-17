# foundry_sdk.v2.ontologies.models.OntologyValueType


OntologyValueType

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| api_name | apiName | ValueTypeApiName | required; no default | No additional field description in SDK source. |
| display_name | displayName | core_models.DisplayName | required; no default | No additional field description in SDK source. |
| description | description | typing.Optional[str] | None | No additional field description in SDK source. |
| rid | rid | ValueTypeRid | required; no default | No additional field description in SDK source. |
| status | status | typing.Optional[ValueTypeStatus] | None | No additional field description in SDK source. |
| field_type | fieldType | ValueTypeFieldType | required; no default | No additional field description in SDK source. |
| version | version | str | required; no default | No additional field description in SDK source. |
| constraints | constraints | typing.List[ValueTypeConstraint] | required; no default | No additional field description in SDK source. |

```python
class OntologyValueType(core.ModelBase):
    """OntologyValueType"""

    api_name: ValueTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    rid: ValueTypeRid
    status: typing.Optional[ValueTypeStatus] = None
    field_type: ValueTypeFieldType = pydantic.Field(alias=str("fieldType"))  # type: ignore[literal-required]
    version: str
    constraints: typing.List[ValueTypeConstraint]
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.DisplayName](../../core/models/DisplayName.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeApiName](ValueTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeConstraint](ValueTypeConstraint.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeFieldType](ValueTypeFieldType.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeRid](ValueTypeRid.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeStatus](ValueTypeStatus.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OntologyValueType.md)
