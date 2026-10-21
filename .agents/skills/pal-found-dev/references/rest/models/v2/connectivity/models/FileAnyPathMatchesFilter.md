# foundry_sdk.v2.connectivity.models.FileAnyPathMatchesFilter


If any file has a relative path matching the regular expression, sync all files in the subfolder that are not otherwise filtered.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| regex | regex | str | required; no default | The regular expression for the relative path to match against. |
| type | type | typing.Literal['anyPathMatchesFilter'] | 'anyPathMatchesFilter' | No additional field description in SDK source. |

```python
class FileAnyPathMatchesFilter(core.ModelBase):
    """If any file has a relative path matching the regular expression, sync all files in the subfolder that are not otherwise filtered."""

    regex: str
    """The regular expression for the relative path to match against."""

    type: typing.Literal["anyPathMatchesFilter"] = "anyPathMatchesFilter"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FileAnyPathMatchesFilter.md)
