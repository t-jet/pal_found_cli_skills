# foundry_sdk.v2.media_sets.models.Color


An RGBA color value.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| r | r | int | required; no default | Red component (0-255). |
| g | g | int | required; no default | Green component (0-255). |
| b | b | int | required; no default | Blue component (0-255). |
| a | a | typing.Optional[float] | None | Alpha component (0-1, where 0 is transparent and 1 is opaque). |

```python
class Color(core.ModelBase):
    """An RGBA color value."""

    r: int
    """Red component (0-255)."""

    g: int
    """Green component (0-255)."""

    b: int
    """Blue component (0-255)."""

    a: typing.Optional[float] = None
    """Alpha component (0-1, where 0 is transparent and 1 is opaque)."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Color.md)
