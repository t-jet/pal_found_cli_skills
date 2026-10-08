# foundry_sdk.v1.ontologies.models.SubmissionCriteriaEvaluation


Contains the status of the **submission criteria**.
**Submission criteria** are the prerequisites that need to be satisfied before an Action can be applied.
These are configured in the **Ontology Manager**.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| configured_failure_message | configuredFailureMessage | typing.Optional[str] | default None | The message indicating one of the **submission criteria** was not satisfied.<br>    This is configured per **submission criteria** in the **Ontology Manager**. |
| result | result | ValidationResult | required; no default | No additional field description in SDK source. |

```python
class SubmissionCriteriaEvaluation(core.ModelBase):
    """
    Contains the status of the **submission criteria**.
    **Submission criteria** are the prerequisites that need to be satisfied before an Action can be applied.
    These are configured in the **Ontology Manager**.
    """

    configured_failure_message: typing.Optional[str] = pydantic.Field(alias=str("configuredFailureMessage"), default=None)  # type: ignore[literal-required]
    """
    The message indicating one of the **submission criteria** was not satisfied.
    This is configured per **submission criteria** in the **Ontology Manager**.
    """

    result: ValidationResult
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.ontologies.models.ValidationResult](ValidationResult.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SubmissionCriteriaEvaluation.md)
