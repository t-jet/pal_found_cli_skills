# foundry_sdk.v2.filesystem.models.Marking


[Markings](https://palantir.com/docs/foundry/security/markings/) provide an additional level of access control for files,
folders, and Projects within Foundry. Markings define eligibility criteria that restrict visibility
and actions to users who meet those criteria. To access a resource, a user must be a member of all
Markings applied to a resource to access it.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| marking_id | markingId | core_models.MarkingId | required; no default | No additional field description in SDK source. |
| is_directly_applied | isDirectlyApplied | IsDirectlyApplied | required; no default | No additional field description in SDK source. |

```python
class Marking(core.ModelBase):
    """
    [Markings](https://palantir.com/docs/foundry/security/markings/) provide an additional level of access control for files,
    folders, and Projects within Foundry. Markings define eligibility criteria that restrict visibility
    and actions to users who meet those criteria. To access a resource, a user must be a member of all
    Markings applied to a resource to access it.
    """

    marking_id: core_models.MarkingId = pydantic.Field(alias=str("markingId"))  # type: ignore[literal-required]
    is_directly_applied: IsDirectlyApplied = pydantic.Field(alias=str("isDirectlyApplied"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.MarkingId](../../core/models/MarkingId.md)
- [foundry_sdk.v2.filesystem.models.IsDirectlyApplied](IsDirectlyApplied.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Marking.md)
