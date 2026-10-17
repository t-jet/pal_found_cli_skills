# foundry_sdk.v2.ontologies.models.AggregationAccuracyRequest



Specifies the accuracy requirement for aggregation results.

- `REQUIRE_ACCURATE`: Only return results if they are guaranteed to be accurate. If accuracy cannot be
  guaranteed (e.g., due to a low `maxGroupCount` relative to distinct values), the request will fail
  with an `AggregationAccuracyNotSupported` error.
- `ALLOW_APPROXIMATE`: Allow approximate results when exact computation is not feasible. This is the
  default behavior if not specified.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
AggregationAccuracyRequest: typing_extensions.TypeAlias = typing.Literal[
    "REQUIRE_ACCURATE", "ALLOW_APPROXIMATE"
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AggregationAccuracyRequest.md)
