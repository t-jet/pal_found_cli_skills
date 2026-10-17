# foundry_sdk.v2.ontologies.models.ActionTypeSearchJsonQueryV2


Represents the search query for an action type search. Supports filters for various action type features.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ActionTypeSearchJsonQueryV2: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "WebhookRidActionTypesQueryV2",
        "HasActionLogActionTypesQueryV2",
        "ActionTypeApiNameActionTypesQueryV2",
        "OrActionTypesQueryV2",
        "PermissionModelActionTypesQueryV2",
        "HasWebhookActionTypesQueryV2",
        "ActionTypeDisplayNameActionTypesQueryV2",
        "AffectedLinkTypeRidActionTypesQueryV2",
        "ActionTypeDescriptionActionTypesQueryV2",
        "SectionRidActionTypesQueryV2",
        "ParameterRidActionTypesQueryV2",
        "ParameterNameActionTypesQueryV2",
        "HasNotificationActionTypesQueryV2",
        "FunctionRidActionTypesQueryV2",
        "InputObjectTypeRidActionTypesQueryV2",
        "RevertActionEnabledActionTypesQueryV2",
        "LogicRuleActionTypesQueryV2",
        "TypeClassesActionTypesQueryV2",
        "AffectedInterfaceTypeRidActionTypesQueryV2",
        "AndActionTypesQueryV2",
        "ActionTypeRidActionTypesQueryV2",
        "AffectedObjectTypeRidActionTypesQueryV2",
        "StatusActionTypesQueryV2",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.ActionTypeApiNameActionTypesQueryV2](ActionTypeApiNameActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeDescriptionActionTypesQueryV2](ActionTypeDescriptionActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeDisplayNameActionTypesQueryV2](ActionTypeDisplayNameActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeRidActionTypesQueryV2](ActionTypeRidActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.AffectedInterfaceTypeRidActionTypesQueryV2](AffectedInterfaceTypeRidActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.AffectedLinkTypeRidActionTypesQueryV2](AffectedLinkTypeRidActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.AffectedObjectTypeRidActionTypesQueryV2](AffectedObjectTypeRidActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.AndActionTypesQueryV2](AndActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.FunctionRidActionTypesQueryV2](FunctionRidActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.HasActionLogActionTypesQueryV2](HasActionLogActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.HasNotificationActionTypesQueryV2](HasNotificationActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.HasWebhookActionTypesQueryV2](HasWebhookActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.InputObjectTypeRidActionTypesQueryV2](InputObjectTypeRidActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.LogicRuleActionTypesQueryV2](LogicRuleActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.OrActionTypesQueryV2](OrActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.ParameterNameActionTypesQueryV2](ParameterNameActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.ParameterRidActionTypesQueryV2](ParameterRidActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.PermissionModelActionTypesQueryV2](PermissionModelActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.RevertActionEnabledActionTypesQueryV2](RevertActionEnabledActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.SectionRidActionTypesQueryV2](SectionRidActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.StatusActionTypesQueryV2](StatusActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.TypeClassesActionTypesQueryV2](TypeClassesActionTypesQueryV2.md)
- [foundry_sdk.v2.ontologies.models.WebhookRidActionTypesQueryV2](WebhookRidActionTypesQueryV2.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ActionTypeSearchJsonQueryV2.md)
