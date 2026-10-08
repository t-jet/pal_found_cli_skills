# foundry_sdk.v2.filesystem.errors.TemplateMarkingNameConflictParameters


Creating the project from template would attempt to create new markings with names conflicting either with other new markings, or existing markings.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| conflictingMarkingNames | conflictingMarkingNames | typing.List[str] | TypedDict key required | No additional field description in SDK source. |

```python
class TemplateMarkingNameConflictParameters(typing_extensions.TypedDict):
    """Creating the project from template would attempt to create new markings with names conflicting either with other new markings, or existing markings."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    conflictingMarkingNames: typing.List[str]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TemplateMarkingNameConflictParameters.md)
