# foundry_sdk.v2.media_sets.models.AudioChannelOperation


Selects a specific channel from multi-channel audio.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| encode_format | encodeFormat | AudioEncodeFormat | required; no default | No additional field description in SDK source. |
| channel | channel | int | required; no default | The channel number to select. |
| type | type | typing.Literal['channel'] | 'channel' | No additional field description in SDK source. |

```python
class AudioChannelOperation(core.ModelBase):
    """Selects a specific channel from multi-channel audio."""

    encode_format: AudioEncodeFormat = pydantic.Field(alias=str("encodeFormat"))  # type: ignore[literal-required]
    channel: int
    """The channel number to select."""

    type: typing.Literal["channel"] = "channel"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.AudioEncodeFormat](AudioEncodeFormat.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AudioChannelOperation.md)
