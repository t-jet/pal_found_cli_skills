# foundry_sdk.v2.data_health.models.SchemaComparisonType



The type of schema comparison to perform:
- EXACT_MATCH_ORDERED_COLUMNS: Schemas must have identical columns in the same order.
- EXACT_MATCH_UNORDERED_COLUMNS: Schemas must have identical columns but order doesn't matter.
- COLUMN_ADDITIONS_ALLOWED: Expected schema columns must be present, additional columns are allowed and 
  missing column types are ignored.
- COLUMN_ADDITIONS_ALLOWED_STRICT: Expected schema columns must be present, additional columns are allowed. 
  Both expected and actual columns must specify types and they must match exactly.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
SchemaComparisonType: typing_extensions.TypeAlias = typing.Literal[
    "EXACT_MATCH_ORDERED_COLUMNS",
    "EXACT_MATCH_UNORDERED_COLUMNS",
    "COLUMN_ADDITIONS_ALLOWED",
    "COLUMN_ADDITIONS_ALLOWED_STRICT",
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SchemaComparisonType.md)
