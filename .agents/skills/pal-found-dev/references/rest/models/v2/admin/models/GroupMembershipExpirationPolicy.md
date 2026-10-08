# foundry_sdk.v2.admin.models.GroupMembershipExpirationPolicy


GroupMembershipExpirationPolicy

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| maximum_value | maximumValue | typing.Optional[GroupMembershipExpiration] | default None | Members in this group must be added with expiration times that occur before this value. |
| maximum_duration | maximumDuration | typing.Optional[core_models.DurationSeconds] | default None | Members in this group must be added with expirations that are less than this duration in seconds into the future from the time they are added. |

```python
class GroupMembershipExpirationPolicy(core.ModelBase):
    """GroupMembershipExpirationPolicy"""

    maximum_value: typing.Optional[GroupMembershipExpiration] = pydantic.Field(alias=str("maximumValue"), default=None)  # type: ignore[literal-required]
    """Members in this group must be added with expiration times that occur before this value."""

    maximum_duration: typing.Optional[core_models.DurationSeconds] = pydantic.Field(alias=str("maximumDuration"), default=None)  # type: ignore[literal-required]
    """Members in this group must be added with expirations that are less than this duration in seconds into the future from the time they are added."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.admin.models.GroupMembershipExpiration](GroupMembershipExpiration.md)
- [foundry_sdk.v2.core.models.DurationSeconds](../../core/models/DurationSeconds.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GroupMembershipExpirationPolicy.md)
