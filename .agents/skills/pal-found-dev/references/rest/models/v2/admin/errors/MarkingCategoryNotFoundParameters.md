# foundry_sdk.v2.admin.errors.MarkingCategoryNotFoundParameters


The given MarkingCategory could not be found.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| markingCategoryId | markingCategoryId | admin_models.MarkingCategoryId | TypedDict key required | No additional field description in SDK source. |

```python
class MarkingCategoryNotFoundParameters(typing_extensions.TypedDict):
    """The given MarkingCategory could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    markingCategoryId: admin_models.MarkingCategoryId
```

## Referenced definitions

- [foundry_sdk.v2.admin.models.MarkingCategoryId](../models/MarkingCategoryId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MarkingCategoryNotFoundParameters.md)
