# foundry_sdk.v2.ontologies.models.AttachmentMetadataResponse


The attachment metadata response

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
AttachmentMetadataResponse: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["AttachmentV2", "ListAttachmentsResponseV2"], pydantic.Field(discriminator="type")
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.AttachmentV2](AttachmentV2.md)
- [foundry_sdk.v2.ontologies.models.ListAttachmentsResponseV2](ListAttachmentsResponseV2.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AttachmentMetadataResponse.md)
