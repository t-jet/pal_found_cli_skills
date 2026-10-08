# foundry_sdk.v2.connectivity.models.AwsAccessKey


[Access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) are long-term
credentials for an IAM user or the AWS account root user.
Access keys consist of two parts: an access key ID (for example, AKIAIOSFODNN7EXAMPLE) and a secret access
key (for example, wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY). You must use both the access key ID and
secret access key together to authenticate your requests.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| access_key_id | accessKeyId | str | required; no default | No additional field description in SDK source. |
| secret_access_key | secretAccessKey | EncryptedProperty | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['awsAccessKey'] | 'awsAccessKey' | No additional field description in SDK source. |

```python
class AwsAccessKey(core.ModelBase):
    """
    [Access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) are long-term
    credentials for an IAM user or the AWS account root user.
    Access keys consist of two parts: an access key ID (for example, AKIAIOSFODNN7EXAMPLE) and a secret access
    key (for example, wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY). You must use both the access key ID and
    secret access key together to authenticate your requests.
    """

    access_key_id: str = pydantic.Field(alias=str("accessKeyId"))  # type: ignore[literal-required]
    secret_access_key: EncryptedProperty = pydantic.Field(alias=str("secretAccessKey"))  # type: ignore[literal-required]
    type: typing.Literal["awsAccessKey"] = "awsAccessKey"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.EncryptedProperty](EncryptedProperty.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AwsAccessKey.md)
