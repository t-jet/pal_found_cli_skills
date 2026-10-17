# foundry_sdk.v2.media_sets.models.AudioEncodeFormat


The output format for encoding audio.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
AudioEncodeFormat: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["Mp3Format", "WavEncodeFormat", "TsAudioContainerFormat"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.media_sets.models.Mp3Format](Mp3Format.md)
- [foundry_sdk.v2.media_sets.models.TsAudioContainerFormat](TsAudioContainerFormat.md)
- [foundry_sdk.v2.media_sets.models.WavEncodeFormat](WavEncodeFormat.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AudioEncodeFormat.md)
