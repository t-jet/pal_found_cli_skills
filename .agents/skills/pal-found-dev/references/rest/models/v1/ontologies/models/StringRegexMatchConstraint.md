# foundry_sdk.v1.ontologies.models.StringRegexMatchConstraint


The parameter value must match a predefined regular expression.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| regex | regex | str | required; no default | The regular expression configured in the **Ontology Manager**. |
| configured_failure_message | configuredFailureMessage | typing.Optional[str] | default None | The message indicating that the regular expression was not matched.<br>    This is configured per parameter in the **Ontology Manager**. |
| type | type | typing.Literal['stringRegexMatch'] | 'stringRegexMatch' | No additional field description in SDK source. |

```python
class StringRegexMatchConstraint(core.ModelBase):
    """The parameter value must match a predefined regular expression."""

    regex: str
    """The regular expression configured in the **Ontology Manager**."""

    configured_failure_message: typing.Optional[str] = pydantic.Field(alias=str("configuredFailureMessage"), default=None)  # type: ignore[literal-required]
    """
    The message indicating that the regular expression was not matched.
    This is configured per parameter in the **Ontology Manager**.
    """

    type: typing.Literal["stringRegexMatch"] = "stringRegexMatch"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](StringRegexMatchConstraint.md)
