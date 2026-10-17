# foundry_sdk.v2.functions.models.StreamingQueryError


An error that occurred during query execution.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| error_code | errorCode | str | required; no default | No additional field description in SDK source. |
| error_name | errorName | str | required; no default | No additional field description in SDK source. |
| error_instance_id | errorInstanceId | str | required; no default | No additional field description in SDK source. |
| error_description | errorDescription | typing.Optional[str] | default None | No additional field description in SDK source. |
| parameters | parameters | typing.Dict[str, typing.Any] | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['error'] | 'error' | No additional field description in SDK source. |

```python
class StreamingQueryError(core.ModelBase):
    """An error that occurred during query execution."""

    error_code: str = pydantic.Field(alias=str("errorCode"))  # type: ignore[literal-required]
    error_name: str = pydantic.Field(alias=str("errorName"))  # type: ignore[literal-required]
    error_instance_id: str = pydantic.Field(alias=str("errorInstanceId"))  # type: ignore[literal-required]
    error_description: typing.Optional[str] = pydantic.Field(alias=str("errorDescription"), default=None)  # type: ignore[literal-required]
    parameters: typing.Dict[str, typing.Any]
    type: typing.Literal["error"] = "error"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](StreamingQueryError.md)
