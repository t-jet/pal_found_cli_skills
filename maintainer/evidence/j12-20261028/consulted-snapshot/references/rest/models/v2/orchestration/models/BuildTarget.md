# foundry_sdk.v2.orchestration.models.BuildTarget


The targets of the build.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
BuildTarget: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["UpstreamTarget", "ManualTarget", "ConnectingTarget"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.orchestration.models.ConnectingTarget](ConnectingTarget.md)
- [foundry_sdk.v2.orchestration.models.ManualTarget](ManualTarget.md)
- [foundry_sdk.v2.orchestration.models.UpstreamTarget](UpstreamTarget.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](BuildTarget.md)
