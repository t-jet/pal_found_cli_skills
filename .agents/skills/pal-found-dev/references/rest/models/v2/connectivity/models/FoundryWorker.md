# foundry_sdk.v2.connectivity.models.FoundryWorker


The [Foundry worker](https://palantir.com/docs/foundry/data-connection/core-concepts/#foundry-worker) is used to run capabilities
in Foundry.
This is the preferred method for connections, as these connections benefit from Foundry's containerized
and scalable job execution, improved stability and do not incur the maintenance overhead associated with agents.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| network_egress_policy_rids | networkEgressPolicyRids | typing.List[core_models.NetworkEgressPolicyRid] | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['foundryWorker'] | 'foundryWorker' | No additional field description in SDK source. |

```python
class FoundryWorker(core.ModelBase):
    """
    The [Foundry worker](https://palantir.com/docs/foundry/data-connection/core-concepts/#foundry-worker) is used to run capabilities
    in Foundry.
    This is the preferred method for connections, as these connections benefit from Foundry's containerized
    and scalable job execution, improved stability and do not incur the maintenance overhead associated with agents.
    """

    network_egress_policy_rids: typing.List[core_models.NetworkEgressPolicyRid] = pydantic.Field(alias=str("networkEgressPolicyRids"))  # type: ignore[literal-required]
    type: typing.Literal["foundryWorker"] = "foundryWorker"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.NetworkEgressPolicyRid](../../core/models/NetworkEgressPolicyRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FoundryWorker.md)
