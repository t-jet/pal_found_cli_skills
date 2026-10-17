# foundry_sdk.v2.orchestration.models.JobOutput


Other types of Job Outputs exist in Foundry. Currently, only Dataset and Media Set are supported by the API.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
JobOutput: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["DatasetJobOutput", "TransactionalMediaSetJobOutput"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.orchestration.models.DatasetJobOutput](DatasetJobOutput.md)
- [foundry_sdk.v2.orchestration.models.TransactionalMediaSetJobOutput](TransactionalMediaSetJobOutput.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](JobOutput.md)
