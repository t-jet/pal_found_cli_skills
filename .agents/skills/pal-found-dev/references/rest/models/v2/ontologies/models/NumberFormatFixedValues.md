# foundry_sdk.v2.ontologies.models.NumberFormatFixedValues


Map integer values to custom human-readable strings.
Example: {1: "First", 2: "Second", 3: "Third"} would display 2 as "Second".

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| values | values | typing.Dict[FixedValuesMapKey, str] | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['fixedValues'] | 'fixedValues' | No additional field description in SDK source. |

```python
class NumberFormatFixedValues(core.ModelBase):
    """
    Map integer values to custom human-readable strings.
    Example: {1: "First", 2: "Second", 3: "Third"} would display 2 as "Second".
    """

    values: typing.Dict[FixedValuesMapKey, str]
    type: typing.Literal["fixedValues"] = "fixedValues"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.FixedValuesMapKey](FixedValuesMapKey.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NumberFormatFixedValues.md)
