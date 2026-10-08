# foundry_sdk.v2.data_health.errors.CheckReportNotFoundParameters


The given CheckReport could not be found.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| checkReportRid | checkReportRid | core_models.CheckReportRid | TypedDict key required | No additional field description in SDK source. |
| checkRid | checkRid | core_models.CheckRid | TypedDict key required | No additional field description in SDK source. |

```python
class CheckReportNotFoundParameters(typing_extensions.TypedDict):
    """The given CheckReport could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    checkReportRid: core_models.CheckReportRid
    checkRid: core_models.CheckRid
```

## Referenced definitions

- [foundry_sdk.v2.core.models.CheckReportRid](../../core/models/CheckReportRid.md)
- [foundry_sdk.v2.core.models.CheckRid](../../core/models/CheckRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CheckReportNotFoundParameters.md)
