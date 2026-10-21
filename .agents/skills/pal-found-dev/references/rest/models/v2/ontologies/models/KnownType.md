# foundry_sdk.v2.ontologies.models.KnownType



Known Foundry types for specialized formatting:
- userOrGroupRid: Format as user or group
- resourceRid: Format as resource 
- artifactGid: Format as artifact


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
KnownType: typing_extensions.TypeAlias = typing.Literal[
    "USER_OR_GROUP_ID", "RESOURCE_RID", "ARTIFACT_GID"
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](KnownType.md)
