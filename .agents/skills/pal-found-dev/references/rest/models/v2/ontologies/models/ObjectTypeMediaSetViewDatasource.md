# foundry_sdk.v2.ontologies.models.ObjectTypeMediaSetViewDatasource


An object type datasource backed by a Foundry media set view, providing media for media reference properties.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| media_set_view_rid | mediaSetViewRid | core_models.MediaSetViewRid | required; no default | No additional field description in SDK source. |
| properties | properties | typing.List[PropertyApiName] | required; no default | The set of properties that are bound to the media view. |
| type | type | typing.Literal['mediaSetView'] | 'mediaSetView' | No additional field description in SDK source. |

```python
class ObjectTypeMediaSetViewDatasource(core.ModelBase):
    """An object type datasource backed by a Foundry media set view, providing media for media reference properties."""

    media_set_view_rid: core_models.MediaSetViewRid = pydantic.Field(alias=str("mediaSetViewRid"))  # type: ignore[literal-required]
    properties: typing.List[PropertyApiName]
    """The set of properties that are bound to the media view."""

    type: typing.Literal["mediaSetView"] = "mediaSetView"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.MediaSetViewRid](../../core/models/MediaSetViewRid.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectTypeMediaSetViewDatasource.md)
