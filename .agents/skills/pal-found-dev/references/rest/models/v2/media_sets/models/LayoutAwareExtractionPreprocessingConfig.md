# foundry_sdk.v2.media_sets.models.LayoutAwareExtractionPreprocessingConfig


Configuration for layout-aware extraction preprocessing.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| transformation_config | transformationConfig | ExtractDocumentLayoutAwareTextV2Config | required; no default | No additional field description in SDK source. |
| crop_config | cropConfig | typing.Optional[CropConfig] | default None | No additional field description in SDK source. |

```python
class LayoutAwareExtractionPreprocessingConfig(core.ModelBase):
    """Configuration for layout-aware extraction preprocessing."""

    transformation_config: ExtractDocumentLayoutAwareTextV2Config = pydantic.Field(alias=str("transformationConfig"))  # type: ignore[literal-required]
    crop_config: typing.Optional[CropConfig] = pydantic.Field(alias=str("cropConfig"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.CropConfig](CropConfig.md)
- [foundry_sdk.v2.media_sets.models.ExtractDocumentLayoutAwareTextV2Config](ExtractDocumentLayoutAwareTextV2Config.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LayoutAwareExtractionPreprocessingConfig.md)
