# foundry_sdk.v2.media_sets.models.RegisterMediaItemResponse


Response after successfully registering a media item.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| media_item_rid | mediaItemRid | core_models.MediaItemRid | required; no default | No additional field description in SDK source. |
| media_type | mediaType | core_models.MediaType | required; no default | No additional field description in SDK source. |

```python
class RegisterMediaItemResponse(core.ModelBase):
    """Response after successfully registering a media item."""

    media_item_rid: core_models.MediaItemRid = pydantic.Field(alias=str("mediaItemRid"))  # type: ignore[literal-required]
    media_type: core_models.MediaType = pydantic.Field(alias=str("mediaType"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.MediaItemRid](../../core/models/MediaItemRid.md)
- [foundry_sdk.v2.core.models.MediaType](../../core/models/MediaType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](RegisterMediaItemResponse.md)
