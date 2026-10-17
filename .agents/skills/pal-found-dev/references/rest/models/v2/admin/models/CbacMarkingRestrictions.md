# foundry_sdk.v2.admin.models.CbacMarkingRestrictions


CbacMarkingRestrictions

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| disallowed_markings | disallowedMarkings | typing.List[core_models.MarkingId] | required; no default | Markings that cannot appear in conjunction with the provided markings. This includes all such markings, not just those present in the provided set. |
| implied_markings | impliedMarkings | typing.List[core_models.MarkingId] | required; no default | Markings that are automatically granted when a user has membership in any of the provided markings. |
| required_markings | requiredMarkings | typing.List[typing.List[core_models.MarkingId]] | required; no default | Markings that must appear in conjunction with the provided markings. Each list contains the requirements for one of the provided markings, and at least one marking from each must be included in the provided markingIds to constitute a valid classification. |
| user_satisfies_markings | userSatisfiesMarkings | CbacMarkingRestrictionsUserSatisfiesMarkings | required; no default | True if the current user satisfies the provided markings. The user must be a member of all conjunctive markings. The provided disjunctive markings are grouped by category, and the user must be a member of at least one marking in each group. |
| is_valid | isValid | CbacMarkingRestrictionsIsValid | required; no default | True if the provided markings constitute a valid classification, containing no disallowed markings and satisfying all required marking constraints. |

```python
class CbacMarkingRestrictions(core.ModelBase):
    """CbacMarkingRestrictions"""

    disallowed_markings: typing.List[core_models.MarkingId] = pydantic.Field(alias=str("disallowedMarkings"))  # type: ignore[literal-required]
    """Markings that cannot appear in conjunction with the provided markings. This includes all such markings, not just those present in the provided set."""

    implied_markings: typing.List[core_models.MarkingId] = pydantic.Field(alias=str("impliedMarkings"))  # type: ignore[literal-required]
    """Markings that are automatically granted when a user has membership in any of the provided markings."""

    required_markings: typing.List[typing.List[core_models.MarkingId]] = pydantic.Field(alias=str("requiredMarkings"))  # type: ignore[literal-required]
    """Markings that must appear in conjunction with the provided markings. Each list contains the requirements for one of the provided markings, and at least one marking from each must be included in the provided markingIds to constitute a valid classification."""

    user_satisfies_markings: CbacMarkingRestrictionsUserSatisfiesMarkings = pydantic.Field(alias=str("userSatisfiesMarkings"))  # type: ignore[literal-required]
    """True if the current user satisfies the provided markings. The user must be a member of all conjunctive markings. The provided disjunctive markings are grouped by category, and the user must be a member of at least one marking in each group."""

    is_valid: CbacMarkingRestrictionsIsValid = pydantic.Field(alias=str("isValid"))  # type: ignore[literal-required]
    """True if the provided markings constitute a valid classification, containing no disallowed markings and satisfying all required marking constraints."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.admin.models.CbacMarkingRestrictionsIsValid](CbacMarkingRestrictionsIsValid.md)
- [foundry_sdk.v2.admin.models.CbacMarkingRestrictionsUserSatisfiesMarkings](CbacMarkingRestrictionsUserSatisfiesMarkings.md)
- [foundry_sdk.v2.core.models.MarkingId](../../core/models/MarkingId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CbacMarkingRestrictions.md)
