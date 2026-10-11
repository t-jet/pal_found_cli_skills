# foundry_sdk.v2.connectivity.models.RestConnectionOAuth2


This authorization variant uses the Connection's `oauth2_client_rid`. An organization administrator must first configure the outbound application and its external OAuth 2.0 authorization-code client; selecting this variant does not provision that application.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| type | type | typing.Literal['oauth2'] | 'oauth2' | No additional field description in SDK source. |

```python
class RestConnectionOAuth2(core.ModelBase):
    """
    In order to use OAuth2 you must have an Outbound application configured in the [Foundry Control Panel Organization settings](https://palantir.com/docs/foundry/administration/configure-outbound-applications#create-an-outbound-application).
    The RID of the Outbound application must be configured in the RestConnectionConfiguration in the `oauth2ClientRid` field.
    """

    type: typing.Literal["oauth2"] = "oauth2"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](RestConnectionOAuth2.md)
