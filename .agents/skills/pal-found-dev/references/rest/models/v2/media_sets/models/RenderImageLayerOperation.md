# foundry_sdk.v2.media_sets.models.RenderImageLayerOperation


Renders a frame of a DICOM file as an image.
If only one dimension is specified, the other is calculated to preserve aspect ratio.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| layer_number | layerNumber | typing.Optional[int] | default None | The layer number to render. If not specified, renders the middle layer. |
| height | height | typing.Optional[int] | None | The desired height in pixels. |
| width | width | typing.Optional[int] | None | The desired width in pixels. |
| type | type | typing.Literal['renderImageLayer'] | 'renderImageLayer' | No additional field description in SDK source. |

```python
class RenderImageLayerOperation(core.ModelBase):
    """
    Renders a frame of a DICOM file as an image.
    If only one dimension is specified, the other is calculated to preserve aspect ratio.
    """

    layer_number: typing.Optional[int] = pydantic.Field(alias=str("layerNumber"), default=None)  # type: ignore[literal-required]
    """The layer number to render. If not specified, renders the middle layer."""

    height: typing.Optional[int] = None
    """The desired height in pixels."""

    width: typing.Optional[int] = None
    """The desired width in pixels."""

    type: typing.Literal["renderImageLayer"] = "renderImageLayer"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](RenderImageLayerOperation.md)
