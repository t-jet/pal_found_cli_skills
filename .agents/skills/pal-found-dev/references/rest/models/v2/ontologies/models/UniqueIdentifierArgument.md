# foundry_sdk.v2.ontologies.models.UniqueIdentifierArgument


Represents a unique identifier argument in a logic rule.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| link_id | linkId | typing.Optional[core.UUID] | default None | By default all UniqueIdentifier Logic Rule arguments will generate different UUID. <br>    If the linkId is present all Logic Rules with the same linkId will all have the same uuid generated as the value. |
| type | type | typing.Literal['uniqueIdentifier'] | 'uniqueIdentifier' | No additional field description in SDK source. |

```python
class UniqueIdentifierArgument(core.ModelBase):
    """Represents a unique identifier argument in a logic rule."""

    link_id: typing.Optional[core.UUID] = pydantic.Field(alias=str("linkId"), default=None)  # type: ignore[literal-required]
    """
    By default all UniqueIdentifier Logic Rule arguments will generate different UUID. 
    If the linkId is present all Logic Rules with the same linkId will all have the same uuid generated as the value.
    """

    type: typing.Literal["uniqueIdentifier"] = "uniqueIdentifier"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.UUID](../../../_core/UUID.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](UniqueIdentifierArgument.md)
