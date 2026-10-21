# foundry_sdk.v2.media_sets.models.CommonDicomDataElements


Common DICOM data elements.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| number_frames | numberFrames | typing.Optional[int] | default None | The number of frames in the DICOM file. |
| modality | modality | typing.Optional[Modality] | None | No additional field description in SDK source. |
| patient_id | patientId | typing.Optional[str] | default None | The patient ID. |
| study_id | studyId | typing.Optional[str] | default None | The study ID. |
| study_uid | studyUid | typing.Optional[str] | default None | The study UID. |
| series_uid | seriesUid | typing.Optional[str] | default None | The series UID. |
| study_time | studyTime | typing.Optional[core.AwareDatetime] | default None | The study time. |
| series_time | seriesTime | typing.Optional[core.AwareDatetime] | default None | The series time. |

```python
class CommonDicomDataElements(core.ModelBase):
    """Common DICOM data elements."""

    number_frames: typing.Optional[int] = pydantic.Field(alias=str("numberFrames"), default=None)  # type: ignore[literal-required]
    """The number of frames in the DICOM file."""

    modality: typing.Optional[Modality] = None
    patient_id: typing.Optional[str] = pydantic.Field(alias=str("patientId"), default=None)  # type: ignore[literal-required]
    """The patient ID."""

    study_id: typing.Optional[str] = pydantic.Field(alias=str("studyId"), default=None)  # type: ignore[literal-required]
    """The study ID."""

    study_uid: typing.Optional[str] = pydantic.Field(alias=str("studyUid"), default=None)  # type: ignore[literal-required]
    """The study UID."""

    series_uid: typing.Optional[str] = pydantic.Field(alias=str("seriesUid"), default=None)  # type: ignore[literal-required]
    """The series UID."""

    study_time: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("studyTime"), default=None)  # type: ignore[literal-required]
    """The study time."""

    series_time: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("seriesTime"), default=None)  # type: ignore[literal-required]
    """The series time."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../_core/AwareDatetime.md)
- [foundry_sdk.v2.media_sets.models.Modality](Modality.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CommonDicomDataElements.md)
