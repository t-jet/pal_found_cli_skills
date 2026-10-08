# foundry_sdk._core.utils.RID


The definition below supplies its fields or permitted values.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
RID: typing.TypeAlias = Annotated[
    str,
    pydantic.StringConstraints(
        pattern=r"^ri\.[a-z][a-z0-9-]*\.([a-z0-9][a-z0-9\-]*)?\.[a-z][a-z0-9-]*\.[a-zA-Z0-9._-]+$",
    ),
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../assets/rest/LICENSE).

[Part 1](RID.md)
