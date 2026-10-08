# foundry_sdk.v2.models.models.ModelVersionCodeRepositorySource


Model version created from a code repository.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| repository_rid | repositoryRid | core.RID | required; no default | No additional field description in SDK source. |
| branch | branch | str | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['codeRepository'] | 'codeRepository' | No additional field description in SDK source. |

```python
class ModelVersionCodeRepositorySource(core.ModelBase):
    """Model version created from a code repository."""

    repository_rid: core.RID = pydantic.Field(alias=str("repositoryRid"))  # type: ignore[literal-required]
    branch: str
    type: typing.Literal["codeRepository"] = "codeRepository"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ModelVersionCodeRepositorySource.md)
