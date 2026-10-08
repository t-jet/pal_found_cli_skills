# foundry_sdk.v2.checkpoints.models.CheckpointedResource


A Foundry resource that was captured as part of a checkpoint.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | core.RID | required; no default | No additional field description in SDK source. |
| resource_type | resourceType | CheckpointedResourceType | required; no default | No additional field description in SDK source. |
| name | name | typing.Optional[RedactableString] | None | No additional field description in SDK source. |
| project_rid | projectRid | typing.Optional[ProjectRid] | default None | No additional field description in SDK source. |
| namespace_rid | namespaceRid | typing.Optional[NamespaceRid] | default None | No additional field description in SDK source. |
| compass_path | compassPath | RedactableString | required; no default | No additional field description in SDK source. |
| org_markings | orgMarkings | typing.List[str] | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['checkpointedResource'] | 'checkpointedResource' | No additional field description in SDK source. |

```python
class CheckpointedResource(core.ModelBase):
    """A Foundry resource that was captured as part of a checkpoint."""

    rid: core.RID
    resource_type: CheckpointedResourceType = pydantic.Field(alias=str("resourceType"))  # type: ignore[literal-required]
    name: typing.Optional[RedactableString] = None
    project_rid: typing.Optional[ProjectRid] = pydantic.Field(alias=str("projectRid"), default=None)  # type: ignore[literal-required]
    namespace_rid: typing.Optional[NamespaceRid] = pydantic.Field(alias=str("namespaceRid"), default=None)  # type: ignore[literal-required]
    compass_path: RedactableString = pydantic.Field(alias=str("compassPath"))  # type: ignore[literal-required]
    org_markings: typing.List[str] = pydantic.Field(alias=str("orgMarkings"))  # type: ignore[literal-required]
    type: typing.Literal["checkpointedResource"] = "checkpointedResource"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)
- [foundry_sdk.v2.checkpoints.models.CheckpointedResourceType](CheckpointedResourceType.md)
- [foundry_sdk.v2.checkpoints.models.NamespaceRid](NamespaceRid.md)
- [foundry_sdk.v2.checkpoints.models.ProjectRid](ProjectRid.md)
- [foundry_sdk.v2.checkpoints.models.RedactableString](RedactableString.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CheckpointedResource.md)
