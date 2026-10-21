# foundry_sdk.v2.media_sets.models.PlainTextNoSegmentData


Plain text transcription output format.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| add_timestamps | addTimestamps | bool | required; no default | Whether to include timestamps in the output. |
| type | type | typing.Literal['plainTextNoSegmentData'] | 'plainTextNoSegmentData' | No additional field description in SDK source. |

```python
class PlainTextNoSegmentData(core.ModelBase):
    """Plain text transcription output format."""

    add_timestamps: bool = pydantic.Field(alias=str("addTimestamps"))  # type: ignore[literal-required]
    """Whether to include timestamps in the output."""

    type: typing.Literal["plainTextNoSegmentData"] = "plainTextNoSegmentData"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PlainTextNoSegmentData.md)
