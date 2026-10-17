# foundry_sdk.v2.checkpoints.models.DropdownSelection


A selection made within a multi-select dropdown justification.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| selected_option | selectedOption | str | required; no default | Dropdown option the user selected. |
| additional_response | additionalResponse | typing.Optional[str] | default None | Extra free-text response submitted alongside the dropdown selection. |

```python
class DropdownSelection(core.ModelBase):
    """A selection made within a multi-select dropdown justification."""

    selected_option: str = pydantic.Field(alias=str("selectedOption"))  # type: ignore[literal-required]
    """Dropdown option the user selected."""

    additional_response: typing.Optional[str] = pydantic.Field(alias=str("additionalResponse"), default=None)  # type: ignore[literal-required]
    """Extra free-text response submitted alongside the dropdown selection."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DropdownSelection.md)
