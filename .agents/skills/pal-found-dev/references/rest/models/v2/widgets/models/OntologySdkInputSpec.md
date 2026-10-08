# foundry_sdk.v2.widgets.models.OntologySdkInputSpec


A specification of an Ontology SDK used by a widget set.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| sdk_package_rid | sdkPackageRid | OntologySdkPackageRid | required; no default | The RID of the Ontology SDK package. |
| sdk_version | sdkVersion | OntologySdkVersion | required; no default | The version of the Ontology SDK. |

```python
class OntologySdkInputSpec(core.ModelBase):
    """A specification of an Ontology SDK used by a widget set."""

    sdk_package_rid: OntologySdkPackageRid = pydantic.Field(alias=str("sdkPackageRid"))  # type: ignore[literal-required]
    """The RID of the Ontology SDK package."""

    sdk_version: OntologySdkVersion = pydantic.Field(alias=str("sdkVersion"))  # type: ignore[literal-required]
    """The version of the Ontology SDK."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.widgets.models.OntologySdkPackageRid](OntologySdkPackageRid.md)
- [foundry_sdk.v2.widgets.models.OntologySdkVersion](OntologySdkVersion.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OntologySdkInputSpec.md)
