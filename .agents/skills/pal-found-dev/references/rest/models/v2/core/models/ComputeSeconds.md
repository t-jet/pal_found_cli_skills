# foundry_sdk.v2.core.models.ComputeSeconds


Compute seconds measure consumed compute time for resource usage accounting. This SDK alias gives a numeric quantity, not a charge or a per-operation quota. Interpret it with the usage record's resource and time window.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ComputeSeconds: typing_extensions.TypeAlias = float
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ComputeSeconds.md)
