# foundry_sdk.v2.ontologies.models.QueryTypeV2


Represents a query type in the Ontology.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| api_name | apiName | QueryApiName | required; no default | No additional field description in SDK source. |
| description | description | typing.Optional[str] | None | No additional field description in SDK source. |
| display_name | displayName | typing.Optional[core_models.DisplayName] | default None | No additional field description in SDK source. |
| parameters | parameters | typing.Dict[ParameterId, QueryParameterV2] | required; no default | No additional field description in SDK source. |
| output | output | QueryDataType | required; no default | No additional field description in SDK source. |
| rid | rid | FunctionRid | required; no default | No additional field description in SDK source. |
| version | version | FunctionVersion | required; no default | No additional field description in SDK source. |
| type_references | typeReferences | typing.Dict[TypeReferenceIdentifier, QueryDataType] | required; no default | No additional field description in SDK source. |

```python
class QueryTypeV2(core.ModelBase):
    """Represents a query type in the Ontology."""

    api_name: QueryApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    parameters: typing.Dict[ParameterId, QueryParameterV2]
    output: QueryDataType
    rid: FunctionRid
    version: FunctionVersion
    type_references: typing.Dict[TypeReferenceIdentifier, QueryDataType] = pydantic.Field(alias=str("typeReferences"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.DisplayName](../../core/models/DisplayName.md)
- [foundry_sdk.v2.ontologies.models.FunctionRid](FunctionRid.md)
- [foundry_sdk.v2.ontologies.models.FunctionVersion](FunctionVersion.md)
- [foundry_sdk.v2.ontologies.models.ParameterId](ParameterId.md)
- [foundry_sdk.v2.ontologies.models.QueryApiName](QueryApiName.md)
- [foundry_sdk.v2.ontologies.models.QueryDataType](QueryDataType.md)
- [foundry_sdk.v2.ontologies.models.QueryParameterV2](QueryParameterV2.md)
- [foundry_sdk.v2.ontologies.models.TypeReferenceIdentifier](TypeReferenceIdentifier.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](QueryTypeV2.md)
