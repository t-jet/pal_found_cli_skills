# foundry_sdk.v2.ontologies.models.ApplyScenarioLogicRule


An Action rule that merges the edits accumulated on a referenced Scenario into the ontology data context
where the Action is applied. If the Action is applied against another Scenario, the edits are merged into
that target Scenario.

The scenario is supplied through the parameter identified by `scenarioParameter`, whose value type is
`scenarioReference`. The affected object types and link types are explicitly enumerated in the scope.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| scenario_parameter | scenarioParameter | ParameterId | required; no default | No additional field description in SDK source. |
| object_type_api_names | objectTypeApiNames | typing.List[ObjectTypeApiName] | required; no default | No additional field description in SDK source. |
| link_types | linkTypes | typing.List[ObjectTypeLinkTypeApiNameMapping] | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['applyScenario'] | 'applyScenario' | No additional field description in SDK source. |

```python
class ApplyScenarioLogicRule(core.ModelBase):
    """
    An Action rule that merges the edits accumulated on a referenced Scenario into the ontology data context
    where the Action is applied. If the Action is applied against another Scenario, the edits are merged into
    that target Scenario.

    The scenario is supplied through the parameter identified by `scenarioParameter`, whose value type is
    `scenarioReference`. The affected object types and link types are explicitly enumerated in the scope.
    """

    scenario_parameter: ParameterId = pydantic.Field(alias=str("scenarioParameter"))  # type: ignore[literal-required]
    object_type_api_names: typing.List[ObjectTypeApiName] = pydantic.Field(alias=str("objectTypeApiNames"))  # type: ignore[literal-required]
    link_types: typing.List[ObjectTypeLinkTypeApiNameMapping] = pydantic.Field(alias=str("linkTypes"))  # type: ignore[literal-required]
    type: typing.Literal["applyScenario"] = "applyScenario"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeLinkTypeApiNameMapping](ObjectTypeLinkTypeApiNameMapping.md)
- [foundry_sdk.v2.ontologies.models.ParameterId](ParameterId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ApplyScenarioLogicRule.md)
