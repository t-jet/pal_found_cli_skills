# foundry_sdk.v2.third_party_applications.errors.DeployWebsitePermissionDeniedParameters


Could not deploy the Website.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| thirdPartyApplicationRid | thirdPartyApplicationRid | third_party_applications_models.ThirdPartyApplicationRid | TypedDict key required | An RID identifying a third-party application created in Developer Console. |

```python
class DeployWebsitePermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not deploy the Website."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    thirdPartyApplicationRid: third_party_applications_models.ThirdPartyApplicationRid
    """An RID identifying a third-party application created in Developer Console."""
```

## Referenced definitions

- [foundry_sdk.v2.third_party_applications.models.ThirdPartyApplicationRid](../models/ThirdPartyApplicationRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DeployWebsitePermissionDeniedParameters.md)
