# foundry_sdk.v2.connectivity.models.S3KmsConfiguration


S3KmsConfiguration

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| kms_key | kmsKey | str | required; no default | The client-side KMS key to use for encryption and decryption of data in the S3 bucket.<br>    If not specified, the default KMS key for the bucket is used. |
| kms_region | kmsRegion | typing.Optional[Region] | default None | The region of the client-side KMS key to use for encryption and decryption of data in the S3 bucket.<br>    If not specified, the default KMS key region for the bucket is used. |

```python
class S3KmsConfiguration(core.ModelBase):
    """S3KmsConfiguration"""

    kms_key: str = pydantic.Field(alias=str("kmsKey"))  # type: ignore[literal-required]
    """
    The client-side KMS key to use for encryption and decryption of data in the S3 bucket.
    If not specified, the default KMS key for the bucket is used.
    """

    kms_region: typing.Optional[Region] = pydantic.Field(alias=str("kmsRegion"), default=None)  # type: ignore[literal-required]
    """
    The region of the client-side KMS key to use for encryption and decryption of data in the S3 bucket.
    If not specified, the default KMS key region for the bucket is used.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.Region](Region.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](S3KmsConfiguration.md)
