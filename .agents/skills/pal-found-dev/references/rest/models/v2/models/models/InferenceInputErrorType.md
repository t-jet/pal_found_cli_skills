# foundry_sdk.v2.models.models.InferenceInputErrorType



The specific type and details of an input validation error for inference requests.
Each variant carries parameters relevant to that specific error category.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
InferenceInputErrorType: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "InvalidArrayShapeError",
        "TypeMismatchError",
        "UnsupportedTypeError",
        "UnknownInputNameError",
        "InvalidTabularFormatError",
        "InconsistentArrayDimensionsError",
        "RequiredValueMissingError",
        "InvalidMapFormatError",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.models.models.InconsistentArrayDimensionsError](InconsistentArrayDimensionsError.md)
- [foundry_sdk.v2.models.models.InvalidArrayShapeError](InvalidArrayShapeError.md)
- [foundry_sdk.v2.models.models.InvalidMapFormatError](InvalidMapFormatError.md)
- [foundry_sdk.v2.models.models.InvalidTabularFormatError](InvalidTabularFormatError.md)
- [foundry_sdk.v2.models.models.RequiredValueMissingError](RequiredValueMissingError.md)
- [foundry_sdk.v2.models.models.TypeMismatchError](TypeMismatchError.md)
- [foundry_sdk.v2.models.models.UnknownInputNameError](UnknownInputNameError.md)
- [foundry_sdk.v2.models.models.UnsupportedTypeError](UnsupportedTypeError.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InferenceInputErrorType.md)
