# foundry_sdk.v2.media_sets.models.MediaAttribution


MediaAttribution

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| creator_id | creatorId | core_models.UserId | required; no default | No additional field description in SDK source. |
| creation_timestamp | creationTimestamp | core.AwareDatetime | required; no default | The timestamp when the media item was created, in ISO 8601 timestamp format. |

```python
class MediaAttribution(core.ModelBase):
    """MediaAttribution"""

    creator_id: core_models.UserId = pydantic.Field(alias=str("creatorId"))  # type: ignore[literal-required]
    creation_timestamp: core.AwareDatetime = pydantic.Field(alias=str("creationTimestamp"))  # type: ignore[literal-required]
    """The timestamp when the media item was created, in ISO 8601 timestamp format."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../_core/AwareDatetime.md)
- [foundry_sdk.v2.core.models.UserId](../../core/models/UserId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MediaAttribution.md)
