# foundry_sdk.v2.core.models.Operation



An operation that can be performed on a resource. Operations are used to define the permissions that a Role has.
Operations are typically in the format `service:action`, where `service` is related to the type of resource and `action` is the action being performed.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
Operation: typing_extensions.TypeAlias = str
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Operation.md)
