# foundry_sdk.v2.ontologies.models.BatchActionObjectEdits


BatchActionObjectEdits

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| edits | edits | typing.List[BatchActionObjectEdit] | required; no default | No additional field description in SDK source. |
| added_object_count | addedObjectCount | int | required; no default | No additional field description in SDK source. |
| modified_objects_count | modifiedObjectsCount | int | required; no default | No additional field description in SDK source. |
| deleted_objects_count | deletedObjectsCount | int | required; no default | No additional field description in SDK source. |
| added_links_count | addedLinksCount | int | required; no default | No additional field description in SDK source. |
| deleted_links_count | deletedLinksCount | int | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['edits'] | 'edits' | No additional field description in SDK source. |

```python
class BatchActionObjectEdits(core.ModelBase):
    """BatchActionObjectEdits"""

    edits: typing.List[BatchActionObjectEdit]
    added_object_count: int = pydantic.Field(alias=str("addedObjectCount"))  # type: ignore[literal-required]
    modified_objects_count: int = pydantic.Field(alias=str("modifiedObjectsCount"))  # type: ignore[literal-required]
    deleted_objects_count: int = pydantic.Field(alias=str("deletedObjectsCount"))  # type: ignore[literal-required]
    added_links_count: int = pydantic.Field(alias=str("addedLinksCount"))  # type: ignore[literal-required]
    deleted_links_count: int = pydantic.Field(alias=str("deletedLinksCount"))  # type: ignore[literal-required]
    type: typing.Literal["edits"] = "edits"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.BatchActionObjectEdit](BatchActionObjectEdit.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](BatchActionObjectEdits.md)
