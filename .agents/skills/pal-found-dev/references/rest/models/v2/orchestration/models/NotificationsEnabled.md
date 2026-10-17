# foundry_sdk.v2.orchestration.models.NotificationsEnabled



Whether to receive a notification at the end of the build.
The notification will be sent to the user that has most recently edited the schedule.
No notification will be sent if the schedule has `scopeMode` set to `ProjectScope`.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
NotificationsEnabled: typing_extensions.TypeAlias = bool
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NotificationsEnabled.md)
