# foundry_sdk.v2.media_sets.models.OcrOnPageOperation


Performs OCR (Optical Character Recognition) on a specific page of a document.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| page_number | pageNumber | int | required; no default | The page number to perform OCR on. |
| parameters | parameters | OcrParameters | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['ocrOnPage'] | 'ocrOnPage' | No additional field description in SDK source. |

```python
class OcrOnPageOperation(core.ModelBase):
    """Performs OCR (Optical Character Recognition) on a specific page of a document."""

    page_number: int = pydantic.Field(alias=str("pageNumber"))  # type: ignore[literal-required]
    """The page number to perform OCR on."""

    parameters: OcrParameters
    type: typing.Literal["ocrOnPage"] = "ocrOnPage"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.OcrParameters](OcrParameters.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OcrOnPageOperation.md)
