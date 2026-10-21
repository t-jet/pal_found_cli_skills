# foundry_sdk.v2.media_sets.models.RenderPageOperation


Renders a PDF page as an image.
If only one dimension is specified, the other is calculated to preserve aspect ratio.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| page_number | pageNumber | typing.Optional[int] | default None | The zero-indexed page number to render. Defaults to the first page if not specified. |
| height | height | typing.Optional[int] | None | The desired height in pixels. |
| width | width | typing.Optional[int] | None | The desired width in pixels. |
| type | type | typing.Literal['renderPage'] | 'renderPage' | No additional field description in SDK source. |

```python
class RenderPageOperation(core.ModelBase):
    """
    Renders a PDF page as an image.
    If only one dimension is specified, the other is calculated to preserve aspect ratio.
    """

    page_number: typing.Optional[int] = pydantic.Field(alias=str("pageNumber"), default=None)  # type: ignore[literal-required]
    """The zero-indexed page number to render. Defaults to the first page if not specified."""

    height: typing.Optional[int] = None
    """The desired height in pixels."""

    width: typing.Optional[int] = None
    """The desired width in pixels."""

    type: typing.Literal["renderPage"] = "renderPage"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](RenderPageOperation.md)
