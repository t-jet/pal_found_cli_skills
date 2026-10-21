# foundry_sdk.v2.ontologies.models.FunctionLogicRule


FunctionLogicRule

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| function_rid | functionRid | FunctionRid | required; no default | No additional field description in SDK source. |
| function_version | functionVersion | FunctionVersion | required; no default | No additional field description in SDK source. |
| function_input_values | functionInputValues | typing.Dict[FunctionParameterName, LogicRuleArgument] | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['function'] | 'function' | No additional field description in SDK source. |

```python
class FunctionLogicRule(core.ModelBase):
    """FunctionLogicRule"""

    function_rid: FunctionRid = pydantic.Field(alias=str("functionRid"))  # type: ignore[literal-required]
    function_version: FunctionVersion = pydantic.Field(alias=str("functionVersion"))  # type: ignore[literal-required]
    function_input_values: typing.Dict[FunctionParameterName, LogicRuleArgument] = pydantic.Field(alias=str("functionInputValues"))  # type: ignore[literal-required]
    type: typing.Literal["function"] = "function"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.FunctionParameterName](FunctionParameterName.md)
- [foundry_sdk.v2.ontologies.models.FunctionRid](FunctionRid.md)
- [foundry_sdk.v2.ontologies.models.FunctionVersion](FunctionVersion.md)
- [foundry_sdk.v2.ontologies.models.LogicRuleArgument](LogicRuleArgument.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FunctionLogicRule.md)
