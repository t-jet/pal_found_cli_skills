# foundry_sdk.v2.checkpoints.models.Justification


Justification submitted by the user to pass a checkpoint.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
Justification: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "ResponseJustification",
        "DropdownJustification",
        "ReauthenticationJustification",
        "AcknowledgementJustification",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.checkpoints.models.AcknowledgementJustification](AcknowledgementJustification.md)
- [foundry_sdk.v2.checkpoints.models.DropdownJustification](DropdownJustification.md)
- [foundry_sdk.v2.checkpoints.models.ReauthenticationJustification](ReauthenticationJustification.md)
- [foundry_sdk.v2.checkpoints.models.ResponseJustification](ResponseJustification.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Justification.md)
