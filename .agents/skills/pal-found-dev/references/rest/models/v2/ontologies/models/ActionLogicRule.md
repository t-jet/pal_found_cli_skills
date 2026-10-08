# foundry_sdk.v2.ontologies.models.ActionLogicRule


A detailed operation for an Action

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ActionLogicRule: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "ModifyInterfaceLogicRule",
        "CreateOrModifyObjectLogicRule",
        "ModifyObjectLogicRule",
        "DeleteLinkLogicRule",
        "CreateObjectLogicRule",
        "CreateLinkLogicRule",
        "BatchedFunctionLogicRule",
        "CreateOrModifyObjectLogicRuleV2",
        "DeleteInterfaceLinkLogicRule",
        "DeleteObjectLogicRule",
        "FunctionLogicRule",
        "CreateInterfaceLinkLogicRule",
        "CreateInterfaceLogicRule",
        "ApplyScenarioLogicRule",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.ApplyScenarioLogicRule](ApplyScenarioLogicRule.md)
- [foundry_sdk.v2.ontologies.models.BatchedFunctionLogicRule](BatchedFunctionLogicRule.md)
- [foundry_sdk.v2.ontologies.models.CreateInterfaceLinkLogicRule](CreateInterfaceLinkLogicRule.md)
- [foundry_sdk.v2.ontologies.models.CreateInterfaceLogicRule](CreateInterfaceLogicRule.md)
- [foundry_sdk.v2.ontologies.models.CreateLinkLogicRule](CreateLinkLogicRule.md)
- [foundry_sdk.v2.ontologies.models.CreateObjectLogicRule](CreateObjectLogicRule.md)
- [foundry_sdk.v2.ontologies.models.CreateOrModifyObjectLogicRule](CreateOrModifyObjectLogicRule.md)
- [foundry_sdk.v2.ontologies.models.CreateOrModifyObjectLogicRuleV2](CreateOrModifyObjectLogicRuleV2.md)
- [foundry_sdk.v2.ontologies.models.DeleteInterfaceLinkLogicRule](DeleteInterfaceLinkLogicRule.md)
- [foundry_sdk.v2.ontologies.models.DeleteLinkLogicRule](DeleteLinkLogicRule.md)
- [foundry_sdk.v2.ontologies.models.DeleteObjectLogicRule](DeleteObjectLogicRule.md)
- [foundry_sdk.v2.ontologies.models.FunctionLogicRule](FunctionLogicRule.md)
- [foundry_sdk.v2.ontologies.models.ModifyInterfaceLogicRule](ModifyInterfaceLogicRule.md)
- [foundry_sdk.v2.ontologies.models.ModifyObjectLogicRule](ModifyObjectLogicRule.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ActionLogicRule.md)
