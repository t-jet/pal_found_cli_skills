# foundry_sdk.v2.ontologies.models.HumanReadableFormat


Formats the duration as a human-readable written string.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| show_full_units | showFullUnits | typing.Optional[bool] | default None | Whether to show full or abbreviated time units. |
| type | type | typing.Literal['humanReadable'] | 'humanReadable' | No additional field description in SDK source. |

```python
class HumanReadableFormat(core.ModelBase):
    """Formats the duration as a human-readable written string."""

    show_full_units: typing.Optional[bool] = pydantic.Field(alias=str("showFullUnits"), default=None)  # type: ignore[literal-required]
    """Whether to show full or abbreviated time units."""

    type: typing.Literal["humanReadable"] = "humanReadable"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](HumanReadableFormat.md)
