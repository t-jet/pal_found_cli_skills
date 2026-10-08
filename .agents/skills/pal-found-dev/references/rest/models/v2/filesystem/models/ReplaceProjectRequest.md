# foundry_sdk.v2.filesystem.models.ReplaceProjectRequest


ReplaceProjectRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| display_name | displayName | ResourceDisplayName | required; no default | The display name of the Project. Must be unique and cannot contain a / |
| description | description | typing.Optional[str] | None | The description associated with the Project. |

```python
class ReplaceProjectRequest(core.ModelBase):
    """ReplaceProjectRequest"""

    display_name: ResourceDisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    """The display name of the Project. Must be unique and cannot contain a /"""

    description: typing.Optional[str] = None
    """The description associated with the Project."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.filesystem.models.ResourceDisplayName](ResourceDisplayName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReplaceProjectRequest.md)
