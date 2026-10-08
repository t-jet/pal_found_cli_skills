# foundry_sdk.v2.orchestration.models.CreateScheduleRequestScopeMode


The boundaries for the schedule build.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
CreateScheduleRequestScopeMode: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["CreateScheduleRequestProjectScope", "CreateScheduleRequestUserScope"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.orchestration.models.CreateScheduleRequestProjectScope](CreateScheduleRequestProjectScope.md)
- [foundry_sdk.v2.orchestration.models.CreateScheduleRequestUserScope](CreateScheduleRequestUserScope.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateScheduleRequestScopeMode.md)
