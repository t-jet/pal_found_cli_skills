# foundry_sdk.v2.functions.models.ExecutionSubmitted


The query was submitted for async processing.
Use the executionId to poll for results via getResult or to cancel via cancel.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| execution_id | executionId | ExecutionId | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['submitted'] | 'submitted' | No additional field description in SDK source. |

```python
class ExecutionSubmitted(core.ModelBase):
    """
    The query was submitted for async processing.
    Use the executionId to poll for results via getResult or to cancel via cancel.
    """

    execution_id: ExecutionId = pydantic.Field(alias=str("executionId"))  # type: ignore[literal-required]
    type: typing.Literal["submitted"] = "submitted"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.functions.models.ExecutionId](ExecutionId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ExecutionSubmitted.md)
