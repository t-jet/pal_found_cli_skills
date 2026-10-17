# foundry_sdk.v2.admin.errors.InvalidGroupMembershipExpirationParameters


The member expiration you provided does not conform to the Group's requirements for member expirations.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| groupId | groupId | core_models.GroupId | TypedDict key required | No additional field description in SDK source. |
| earliestExpiration | earliestExpiration | core.AwareDatetime | TypedDict key required | No additional field description in SDK source. |
| maximumDuration | maximumDuration | typing_extensions.NotRequired[core_models.DurationSeconds] | TypedDict key may be omitted | No additional field description in SDK source. |
| maximumValue | maximumValue | typing_extensions.NotRequired[admin_models.GroupMembershipExpiration] | TypedDict key may be omitted | No additional field description in SDK source. |

```python
class InvalidGroupMembershipExpirationParameters(typing_extensions.TypedDict):
    """The member expiration you provided does not conform to the Group's requirements for member expirations."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    groupId: core_models.GroupId
    earliestExpiration: core.AwareDatetime
    maximumDuration: typing_extensions.NotRequired[core_models.DurationSeconds]
    maximumValue: typing_extensions.NotRequired[admin_models.GroupMembershipExpiration]
```

## Referenced definitions

- [foundry_sdk._core.utils.AwareDatetime](../../../_core/AwareDatetime.md)
- [foundry_sdk.v2.admin.models.GroupMembershipExpiration](../models/GroupMembershipExpiration.md)
- [foundry_sdk.v2.core.models.DurationSeconds](../../core/models/DurationSeconds.md)
- [foundry_sdk.v2.core.models.GroupId](../../core/models/GroupId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidGroupMembershipExpirationParameters.md)
