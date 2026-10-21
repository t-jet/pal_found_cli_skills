# foundry_sdk.v2.media_sets.models.DataType


The data type of a band.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
DataType: typing_extensions.TypeAlias = typing.Literal[
    "UNDEFINED",
    "BYTE",
    "UINT16",
    "INT16",
    "UINT32",
    "INT32",
    "FLOAT32",
    "FLOAT64",
    "COMPLEX_INT16",
    "COMPLEX_INT32",
    "COMPLEX_FLOAT32",
    "COMPLEX_FLOAT64",
    "UINT64",
    "INT64",
    "INT8",
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DataType.md)
