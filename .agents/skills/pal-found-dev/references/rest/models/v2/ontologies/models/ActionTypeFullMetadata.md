# foundry_sdk.v2.ontologies.models.ActionTypeFullMetadata


Returns the full metadata for an Action type in the Ontology.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| action_type | actionType | ActionTypeV2 | required; no default | No additional field description in SDK source. |
| full_logic_rules | fullLogicRules | typing.List[ActionLogicRule] | required; no default | No additional field description in SDK source. |

```python
class ActionTypeFullMetadata(core.ModelBase):
    """Returns the full metadata for an Action type in the Ontology."""

    action_type: ActionTypeV2 = pydantic.Field(alias=str("actionType"))  # type: ignore[literal-required]
    full_logic_rules: typing.List[ActionLogicRule] = pydantic.Field(alias=str("fullLogicRules"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.ActionLogicRule](ActionLogicRule.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeV2](ActionTypeV2.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ActionTypeFullMetadata.md)
