# foundry_sdk.v2.models.models.CreateModelVersionRequest


CreateModelVersionRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| model_files | modelFiles | ModelFiles | required; no default | No additional field description in SDK source. |
| backing_repositories | backingRepositories | typing.List[core.RID] | required; no default | No additional field description in SDK source. |
| conda_requirements | condaRequirements | typing.List[str] | required; no default | No additional field description in SDK source. |
| model_api | modelApi | ModelApi | required; no default | No additional field description in SDK source. |

```python
class CreateModelVersionRequest(core.ModelBase):
    """CreateModelVersionRequest"""

    model_files: ModelFiles = pydantic.Field(alias=str("modelFiles"))  # type: ignore[literal-required]
    backing_repositories: typing.List[core.RID] = pydantic.Field(alias=str("backingRepositories"))  # type: ignore[literal-required]
    conda_requirements: typing.List[str] = pydantic.Field(alias=str("condaRequirements"))  # type: ignore[literal-required]
    model_api: ModelApi = pydantic.Field(alias=str("modelApi"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)
- [foundry_sdk.v2.models.models.ModelApi](ModelApi.md)
- [foundry_sdk.v2.models.models.ModelFiles](ModelFiles.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateModelVersionRequest.md)
