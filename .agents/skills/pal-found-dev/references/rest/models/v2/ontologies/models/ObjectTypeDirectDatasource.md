# foundry_sdk.v2.ontologies.models.ObjectTypeDirectDatasource


An object type datasource backed by a direct-write source. Property values are written directly to the
datasource rather than being read from a separate Foundry resource. Unlike an edits-only datasource, a direct
datasource has a backing source that values are written to by some writer. An edits-only datasource has no
backing source at all and its properties are populated solely via Actions.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| direct_source_rid | directSourceRid | DirectSourceRid | required; no default | No additional field description in SDK source. |
| property_mapping | propertyMapping | typing.Dict[PropertyApiName, PropertyTypeMappingInfo] | required; no default | A mapping from property API name to a description of how that property is bound to the direct datasource.<br>    Properties whose mapping info cannot be modeled are omitted. |
| type | type | typing.Literal['direct'] | 'direct' | No additional field description in SDK source. |

```python
class ObjectTypeDirectDatasource(core.ModelBase):
    """
    An object type datasource backed by a direct-write source. Property values are written directly to the
    datasource rather than being read from a separate Foundry resource. Unlike an edits-only datasource, a direct
    datasource has a backing source that values are written to by some writer. An edits-only datasource has no
    backing source at all and its properties are populated solely via Actions.
    """

    direct_source_rid: DirectSourceRid = pydantic.Field(alias=str("directSourceRid"))  # type: ignore[literal-required]
    property_mapping: typing.Dict[PropertyApiName, PropertyTypeMappingInfo] = pydantic.Field(alias=str("propertyMapping"))  # type: ignore[literal-required]
    """
    A mapping from property API name to a description of how that property is bound to the direct datasource.
    Properties whose mapping info cannot be modeled are omitted.
    """

    type: typing.Literal["direct"] = "direct"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.DirectSourceRid](DirectSourceRid.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeMappingInfo](PropertyTypeMappingInfo.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectTypeDirectDatasource.md)
