# foundry_sdk.v2.widgets.models.WidgetSetInputSpec


A specification of the Foundry data inputs that a widget set uses. This restricts
the data access that a widget set has at runtime.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| sdks | sdks | typing.List[OntologySdkInputSpec] | required; no default | The Ontology SDK specifications used by the widget set. |

```python
class WidgetSetInputSpec(core.ModelBase):
    """
    A specification of the Foundry data inputs that a widget set uses. This restricts
    the data access that a widget set has at runtime.
    """

    sdks: typing.List[OntologySdkInputSpec]
    """The Ontology SDK specifications used by the widget set."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.widgets.models.OntologySdkInputSpec](OntologySdkInputSpec.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](WidgetSetInputSpec.md)
