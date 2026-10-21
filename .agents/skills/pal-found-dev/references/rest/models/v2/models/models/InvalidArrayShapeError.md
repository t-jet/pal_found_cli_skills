# foundry_sdk.v2.models.models.InvalidArrayShapeError


Array dimensions do not match expected ndarray shape.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| expected_shape | expectedShape | typing.List[int] | required; no default | The expected array shape from the model API specification |
| actual_shape | actualShape | typing.Optional[typing.List[int]] | default None | The actual shape of the provided array |
| type | type | typing.Literal['invalidArrayShape'] | 'invalidArrayShape' | No additional field description in SDK source. |

```python
class InvalidArrayShapeError(core.ModelBase):
    """Array dimensions do not match expected ndarray shape."""

    expected_shape: typing.List[int] = pydantic.Field(alias=str("expectedShape"))  # type: ignore[literal-required]
    """The expected array shape from the model API specification"""

    actual_shape: typing.Optional[typing.List[int]] = pydantic.Field(alias=str("actualShape"), default=None)  # type: ignore[literal-required]
    """The actual shape of the provided array"""

    type: typing.Literal["invalidArrayShape"] = "invalidArrayShape"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidArrayShapeError.md)
