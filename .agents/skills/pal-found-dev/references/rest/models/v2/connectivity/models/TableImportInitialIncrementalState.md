# foundry_sdk.v2.connectivity.models.TableImportInitialIncrementalState



The incremental configuration for a table import enables append-style transactions from the same table without duplication of data.
You must provide a monotonically increasing column such as a timestamp or id and an initial value for this column. 
An incremental table import will import rows where the value is greater than the largest already imported.

You can use the '?' character to reference the incremental state value when constructing your query. 
Normally this would be used in a WHERE clause or similar filter applied in order to only sync data with an incremental column value 
larger than the previously observed maximum value stored in the incremental state.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
TableImportInitialIncrementalState: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "StringColumnInitialIncrementalState",
        "DateColumnInitialIncrementalState",
        "IntegerColumnInitialIncrementalState",
        "TimestampColumnInitialIncrementalState",
        "LongColumnInitialIncrementalState",
        "DecimalColumnInitialIncrementalState",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.connectivity.models.DateColumnInitialIncrementalState](DateColumnInitialIncrementalState.md)
- [foundry_sdk.v2.connectivity.models.DecimalColumnInitialIncrementalState](DecimalColumnInitialIncrementalState.md)
- [foundry_sdk.v2.connectivity.models.IntegerColumnInitialIncrementalState](IntegerColumnInitialIncrementalState.md)
- [foundry_sdk.v2.connectivity.models.LongColumnInitialIncrementalState](LongColumnInitialIncrementalState.md)
- [foundry_sdk.v2.connectivity.models.StringColumnInitialIncrementalState](StringColumnInitialIncrementalState.md)
- [foundry_sdk.v2.connectivity.models.TimestampColumnInitialIncrementalState](TimestampColumnInitialIncrementalState.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TableImportInitialIncrementalState.md)
