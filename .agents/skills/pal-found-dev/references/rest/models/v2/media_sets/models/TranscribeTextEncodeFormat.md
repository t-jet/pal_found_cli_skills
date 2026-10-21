# foundry_sdk.v2.media_sets.models.TranscribeTextEncodeFormat


The output format for transcription results.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
TranscribeTextEncodeFormat: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["PlainTextNoSegmentData", "TranscribeJson", "Pttml"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.media_sets.models.PlainTextNoSegmentData](PlainTextNoSegmentData.md)
- [foundry_sdk.v2.media_sets.models.Pttml](Pttml.md)
- [foundry_sdk.v2.media_sets.models.TranscribeJson](TranscribeJson.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TranscribeTextEncodeFormat.md)
