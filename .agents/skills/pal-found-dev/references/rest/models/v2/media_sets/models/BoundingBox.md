# foundry_sdk.v2.media_sets.models.BoundingBox


A rectangular bounding box for annotations.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| left | left | float | required; no default | The left coordinate of the bounding box. |
| top | top | float | required; no default | The top coordinate of the bounding box. |
| width | width | float | required; no default | The width of the bounding box. |
| height | height | float | required; no default | The height of the bounding box. |

```python
class BoundingBox(core.ModelBase):
    """A rectangular bounding box for annotations."""

    left: float
    """The left coordinate of the bounding box."""

    top: float
    """The top coordinate of the bounding box."""

    width: float
    """The width of the bounding box."""

    height: float
    """The height of the bounding box."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](BoundingBox.md)
