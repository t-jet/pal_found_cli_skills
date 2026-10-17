# foundry_sdk.v2.media_sets.models.AudioSpecification


Technical specifications for audio media items.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| bit_rate | bitRate | int | required; no default | Approximate (average) bits per second of the audio, rounded up in case of a fractional average bits per second. |
| duration_seconds | durationSeconds | float | required; no default | Approximate duration of the audio, in seconds with up to two decimal digits (rounded up). |
| number_of_channels | numberOfChannels | typing.Optional[int] | default None | Number of audio channels in the audio stream. |

```python
class AudioSpecification(core.ModelBase):
    """Technical specifications for audio media items."""

    bit_rate: int = pydantic.Field(alias=str("bitRate"))  # type: ignore[literal-required]
    """Approximate (average) bits per second of the audio, rounded up in case of a fractional average bits per second."""

    duration_seconds: float = pydantic.Field(alias=str("durationSeconds"))  # type: ignore[literal-required]
    """Approximate duration of the audio, in seconds with up to two decimal digits (rounded up)."""

    number_of_channels: typing.Optional[int] = pydantic.Field(alias=str("numberOfChannels"), default=None)  # type: ignore[literal-required]
    """Number of audio channels in the audio stream."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AudioSpecification.md)
