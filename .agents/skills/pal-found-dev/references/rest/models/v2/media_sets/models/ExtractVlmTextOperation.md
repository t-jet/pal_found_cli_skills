# foundry_sdk.v2.media_sets.models.ExtractVlmTextOperation


Extract text from a document using vision language models (VLMs).
VLMs can understand document layout and structure more intelligently than traditional OCR.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| llm_spec | llmSpec | LlmSpec | required; no default | No additional field description in SDK source. |
| preprocessing_configuration | preprocessingConfiguration | typing.Optional[VlmPreprocessingConfig] | default None | No additional field description in SDK source. |
| image_spec | imageSpec | typing.Optional[ImageSpec] | default None | No additional field description in SDK source. |
| output_format | outputFormat | TextOutputFormat | required; no default | No additional field description in SDK source. |
| page_range | pageRange | typing.Optional[PageRange] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['extractVlmText'] | 'extractVlmText' | No additional field description in SDK source. |

```python
class ExtractVlmTextOperation(core.ModelBase):
    """
    Extract text from a document using vision language models (VLMs).
    VLMs can understand document layout and structure more intelligently than traditional OCR.
    """

    llm_spec: LlmSpec = pydantic.Field(alias=str("llmSpec"))  # type: ignore[literal-required]
    preprocessing_configuration: typing.Optional[VlmPreprocessingConfig] = pydantic.Field(alias=str("preprocessingConfiguration"), default=None)  # type: ignore[literal-required]
    image_spec: typing.Optional[ImageSpec] = pydantic.Field(alias=str("imageSpec"), default=None)  # type: ignore[literal-required]
    output_format: TextOutputFormat = pydantic.Field(alias=str("outputFormat"))  # type: ignore[literal-required]
    page_range: typing.Optional[PageRange] = pydantic.Field(alias=str("pageRange"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["extractVlmText"] = "extractVlmText"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.ImageSpec](ImageSpec.md)
- [foundry_sdk.v2.media_sets.models.LlmSpec](LlmSpec.md)
- [foundry_sdk.v2.media_sets.models.PageRange](PageRange.md)
- [foundry_sdk.v2.media_sets.models.TextOutputFormat](TextOutputFormat.md)
- [foundry_sdk.v2.media_sets.models.VlmPreprocessingConfig](VlmPreprocessingConfig.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ExtractVlmTextOperation.md)
