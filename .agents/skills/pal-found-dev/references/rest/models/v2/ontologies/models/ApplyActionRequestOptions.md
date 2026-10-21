# foundry_sdk.v2.ontologies.models.ApplyActionRequestOptions


ApplyActionRequestOptions

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| mode | mode | typing.Optional[ApplyActionMode] | None | No additional field description in SDK source. |
| return_edits | returnEdits | typing.Optional[ReturnEditsMode] | default None | No additional field description in SDK source. |

```python
class ApplyActionRequestOptions(core.ModelBase):
    """ApplyActionRequestOptions"""

    mode: typing.Optional[ApplyActionMode] = None
    return_edits: typing.Optional[ReturnEditsMode] = pydantic.Field(alias=str("returnEdits"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.ApplyActionMode](ApplyActionMode.md)
- [foundry_sdk.v2.ontologies.models.ReturnEditsMode](ReturnEditsMode.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ApplyActionRequestOptions.md)
