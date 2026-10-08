# foundry_sdk.v2.connectivity.models.FilePathMatchesFilter


Only import files whose path (relative to the root of the source) matches the regular expression.

**Example**
Suppose we are importing files from `relative/subfolder`.
`relative/subfolder` contains:
- `relative/subfolder/include-file.txt`
- `relative/subfolder/exclude-file.txt`
- `relative/subfolder/other-file.txt`

With the `relative/subfolder/include-.*.txt` regex, only `relative/subfolder/include-file.txt` will be imported.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| regex | regex | str | required; no default | Must be written to match the paths relative to the root of the source, even if a subfolder is specified. |
| type | type | typing.Literal['pathMatchesFilter'] | 'pathMatchesFilter' | No additional field description in SDK source. |

```python
class FilePathMatchesFilter(core.ModelBase):
    """
    Only import files whose path (relative to the root of the source) matches the regular expression.

    **Example**
    Suppose we are importing files from `relative/subfolder`.
    `relative/subfolder` contains:
    - `relative/subfolder/include-file.txt`
    - `relative/subfolder/exclude-file.txt`
    - `relative/subfolder/other-file.txt`

    With the `relative/subfolder/include-.*.txt` regex, only `relative/subfolder/include-file.txt` will be imported.
    """

    regex: str
    """Must be written to match the paths relative to the root of the source, even if a subfolder is specified."""

    type: typing.Literal["pathMatchesFilter"] = "pathMatchesFilter"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FilePathMatchesFilter.md)
