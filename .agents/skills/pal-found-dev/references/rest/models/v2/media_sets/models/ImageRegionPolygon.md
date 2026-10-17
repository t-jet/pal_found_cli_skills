# foundry_sdk.v2.media_sets.models.ImageRegionPolygon



Polygon drawn by connecting adjacent coordinates in the list with straight lines.
A line is drawn between the last and first coordinates in the list to create a closed shape.
Used to define regions in an image for operations like encryption/decryption.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ImageRegionPolygon: typing_extensions.TypeAlias = typing.List["ImagePixelCoordinate"]
```

## Referenced definitions

- [foundry_sdk.v2.media_sets.models.ImagePixelCoordinate](ImagePixelCoordinate.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ImageRegionPolygon.md)
