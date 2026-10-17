# foundry_sdk.v2.connectivity.models.QueryParameterApiKey


QueryParameterApiKey

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| query_parameter_name | queryParameterName | str | required; no default | The name of the query parameter that the API key is passed in. |
| type | type | typing.Literal['queryParameter'] | 'queryParameter' | No additional field description in SDK source. |

```python
class QueryParameterApiKey(core.ModelBase):
    """QueryParameterApiKey"""

    query_parameter_name: str = pydantic.Field(alias=str("queryParameterName"))  # type: ignore[literal-required]
    """The name of the query parameter that the API key is passed in."""

    type: typing.Literal["queryParameter"] = "queryParameter"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](QueryParameterApiKey.md)
