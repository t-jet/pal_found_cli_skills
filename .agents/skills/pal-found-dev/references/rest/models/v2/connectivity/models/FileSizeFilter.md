# foundry_sdk.v2.connectivity.models.FileSizeFilter


Only import files whose size is between the specified minimum and maximum values.
At least one of `gt` or `lt` should be present.
If both are present, the value specified for `gt` must be strictly less than `lt - 1`.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| gt | gt | typing.Optional[core_models.SizeBytes] | None | File size must be greater than this number for it to be imported.<br>    The value specified cannot be a negative number. |
| lt | lt | typing.Optional[core_models.SizeBytes] | None | File size must be less than this number for it to be imported.<br>    The value specified must be at least 1 byte. |
| type | type | typing.Literal['fileSizeFilter'] | 'fileSizeFilter' | No additional field description in SDK source. |

```python
class FileSizeFilter(core.ModelBase):
    """
    Only import files whose size is between the specified minimum and maximum values.
    At least one of `gt` or `lt` should be present.
    If both are present, the value specified for `gt` must be strictly less than `lt - 1`.
    """

    gt: typing.Optional[core_models.SizeBytes] = None
    """
    File size must be greater than this number for it to be imported.
    The value specified cannot be a negative number.
    """

    lt: typing.Optional[core_models.SizeBytes] = None
    """
    File size must be less than this number for it to be imported.
    The value specified must be at least 1 byte.
    """

    type: typing.Literal["fileSizeFilter"] = "fileSizeFilter"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.SizeBytes](../../core/models/SizeBytes.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FileSizeFilter.md)
