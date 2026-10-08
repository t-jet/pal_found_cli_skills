# foundry_sdk.v2.sql_queries.errors.OntologyObjectTypeNotFoundParameters


The ontology query referenced an object type RID that does not exist or
is not visible to the requesting user. Verify the RID (e.g. via
list-object-types or get-object-type-details) and retry.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| objectTypeRid | objectTypeRid | core.RID | TypedDict key required | No additional field description in SDK source. |

```python
class OntologyObjectTypeNotFoundParameters(typing_extensions.TypedDict):
    """
    The ontology query referenced an object type RID that does not exist or
    is not visible to the requesting user. Verify the RID (e.g. via
    list-object-types or get-object-type-details) and retry.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectTypeRid: core.RID
```

## Referenced definitions

- [foundry_sdk._core.utils.RID](../../../_core/RID.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OntologyObjectTypeNotFoundParameters.md)
