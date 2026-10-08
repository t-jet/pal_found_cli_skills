# foundry_sdk.v2.media_sets.models.ResizeToFitBoundingBoxOperation


Resizes an image to maximally fit within a bounding box while preserving aspect ratio.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| width | width | int | required; no default | The width of the bounding box in pixels. |
| height | height | int | required; no default | The height of the bounding box in pixels. |
| type | type | typing.Literal['resizeToFitBoundingBox'] | 'resizeToFitBoundingBox' | No additional field description in SDK source. |

```python
class ResizeToFitBoundingBoxOperation(core.ModelBase):
    """Resizes an image to maximally fit within a bounding box while preserving aspect ratio."""

    width: int
    """The width of the bounding box in pixels."""

    height: int
    """The height of the bounding box in pixels."""

    type: typing.Literal["resizeToFitBoundingBox"] = "resizeToFitBoundingBox"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ResizeToFitBoundingBoxOperation.md)
