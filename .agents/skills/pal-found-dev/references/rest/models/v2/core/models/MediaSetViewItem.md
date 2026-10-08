# foundry_sdk.v2.core.models.MediaSetViewItem


MediaSetViewItem

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| media_set_rid | mediaSetRid | MediaSetRid | required; no default | No additional field description in SDK source. |
| media_set_view_rid | mediaSetViewRid | MediaSetViewRid | required; no default | No additional field description in SDK source. |
| media_item_rid | mediaItemRid | MediaItemRid | required; no default | No additional field description in SDK source. |
| token | token | typing.Optional[MediaItemReadToken] | None | No additional field description in SDK source. |

```python
class MediaSetViewItem(core.ModelBase):
    """MediaSetViewItem"""

    media_set_rid: MediaSetRid = pydantic.Field(alias=str("mediaSetRid"))  # type: ignore[literal-required]
    media_set_view_rid: MediaSetViewRid = pydantic.Field(alias=str("mediaSetViewRid"))  # type: ignore[literal-required]
    media_item_rid: MediaItemRid = pydantic.Field(alias=str("mediaItemRid"))  # type: ignore[literal-required]
    token: typing.Optional[MediaItemReadToken] = None
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.MediaItemReadToken](MediaItemReadToken.md)
- [foundry_sdk.v2.core.models.MediaItemRid](MediaItemRid.md)
- [foundry_sdk.v2.core.models.MediaSetRid](MediaSetRid.md)
- [foundry_sdk.v2.core.models.MediaSetViewRid](MediaSetViewRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MediaSetViewItem.md)
