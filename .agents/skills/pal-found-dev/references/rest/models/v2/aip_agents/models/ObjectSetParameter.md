# foundry_sdk.v2.aip_agents.models.ObjectSetParameter


ObjectSetParameter

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| expected_object_types | expectedObjectTypes | typing.List[ontologies_models.ObjectTypeId] | required; no default | The types of objects that are expected in ObjectSet values passed for this variable. |
| type | type | typing.Literal['objectSet'] | 'objectSet' | No additional field description in SDK source. |

```python
class ObjectSetParameter(core.ModelBase):
    """ObjectSetParameter"""

    expected_object_types: typing.List[ontologies_models.ObjectTypeId] = pydantic.Field(alias=str("expectedObjectTypes"))  # type: ignore[literal-required]
    """The types of objects that are expected in ObjectSet values passed for this variable."""

    type: typing.Literal["objectSet"] = "objectSet"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeId](../../ontologies/models/ObjectTypeId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectSetParameter.md)
