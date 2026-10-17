# foundry_sdk.v2.media_sets.models.Annotation


An annotation to draw on an image.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| geometry | geometry | AnnotateGeometry | required; no default | No additional field description in SDK source. |
| label | label | typing.Optional[str] | None | An optional text label to display with the annotation. |
| color | color | typing.Optional[Color] | None | No additional field description in SDK source. |
| thickness | thickness | typing.Optional[float] | None | The thickness of the annotation lines. |
| font_size | fontSize | typing.Optional[int] | default None | The font size for the label text. |

```python
class Annotation(core.ModelBase):
    """An annotation to draw on an image."""

    geometry: AnnotateGeometry
    label: typing.Optional[str] = None
    """An optional text label to display with the annotation."""

    color: typing.Optional[Color] = None
    thickness: typing.Optional[float] = None
    """The thickness of the annotation lines."""

    font_size: typing.Optional[int] = pydantic.Field(alias=str("fontSize"), default=None)  # type: ignore[literal-required]
    """The font size for the label text."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.AnnotateGeometry](AnnotateGeometry.md)
- [foundry_sdk.v2.media_sets.models.Color](Color.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Annotation.md)
