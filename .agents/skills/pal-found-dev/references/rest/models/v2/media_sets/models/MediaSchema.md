# foundry_sdk.v2.media_sets.models.MediaSchema


The schema type of a media set, indicating what type of media items it can contain.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
MediaSchema: typing_extensions.TypeAlias = typing.Literal[
    "AUDIO",
    "DICOM",
    "DOCUMENT",
    "IMAGERY",
    "MODEL_3D",
    "MULTIMODAL",
    "SPREADSHEET",
    "STREAMING_VIDEO",
    "VIDEO",
    "EMAIL",
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MediaSchema.md)
