# foundry_sdk.v2.ontologies.models.GetQueryTypeByRidBatchRequestElement


GetQueryTypeByRidBatchRequestElement

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| query_type_rid | queryTypeRid | FunctionRid | required; no default | No additional field description in SDK source. |
| function_version | functionVersion | typing.Optional[FunctionVersion] | default None | No additional field description in SDK source. |

```python
class GetQueryTypeByRidBatchRequestElement(core.ModelBase):
    """GetQueryTypeByRidBatchRequestElement"""

    query_type_rid: FunctionRid = pydantic.Field(alias=str("queryTypeRid"))  # type: ignore[literal-required]
    function_version: typing.Optional[FunctionVersion] = pydantic.Field(alias=str("functionVersion"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.FunctionRid](FunctionRid.md)
- [foundry_sdk.v2.ontologies.models.FunctionVersion](FunctionVersion.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetQueryTypeByRidBatchRequestElement.md)
