# foundry_sdk.v2.widgets.models.ScriptEntrypoint


A script entrypoint to be loaded into the runtime environment.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| file_path | filePath | FilePath | required; no default | A relative path from the root to a JavaScript entrypoint. It must satisfy:<br><br>    - Must contain one or more non-empty segments separated by `/`.<br>    - Each segment must only contain the following ASCII characters: a-z, A-Z, 0-9 and -_..<br>    - Must have a maximum length of 100. |
| script_type | scriptType | ScriptType | required; no default | Defines HTML "type" attribute to be used for the script entrypoint. The supported<br>    values are `DEFAULT` and `MODULE`, where `DEFAULT` maps to "text/javascript" and<br>    `MODULE` maps to "module". |

```python
class ScriptEntrypoint(core.ModelBase):
    """A script entrypoint to be loaded into the runtime environment."""

    file_path: FilePath = pydantic.Field(alias=str("filePath"))  # type: ignore[literal-required]
    """
    A relative path from the root to a JavaScript entrypoint. It must satisfy:

    - Must contain one or more non-empty segments separated by `/`.
    - Each segment must only contain the following ASCII characters: a-z, A-Z, 0-9 and -_..
    - Must have a maximum length of 100.
    """

    script_type: ScriptType = pydantic.Field(alias=str("scriptType"))  # type: ignore[literal-required]
    """
    Defines HTML "type" attribute to be used for the script entrypoint. The supported
    values are `DEFAULT` and `MODULE`, where `DEFAULT` maps to "text/javascript" and
    `MODULE` maps to "module".
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.widgets.models.FilePath](FilePath.md)
- [foundry_sdk.v2.widgets.models.ScriptType](ScriptType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ScriptEntrypoint.md)
