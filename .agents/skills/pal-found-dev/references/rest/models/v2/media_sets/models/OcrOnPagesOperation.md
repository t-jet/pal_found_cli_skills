# foundry_sdk.v2.media_sets.models.OcrOnPagesOperation


Creates access patterns for OCR across pages of a document.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| parameters | parameters | OcrParameters | required; no default | No additional field description in SDK source. |
| page_number | pageNumber | int | required; no default | The page number. |
| type | type | typing.Literal['ocrOnPages'] | 'ocrOnPages' | No additional field description in SDK source. |

```python
class OcrOnPagesOperation(core.ModelBase):
    """Creates access patterns for OCR across pages of a document."""

    parameters: OcrParameters
    page_number: int = pydantic.Field(alias=str("pageNumber"))  # type: ignore[literal-required]
    """The page number."""

    type: typing.Literal["ocrOnPages"] = "ocrOnPages"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.OcrParameters](OcrParameters.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OcrOnPagesOperation.md)
