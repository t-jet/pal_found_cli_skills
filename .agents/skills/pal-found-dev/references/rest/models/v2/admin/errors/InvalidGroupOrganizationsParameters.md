# foundry_sdk.v2.admin.errors.InvalidGroupOrganizationsParameters


At least one Organization RID must be provided for a group

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
class InvalidGroupOrganizationsParameters(typing_extensions.TypedDict):
    """At least one Organization RID must be provided for a group"""

    __pydantic_config__ = {"extra": "allow"}
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidGroupOrganizationsParameters.md)
