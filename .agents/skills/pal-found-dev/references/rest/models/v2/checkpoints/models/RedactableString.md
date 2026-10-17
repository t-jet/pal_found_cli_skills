# foundry_sdk.v2.checkpoints.models.RedactableString


A string value that may be redacted for privacy reasons.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| value | value | typing.Optional[str] | None | No additional field description in SDK source. |
| redaction_type | redactionType | typing.Optional[RedactionType] | default None | No additional field description in SDK source. |

```python
class RedactableString(core.ModelBase):
    """A string value that may be redacted for privacy reasons."""

    value: typing.Optional[str] = None
    redaction_type: typing.Optional[RedactionType] = pydantic.Field(alias=str("redactionType"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.checkpoints.models.RedactionType](RedactionType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](RedactableString.md)
