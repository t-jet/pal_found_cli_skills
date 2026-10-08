# foundry_sdk.v2.connectivity.models.JdbcProperties



A map of [properties](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Properties.html) passed 
to the JDBC driver to configure behavior. Refer to the documentation of your specific connection type for additional 
available JDBC properties to add to your connection configuration.
This should only contain unencrypted properties, all values specified here are sent unencrypted to Foundry.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
JdbcProperties: typing_extensions.TypeAlias = typing.Dict[str, str]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](JdbcProperties.md)
