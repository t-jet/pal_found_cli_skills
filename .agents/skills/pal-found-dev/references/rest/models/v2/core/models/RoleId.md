# foundry_sdk.v2.core.models.RoleId



The unique ID for a Role. Roles are sets of permissions that grant different levels of access to resources.
The default roles in Foundry are: Owner, Editor, Viewer, and Discoverer. See more about 
[roles](https://palantir.com/docs/foundry/security/projects-and-roles#roles) in the user documentation.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
RoleId: typing_extensions.TypeAlias = str
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](RoleId.md)
