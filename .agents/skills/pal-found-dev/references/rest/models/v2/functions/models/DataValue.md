# foundry_sdk.v2.functions.models.DataValue



Represents the value of data in the following format. Note that these values can be nested, for example an array of structs.
| Type                        | JSON encoding                                         | Example                                                                       |
|-----------------------------|-------------------------------------------------------|-------------------------------------------------------------------------------|
| Array                       | array                                                 | `["alpha", "bravo", "charlie"]`                                               |
| Attachment                  | string                                                | `"ri.attachments.main.attachment.2f944bae-5851-4204-8615-920c969a9f2e"`       |
| Boolean                     | boolean                                               | `true`                                                                        |
| Byte                        | number                                                | `31`                                                                          |
| Date                        | ISO 8601 extended local date string                   | `"2021-05-01"`                                                                |
| Decimal                     | string                                                | `"2.718281828"`                                                               |
| Float                       | number                                                | `3.14159265`                                                                  |
| Double                      | number                                                | `3.14159265`                                                                  |
| Integer                     | number                                                | `238940`                                                                      |
| Long                        | string                                                | `"58319870951433"`                                                            |
| Marking                     | string                                                | `"MU"`                                                                        |
| Null                        | null                                                  | `null`                                                                        |
| Set                         | array                                                 | `["alpha", "bravo", "charlie"]`                                               |
| Short                       | number                                                | `8739`                                                                        |
| String                      | string                                                | `"Call me Ishmael"`                                                           |
| Struct                      | JSON object                                           | `{"name": "John Doe", "age": 42}`                                             |
| TwoDimensionalAggregation   | JSON object                                           | `{"groups": [{"key": "alpha", "value": 100}, {"key": "beta", "value": 101}]}` |
| ThreeDimensionalAggregation | JSON object                                           | `{"groups": [{"key": "NYC", "groups": [{"key": "Engineer", "value" : 100}]}]}`|
| Timestamp                   | ISO 8601 extended offset date-time string in UTC zone | `"2021-01-04T05:00:00Z"`                                                      |


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
DataValue: typing_extensions.TypeAlias = typing.Any
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DataValue.md)
