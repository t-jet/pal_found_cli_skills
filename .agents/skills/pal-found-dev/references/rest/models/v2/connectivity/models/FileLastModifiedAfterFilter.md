# foundry_sdk.v2.connectivity.models.FileLastModifiedAfterFilter


Only import files that have been modified after a specified timestamp

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| after_timestamp | afterTimestamp | typing.Optional[core.AwareDatetime] | default None | Timestamp threshold, specified in ISO-8601 format.<br>    If not specified, defaults to the timestamp the filter is added to the file import. |
| type | type | typing.Literal['lastModifiedAfterFilter'] | 'lastModifiedAfterFilter' | No additional field description in SDK source. |

```python
class FileLastModifiedAfterFilter(core.ModelBase):
    """Only import files that have been modified after a specified timestamp"""

    after_timestamp: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("afterTimestamp"), default=None)  # type: ignore[literal-required]
    """
    Timestamp threshold, specified in ISO-8601 format.
    If not specified, defaults to the timestamp the filter is added to the file import.
    """

    type: typing.Literal["lastModifiedAfterFilter"] = "lastModifiedAfterFilter"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../_core/AwareDatetime.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FileLastModifiedAfterFilter.md)
