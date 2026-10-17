# foundry_sdk.v2.media_sets.models.SlicePdfRangeOperation


Slices a PDF to a specified page range.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| start_page_inclusive | startPageInclusive | int | required; no default | The zero-indexed start page (inclusive). |
| end_page_exclusive | endPageExclusive | int | required; no default | The zero-indexed end page (exclusive). |
| strictly_enforce_end_page | strictlyEnforceEndPage | typing.Optional[bool] | default None | If true (default), the operation fails if endPage exceeds the document's page count.<br>    If false, ends at min(endPage, lastPage). |
| type | type | typing.Literal['slicePdfRange'] | 'slicePdfRange' | No additional field description in SDK source. |

```python
class SlicePdfRangeOperation(core.ModelBase):
    """Slices a PDF to a specified page range."""

    start_page_inclusive: int = pydantic.Field(alias=str("startPageInclusive"))  # type: ignore[literal-required]
    """The zero-indexed start page (inclusive)."""

    end_page_exclusive: int = pydantic.Field(alias=str("endPageExclusive"))  # type: ignore[literal-required]
    """The zero-indexed end page (exclusive)."""

    strictly_enforce_end_page: typing.Optional[bool] = pydantic.Field(alias=str("strictlyEnforceEndPage"), default=None)  # type: ignore[literal-required]
    """
    If true (default), the operation fails if endPage exceeds the document's page count.
    If false, ends at min(endPage, lastPage).
    """

    type: typing.Literal["slicePdfRange"] = "slicePdfRange"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SlicePdfRangeOperation.md)
