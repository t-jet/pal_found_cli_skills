# foundry_sdk.v2.models.models.ModelApiInput


ModelApiInput

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ModelApiInput: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[core_models.UnsupportedType, "ModelApiParameterType", "ModelApiTabularType"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.core.models.UnsupportedType](../../core/models/UnsupportedType.md)
- [foundry_sdk.v2.models.models.ModelApiParameterType](ModelApiParameterType.md)
- [foundry_sdk.v2.models.models.ModelApiTabularType](ModelApiTabularType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ModelApiInput.md)
