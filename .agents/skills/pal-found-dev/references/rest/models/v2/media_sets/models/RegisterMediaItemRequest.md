# foundry_sdk.v2.media_sets.models.RegisterMediaItemRequest


Request to register a media item from a federated store.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| physical_item_name | physicalItemName | str | required; no default | The relative path within the federated media store where the media item exists. |
| media_item_path | mediaItemPath | typing.Optional[core_models.MediaItemPath] | default None | No additional field description in SDK source. |

```python
class RegisterMediaItemRequest(core.ModelBase):
    """Request to register a media item from a federated store."""

    physical_item_name: str = pydantic.Field(alias=str("physicalItemName"))  # type: ignore[literal-required]
    """The relative path within the federated media store where the media item exists."""

    media_item_path: typing.Optional[core_models.MediaItemPath] = pydantic.Field(alias=str("mediaItemPath"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.MediaItemPath](../../core/models/MediaItemPath.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](RegisterMediaItemRequest.md)
