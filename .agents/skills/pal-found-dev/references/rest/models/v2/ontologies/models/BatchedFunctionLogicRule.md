# foundry_sdk.v2.ontologies.models.BatchedFunctionLogicRule


BatchedFunctionLogicRule

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_set_rid_input_name | objectSetRidInputName | FunctionParameterName | required; no default | No additional field description in SDK source. |
| function_rule | functionRule | FunctionLogicRule | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['batchedFunction'] | 'batchedFunction' | No additional field description in SDK source. |

```python
class BatchedFunctionLogicRule(core.ModelBase):
    """BatchedFunctionLogicRule"""

    object_set_rid_input_name: FunctionParameterName = pydantic.Field(alias=str("objectSetRidInputName"))  # type: ignore[literal-required]
    function_rule: FunctionLogicRule = pydantic.Field(alias=str("functionRule"))  # type: ignore[literal-required]
    type: typing.Literal["batchedFunction"] = "batchedFunction"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.FunctionLogicRule](FunctionLogicRule.md)
- [foundry_sdk.v2.ontologies.models.FunctionParameterName](FunctionParameterName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](BatchedFunctionLogicRule.md)
