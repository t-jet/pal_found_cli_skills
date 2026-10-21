# foundry_sdk.v2.models.models.ModelApiTabularType


ModelApiTabularType

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| name | name | str | required; no default | No additional field description in SDK source. |
| required | required | typing.Optional[bool] | None | true by default; false if the input or output can be null or omitted |
| columns | columns | typing.List[ModelApiColumn] | required; no default | No additional field description in SDK source. |
| format | format | typing.Optional[ModelApiTabularFormat] | None | Dataframe format the model will receive or is expected to return for this input or output. PANDAS is the default. |
| type | type | typing.Literal['tabular'] | 'tabular' | No additional field description in SDK source. |

```python
class ModelApiTabularType(core.ModelBase):
    """ModelApiTabularType"""

    name: str
    required: typing.Optional[bool] = None
    """true by default; false if the input or output can be null or omitted"""

    columns: typing.List[ModelApiColumn]
    format: typing.Optional[ModelApiTabularFormat] = None
    """Dataframe format the model will receive or is expected to return for this input or output. PANDAS is the default."""

    type: typing.Literal["tabular"] = "tabular"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.ModelApiColumn](ModelApiColumn.md)
- [foundry_sdk.v2.models.models.ModelApiTabularFormat](ModelApiTabularFormat.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ModelApiTabularType.md)
