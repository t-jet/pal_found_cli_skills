# foundry_sdk.v2.core.models.RoleId


A Role ID identifies a permission set on a resource. Common roles are Owner, Editor, Viewer and Discoverer, but use the ID returned for the target resource and enrollment when assigning a role. A display name alone does not establish its ID or effective access.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
RoleId: typing_extensions.TypeAlias = str
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](RoleId.md)
