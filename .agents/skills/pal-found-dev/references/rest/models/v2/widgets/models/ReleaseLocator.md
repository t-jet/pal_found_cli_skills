# foundry_sdk.v2.widgets.models.ReleaseLocator


A locator for where the backing files of a release are stored.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| repository_rid | repositoryRid | RepositoryRid | required; no default | The Resource Identifier (RID) of the repository that contains the release. |
| repository_version | repositoryVersion | RepositoryVersion | required; no default | The version of the repository storing the backing files. |

```python
class ReleaseLocator(core.ModelBase):
    """A locator for where the backing files of a release are stored."""

    repository_rid: RepositoryRid = pydantic.Field(alias=str("repositoryRid"))  # type: ignore[literal-required]
    """The Resource Identifier (RID) of the repository that contains the release."""

    repository_version: RepositoryVersion = pydantic.Field(alias=str("repositoryVersion"))  # type: ignore[literal-required]
    """The version of the repository storing the backing files."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.widgets.models.RepositoryRid](RepositoryRid.md)
- [foundry_sdk.v2.widgets.models.RepositoryVersion](RepositoryVersion.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReleaseLocator.md)
