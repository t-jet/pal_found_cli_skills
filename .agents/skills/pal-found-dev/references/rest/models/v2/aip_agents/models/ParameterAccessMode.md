# foundry_sdk.v2.aip_agents.models.ParameterAccessMode



READ_ONLY: Allows the variable to be read by the Agent, but the Agent cannot generate updates for it.
READ_WRITE: Allows the variable to be read and updated by the Agent.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ParameterAccessMode: typing_extensions.TypeAlias = typing.Literal["READ_ONLY", "READ_WRITE"]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ParameterAccessMode.md)
