# foundry_sdk.v2.media_sets.models.Mailbox


An email mailbox with an optional display name and email address.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| display_name | displayName | typing.Optional[str] | default None | The display name of the mailbox. |
| email_address | emailAddress | str | required; no default | The email address of the mailbox. |

```python
class Mailbox(core.ModelBase):
    """An email mailbox with an optional display name and email address."""

    display_name: typing.Optional[str] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    """The display name of the mailbox."""

    email_address: str = pydantic.Field(alias=str("emailAddress"))  # type: ignore[literal-required]
    """The email address of the mailbox."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Mailbox.md)
