# foundry_sdk.v2.media_sets.models.NumberOfChannels


Specifies the number of audio channels. Defaults to 2 (stereo).

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| number_of_channels | numberOfChannels | int | required; no default | The number of audio channels. |
| type | type | typing.Literal['numberOfChannels'] | 'numberOfChannels' | No additional field description in SDK source. |

```python
class NumberOfChannels(core.ModelBase):
    """Specifies the number of audio channels. Defaults to 2 (stereo)."""

    number_of_channels: int = pydantic.Field(alias=str("numberOfChannels"))  # type: ignore[literal-required]
    """The number of audio channels."""

    type: typing.Literal["numberOfChannels"] = "numberOfChannels"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NumberOfChannels.md)
