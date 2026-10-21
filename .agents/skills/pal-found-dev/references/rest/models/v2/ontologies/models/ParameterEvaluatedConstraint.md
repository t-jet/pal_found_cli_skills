# foundry_sdk.v2.ontologies.models.ParameterEvaluatedConstraint



A constraint that an action parameter value must satisfy in order to be considered valid.
Constraints can be configured on action parameters in the **Ontology Manager**. 
Applicable constraints are determined dynamically based on parameter inputs. 
Parameter values are evaluated against the final set of constraints.

The type of the constraint.
| Type                  | Description                                                                                                                                                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `arraySize`           | The parameter expects an array of values and the size of the array must fall within the defined range.                                                                                                                          |
| `groupMember`         | The parameter value must be the user id of a member belonging to at least one of the groups defined by the constraint.                                                                                                          |
| `objectPropertyValue` | The parameter value must be a property value of an object found within an object set.                                                                                                                                           |
| `objectQueryResult`   | The parameter value must be the primary key of an object found within an object set.                                                                                                                                            |
| `oneOf`               | The parameter has a manually predefined set of options.                                                                                                                                                                         |
| `range`               | The parameter value must be within the defined range.                                                                                                                                                                           |
| `stringLength`        | The parameter value must have a length within the defined range.                                                                                                                                                                |
| `stringRegexMatch`    | The parameter value must match a predefined regular expression.                                                                                                                                                                 |
| `unevaluable`         | The parameter cannot be evaluated because it depends on another parameter or object set that can't be evaluated. This can happen when a parameter's allowed values are defined by another parameter that is missing or invalid. |


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ParameterEvaluatedConstraint: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "StructEvaluatedConstraint",
        "OneOfConstraint",
        "ArrayEvaluatedConstraint",
        "GroupMemberConstraint",
        "ObjectPropertyValueConstraint",
        "RangeConstraint",
        "ArraySizeConstraint",
        "ObjectQueryResultConstraint",
        "StringLengthConstraint",
        "StringRegexMatchConstraint",
        "UnevaluableConstraint",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.ArrayEvaluatedConstraint](ArrayEvaluatedConstraint.md)
- [foundry_sdk.v2.ontologies.models.ArraySizeConstraint](ArraySizeConstraint.md)
- [foundry_sdk.v2.ontologies.models.GroupMemberConstraint](GroupMemberConstraint.md)
- [foundry_sdk.v2.ontologies.models.ObjectPropertyValueConstraint](ObjectPropertyValueConstraint.md)
- [foundry_sdk.v2.ontologies.models.ObjectQueryResultConstraint](ObjectQueryResultConstraint.md)
- [foundry_sdk.v2.ontologies.models.OneOfConstraint](OneOfConstraint.md)
- [foundry_sdk.v2.ontologies.models.RangeConstraint](RangeConstraint.md)
- [foundry_sdk.v2.ontologies.models.StringLengthConstraint](StringLengthConstraint.md)
- [foundry_sdk.v2.ontologies.models.StringRegexMatchConstraint](StringRegexMatchConstraint.md)
- [foundry_sdk.v2.ontologies.models.StructEvaluatedConstraint](StructEvaluatedConstraint.md)
- [foundry_sdk.v2.ontologies.models.UnevaluableConstraint](UnevaluableConstraint.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ParameterEvaluatedConstraint.md)
