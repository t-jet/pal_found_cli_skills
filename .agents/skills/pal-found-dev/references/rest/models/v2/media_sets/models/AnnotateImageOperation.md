# foundry_sdk.v2.media_sets.models.AnnotateImageOperation


Annotates an image with bounding boxes, labels, and colors.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| annotations | annotations | typing.List[Annotation] | required; no default | The list of annotations to draw on the image. |
| type | type | typing.Literal['annotate'] | 'annotate' | No additional field description in SDK source. |

```python
class AnnotateImageOperation(core.ModelBase):
    """Annotates an image with bounding boxes, labels, and colors."""

    annotations: typing.List[Annotation]
    """The list of annotations to draw on the image."""

    type: typing.Literal["annotate"] = "annotate"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.Annotation](Annotation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AnnotateImageOperation.md)
