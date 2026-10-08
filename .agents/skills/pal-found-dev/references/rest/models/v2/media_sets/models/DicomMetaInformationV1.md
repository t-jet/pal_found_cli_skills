# foundry_sdk.v2.media_sets.models.DicomMetaInformationV1


DICOM meta information version 1.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| media_storage_sop | mediaStorageSop | str | required; no default | The Media Storage SOP (Service-Object Pair) Class UID, which identifies <br>    the type of DICOM object stored (e.g., CT Image, MR Image). |
| media_storage_sop_instance | mediaStorageSopInstance | str | required; no default | The Media Storage SOP Instance UID. |
| transfer_syntax | transferSyntax | str | required; no default | The Transfer Syntax UID, which specifies how the DICOM data is encoded <br>    (e.g., compression method, byte ordering). |
| type | type | typing.Literal['v1'] | 'v1' | No additional field description in SDK source. |

```python
class DicomMetaInformationV1(core.ModelBase):
    """DICOM meta information version 1."""

    media_storage_sop: str = pydantic.Field(alias=str("mediaStorageSop"))  # type: ignore[literal-required]
    """
    The Media Storage SOP (Service-Object Pair) Class UID, which identifies 
    the type of DICOM object stored (e.g., CT Image, MR Image).
    """

    media_storage_sop_instance: str = pydantic.Field(alias=str("mediaStorageSopInstance"))  # type: ignore[literal-required]
    """The Media Storage SOP Instance UID."""

    transfer_syntax: str = pydantic.Field(alias=str("transferSyntax"))  # type: ignore[literal-required]
    """
    The Transfer Syntax UID, which specifies how the DICOM data is encoded 
    (e.g., compression method, byte ordering).
    """

    type: typing.Literal["v1"] = "v1"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DicomMetaInformationV1.md)
