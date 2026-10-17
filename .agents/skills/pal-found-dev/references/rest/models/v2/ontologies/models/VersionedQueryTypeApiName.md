# foundry_sdk.v2.ontologies.models.VersionedQueryTypeApiName



The name of the Query in the API and an optional version identifier separated by a colon.
If the API name contains a colon, then a version identifier of either "latest" or a semantic version must
be included.
If the API does not contain a colon, then either the version identifier must be excluded or a version
identifier of a semantic version must be included.
Examples: 'myGroup:myFunction:latest', 'myGroup:myFunction:1.0.0', 'myFunction', 'myFunction:2.0.0'


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
VersionedQueryTypeApiName: typing_extensions.TypeAlias = str
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](VersionedQueryTypeApiName.md)
