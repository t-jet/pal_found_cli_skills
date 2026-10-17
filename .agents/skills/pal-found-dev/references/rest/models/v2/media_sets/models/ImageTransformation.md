# foundry_sdk.v2.media_sets.models.ImageTransformation


Transforms images with multiple operations applied in sequence.
Operations are applied in the order they appear in the list.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| encoding | encoding | ImageryEncodeFormat | required; no default | No additional field description in SDK source. |
| operations | operations | typing.List[ImageOperation] | required; no default | The list of operations to apply to the image, in order. |
| type | type | typing.Literal['image'] | 'image' | No additional field description in SDK source. |

```python
class ImageTransformation(core.ModelBase):
    """
    Transforms images with multiple operations applied in sequence.
    Operations are applied in the order they appear in the list.
    """

    encoding: ImageryEncodeFormat
    operations: typing.List[ImageOperation]
    """The list of operations to apply to the image, in order."""

    type: typing.Literal["image"] = "image"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.ImageOperation](ImageOperation.md)
- [foundry_sdk.v2.media_sets.models.ImageryEncodeFormat](ImageryEncodeFormat.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ImageTransformation.md)
