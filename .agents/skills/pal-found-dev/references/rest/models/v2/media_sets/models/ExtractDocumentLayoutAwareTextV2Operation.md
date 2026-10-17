# foundry_sdk.v2.media_sets.models.ExtractDocumentLayoutAwareTextV2Operation


Extract layout aware text with bounding boxes across all pages using the v2 text extraction endpoint.
This only supports PDFs.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| page_range | pageRange | typing.Optional[PageRange] | default None | No additional field description in SDK source. |
| config | config | ExtractDocumentLayoutAwareTextV2Config | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['extractLayoutAwareTextV2'] | 'extractLayoutAwareTextV2' | No additional field description in SDK source. |

```python
class ExtractDocumentLayoutAwareTextV2Operation(core.ModelBase):
    """
    Extract layout aware text with bounding boxes across all pages using the v2 text extraction endpoint.
    This only supports PDFs.
    """

    page_range: typing.Optional[PageRange] = pydantic.Field(alias=str("pageRange"), default=None)  # type: ignore[literal-required]
    config: ExtractDocumentLayoutAwareTextV2Config
    type: typing.Literal["extractLayoutAwareTextV2"] = "extractLayoutAwareTextV2"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.ExtractDocumentLayoutAwareTextV2Config](ExtractDocumentLayoutAwareTextV2Config.md)
- [foundry_sdk.v2.media_sets.models.PageRange](PageRange.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ExtractDocumentLayoutAwareTextV2Operation.md)
