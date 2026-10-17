# foundry_sdk.v2.filesystem.errors.InvalidDescriptionParameters


Either the user has not passed a value for a template with unset project description, or has passed a value for a template with fixed project description.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
class InvalidDescriptionParameters(typing_extensions.TypedDict):
    """Either the user has not passed a value for a template with unset project description, or has passed a value for a template with fixed project description."""

    __pydantic_config__ = {"extra": "allow"}
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidDescriptionParameters.md)
