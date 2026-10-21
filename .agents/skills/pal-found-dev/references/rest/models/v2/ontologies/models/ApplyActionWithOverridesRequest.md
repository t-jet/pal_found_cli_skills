# foundry_sdk.v2.ontologies.models.ApplyActionWithOverridesRequest


ApplyActionWithOverridesRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| request | request | ApplyActionRequestV2 | required; no default | No additional field description in SDK source. |
| overrides | overrides | ApplyActionOverrides | required; no default | No additional field description in SDK source. |

```python
class ApplyActionWithOverridesRequest(core.ModelBase):
    """ApplyActionWithOverridesRequest"""

    request: ApplyActionRequestV2
    overrides: ApplyActionOverrides
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.ApplyActionOverrides](ApplyActionOverrides.md)
- [foundry_sdk.v2.ontologies.models.ApplyActionRequestV2](ApplyActionRequestV2.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ApplyActionWithOverridesRequest.md)
