# foundry_sdk.v1.core.models.FilePath



The path to a File within Foundry. Paths are relative and must not start with a leading slash.
Examples: `my-file.txt`, `path/to/my-file.jpg`, `dataframe.snappy.parquet`.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
FilePath: typing_extensions.TypeAlias = str
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FilePath.md)
