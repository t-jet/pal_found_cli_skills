# foundry_sdk.v2.widgets.models.Repository


Repository

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | RepositoryRid | required; no default | A Resource Identifier (RID) identifying a repository. |
| widget_set_rid | widgetSetRid | typing.Optional[WidgetSetRid] | default None | The Resource Identifier (RID) of the widget set that has authorized this repository<br>    to publish new widget releases. |

```python
class Repository(core.ModelBase):
    """Repository"""

    rid: RepositoryRid
    """A Resource Identifier (RID) identifying a repository."""

    widget_set_rid: typing.Optional[WidgetSetRid] = pydantic.Field(alias=str("widgetSetRid"), default=None)  # type: ignore[literal-required]
    """
    The Resource Identifier (RID) of the widget set that has authorized this repository
    to publish new widget releases.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.widgets.models.RepositoryRid](RepositoryRid.md)
- [foundry_sdk.v2.widgets.models.WidgetSetRid](WidgetSetRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Repository.md)
