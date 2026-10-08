# foundry_sdk.v2.checkpoints.models.AcknowledgementJustification


Checkpoint justification that requires the user to mark a checkbox.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| prompt | prompt | str | required; no default | Prompt acknowledged by the user. |
| description | description | typing.Optional[str] | None | Supplemental information that helps users understand the prompt. |
| title | title | str | required; no default | Title of the checkpoint the user is acknowledging. |
| type | type | typing.Literal['acknowledgementJustification'] | 'acknowledgementJustification' | No additional field description in SDK source. |

```python
class AcknowledgementJustification(core.ModelBase):
    """Checkpoint justification that requires the user to mark a checkbox."""

    prompt: str
    """Prompt acknowledged by the user."""

    description: typing.Optional[str] = None
    """Supplemental information that helps users understand the prompt."""

    title: str
    """Title of the checkpoint the user is acknowledging."""

    type: typing.Literal["acknowledgementJustification"] = "acknowledgementJustification"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AcknowledgementJustification.md)
