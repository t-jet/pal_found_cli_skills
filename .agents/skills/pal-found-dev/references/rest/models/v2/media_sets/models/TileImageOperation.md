# foundry_sdk.v2.media_sets.models.TileImageOperation


Generates Slippy map tiles (EPSG 3857) from a geo-embedded image.
Only supported for geo-embedded TIFF and NITF images with at most 100M square pixels.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| zoom | zoom | int | required; no default | The zoom level of the tile. |
| x | x | int | required; no default | The x coordinate of the tile. |
| y | y | int | required; no default | The y coordinate of the tile. |
| type | type | typing.Literal['tile'] | 'tile' | No additional field description in SDK source. |

```python
class TileImageOperation(core.ModelBase):
    """
    Generates Slippy map tiles (EPSG 3857) from a geo-embedded image.
    Only supported for geo-embedded TIFF and NITF images with at most 100M square pixels.
    """

    zoom: int
    """The zoom level of the tile."""

    x: int
    """The x coordinate of the tile."""

    y: int
    """The y coordinate of the tile."""

    type: typing.Literal["tile"] = "tile"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TileImageOperation.md)
