# foundry_sdk.v2.media_sets.models.OcrParameters


Parameters for OCR (Optical Character Recognition) operations.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| output_format | outputFormat | OcrOutputFormat | required; no default | No additional field description in SDK source. |
| languages | languages | typing.List[OcrLanguageOrScript] | required; no default | The languages or scripts to use for OCR. |

```python
class OcrParameters(core.ModelBase):
    """Parameters for OCR (Optical Character Recognition) operations."""

    output_format: OcrOutputFormat = pydantic.Field(alias=str("outputFormat"))  # type: ignore[literal-required]
    languages: typing.List[OcrLanguageOrScript]
    """The languages or scripts to use for OCR."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.OcrLanguageOrScript](OcrLanguageOrScript.md)
- [foundry_sdk.v2.media_sets.models.OcrOutputFormat](OcrOutputFormat.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OcrParameters.md)
