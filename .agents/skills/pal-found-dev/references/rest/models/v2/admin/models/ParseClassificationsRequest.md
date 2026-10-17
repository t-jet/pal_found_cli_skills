# foundry_sdk.v2.admin.models.ParseClassificationsRequest


ParseClassificationsRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| classification_strings | classificationStrings | typing.List[str] | required; no default | The classification strings to parse, e.g. 'S//NF'. Duplicate entries are ignored. At most 1000 entries are accepted. |

```python
class ParseClassificationsRequest(core.ModelBase):
    """ParseClassificationsRequest"""

    classification_strings: typing.List[str] = pydantic.Field(alias=str("classificationStrings"))  # type: ignore[literal-required]
    """The classification strings to parse, e.g. 'S//NF'. Duplicate entries are ignored. At most 1000 entries are accepted."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ParseClassificationsRequest.md)
