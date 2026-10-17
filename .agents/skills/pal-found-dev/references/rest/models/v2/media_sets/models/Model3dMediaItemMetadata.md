# foundry_sdk.v2.media_sets.models.Model3dMediaItemMetadata


Metadata for 3D model media items.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| format | format | Model3dDecodeFormat | required; no default | No additional field description in SDK source. |
| model_type | modelType | Model3dType | required; no default | No additional field description in SDK source. |
| size_bytes | sizeBytes | int | required; no default | The size of the media item in bytes. |
| type | type | typing.Literal['model3d'] | 'model3d' | No additional field description in SDK source. |

```python
class Model3dMediaItemMetadata(core.ModelBase):
    """Metadata for 3D model media items."""

    format: Model3dDecodeFormat
    model_type: Model3dType = pydantic.Field(alias=str("modelType"))  # type: ignore[literal-required]
    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    type: typing.Literal["model3d"] = "model3d"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.Model3dDecodeFormat](Model3dDecodeFormat.md)
- [foundry_sdk.v2.media_sets.models.Model3dType](Model3dType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Model3dMediaItemMetadata.md)
