# foundry_sdk.v2.ontologies.models.TypeClassPredicateV2


A predicate for matching type classes. Matches a type class when `kind`, and `name` if provided, match the
corresponding attribute of the type class. If `name` is empty, only `kind` is required to match. You can
search for both parameter type classes and action type type classes.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| kind | kind | str | required; no default | Exact match predicate for the `kind` attribute of a type class. |
| name | name | typing.Optional[str] | None | Exact match predicate for the `name` attribute of a type class. |

```python
class TypeClassPredicateV2(core.ModelBase):
    """
    A predicate for matching type classes. Matches a type class when `kind`, and `name` if provided, match the
    corresponding attribute of the type class. If `name` is empty, only `kind` is required to match. You can
    search for both parameter type classes and action type type classes.
    """

    kind: str
    """Exact match predicate for the `kind` attribute of a type class."""

    name: typing.Optional[str] = None
    """Exact match predicate for the `name` attribute of a type class."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TypeClassPredicateV2.md)
