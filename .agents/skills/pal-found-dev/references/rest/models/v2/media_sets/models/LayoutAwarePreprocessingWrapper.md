# foundry_sdk.v2.media_sets.models.LayoutAwarePreprocessingWrapper


Wrapper for layout-aware preprocessing.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| layout_aware | layoutAware | LayoutAwareExtractionPreprocessingConfig | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['layoutAware'] | 'layoutAware' | No additional field description in SDK source. |

```python
class LayoutAwarePreprocessingWrapper(core.ModelBase):
    """Wrapper for layout-aware preprocessing."""

    layout_aware: LayoutAwareExtractionPreprocessingConfig = pydantic.Field(alias=str("layoutAware"))  # type: ignore[literal-required]
    type: typing.Literal["layoutAware"] = "layoutAware"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.LayoutAwareExtractionPreprocessingConfig](LayoutAwareExtractionPreprocessingConfig.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LayoutAwarePreprocessingWrapper.md)
