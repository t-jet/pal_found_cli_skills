# foundry_sdk.v1.ontologies.models.ValidateActionResponse


ValidateActionResponse

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| result | result | ValidationResult | required; no default | No additional field description in SDK source. |
| submission_criteria | submissionCriteria | typing.List[SubmissionCriteriaEvaluation] | required; no default | No additional field description in SDK source. |
| parameters | parameters | typing.Dict[ParameterId, ParameterEvaluationResult] | required; no default | No additional field description in SDK source. |

```python
class ValidateActionResponse(core.ModelBase):
    """ValidateActionResponse"""

    result: ValidationResult
    submission_criteria: typing.List[SubmissionCriteriaEvaluation] = pydantic.Field(alias=str("submissionCriteria"))  # type: ignore[literal-required]
    parameters: typing.Dict[ParameterId, ParameterEvaluationResult]
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.ontologies.models.ParameterEvaluationResult](ParameterEvaluationResult.md)
- [foundry_sdk.v1.ontologies.models.ParameterId](ParameterId.md)
- [foundry_sdk.v1.ontologies.models.SubmissionCriteriaEvaluation](SubmissionCriteriaEvaluation.md)
- [foundry_sdk.v1.ontologies.models.ValidationResult](ValidationResult.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ValidateActionResponse.md)
