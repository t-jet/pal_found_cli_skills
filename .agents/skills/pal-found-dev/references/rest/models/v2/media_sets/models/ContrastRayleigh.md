# foundry_sdk.v2.media_sets.models.ContrastRayleigh


Applies Rayleigh distribution-based contrast adjustment.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| sigma | sigma | float | required; no default | The scaling parameter for the Rayleigh distribution (0-1). |
| type | type | typing.Literal['rayleigh'] | 'rayleigh' | No additional field description in SDK source. |

```python
class ContrastRayleigh(core.ModelBase):
    """Applies Rayleigh distribution-based contrast adjustment."""

    sigma: float
    """The scaling parameter for the Rayleigh distribution (0-1)."""

    type: typing.Literal["rayleigh"] = "rayleigh"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ContrastRayleigh.md)
