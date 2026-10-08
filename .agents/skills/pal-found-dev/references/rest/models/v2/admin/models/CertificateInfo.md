# foundry_sdk.v2.admin.models.CertificateInfo


CertificateInfo

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| pem_certificate | pemCertificate | str | required; no default | The certificate, in PEM format. |
| common_name | commonName | typing.Optional[str] | default None | No additional field description in SDK source. |
| expiry_date | expiryDate | core.AwareDatetime | required; no default | No additional field description in SDK source. |
| usage_type | usageType | CertificateUsageType | required; no default | No additional field description in SDK source. |

```python
class CertificateInfo(core.ModelBase):
    """CertificateInfo"""

    pem_certificate: str = pydantic.Field(alias=str("pemCertificate"))  # type: ignore[literal-required]
    """The certificate, in PEM format."""

    common_name: typing.Optional[str] = pydantic.Field(alias=str("commonName"), default=None)  # type: ignore[literal-required]
    expiry_date: core.AwareDatetime = pydantic.Field(alias=str("expiryDate"))  # type: ignore[literal-required]
    usage_type: CertificateUsageType = pydantic.Field(alias=str("usageType"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../_core/AwareDatetime.md)
- [foundry_sdk.v2.admin.models.CertificateUsageType](CertificateUsageType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CertificateInfo.md)
