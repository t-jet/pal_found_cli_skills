# foundry_sdk.v2.ontologies.models.InterfacePropertyStructImplementation


An implementation of a struct interface property via a local struct property. Specifies a mapping of interface
struct fields to local struct fields or properties.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| mapping | mapping | InterfacePropertyStructImplementationMapping | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['structImplementation'] | 'structImplementation' | No additional field description in SDK source. |

```python
class InterfacePropertyStructImplementation(core.ModelBase):
    """
    An implementation of a struct interface property via a local struct property. Specifies a mapping of interface
    struct fields to local struct fields or properties.
    """

    mapping: InterfacePropertyStructImplementationMapping
    type: typing.Literal["structImplementation"] = "structImplementation"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyStructImplementationMapping](InterfacePropertyStructImplementationMapping.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InterfacePropertyStructImplementation.md)
