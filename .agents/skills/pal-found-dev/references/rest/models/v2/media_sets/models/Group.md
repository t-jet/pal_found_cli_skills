# foundry_sdk.v2.media_sets.models.Group


A named group of mailboxes.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| group_name | groupName | str | required; no default | The name of the group. |
| mailboxes | mailboxes | typing.List[Mailbox] | required; no default | The mailboxes in the group. |

```python
class Group(core.ModelBase):
    """A named group of mailboxes."""

    group_name: str = pydantic.Field(alias=str("groupName"))  # type: ignore[literal-required]
    """The name of the group."""

    mailboxes: typing.List[Mailbox]
    """The mailboxes in the group."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.Mailbox](Mailbox.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Group.md)
