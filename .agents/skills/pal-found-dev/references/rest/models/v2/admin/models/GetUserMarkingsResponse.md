# foundry_sdk.v2.admin.models.GetUserMarkingsResponse


GetUserMarkingsResponse

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| view | view | typing.List[core_models.MarkingId] | required; no default | The markings that the user has access to. The user will be able to access resources protected with these<br>    markings. This includes organization markings for organizations in which the user is a guest member. |

```python
class GetUserMarkingsResponse(core.ModelBase):
    """GetUserMarkingsResponse"""

    view: typing.List[core_models.MarkingId]
    """
    The markings that the user has access to. The user will be able to access resources protected with these
    markings. This includes organization markings for organizations in which the user is a guest member.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.MarkingId](../../core/models/MarkingId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetUserMarkingsResponse.md)
