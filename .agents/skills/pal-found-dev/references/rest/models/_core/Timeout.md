# foundry_sdk._core.utils.Timeout


A positive integer request timeout in seconds. Supply it as `request_timeout` where the operation signature permits it. Reaching this bound does not prove whether a write succeeded; reconcile the known resource or transaction before replaying a mutation.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
Timeout: typing.TypeAlias = Annotated[int, pydantic.Field(gt=0)]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../assets/rest/LICENSE).

[Part 1](Timeout.md)
