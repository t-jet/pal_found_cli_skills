# foundry_sdk.v2.models.models.ExperimentCodeWorkspaceSource


Experiment created from a code workspace.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| container_rid | containerRid | core.RID | required; no default | No additional field description in SDK source. |
| deployment_rid | deploymentRid | typing.Optional[core.RID] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['codeWorkspace'] | 'codeWorkspace' | No additional field description in SDK source. |

```python
class ExperimentCodeWorkspaceSource(core.ModelBase):
    """Experiment created from a code workspace."""

    container_rid: core.RID = pydantic.Field(alias=str("containerRid"))  # type: ignore[literal-required]
    deployment_rid: typing.Optional[core.RID] = pydantic.Field(alias=str("deploymentRid"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["codeWorkspace"] = "codeWorkspace"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ExperimentCodeWorkspaceSource.md)
