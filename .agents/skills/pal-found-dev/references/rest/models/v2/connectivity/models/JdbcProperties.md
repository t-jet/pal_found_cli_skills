# foundry_sdk.v2.connectivity.models.JdbcProperties


This is a map of JDBC driver property names to unencrypted values. Take supported keys from the approved driver and connector configuration; this SDK type declares no universal keys or defaults. Put passwords and tokens in the connector's encrypted authentication fields.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
JdbcProperties: typing_extensions.TypeAlias = typing.Dict[str, str]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](JdbcProperties.md)
