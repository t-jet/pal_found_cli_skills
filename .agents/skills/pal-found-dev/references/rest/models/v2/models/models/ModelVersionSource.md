# foundry_sdk.v2.models.models.ModelVersionSource


The source from which this model version was created.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ModelVersionSource: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "ModelVersionContainerizedSource",
        "ModelVersionExternalSource",
        "ModelVersionCodeWorkspaceSource",
        "ModelVersionModelStudioSource",
        "ModelVersionCodeRepositorySource",
        "ModelVersionSdkSource",
        "ModelVersionPromotedSource",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.models.models.ModelVersionCodeRepositorySource](ModelVersionCodeRepositorySource.md)
- [foundry_sdk.v2.models.models.ModelVersionCodeWorkspaceSource](ModelVersionCodeWorkspaceSource.md)
- [foundry_sdk.v2.models.models.ModelVersionContainerizedSource](ModelVersionContainerizedSource.md)
- [foundry_sdk.v2.models.models.ModelVersionExternalSource](ModelVersionExternalSource.md)
- [foundry_sdk.v2.models.models.ModelVersionModelStudioSource](ModelVersionModelStudioSource.md)
- [foundry_sdk.v2.models.models.ModelVersionPromotedSource](ModelVersionPromotedSource.md)
- [foundry_sdk.v2.models.models.ModelVersionSdkSource](ModelVersionSdkSource.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ModelVersionSource.md)
