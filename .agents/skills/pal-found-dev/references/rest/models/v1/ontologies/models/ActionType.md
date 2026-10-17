# foundry_sdk.v1.ontologies.models.ActionType


Represents an action type in the Ontology.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| api_name | apiName | ActionTypeApiName | required; no default | No additional field description in SDK source. |
| description | description | typing.Optional[str] | None | No additional field description in SDK source. |
| display_name | displayName | typing.Optional[core_models.DisplayName] | default None | No additional field description in SDK source. |
| status | status | core_models.ReleaseStatus | required; no default | No additional field description in SDK source. |
| parameters | parameters | typing.Dict[ParameterId, Parameter] | required; no default | No additional field description in SDK source. |
| rid | rid | ActionTypeRid | required; no default | No additional field description in SDK source. |
| operations | operations | typing.List[LogicRule] | required; no default | No additional field description in SDK source. |

```python
class ActionType(core.ModelBase):
    """Represents an action type in the Ontology."""

    api_name: ActionTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    status: core_models.ReleaseStatus
    parameters: typing.Dict[ParameterId, Parameter]
    rid: ActionTypeRid
    operations: typing.List[LogicRule]
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.core.models.DisplayName](../../core/models/DisplayName.md)
- [foundry_sdk.v1.core.models.ReleaseStatus](../../core/models/ReleaseStatus.md)
- [foundry_sdk.v1.ontologies.models.ActionTypeApiName](ActionTypeApiName.md)
- [foundry_sdk.v1.ontologies.models.ActionTypeRid](ActionTypeRid.md)
- [foundry_sdk.v1.ontologies.models.LogicRule](LogicRule.md)
- [foundry_sdk.v1.ontologies.models.Parameter](Parameter.md)
- [foundry_sdk.v1.ontologies.models.ParameterId](ParameterId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ActionType.md)
