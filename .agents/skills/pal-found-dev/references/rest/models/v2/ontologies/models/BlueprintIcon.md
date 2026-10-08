# foundry_sdk.v2.ontologies.models.BlueprintIcon


BlueprintIcon

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| color | color | str | required; no default | A hexadecimal color code. |
| name | name | str | required; no default | The [name](https://blueprintjs.com/docs/#icons/icons-list) of the Blueprint icon. <br>    Used to specify the Blueprint icon to represent the object type in a React app. |
| type | type | typing.Literal['blueprint'] | 'blueprint' | No additional field description in SDK source. |

```python
class BlueprintIcon(core.ModelBase):
    """BlueprintIcon"""

    color: str
    """A hexadecimal color code."""

    name: str
    """
    The [name](https://blueprintjs.com/docs/#icons/icons-list) of the Blueprint icon. 
    Used to specify the Blueprint icon to represent the object type in a React app.
    """

    type: typing.Literal["blueprint"] = "blueprint"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](BlueprintIcon.md)
