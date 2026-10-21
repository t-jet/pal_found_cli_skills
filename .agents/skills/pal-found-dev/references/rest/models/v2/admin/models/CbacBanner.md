# foundry_sdk.v2.admin.models.CbacBanner


CbacBanner

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| classification_string | classificationString | CbacBannerClassificationString | required; no default | No additional field description in SDK source. |
| markings | markings | typing.List[core_models.MarkingId] | required; no default | No additional field description in SDK source. |
| text_color | textColor | core_models.Color | required; no default | No additional field description in SDK source. |
| background_colors | backgroundColors | typing.List[core_models.Color] | required; no default | No additional field description in SDK source. |

```python
class CbacBanner(core.ModelBase):
    """CbacBanner"""

    classification_string: CbacBannerClassificationString = pydantic.Field(alias=str("classificationString"))  # type: ignore[literal-required]
    markings: typing.List[core_models.MarkingId]
    text_color: core_models.Color = pydantic.Field(alias=str("textColor"))  # type: ignore[literal-required]
    background_colors: typing.List[core_models.Color] = pydantic.Field(alias=str("backgroundColors"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.admin.models.CbacBannerClassificationString](CbacBannerClassificationString.md)
- [foundry_sdk.v2.core.models.Color](../../core/models/Color.md)
- [foundry_sdk.v2.core.models.MarkingId](../../core/models/MarkingId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CbacBanner.md)
