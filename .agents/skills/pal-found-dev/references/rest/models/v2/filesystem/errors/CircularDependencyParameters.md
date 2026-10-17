# foundry_sdk.v2.filesystem.errors.CircularDependencyParameters


The requested operation would result in a circular dependency in the folder hierarchy. For example, moving a folder into one of its descendants.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
class CircularDependencyParameters(typing_extensions.TypedDict):
    """The requested operation would result in a circular dependency in the folder hierarchy. For example, moving a folder into one of its descendants."""

    __pydantic_config__ = {"extra": "allow"}
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CircularDependencyParameters.md)
