# foundry_sdk.v2.media_sets.models.BandInfo


Information about a band in an image.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| data_type | dataType | typing.Optional[DataType] | default None | No additional field description in SDK source. |
| color_interpretation | colorInterpretation | typing.Optional[ColorInterpretation] | default None | No additional field description in SDK source. |
| palette_interpretation | paletteInterpretation | typing.Optional[PaletteInterpretation] | default None | No additional field description in SDK source. |
| unit_interpretation | unitInterpretation | typing.Optional[UnitInterpretation] | default None | No additional field description in SDK source. |

```python
class BandInfo(core.ModelBase):
    """Information about a band in an image."""

    data_type: typing.Optional[DataType] = pydantic.Field(alias=str("dataType"), default=None)  # type: ignore[literal-required]
    color_interpretation: typing.Optional[ColorInterpretation] = pydantic.Field(alias=str("colorInterpretation"), default=None)  # type: ignore[literal-required]
    palette_interpretation: typing.Optional[PaletteInterpretation] = pydantic.Field(alias=str("paletteInterpretation"), default=None)  # type: ignore[literal-required]
    unit_interpretation: typing.Optional[UnitInterpretation] = pydantic.Field(alias=str("unitInterpretation"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.ColorInterpretation](ColorInterpretation.md)
- [foundry_sdk.v2.media_sets.models.DataType](DataType.md)
- [foundry_sdk.v2.media_sets.models.PaletteInterpretation](PaletteInterpretation.md)
- [foundry_sdk.v2.media_sets.models.UnitInterpretation](UnitInterpretation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](BandInfo.md)
