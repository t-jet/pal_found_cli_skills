# foundry_sdk.v2.media_sets.models.OcrOutputFormat


The output format for OCR results.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
OcrOutputFormat: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["OcrHocrOutputFormat", "OcrTextOutputFormat"], pydantic.Field(discriminator="type")
]
```

## Referenced definitions

- [foundry_sdk.v2.media_sets.models.OcrHocrOutputFormat](OcrHocrOutputFormat.md)
- [foundry_sdk.v2.media_sets.models.OcrTextOutputFormat](OcrTextOutputFormat.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OcrOutputFormat.md)
