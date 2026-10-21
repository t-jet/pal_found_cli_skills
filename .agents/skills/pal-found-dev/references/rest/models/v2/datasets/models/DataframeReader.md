# foundry_sdk.v2.datasets.models.DataframeReader


The dataframe reader used for reading the dataset schema.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
DataframeReader: typing_extensions.TypeAlias = typing.Literal[
    "AVRO", "CSV", "PARQUET", "DATASOURCE"
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DataframeReader.md)
