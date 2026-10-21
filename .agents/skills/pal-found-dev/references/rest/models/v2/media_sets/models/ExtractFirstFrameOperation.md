# foundry_sdk.v2.media_sets.models.ExtractFirstFrameOperation


Extracts the first full scene frame from the video.
If both width and height are not specified, preserves the original size.
If only one dimension is specified, the other is calculated to preserve aspect ratio.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| height | height | typing.Optional[int] | None | The desired height in pixels. |
| width | width | typing.Optional[int] | None | The desired width in pixels. |
| type | type | typing.Literal['extractFirstFrame'] | 'extractFirstFrame' | No additional field description in SDK source. |

```python
class ExtractFirstFrameOperation(core.ModelBase):
    """
    Extracts the first full scene frame from the video.
    If both width and height are not specified, preserves the original size.
    If only one dimension is specified, the other is calculated to preserve aspect ratio.
    """

    height: typing.Optional[int] = None
    """The desired height in pixels."""

    width: typing.Optional[int] = None
    """The desired width in pixels."""

    type: typing.Literal["extractFirstFrame"] = "extractFirstFrame"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ExtractFirstFrameOperation.md)
