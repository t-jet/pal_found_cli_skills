# foundry_sdk.v2.ontologies.models.LogicRule


LogicRule

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
LogicRule: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "DeleteInterfaceObjectRule",
        "ModifyInterfaceObjectRule",
        "ModifyObjectRule",
        "DeleteObjectRule",
        "CreateInterfaceObjectRule",
        "DeleteLinkRule",
        "CreateObjectRule",
        "CreateLinkRule",
        "ApplyScenarioRule",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.ApplyScenarioRule](ApplyScenarioRule.md)
- [foundry_sdk.v2.ontologies.models.CreateInterfaceObjectRule](CreateInterfaceObjectRule.md)
- [foundry_sdk.v2.ontologies.models.CreateLinkRule](CreateLinkRule.md)
- [foundry_sdk.v2.ontologies.models.CreateObjectRule](CreateObjectRule.md)
- [foundry_sdk.v2.ontologies.models.DeleteInterfaceObjectRule](DeleteInterfaceObjectRule.md)
- [foundry_sdk.v2.ontologies.models.DeleteLinkRule](DeleteLinkRule.md)
- [foundry_sdk.v2.ontologies.models.DeleteObjectRule](DeleteObjectRule.md)
- [foundry_sdk.v2.ontologies.models.ModifyInterfaceObjectRule](ModifyInterfaceObjectRule.md)
- [foundry_sdk.v2.ontologies.models.ModifyObjectRule](ModifyObjectRule.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LogicRule.md)
