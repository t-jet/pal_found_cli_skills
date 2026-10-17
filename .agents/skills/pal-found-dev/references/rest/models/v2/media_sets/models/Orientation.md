# foundry_sdk.v2.media_sets.models.Orientation


The orientation information as encoded in EXIF metadata.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rotation_angle | rotationAngle | typing.Optional[RotationAngle] | default None | No additional field description in SDK source. |
| flip_axis | flipAxis | typing.Optional[FlipAxis] | default None | No additional field description in SDK source. |

```python
class Orientation(core.ModelBase):
    """The orientation information as encoded in EXIF metadata."""

    rotation_angle: typing.Optional[RotationAngle] = pydantic.Field(alias=str("rotationAngle"), default=None)  # type: ignore[literal-required]
    flip_axis: typing.Optional[FlipAxis] = pydantic.Field(alias=str("flipAxis"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.FlipAxis](FlipAxis.md)
- [foundry_sdk.v2.media_sets.models.RotationAngle](RotationAngle.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Orientation.md)
