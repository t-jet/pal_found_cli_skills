# foundry_sdk.v2.filesystem.models.ProjectExternalResourceReference


A reference to a resource that exists outside of the Foundry filesystem such as a spark profile or an LLM model.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| resource_rid | resourceRid | core.RID | required; no default | The resource identifier of the external resource. |
| name | name | str | required; no default | The user-provided label for this reference, used to identify the import within the project. |
| imported_at | importedAt | core.AwareDatetime | required; no default | No additional field description in SDK source. |
| imported_by | importedBy | core_models.UserId | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['external'] | 'external' | No additional field description in SDK source. |

```python
class ProjectExternalResourceReference(core.ModelBase):
    """A reference to a resource that exists outside of the Foundry filesystem such as a spark profile or an LLM model."""

    resource_rid: core.RID = pydantic.Field(alias=str("resourceRid"))  # type: ignore[literal-required]
    """The resource identifier of the external resource."""

    name: str
    """The user-provided label for this reference, used to identify the import within the project."""

    imported_at: core.AwareDatetime = pydantic.Field(alias=str("importedAt"))  # type: ignore[literal-required]
    imported_by: core_models.UserId = pydantic.Field(alias=str("importedBy"))  # type: ignore[literal-required]
    type: typing.Literal["external"] = "external"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)
- [foundry_sdk.v2.core.models.UserId](../../core/models/UserId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ProjectExternalResourceReference.md)
