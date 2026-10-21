# foundry_sdk.v2.checkpoints.models.ResponseJustification


Checkpoint justification that requires the user to input a free-text response.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| response | response | str | required; no default | User-submitted free-text justification. |
| prompt | prompt | str | required; no default | Prompt to which the user responds. |
| description | description | typing.Optional[str] | None | Supplemental information that helps users understand the prompt. |
| title | title | str | required; no default | Title of the checkpoint to which the user is responding. |
| type | type | typing.Literal['responseJustification'] | 'responseJustification' | No additional field description in SDK source. |

```python
class ResponseJustification(core.ModelBase):
    """Checkpoint justification that requires the user to input a free-text response."""

    response: str
    """User-submitted free-text justification."""

    prompt: str
    """Prompt to which the user responds."""

    description: typing.Optional[str] = None
    """Supplemental information that helps users understand the prompt."""

    title: str
    """Title of the checkpoint to which the user is responding."""

    type: typing.Literal["responseJustification"] = "responseJustification"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ResponseJustification.md)
