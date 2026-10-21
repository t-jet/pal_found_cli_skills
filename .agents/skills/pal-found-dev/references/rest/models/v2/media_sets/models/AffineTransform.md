# foundry_sdk.v2.media_sets.models.AffineTransform


An affine transformation for geo-referencing.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| x_translate | xTranslate | typing.Optional[float] | default None | No additional field description in SDK source. |
| x_scale | xScale | typing.Optional[float] | default None | No additional field description in SDK source. |
| x_shear | xShear | typing.Optional[float] | default None | No additional field description in SDK source. |
| y_translate | yTranslate | typing.Optional[float] | default None | No additional field description in SDK source. |
| y_shear | yShear | typing.Optional[float] | default None | No additional field description in SDK source. |
| y_scale | yScale | typing.Optional[float] | default None | No additional field description in SDK source. |

```python
class AffineTransform(core.ModelBase):
    """An affine transformation for geo-referencing."""

    x_translate: typing.Optional[float] = pydantic.Field(alias=str("xTranslate"), default=None)  # type: ignore[literal-required]
    x_scale: typing.Optional[float] = pydantic.Field(alias=str("xScale"), default=None)  # type: ignore[literal-required]
    x_shear: typing.Optional[float] = pydantic.Field(alias=str("xShear"), default=None)  # type: ignore[literal-required]
    y_translate: typing.Optional[float] = pydantic.Field(alias=str("yTranslate"), default=None)  # type: ignore[literal-required]
    y_shear: typing.Optional[float] = pydantic.Field(alias=str("yShear"), default=None)  # type: ignore[literal-required]
    y_scale: typing.Optional[float] = pydantic.Field(alias=str("yScale"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AffineTransform.md)
