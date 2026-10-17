# foundry_sdk.v1.datasets.models.ListFilesResponse


A page of Files and an optional page token that can be used to retrieve the next page.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| next_page_token | nextPageToken | typing.Optional[core_models.PageToken] | default None | No additional field description in SDK source. |
| data | data | typing.List[File] | required; no default | No additional field description in SDK source. |

```python
class ListFilesResponse(core.ModelBase):
    """A page of Files and an optional page token that can be used to retrieve the next page."""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    data: typing.List[File]
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.core.models.PageToken](../../core/models/PageToken.md)
- [foundry_sdk.v1.datasets.models.File](File.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ListFilesResponse.md)
