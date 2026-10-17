# foundry_sdk.v2.media_sets.models.GroundControlPoint


A ground control point for geo-referencing.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| pix_x | pixX | typing.Optional[float] | default None | The pixel X coordinate. |
| pix_y | pixY | typing.Optional[float] | default None | The pixel Y coordinate. |
| proj_x | projX | typing.Optional[float] | default None | The projected X coordinate. |
| proj_y | projY | typing.Optional[float] | default None | The projected Y coordinate. |
| proj_z | projZ | typing.Optional[float] | default None | The projected Z coordinate. |

```python
class GroundControlPoint(core.ModelBase):
    """A ground control point for geo-referencing."""

    pix_x: typing.Optional[float] = pydantic.Field(alias=str("pixX"), default=None)  # type: ignore[literal-required]
    """The pixel X coordinate."""

    pix_y: typing.Optional[float] = pydantic.Field(alias=str("pixY"), default=None)  # type: ignore[literal-required]
    """The pixel Y coordinate."""

    proj_x: typing.Optional[float] = pydantic.Field(alias=str("projX"), default=None)  # type: ignore[literal-required]
    """The projected X coordinate."""

    proj_y: typing.Optional[float] = pydantic.Field(alias=str("projY"), default=None)  # type: ignore[literal-required]
    """The projected Y coordinate."""

    proj_z: typing.Optional[float] = pydantic.Field(alias=str("projZ"), default=None)  # type: ignore[literal-required]
    """The projected Z coordinate."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GroundControlPoint.md)
