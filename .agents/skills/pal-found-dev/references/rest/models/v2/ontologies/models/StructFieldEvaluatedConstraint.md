# foundry_sdk.v2.ontologies.models.StructFieldEvaluatedConstraint



A constraint that an action struct parameter field value must satisfy in order to be considered valid.
Constraints can be configured on fields of struct parameters in the **Ontology Manager**. 
Applicable constraints are determined dynamically based on parameter inputs. 
Parameter values are evaluated against the final set of constraints.

The type of the constraint.
| Type                  | Description                                                                                                                                                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `oneOf`               | The struct parameter field has a manually predefined set of options.                                                                                                                                                            |
| `range`               | The struct parameter field value must be within the defined range.                                                                                                                                                              |
| `stringLength`        | The struct parameter field value must have a length within the defined range.                                                                                                                                                   |
| `stringRegexMatch`    | The struct parameter field value must match a predefined regular expression.                                                                                                                                                    |
| `objectQueryResult`   | The struct parameter field value must be the primary key of an object found within an object set.                                                                                                                               |


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
StructFieldEvaluatedConstraint: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "OneOfConstraint",
        "RangeConstraint",
        "ObjectQueryResultConstraint",
        "StringLengthConstraint",
        "StringRegexMatchConstraint",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.ObjectQueryResultConstraint](ObjectQueryResultConstraint.md)
- [foundry_sdk.v2.ontologies.models.OneOfConstraint](OneOfConstraint.md)
- [foundry_sdk.v2.ontologies.models.RangeConstraint](RangeConstraint.md)
- [foundry_sdk.v2.ontologies.models.StringLengthConstraint](StringLengthConstraint.md)
- [foundry_sdk.v2.ontologies.models.StringRegexMatchConstraint](StringRegexMatchConstraint.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](StructFieldEvaluatedConstraint.md)
