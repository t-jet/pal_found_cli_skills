# foundry_sdk.v2.media_sets.models.Transformation



A transformation to apply to a media item. Each variant specifies the type of transformation
and any parameters required for the operation.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
Transformation: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "EmailToTextTransformation",
        "ImageTransformation",
        "SpreadsheetToTextTransformation",
        "VideoToAudioTransformation",
        "AudioToTextTransformation",
        "EmailToAttachmentTransformation",
        "VideoToArchiveTransformation",
        "VideoToTextTransformation",
        "ImageToTextTransformation",
        "VideoToImageTransformation",
        "VideoTransformation",
        "ImageToDocumentTransformation",
        "DicomToImageTransformation",
        "DocumentToDocumentTransformation",
        "DocumentToImageTransformation",
        "ImageToEmbeddingTransformation",
        "AudioTransformation",
        "DocumentToTextTransformation",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.media_sets.models.AudioToTextTransformation](AudioToTextTransformation.md)
- [foundry_sdk.v2.media_sets.models.AudioTransformation](AudioTransformation.md)
- [foundry_sdk.v2.media_sets.models.DicomToImageTransformation](DicomToImageTransformation.md)
- [foundry_sdk.v2.media_sets.models.DocumentToDocumentTransformation](DocumentToDocumentTransformation.md)
- [foundry_sdk.v2.media_sets.models.DocumentToImageTransformation](DocumentToImageTransformation.md)
- [foundry_sdk.v2.media_sets.models.DocumentToTextTransformation](DocumentToTextTransformation.md)
- [foundry_sdk.v2.media_sets.models.EmailToAttachmentTransformation](EmailToAttachmentTransformation.md)
- [foundry_sdk.v2.media_sets.models.EmailToTextTransformation](EmailToTextTransformation.md)
- [foundry_sdk.v2.media_sets.models.ImageToDocumentTransformation](ImageToDocumentTransformation.md)
- [foundry_sdk.v2.media_sets.models.ImageToEmbeddingTransformation](ImageToEmbeddingTransformation.md)
- [foundry_sdk.v2.media_sets.models.ImageToTextTransformation](ImageToTextTransformation.md)
- [foundry_sdk.v2.media_sets.models.ImageTransformation](ImageTransformation.md)
- [foundry_sdk.v2.media_sets.models.SpreadsheetToTextTransformation](SpreadsheetToTextTransformation.md)
- [foundry_sdk.v2.media_sets.models.VideoToArchiveTransformation](VideoToArchiveTransformation.md)
- [foundry_sdk.v2.media_sets.models.VideoToAudioTransformation](VideoToAudioTransformation.md)
- [foundry_sdk.v2.media_sets.models.VideoToImageTransformation](VideoToImageTransformation.md)
- [foundry_sdk.v2.media_sets.models.VideoToTextTransformation](VideoToTextTransformation.md)
- [foundry_sdk.v2.media_sets.models.VideoTransformation](VideoTransformation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Transformation.md)
