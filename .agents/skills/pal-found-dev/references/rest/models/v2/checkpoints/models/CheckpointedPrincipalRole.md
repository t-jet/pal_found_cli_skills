# foundry_sdk.v2.checkpoints.models.CheckpointedPrincipalRole


Role the principal had relative to the checkpointed entity.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
CheckpointedPrincipalRole: typing_extensions.TypeAlias = typing.Literal[
    "SOURCE_SHARE_RECIPIENT",
    "TARGET_GROUP",
    "GROUP_MEMBER",
    "MARKING_MEMBER",
    "ROLE_GRANT_RECIPIENT",
    "MFA_METHOD_RESET_TARGET",
    "ISSUE_ASSIGNEE",
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CheckpointedPrincipalRole.md)
