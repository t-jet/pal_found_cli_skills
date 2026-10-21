# foundry_sdk.v2.orchestration.errors.CancelBuildPermissionDeniedParameters


Could not cancel the Build.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| buildRid | buildRid | core_models.BuildRid | TypedDict key required | The RID of a Build. |

```python
class CancelBuildPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not cancel the Build."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    buildRid: core_models.BuildRid
    """The RID of a Build."""
```

## Referenced definitions

- [foundry_sdk.v2.core.models.BuildRid](../../core/models/BuildRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CancelBuildPermissionDeniedParameters.md)
