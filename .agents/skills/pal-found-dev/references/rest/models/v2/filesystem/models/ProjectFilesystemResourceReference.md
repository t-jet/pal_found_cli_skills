# foundry_sdk.v2.filesystem.models.ProjectFilesystemResourceReference


A reference to a resource that exists within another project

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| resource_rid | resourceRid | ResourceRid | required; no default | No additional field description in SDK source. |
| name | name | str | required; no default | The display name of the referenced resource. |
| imported_at | importedAt | core.AwareDatetime | required; no default | No additional field description in SDK source. |
| imported_by | importedBy | core_models.UserId | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['filesystem'] | 'filesystem' | No additional field description in SDK source. |

```python
class ProjectFilesystemResourceReference(core.ModelBase):
    """A reference to a resource that exists within another project"""

    resource_rid: ResourceRid = pydantic.Field(alias=str("resourceRid"))  # type: ignore[literal-required]
    name: str
    """The display name of the referenced resource."""

    imported_at: core.AwareDatetime = pydantic.Field(alias=str("importedAt"))  # type: ignore[literal-required]
    imported_by: core_models.UserId = pydantic.Field(alias=str("importedBy"))  # type: ignore[literal-required]
    type: typing.Literal["filesystem"] = "filesystem"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../_core/AwareDatetime.md)
- [foundry_sdk.v2.core.models.UserId](../../core/models/UserId.md)
- [foundry_sdk.v2.filesystem.models.ResourceRid](ResourceRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ProjectFilesystemResourceReference.md)
