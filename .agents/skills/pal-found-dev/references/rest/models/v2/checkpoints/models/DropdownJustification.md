# foundry_sdk.v2.checkpoints.models.DropdownJustification


Checkpoint justification where the user selects one or more options from a dropdown.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| selected_options | selectedOptions | typing.List[DropdownSelection] | required; no default | Options the user selected in the dropdown. |
| prompt | prompt | str | required; no default | Prompt to which the user-selected options respond. |
| description | description | typing.Optional[str] | None | Supplemental information that helps users understand the prompt. |
| title | title | str | required; no default | Title of the checkpoint to which the user is responding. |
| type | type | typing.Literal['dropdownJustification'] | 'dropdownJustification' | No additional field description in SDK source. |

```python
class DropdownJustification(core.ModelBase):
    """Checkpoint justification where the user selects one or more options from a dropdown."""

    selected_options: typing.List[DropdownSelection] = pydantic.Field(alias=str("selectedOptions"))  # type: ignore[literal-required]
    """Options the user selected in the dropdown."""

    prompt: str
    """Prompt to which the user-selected options respond."""

    description: typing.Optional[str] = None
    """Supplemental information that helps users understand the prompt."""

    title: str
    """Title of the checkpoint to which the user is responding."""

    type: typing.Literal["dropdownJustification"] = "dropdownJustification"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.checkpoints.models.DropdownSelection](DropdownSelection.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DropdownJustification.md)
