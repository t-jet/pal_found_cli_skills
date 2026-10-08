# foundry_sdk.v2.ontologies.models.LogicRuleArgument


Represents an argument for a logic rule operation. An argument can be passed in via the action parameters, as a static value, or as some other value.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
LogicRuleArgument: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "CurrentTimeArgument",
        "StaticArgument",
        "CurrentUserArgument",
        "ParameterIdArgument",
        "InterfaceParameterPropertyArgument",
        "SynchronousWebhookOutputArgument",
        "ObjectParameterPropertyArgument",
        "UniqueIdentifierArgument",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.CurrentTimeArgument](CurrentTimeArgument.md)
- [foundry_sdk.v2.ontologies.models.CurrentUserArgument](CurrentUserArgument.md)
- [foundry_sdk.v2.ontologies.models.InterfaceParameterPropertyArgument](InterfaceParameterPropertyArgument.md)
- [foundry_sdk.v2.ontologies.models.ObjectParameterPropertyArgument](ObjectParameterPropertyArgument.md)
- [foundry_sdk.v2.ontologies.models.ParameterIdArgument](ParameterIdArgument.md)
- [foundry_sdk.v2.ontologies.models.StaticArgument](StaticArgument.md)
- [foundry_sdk.v2.ontologies.models.SynchronousWebhookOutputArgument](SynchronousWebhookOutputArgument.md)
- [foundry_sdk.v2.ontologies.models.UniqueIdentifierArgument](UniqueIdentifierArgument.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LogicRuleArgument.md)
