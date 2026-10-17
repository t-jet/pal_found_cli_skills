# foundry_sdk.v2.media_sets.models.PageRange


Page range for document extraction.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| start_page_inclusive | startPageInclusive | typing.Optional[int] | default None | Start page index (0-based, inclusive). If not provided, defaults to start of document. |
| end_page_exclusive | endPageExclusive | typing.Optional[int] | default None | End page index (0-based, exclusive). If not provided, defaults to end of document. |

```python
class PageRange(core.ModelBase):
    """Page range for document extraction."""

    start_page_inclusive: typing.Optional[int] = pydantic.Field(alias=str("startPageInclusive"), default=None)  # type: ignore[literal-required]
    """Start page index (0-based, inclusive). If not provided, defaults to start of document."""

    end_page_exclusive: typing.Optional[int] = pydantic.Field(alias=str("endPageExclusive"), default=None)  # type: ignore[literal-required]
    """End page index (0-based, exclusive). If not provided, defaults to end of document."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PageRange.md)
