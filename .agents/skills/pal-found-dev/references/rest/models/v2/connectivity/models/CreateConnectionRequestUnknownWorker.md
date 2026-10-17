# foundry_sdk.v2.connectivity.models.CreateConnectionRequestUnknownWorker


This create-union arm contains only `type='unknownWorker'`. It supplies no host, credential or egress configuration and cannot describe a legacy agent worker. The frozen SDK does not specify server acceptance or behavior for authoring an unknown worker. Use the supported Foundry-worker arm for a new configured worker.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| type | type | typing.Literal['unknownWorker'] | 'unknownWorker' | No additional field description in SDK source. |

```python
class CreateConnectionRequestUnknownWorker(core.ModelBase):
    """CreateConnectionRequestUnknownWorker"""

    type: typing.Literal["unknownWorker"] = "unknownWorker"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateConnectionRequestUnknownWorker.md)
