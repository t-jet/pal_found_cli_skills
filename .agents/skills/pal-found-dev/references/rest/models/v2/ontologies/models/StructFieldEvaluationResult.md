# foundry_sdk.v2.ontologies.models.StructFieldEvaluationResult


Represents the validity of a struct parameter's fields against the configured constraints.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| result | result | ValidationResult | required; no default | No additional field description in SDK source. |
| evaluated_constraints | evaluatedConstraints | typing.List[StructFieldEvaluatedConstraint] | required; no default | No additional field description in SDK source. |
| required | required | bool | required; no default | Represents whether the parameter is a required input to the action. |

```python
class StructFieldEvaluationResult(core.ModelBase):
    """Represents the validity of a struct parameter's fields against the configured constraints."""

    result: ValidationResult
    evaluated_constraints: typing.List[StructFieldEvaluatedConstraint] = pydantic.Field(alias=str("evaluatedConstraints"))  # type: ignore[literal-required]
    required: bool
    """Represents whether the parameter is a required input to the action."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.StructFieldEvaluatedConstraint](StructFieldEvaluatedConstraint.md)
- [foundry_sdk.v2.ontologies.models.ValidationResult](ValidationResult.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](StructFieldEvaluationResult.md)
