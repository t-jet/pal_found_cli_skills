# foundry_sdk.v2.models.errors.OntologyNotFoundParameters


The specified ontology was not found.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| ontologyRid | ontologyRid | core.RID | TypedDict key required | No additional field description in SDK source. |

```python
class OntologyNotFoundParameters(typing_extensions.TypedDict):
    """The specified ontology was not found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    ontologyRid: core.RID
```

## Referenced definitions

- [foundry_sdk._core.utils.RID](../../../_core/RID.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OntologyNotFoundParameters.md)
