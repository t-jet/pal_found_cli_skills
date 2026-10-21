# foundry_sdk.v2.language_models.models.AnthropicDocument


AnthropicDocument

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| source | source | AnthropicDocumentSource | required; no default | No additional field description in SDK source. |
| cache_control | cacheControl | typing.Optional[AnthropicCacheControl] | default None | No additional field description in SDK source. |
| citations | citations | typing.Optional[AnthropicDocumentCitations] | None | No additional field description in SDK source. |
| context | context | typing.Optional[str] | None | No additional field description in SDK source. |
| title | title | typing.Optional[str] | None | No additional field description in SDK source. |
| type | type | typing.Literal['document'] | 'document' | No additional field description in SDK source. |

```python
class AnthropicDocument(core.ModelBase):
    """AnthropicDocument"""

    source: AnthropicDocumentSource
    cache_control: typing.Optional[AnthropicCacheControl] = pydantic.Field(alias=str("cacheControl"), default=None)  # type: ignore[literal-required]
    citations: typing.Optional[AnthropicDocumentCitations] = None
    context: typing.Optional[str] = None
    title: typing.Optional[str] = None
    type: typing.Literal["document"] = "document"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.language_models.models.AnthropicCacheControl](AnthropicCacheControl.md)
- [foundry_sdk.v2.language_models.models.AnthropicDocumentCitations](AnthropicDocumentCitations.md)
- [foundry_sdk.v2.language_models.models.AnthropicDocumentSource](AnthropicDocumentSource.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AnthropicDocument.md)
