# foundry_sdk.v2.media_sets.models.DocumentToDocumentOperation


The operation to perform for document to document conversion.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
DocumentToDocumentOperation: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["SlicePdfRangeOperation", "ConvertDocumentOperation"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.media_sets.models.ConvertDocumentOperation](ConvertDocumentOperation.md)
- [foundry_sdk.v2.media_sets.models.SlicePdfRangeOperation](SlicePdfRangeOperation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DocumentToDocumentOperation.md)
