# foundry_sdk.v2.media_sets.models.EncryptImageOperation


Encrypts bounding boxes in an image using a commutative encryption algorithm.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| polygons | polygons | typing.List[ImageRegionPolygon] | required; no default | The polygons defining the regions to encrypt. |
| cipher_license_rid | cipherLicenseRid | core.RID | required; no default | The resource identifier for the cipher license. |
| type | type | typing.Literal['encrypt'] | 'encrypt' | No additional field description in SDK source. |

```python
class EncryptImageOperation(core.ModelBase):
    """Encrypts bounding boxes in an image using a commutative encryption algorithm."""

    polygons: typing.List[ImageRegionPolygon]
    """The polygons defining the regions to encrypt."""

    cipher_license_rid: core.RID = pydantic.Field(alias=str("cipherLicenseRid"))  # type: ignore[literal-required]
    """The resource identifier for the cipher license."""

    type: typing.Literal["encrypt"] = "encrypt"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)
- [foundry_sdk.v2.media_sets.models.ImageRegionPolygon](ImageRegionPolygon.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](EncryptImageOperation.md)
