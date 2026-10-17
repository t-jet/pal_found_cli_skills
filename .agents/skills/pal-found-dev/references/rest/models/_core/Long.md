# foundry_sdk._core.utils.Long


A long integer that is serialized to a string in JSON.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
Long: typing.TypeAlias = Annotated[
    int,
    pydantic.PlainSerializer(
        lambda value: str(value),
        return_type=str,
        # Important: This ensures the value is not serialized when using to_dict()
        # We only want to serialize when dumping to a JSON string
        when_used="json",
    ),
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../assets/rest/LICENSE).

[Part 1](Long.md)
