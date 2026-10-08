# foundry_sdk.v2.media_sets.models.TranscribeOperation


Transcribes speech in audio to text.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| language | language | typing.Optional[TranscriptionLanguage] | None | No additional field description in SDK source. |
| diarize | diarize | typing.Optional[bool] | None | Whether to perform speaker diarization. Defaults to false.<br>    Not supported in economical performance mode. |
| output_format | outputFormat | typing.Optional[TranscribeTextEncodeFormat] | default None | No additional field description in SDK source. |
| performance_mode | performanceMode | typing.Optional[PerformanceMode] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['transcribe'] | 'transcribe' | No additional field description in SDK source. |

```python
class TranscribeOperation(core.ModelBase):
    """Transcribes speech in audio to text."""

    language: typing.Optional[TranscriptionLanguage] = None
    diarize: typing.Optional[bool] = None
    """
    Whether to perform speaker diarization. Defaults to false.
    Not supported in economical performance mode.
    """

    output_format: typing.Optional[TranscribeTextEncodeFormat] = pydantic.Field(alias=str("outputFormat"), default=None)  # type: ignore[literal-required]
    performance_mode: typing.Optional[PerformanceMode] = pydantic.Field(alias=str("performanceMode"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["transcribe"] = "transcribe"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.PerformanceMode](PerformanceMode.md)
- [foundry_sdk.v2.media_sets.models.TranscribeTextEncodeFormat](TranscribeTextEncodeFormat.md)
- [foundry_sdk.v2.media_sets.models.TranscriptionLanguage](TranscriptionLanguage.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TranscribeOperation.md)
