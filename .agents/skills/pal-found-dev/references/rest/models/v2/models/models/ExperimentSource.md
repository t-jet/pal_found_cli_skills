# foundry_sdk.v2.models.models.ExperimentSource


The source from which the experiment was created.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ExperimentSource: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "ExperimentCodeWorkspaceSource", "ExperimentAuthoringSource", "ExperimentSdkSource"
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.models.models.ExperimentAuthoringSource](ExperimentAuthoringSource.md)
- [foundry_sdk.v2.models.models.ExperimentCodeWorkspaceSource](ExperimentCodeWorkspaceSource.md)
- [foundry_sdk.v2.models.models.ExperimentSdkSource](ExperimentSdkSource.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ExperimentSource.md)
