# foundry_sdk.v2.filesystem.models.ResourceTag


ResourceTag

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| tag_rid | tagRid | TagRid | required; no default | No additional field description in SDK source. |
| display_name | displayName | ResourceTagDisplayName | required; no default | The display name of the tag, qualified by its category as `{category}:{tag}`. |

```python
class ResourceTag(core.ModelBase):
    """ResourceTag"""

    tag_rid: TagRid = pydantic.Field(alias=str("tagRid"))  # type: ignore[literal-required]
    display_name: ResourceTagDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The display name of the tag, qualified by its category as `{category}:{tag}`."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.filesystem.models.ResourceTagDisplayName](ResourceTagDisplayName.md)
- [foundry_sdk.v2.filesystem.models.TagRid](TagRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ResourceTag.md)
