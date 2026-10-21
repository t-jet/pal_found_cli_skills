# foundry_sdk.v2.filesystem.errors.SpaceNameInvalidParameters


The provided space name is invalid. It may be a reserved name or contain invalid characters.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
class SpaceNameInvalidParameters(typing_extensions.TypedDict):
    """The provided space name is invalid. It may be a reserved name or contain invalid characters."""

    __pydantic_config__ = {"extra": "allow"}
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SpaceNameInvalidParameters.md)
