# foundry_sdk.v2.core.models.StreamSchema


The schema for a Foundry stream. Records pushed to this stream must match this schema.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| fields | fields | typing.List[Field] | required; no default | No additional field description in SDK source. |
| key_field_names | keyFieldNames | typing.Optional[typing.List[FieldName]] | default None | The names of the fields to be used as keys for partitioning records. These key fields are used to group<br>    all records with the same key into the same partition, to guarantee processing order of grouped records. These<br>    keys are not meant to uniquely identify records, and do not by themselves deduplicate records. To deduplicate<br>    records, provide a change data capture configuration for the schema.<br><br>    Key fields can only be of the following types:<br>    - Boolean<br>    - Byte<br>    - Date<br>    - Decimal<br>    - Integer<br>    - Long<br>    - Short<br>    - String<br>    - Timestamp<br><br>    For additional information on keys for Foundry streams, see the<br>    [streaming keys](https://palantir.com/docs/foundry/building-pipelines/streaming-keys/) user documentation. |
| change_data_capture | changeDataCapture | typing.Optional[ChangeDataCaptureConfiguration] | default None | No additional field description in SDK source. |

```python
class StreamSchema(core.ModelBase):
    """The schema for a Foundry stream. Records pushed to this stream must match this schema."""

    fields: typing.List[Field]
    key_field_names: typing.Optional[typing.List[FieldName]] = pydantic.Field(alias=str("keyFieldNames"), default=None)  # type: ignore[literal-required]
    """
    The names of the fields to be used as keys for partitioning records. These key fields are used to group
    all records with the same key into the same partition, to guarantee processing order of grouped records. These
    keys are not meant to uniquely identify records, and do not by themselves deduplicate records. To deduplicate
    records, provide a change data capture configuration for the schema.

    Key fields can only be of the following types:
    - Boolean
    - Byte
    - Date
    - Decimal
    - Integer
    - Long
    - Short
    - String
    - Timestamp

    For additional information on keys for Foundry streams, see the
    [streaming keys](https://palantir.com/docs/foundry/building-pipelines/streaming-keys/) user documentation.
    """

    change_data_capture: typing.Optional[ChangeDataCaptureConfiguration] = pydantic.Field(alias=str("changeDataCapture"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.ChangeDataCaptureConfiguration](ChangeDataCaptureConfiguration.md)
- [foundry_sdk.v2.core.models.Field](Field.md)
- [foundry_sdk.v2.core.models.FieldName](FieldName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](StreamSchema.md)
