# foundry_sdk.v2.orchestration.models.FallbackBranches



The branches to retrieve JobSpecs from if no JobSpec is found on the
target branch.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
FallbackBranches: typing_extensions.TypeAlias = typing.List[core_models.BranchName]
```

## Referenced definitions

- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FallbackBranches.md)
