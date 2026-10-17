# foundry_sdk.v2.models.models.GpuType


The specific type of GPU hardware to use.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
GpuType: typing_extensions.TypeAlias = typing.Literal[
    "A100", "A10G", "A16", "H100", "H200", "L4", "L40S", "T4", "V100"
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GpuType.md)
