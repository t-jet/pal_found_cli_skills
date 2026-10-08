# foundry_sdk.v2.models.errors.ParquetExperimentSeriesPermissionDeniedParameters


Could not parquet the ExperimentSeries.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| experimentSeriesName | experimentSeriesName | models_models.SeriesName | TypedDict key required | No additional field description in SDK source. |
| experimentRid | experimentRid | models_models.ExperimentRid | TypedDict key required | No additional field description in SDK source. |
| modelRid | modelRid | models_models.ModelRid | TypedDict key required | No additional field description in SDK source. |

```python
class ParquetExperimentSeriesPermissionDeniedParameters(typing_extensions.TypedDict):
    """Could not parquet the ExperimentSeries."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    experimentSeriesName: models_models.SeriesName
    experimentRid: models_models.ExperimentRid
    modelRid: models_models.ModelRid
```

## Referenced definitions

- [foundry_sdk.v2.models.models.ExperimentRid](../models/ExperimentRid.md)
- [foundry_sdk.v2.models.models.ModelRid](../models/ModelRid.md)
- [foundry_sdk.v2.models.models.SeriesName](../models/SeriesName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ParquetExperimentSeriesPermissionDeniedParameters.md)
