# foundry_sdk.v2.sql_queries.errors.OntologyQueryInvalidObjectBackendParameters


The ontology query references object types or link types indexed in Object
Storage V1, which is incompatible with Ontology SQL. Migrate the entities
to Object Storage V2 or remove them from the query.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| objectTypeRids | objectTypeRids | typing.List[core.RID] | TypedDict key required | No additional field description in SDK source. |
| linkTypeRids | linkTypeRids | typing.List[core.RID] | TypedDict key required | No additional field description in SDK source. |

```python
class OntologyQueryInvalidObjectBackendParameters(typing_extensions.TypedDict):
    """
    The ontology query references object types or link types indexed in Object
    Storage V1, which is incompatible with Ontology SQL. Migrate the entities
    to Object Storage V2 or remove them from the query.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    objectTypeRids: typing.List[core.RID]
    linkTypeRids: typing.List[core.RID]
```

## Referenced definitions

- [foundry_sdk._core.utils.RID](../../../_core/RID.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OntologyQueryInvalidObjectBackendParameters.md)
