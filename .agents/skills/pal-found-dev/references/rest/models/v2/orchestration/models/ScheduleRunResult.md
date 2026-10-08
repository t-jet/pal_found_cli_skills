# foundry_sdk.v2.orchestration.models.ScheduleRunResult



The result of attempting to trigger the schedule. The schedule run will either be submitted as a build,
ignored if all targets are up-to-date or error.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ScheduleRunResult: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["ScheduleRunIgnored", "ScheduleRunSubmitted", "ScheduleRunError"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.orchestration.models.ScheduleRunError](ScheduleRunError.md)
- [foundry_sdk.v2.orchestration.models.ScheduleRunIgnored](ScheduleRunIgnored.md)
- [foundry_sdk.v2.orchestration.models.ScheduleRunSubmitted](ScheduleRunSubmitted.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ScheduleRunResult.md)
