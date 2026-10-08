# foundry_sdk.v2.media_sets.models.MediaItemMetadata



Detailed metadata about a media item, including type-specific information such as dimensions for images,
duration for audio/video, page count for documents, etc.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
MediaItemMetadata: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "DocumentMediaItemMetadata",
        "ImageryMediaItemMetadata",
        "SpreadsheetMediaItemMetadata",
        "UntypedMediaItemMetadata",
        "AudioMediaItemMetadata",
        "Model3dMediaItemMetadata",
        "VideoMediaItemMetadata",
        "DicomMediaItemMetadata",
        "EmailMediaItemMetadata",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.media_sets.models.AudioMediaItemMetadata](AudioMediaItemMetadata.md)
- [foundry_sdk.v2.media_sets.models.DicomMediaItemMetadata](DicomMediaItemMetadata.md)
- [foundry_sdk.v2.media_sets.models.DocumentMediaItemMetadata](DocumentMediaItemMetadata.md)
- [foundry_sdk.v2.media_sets.models.EmailMediaItemMetadata](EmailMediaItemMetadata.md)
- [foundry_sdk.v2.media_sets.models.ImageryMediaItemMetadata](ImageryMediaItemMetadata.md)
- [foundry_sdk.v2.media_sets.models.Model3dMediaItemMetadata](Model3dMediaItemMetadata.md)
- [foundry_sdk.v2.media_sets.models.SpreadsheetMediaItemMetadata](SpreadsheetMediaItemMetadata.md)
- [foundry_sdk.v2.media_sets.models.UntypedMediaItemMetadata](UntypedMediaItemMetadata.md)
- [foundry_sdk.v2.media_sets.models.VideoMediaItemMetadata](VideoMediaItemMetadata.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MediaItemMetadata.md)
