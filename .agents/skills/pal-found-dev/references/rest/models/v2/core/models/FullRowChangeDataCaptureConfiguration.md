# foundry_sdk.v2.core.models.FullRowChangeDataCaptureConfiguration


Configuration for change data capture which resolves the latest state of the dataset based on new full rows
being pushed to the stream. For example, if a value for a row is updated, it is only sufficient to publish
the entire new state of that row to the stream.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| deletion_field_name | deletionFieldName | FieldName | required; no default | The name of a boolean field in the schema that indicates whether or not a row has been deleted. |
| ordering_field_name | orderingFieldName | FieldName | required; no default | The name of an ordering field that determines the newest state for a row in the dataset. <br><br>    The ordering field can only be of the following types:<br>    - Byte<br>    - Date<br>    - Decimal<br>    - Integer<br>    - Long<br>    - Short<br>    - String<br>    - Timestamp |
| type | type | typing.Literal['fullRow'] | 'fullRow' | No additional field description in SDK source. |

```python
class FullRowChangeDataCaptureConfiguration(core.ModelBase):
    """
    Configuration for change data capture which resolves the latest state of the dataset based on new full rows
    being pushed to the stream. For example, if a value for a row is updated, it is only sufficient to publish
    the entire new state of that row to the stream.
    """

    deletion_field_name: FieldName = pydantic.Field(alias=str("deletionFieldName"))  # type: ignore[literal-required]
    """The name of a boolean field in the schema that indicates whether or not a row has been deleted."""

    ordering_field_name: FieldName = pydantic.Field(alias=str("orderingFieldName"))  # type: ignore[literal-required]
    """
    The name of an ordering field that determines the newest state for a row in the dataset. 

    The ordering field can only be of the following types:
    - Byte
    - Date
    - Decimal
    - Integer
    - Long
    - Short
    - String
    - Timestamp
    """

    type: typing.Literal["fullRow"] = "fullRow"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.FieldName](FieldName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FullRowChangeDataCaptureConfiguration.md)
