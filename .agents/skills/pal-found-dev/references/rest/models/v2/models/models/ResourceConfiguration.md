# foundry_sdk.v2.models.models.ResourceConfiguration


Compute resource configuration for training runs.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| memory | memory | str | required; no default | Memory allocation (e.g., "4G"). |
| cpu | cpu | str | required; no default | CPU allocation (e.g., "2"). |
| gpu | gpu | typing.Optional[GpuType] | None | GPU allocation (must be available in the project's resource queue). |

```python
class ResourceConfiguration(core.ModelBase):
    """Compute resource configuration for training runs."""

    memory: str
    """Memory allocation (e.g., "4G")."""

    cpu: str
    """CPU allocation (e.g., "2")."""

    gpu: typing.Optional[GpuType] = None
    """GPU allocation (must be available in the project's resource queue)."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.GpuType](GpuType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ResourceConfiguration.md)
