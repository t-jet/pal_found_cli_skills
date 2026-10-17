# foundry_sdk.v2.aip_agents.models.ObjectSetParameterValue


A value passed for `ObjectSetParameter` application variable types.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_set | objectSet | ontologies_models.ObjectSet | required; no default | No additional field description in SDK source. |
| ontology | ontology | ontologies_models.OntologyIdentifier | required; no default | The API name of the Ontology for the provided `ObjectSet`.<br>    To find the API name, use the `List ontologies` endpoint or check the Ontology Manager. |
| type | type | typing.Literal['objectSet'] | 'objectSet' | No additional field description in SDK source. |

```python
class ObjectSetParameterValue(core.ModelBase):
    """A value passed for `ObjectSetParameter` application variable types."""

    object_set: ontologies_models.ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    ontology: ontologies_models.OntologyIdentifier
    """
    The API name of the Ontology for the provided `ObjectSet`.
    To find the API name, use the `List ontologies` endpoint or check the [Ontology Manager](https://palantir.com/docs/foundry/ontology-manager/overview/).
    """

    type: typing.Literal["objectSet"] = "objectSet"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.ObjectSet](../../ontologies/models/ObjectSet.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../ontologies/models/OntologyIdentifier.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectSetParameterValue.md)
