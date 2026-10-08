# foundry_sdk.v2.models.models.ModelFunction


ModelFunction

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| function_rid | functionRid | ModelFunctionFunctionRid | required; no default | No additional field description in SDK source. |
| function_version | functionVersion | ModelFunctionFunctionVersion | required; no default | No additional field description in SDK source. |
| display_name | displayName | ModelFunctionDisplayName | required; no default | No additional field description in SDK source. |
| api_name | apiName | ModelFunctionApiName | required; no default | No additional field description in SDK source. |
| is_row_wise | isRowWise | ModelFunctionIsRowWise | required; no default | No additional field description in SDK source. |
| ontology_binding | ontologyBinding | typing.Optional[ontologies_models.OntologyRid] | default None | No additional field description in SDK source. |

```python
class ModelFunction(core.ModelBase):
    """ModelFunction"""

    function_rid: ModelFunctionFunctionRid = pydantic.Field(alias=str("functionRid"))  # type: ignore[literal-required]
    function_version: ModelFunctionFunctionVersion = pydantic.Field(alias=str("functionVersion"))  # type: ignore[literal-required]
    display_name: ModelFunctionDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    api_name: ModelFunctionApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    is_row_wise: ModelFunctionIsRowWise = pydantic.Field(alias=str("isRowWise"))  # type: ignore[literal-required]
    ontology_binding: typing.Optional[ontologies_models.OntologyRid] = pydantic.Field(alias=str("ontologyBinding"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.ModelFunctionApiName](ModelFunctionApiName.md)
- [foundry_sdk.v2.models.models.ModelFunctionDisplayName](ModelFunctionDisplayName.md)
- [foundry_sdk.v2.models.models.ModelFunctionFunctionRid](ModelFunctionFunctionRid.md)
- [foundry_sdk.v2.models.models.ModelFunctionFunctionVersion](ModelFunctionFunctionVersion.md)
- [foundry_sdk.v2.models.models.ModelFunctionIsRowWise](ModelFunctionIsRowWise.md)
- [foundry_sdk.v2.ontologies.models.OntologyRid](../../ontologies/models/OntologyRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ModelFunction.md)
