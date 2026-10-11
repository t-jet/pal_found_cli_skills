# foundry_sdk._core.utils.UUID


A hyphenated UUID string matching the SDK hexadecimal pattern below. Preserve the returned identifier for later requests; this shape alone does not imply a Foundry RID or validate a resource's existence.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
UUID: typing.TypeAlias = Annotated[
    str,
    pydantic.StringConstraints(
        pattern=r"^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$",
    ),
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../assets/rest/LICENSE).

[Part 1](UUID.md)
