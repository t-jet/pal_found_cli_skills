# foundry_sdk.v2.media_sets.models.WavEncodeFormat


WAV audio format with optional sample rate and channel layout.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| sample_rate | sampleRate | typing.Optional[int] | default None | The sample rate in Hz. Defaults to 44100 Hz if not specified. |
| audio_channel_layout | audioChannelLayout | typing.Optional[AudioChannelLayout] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['wav'] | 'wav' | No additional field description in SDK source. |

```python
class WavEncodeFormat(core.ModelBase):
    """WAV audio format with optional sample rate and channel layout."""

    sample_rate: typing.Optional[int] = pydantic.Field(alias=str("sampleRate"), default=None)  # type: ignore[literal-required]
    """The sample rate in Hz. Defaults to 44100 Hz if not specified."""

    audio_channel_layout: typing.Optional[AudioChannelLayout] = pydantic.Field(alias=str("audioChannelLayout"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["wav"] = "wav"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.AudioChannelLayout](AudioChannelLayout.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](WavEncodeFormat.md)
