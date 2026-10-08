# foundry_sdk.v2.filesystem.models.AddExternalResourceReferenceRequest


A request to add an external resource as a reference to a project

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| resource_rid | resourceRid | core.RID | required; no default | The resource identifier of the external resource to add as a reference. Note that this is not a Foundry filesystem resource. |
| import_name | importName | str | required; no default | A user-provided label for this reference, used to identify the import within the project. |
| type | type | typing.Literal['external'] | 'external' | No additional field description in SDK source. |

```python
class AddExternalResourceReferenceRequest(core.ModelBase):
    """A request to add an external resource as a reference to a project"""

    resource_rid: core.RID = pydantic.Field(alias=str("resourceRid"))  # type: ignore[literal-required]
    """The resource identifier of the external resource to add as a reference. Note that this is not a Foundry filesystem resource."""

    import_name: str = pydantic.Field(alias=str("importName"))  # type: ignore[literal-required]
    """A user-provided label for this reference, used to identify the import within the project."""

    type: typing.Literal["external"] = "external"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AddExternalResourceReferenceRequest.md)
