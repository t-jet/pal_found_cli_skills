# foundry_sdk.v2.orchestration.models.Trigger


Trigger

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
Trigger: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "JobSucceededTrigger",
        "OrTrigger",
        "NewLogicTrigger",
        "TableUpdatedTrigger",
        "AndTrigger",
        "DatasetUpdatedTrigger",
        "ScheduleSucceededTrigger",
        "MediaSetUpdatedTrigger",
        "TimeTrigger",
        "ManualTrigger",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.orchestration.models.AndTrigger](AndTrigger.md)
- [foundry_sdk.v2.orchestration.models.DatasetUpdatedTrigger](DatasetUpdatedTrigger.md)
- [foundry_sdk.v2.orchestration.models.JobSucceededTrigger](JobSucceededTrigger.md)
- [foundry_sdk.v2.orchestration.models.ManualTrigger](ManualTrigger.md)
- [foundry_sdk.v2.orchestration.models.MediaSetUpdatedTrigger](MediaSetUpdatedTrigger.md)
- [foundry_sdk.v2.orchestration.models.NewLogicTrigger](NewLogicTrigger.md)
- [foundry_sdk.v2.orchestration.models.OrTrigger](OrTrigger.md)
- [foundry_sdk.v2.orchestration.models.ScheduleSucceededTrigger](ScheduleSucceededTrigger.md)
- [foundry_sdk.v2.orchestration.models.TableUpdatedTrigger](TableUpdatedTrigger.md)
- [foundry_sdk.v2.orchestration.models.TimeTrigger](TimeTrigger.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Trigger.md)
