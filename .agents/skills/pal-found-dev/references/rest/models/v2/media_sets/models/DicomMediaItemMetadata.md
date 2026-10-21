# foundry_sdk.v2.media_sets.models.DicomMediaItemMetadata


Metadata for DICOM (Digital Imaging and Communications in Medicine) media items.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| meta_information | metaInformation | DicomMetaInformation | required; no default | No additional field description in SDK source. |
| media_type | mediaType | DicomMediaType | required; no default | No additional field description in SDK source. |
| common_data_elements | commonDataElements | CommonDicomDataElements | required; no default | No additional field description in SDK source. |
| other_data_elements | otherDataElements | typing.Dict[DicomDataElementKey, typing.Any] | required; no default | The data elements for a particular DICOM file outside of the media contained within it and the<br>    data elements within the commonDataElements field. |
| size_bytes | sizeBytes | int | required; no default | The size of the media item in bytes. |
| type | type | typing.Literal['dicom'] | 'dicom' | No additional field description in SDK source. |

```python
class DicomMediaItemMetadata(core.ModelBase):
    """Metadata for DICOM (Digital Imaging and Communications in Medicine) media items."""

    meta_information: DicomMetaInformation = pydantic.Field(alias=str("metaInformation"))  # type: ignore[literal-required]
    media_type: DicomMediaType = pydantic.Field(alias=str("mediaType"))  # type: ignore[literal-required]
    common_data_elements: CommonDicomDataElements = pydantic.Field(alias=str("commonDataElements"))  # type: ignore[literal-required]
    other_data_elements: typing.Dict[DicomDataElementKey, typing.Any] = pydantic.Field(alias=str("otherDataElements"))  # type: ignore[literal-required]
    """
    The data elements for a particular DICOM file outside of the media contained within it and the
    data elements within the commonDataElements field.
    """

    size_bytes: int = pydantic.Field(alias=str("sizeBytes"))  # type: ignore[literal-required]
    """The size of the media item in bytes."""

    type: typing.Literal["dicom"] = "dicom"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.CommonDicomDataElements](CommonDicomDataElements.md)
- [foundry_sdk.v2.media_sets.models.DicomDataElementKey](DicomDataElementKey.md)
- [foundry_sdk.v2.media_sets.models.DicomMediaType](DicomMediaType.md)
- [foundry_sdk.v2.media_sets.models.DicomMetaInformation](DicomMetaInformation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DicomMediaItemMetadata.md)
