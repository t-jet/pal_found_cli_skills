# foundry_sdk.v2.filesystem.errors.InvalidDefaultRolesParameters


Either the user has not passed default roles for a template with suggested default roles, or has passed default roles for a template with fixed default roles.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
class InvalidDefaultRolesParameters(typing_extensions.TypedDict):
    """Either the user has not passed default roles for a template with suggested default roles, or has passed default roles for a template with fixed default roles."""

    __pydantic_config__ = {"extra": "allow"}
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidDefaultRolesParameters.md)
