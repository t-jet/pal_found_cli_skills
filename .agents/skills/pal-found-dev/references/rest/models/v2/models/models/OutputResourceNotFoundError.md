# foundry_sdk.v2.models.models.OutputResourceNotFoundError


The output resource does not exist or is in the trash.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| resource_rid | resourceRid | core.RID | required; no default | The RID of the resource that was not found. |
| output_alias | outputAlias | OutputAlias | required; no default | The alias of the output referencing the missing resource. |
| type | type | typing.Literal['outputResourceNotFound'] | 'outputResourceNotFound' | No additional field description in SDK source. |

```python
class OutputResourceNotFoundError(core.ModelBase):
    """The output resource does not exist or is in the trash."""

    resource_rid: core.RID = pydantic.Field(alias=str("resourceRid"))  # type: ignore[literal-required]
    """The RID of the resource that was not found."""

    output_alias: OutputAlias = pydantic.Field(alias=str("outputAlias"))  # type: ignore[literal-required]
    """The alias of the output referencing the missing resource."""

    type: typing.Literal["outputResourceNotFound"] = "outputResourceNotFound"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)
- [foundry_sdk.v2.models.models.OutputAlias](OutputAlias.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OutputResourceNotFoundError.md)
