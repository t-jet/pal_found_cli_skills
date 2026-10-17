# foundry_sdk.v2.checkpoints.models.ReauthenticationJustification


Checkpoint justification that requires the user to reauthenticate with the platform.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| reauthentication_id | reauthenticationId | core.UUID | required; no default | Identifier for the reauthentication instance. |
| prompt | prompt | str | required; no default | Prompt shown to the user during reauthentication. |
| description | description | typing.Optional[str] | None | Supplemental information that helps users understand the prompt. |
| title | title | str | required; no default | Title of the checkpoint that the user is acknowledging. |
| type | type | typing.Literal['reauthenticationJustification'] | 'reauthenticationJustification' | No additional field description in SDK source. |

```python
class ReauthenticationJustification(core.ModelBase):
    """Checkpoint justification that requires the user to reauthenticate with the platform."""

    reauthentication_id: core.UUID = pydantic.Field(alias=str("reauthenticationId"))  # type: ignore[literal-required]
    """Identifier for the reauthentication instance."""

    prompt: str
    """Prompt shown to the user during reauthentication."""

    description: typing.Optional[str] = None
    """Supplemental information that helps users understand the prompt."""

    title: str
    """Title of the checkpoint that the user is acknowledging."""

    type: typing.Literal["reauthenticationJustification"] = "reauthenticationJustification"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.UUID](../../../_core/UUID.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReauthenticationJustification.md)
