# foundry_sdk.v2.connectivity.models.StsRoleConfiguration


`role_arn` names the AWS IAM role to assume, for example `arn:aws:iam::123456789012:role/example-role`; it is not a user or account-root ARN. `role_session_name` identifies this assumed session and should be unique enough for audit. If supplied, `role_session_duration` is at least 900 seconds and no greater than the role's configured maximum (which can be 1–12 hours); AWS role chaining imposes a one-hour maximum. `external_id` must match the role trust arrangement when one is required. `sts_endpoint` selects the STS endpoint; use the tenant's approved region/endpoint. A valid ARN alone does not grant AssumeRole permission or satisfy the trust policy.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| role_arn | roleArn | str | required; no default | The Amazon Resource Name (ARN) of the role to assume.<br>     |
| role_session_name | roleSessionName | str | required; no default | An identifier for the assumed role session.<br>    The value can be any string that you assume will be unique within the AWS account.<br>     |
| role_session_duration | roleSessionDuration | typing.Optional[core_models.Duration] | default None | The duration of the role session.<br>    The value specified can range from 900 seconds (15 minutes) up to the maximum session duration set for the role.<br>    The maximum session duration setting can have a value from 1 hour to 12 hours.  |
| external_id | externalId | typing.Optional[str] | default None | A unique identifier that is used by third parties when assuming roles in their customers' accounts.<br>     |
| sts_endpoint | stsEndpoint | typing.Optional[str] | default None | By default, the AWS Security Token Service (AWS STS) is available as a global service, and all AWS STS requests go to a single endpoint at https://sts.amazonaws.com.<br>    AWS recommends using Regional AWS STS endpoints instead of the global endpoint to reduce latency, build in redundancy, and increase session token validity. |

```python
class StsRoleConfiguration(core.ModelBase):
    """StsRoleConfiguration"""

    role_arn: str = pydantic.Field(alias=str("roleArn"))  # type: ignore[literal-required]
    """
    The Amazon Resource Name (ARN) of the role to assume.
    For more information, see the official [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-arn-format).
    """

    role_session_name: str = pydantic.Field(alias=str("roleSessionName"))  # type: ignore[literal-required]
    """
    An identifier for the assumed role session.
    The value can be any string that you assume will be unique within the AWS account.
    For more information, see the official [AWS documentation](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html#API_AssumeRole_RequestParameters).
    """

    role_session_duration: typing.Optional[core_models.Duration] = pydantic.Field(alias=str("roleSessionDuration"), default=None)  # type: ignore[literal-required]
    """
    The duration of the role session.
    The value specified can range from 900 seconds (15 minutes) up to the maximum session duration set for the role.
    The maximum session duration setting can have a value from 1 hour to 12 hours. For more details see the official [AWS documentation](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html#API_AssumeRole_RequestParameters).
    """

    external_id: typing.Optional[str] = pydantic.Field(alias=str("externalId"), default=None)  # type: ignore[literal-required]
    """
    A unique identifier that is used by third parties when assuming roles in their customers' accounts.
    For more information, see the official [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html).
    """

    sts_endpoint: typing.Optional[str] = pydantic.Field(alias=str("stsEndpoint"), default=None)  # type: ignore[literal-required]
    """
    By default, the AWS Security Token Service (AWS STS) is available as a global service, and all AWS STS requests go to a single endpoint at https://sts.amazonaws.com.
    AWS recommends using Regional AWS STS endpoints instead of the global endpoint to reduce latency, build in redundancy, and increase session token validity.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.Duration](../../core/models/Duration.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](StsRoleConfiguration.md)
