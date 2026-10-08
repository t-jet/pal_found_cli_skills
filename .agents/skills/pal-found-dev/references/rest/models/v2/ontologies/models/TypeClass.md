# foundry_sdk.v2.ontologies.models.TypeClass


Additional metadata that can be interpreted by user applications that interact with the Ontology

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| kind | kind | str | required; no default | A namespace for the type class. |
| name | name | str | required; no default | The value of the type class. |

```python
class TypeClass(core.ModelBase):
    """Additional metadata that can be interpreted by user applications that interact with the Ontology"""

    kind: str
    """A namespace for the type class."""

    name: str
    """The value of the type class."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TypeClass.md)
