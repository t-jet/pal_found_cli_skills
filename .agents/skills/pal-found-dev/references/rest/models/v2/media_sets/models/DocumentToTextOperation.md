# foundry_sdk.v2.media_sets.models.DocumentToTextOperation


The operation to perform for document to text conversion.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
DocumentToTextOperation: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "ExtractTableOfContentsOperation",
        "GetPdfPageDimensionsOperation",
        "ExtractAllTextOperation",
        "ExtractVlmTextOperation",
        "ExtractTextFromPagesToArrayOperation",
        "OcrOnPageOperation",
        "ExtractFormFieldsOperation",
        "ExtractDocumentLayoutAwareTextV2Operation",
        "ExtractDocumentTextV2Operation",
        "ExtractUnstructuredTextFromPageOperation",
        "DocumentExtractLayoutAwareContentOperation",
        "OcrOnPagesOperation",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.media_sets.models.DocumentExtractLayoutAwareContentOperation](DocumentExtractLayoutAwareContentOperation.md)
- [foundry_sdk.v2.media_sets.models.ExtractAllTextOperation](ExtractAllTextOperation.md)
- [foundry_sdk.v2.media_sets.models.ExtractDocumentLayoutAwareTextV2Operation](ExtractDocumentLayoutAwareTextV2Operation.md)
- [foundry_sdk.v2.media_sets.models.ExtractDocumentTextV2Operation](ExtractDocumentTextV2Operation.md)
- [foundry_sdk.v2.media_sets.models.ExtractFormFieldsOperation](ExtractFormFieldsOperation.md)
- [foundry_sdk.v2.media_sets.models.ExtractTableOfContentsOperation](ExtractTableOfContentsOperation.md)
- [foundry_sdk.v2.media_sets.models.ExtractTextFromPagesToArrayOperation](ExtractTextFromPagesToArrayOperation.md)
- [foundry_sdk.v2.media_sets.models.ExtractUnstructuredTextFromPageOperation](ExtractUnstructuredTextFromPageOperation.md)
- [foundry_sdk.v2.media_sets.models.ExtractVlmTextOperation](ExtractVlmTextOperation.md)
- [foundry_sdk.v2.media_sets.models.GetPdfPageDimensionsOperation](GetPdfPageDimensionsOperation.md)
- [foundry_sdk.v2.media_sets.models.OcrOnPageOperation](OcrOnPageOperation.md)
- [foundry_sdk.v2.media_sets.models.OcrOnPagesOperation](OcrOnPagesOperation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DocumentToTextOperation.md)
