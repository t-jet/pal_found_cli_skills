# foundry_sdk.v2.media_sets.models.WaveformOperation


Generates waveform visualization data from audio.
Returns JSON with normalized doubles (0-1) representing amplitude.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| peaks_per_second | peaksPerSecond | int | required; no default | The number of peaks per second (1-1000). |
| type | type | typing.Literal['waveform'] | 'waveform' | No additional field description in SDK source. |

```python
class WaveformOperation(core.ModelBase):
    """
    Generates waveform visualization data from audio.
    Returns JSON with normalized doubles (0-1) representing amplitude.
    """

    peaks_per_second: int = pydantic.Field(alias=str("peaksPerSecond"))  # type: ignore[literal-required]
    """The number of peaks per second (1-1000)."""

    type: typing.Literal["waveform"] = "waveform"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](WaveformOperation.md)
