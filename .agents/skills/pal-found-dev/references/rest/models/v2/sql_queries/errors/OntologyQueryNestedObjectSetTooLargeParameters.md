# foundry_sdk.v2.sql_queries.errors.OntologyQueryNestedObjectSetTooLargeParameters


The query references too many objects across joins, link lookups, or
sub-queries. Narrow the scope (add filters, reduce joins, restrict
object types) and retry. The actual and maximum object counts are
returned as parameters.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| nestedObjectSetSize | nestedObjectSetSize | core.Long | TypedDict key required | No additional field description in SDK source. |
| maxAllowedNestedObjectSetSize | maxAllowedNestedObjectSetSize | core.Long | TypedDict key required | No additional field description in SDK source. |

```python
class OntologyQueryNestedObjectSetTooLargeParameters(typing_extensions.TypedDict):
    """
    The query references too many objects across joins, link lookups, or
    sub-queries. Narrow the scope (add filters, reduce joins, restrict
    object types) and retry. The actual and maximum object counts are
    returned as parameters.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    nestedObjectSetSize: core.Long
    maxAllowedNestedObjectSetSize: core.Long
```

## Referenced definitions

- [foundry_sdk._core.utils.Long](../../../_core/Long.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OntologyQueryNestedObjectSetTooLargeParameters.md)
