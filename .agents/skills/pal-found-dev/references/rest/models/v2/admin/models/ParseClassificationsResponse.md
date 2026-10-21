# foundry_sdk.v2.admin.models.ParseClassificationsResponse


ParseClassificationsResponse

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| parsed | parsed | typing.Dict[str, typing.List[core_models.MarkingId]] | required; no default | Map of valid classification strings to their component marking IDs. Strings that could not be parsed are absent from this map and appear in 'errors' instead. |
| errors | errors | typing.Dict[str, str] | required; no default | Map of classification strings that could not be parsed to a human-readable error message. |

```python
class ParseClassificationsResponse(core.ModelBase):
    """ParseClassificationsResponse"""

    parsed: typing.Dict[str, typing.List[core_models.MarkingId]]
    """Map of valid classification strings to their component marking IDs. Strings that could not be parsed are absent from this map and appear in 'errors' instead."""

    errors: typing.Dict[str, str]
    """Map of classification strings that could not be parsed to a human-readable error message."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.MarkingId](../../core/models/MarkingId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ParseClassificationsResponse.md)
