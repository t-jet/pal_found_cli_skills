# foundry_sdk.v2.sql_queries.errors.ReadQueryInputsPermissionDeniedParameters


The provided token does not have permission to access the inputs to the query.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rids | rids | typing.List[core.RID] | TypedDict key required | The RIDs of the inputs to the query that the user does not have permission to query. |

```python
class ReadQueryInputsPermissionDeniedParameters(typing_extensions.TypedDict):
    """The provided token does not have permission to access the inputs to the query."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    rids: typing.List[core.RID]
    """The RIDs of the inputs to the query that the user does not have permission to query."""
```

## Referenced definitions

- [foundry_sdk._core.utils.RID](../../../_core/RID.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReadQueryInputsPermissionDeniedParameters.md)
