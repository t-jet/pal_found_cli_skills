# foundry_sdk.v2.models.models.CreateConfigValidationFailureReason


A specific reason why configuration validation failed.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
CreateConfigValidationFailureReason: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "JsonSchemaValidationError",
        "OutputResourceInDifferentProjectError",
        "OtherValidationError",
        "MissingWorkerConfigOutputError",
        "MissingRequiredDatasetColumnError",
        "MultiplePropertiesNotAllowedForTrainerError",
        "FieldValidationError",
        "ChangelogTooLongError",
        "UnknownColumnSpecIdInConfigColumnMappingError",
        "MultipleColumnsNotAllowedForTrainerError",
        "MissingWorkerConfigInputDatasetColumnMappingError",
        "DatasetSchemaNotFoundError",
        "MissingWorkerConfigInputError",
        "MissingWorkerConfigInputObjectSetPropertyMappingError",
        "OutputResourceNotFoundError",
        "InvalidResourceConfigurationError",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.models.models.ChangelogTooLongError](ChangelogTooLongError.md)
- [foundry_sdk.v2.models.models.DatasetSchemaNotFoundError](DatasetSchemaNotFoundError.md)
- [foundry_sdk.v2.models.models.FieldValidationError](FieldValidationError.md)
- [foundry_sdk.v2.models.models.InvalidResourceConfigurationError](InvalidResourceConfigurationError.md)
- [foundry_sdk.v2.models.models.JsonSchemaValidationError](JsonSchemaValidationError.md)
- [foundry_sdk.v2.models.models.MissingRequiredDatasetColumnError](MissingRequiredDatasetColumnError.md)
- [foundry_sdk.v2.models.models.MissingWorkerConfigInputDatasetColumnMappingError](MissingWorkerConfigInputDatasetColumnMappingError.md)
- [foundry_sdk.v2.models.models.MissingWorkerConfigInputError](MissingWorkerConfigInputError.md)
- [foundry_sdk.v2.models.models.MissingWorkerConfigInputObjectSetPropertyMappingError](MissingWorkerConfigInputObjectSetPropertyMappingError.md)
- [foundry_sdk.v2.models.models.MissingWorkerConfigOutputError](MissingWorkerConfigOutputError.md)
- [foundry_sdk.v2.models.models.MultipleColumnsNotAllowedForTrainerError](MultipleColumnsNotAllowedForTrainerError.md)
- [foundry_sdk.v2.models.models.MultiplePropertiesNotAllowedForTrainerError](MultiplePropertiesNotAllowedForTrainerError.md)
- [foundry_sdk.v2.models.models.OtherValidationError](OtherValidationError.md)
- [foundry_sdk.v2.models.models.OutputResourceInDifferentProjectError](OutputResourceInDifferentProjectError.md)
- [foundry_sdk.v2.models.models.OutputResourceNotFoundError](OutputResourceNotFoundError.md)
- [foundry_sdk.v2.models.models.UnknownColumnSpecIdInConfigColumnMappingError](UnknownColumnSpecIdInConfigColumnMappingError.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateConfigValidationFailureReason.md)
