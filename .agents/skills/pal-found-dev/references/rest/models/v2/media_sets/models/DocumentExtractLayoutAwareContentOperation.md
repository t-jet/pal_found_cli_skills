# foundry_sdk.v2.media_sets.models.DocumentExtractLayoutAwareContentOperation


Extracts content from a document with layout information preserved.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| parameters | parameters | LayoutAwareExtractionParameters | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['extractLayoutAwareContent'] | 'extractLayoutAwareContent' | No additional field description in SDK source. |

```python
class DocumentExtractLayoutAwareContentOperation(core.ModelBase):
    """Extracts content from a document with layout information preserved."""

    parameters: LayoutAwareExtractionParameters
    type: typing.Literal["extractLayoutAwareContent"] = "extractLayoutAwareContent"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.LayoutAwareExtractionParameters](LayoutAwareExtractionParameters.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DocumentExtractLayoutAwareContentOperation.md)
