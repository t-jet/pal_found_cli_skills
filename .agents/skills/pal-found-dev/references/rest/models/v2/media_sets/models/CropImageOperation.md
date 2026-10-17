# foundry_sdk.v2.media_sets.models.CropImageOperation


Crops an image to a rectangular sub-window.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| x_offset | xOffset | int | required; no default | The x offset in pixels from the left hand side of the image. |
| y_offset | yOffset | int | required; no default | The y offset in pixels from the top of the image. |
| width | width | int | required; no default | The width of the cropping box in pixels. |
| height | height | int | required; no default | The height of the cropping box in pixels. |
| type | type | typing.Literal['crop'] | 'crop' | No additional field description in SDK source. |

```python
class CropImageOperation(core.ModelBase):
    """Crops an image to a rectangular sub-window."""

    x_offset: int = pydantic.Field(alias=str("xOffset"))  # type: ignore[literal-required]
    """The x offset in pixels from the left hand side of the image."""

    y_offset: int = pydantic.Field(alias=str("yOffset"))  # type: ignore[literal-required]
    """The y offset in pixels from the top of the image."""

    width: int
    """The width of the cropping box in pixels."""

    height: int
    """The height of the cropping box in pixels."""

    type: typing.Literal["crop"] = "crop"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CropImageOperation.md)
