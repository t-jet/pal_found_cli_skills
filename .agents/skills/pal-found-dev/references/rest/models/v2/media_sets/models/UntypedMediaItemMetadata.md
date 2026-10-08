# foundry_sdk.v2.media_sets.models.UntypedMediaItemMetadata


Metadata for untyped media items (media items without a recognized type).

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| size_bytes | sizeBytes | int | required; no default | The size of the media item in bytes. |
| type | type | typing.Literal['untyped'] | 'untyped' | No additional field description in SDK source. |

```python
class UntypedMediaItemMetadata(core.ModelBase):
    """Metadata for untyped media items (media items without a recognized type)."""

    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    type: typing.Literal["untyped"] = "untyped"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](UntypedMediaItemMetadata.md)
