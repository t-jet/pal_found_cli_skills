# foundry_sdk.v2.models.models.LiveDeploymentState



The operational state of a live deployment.

| Value | Description |
| --- | --- |
| ACTIVE | The deployment is active. It may have zero replicas due to autoscaling and still not be ready. |
| STARTING | The deployment is starting up. |
| DEGRADED | At least one replica is ready, but not all replicas are healthy. |
| DISABLED | The deployment is disabled. |
| FAILED | The deployment has failed. No healthy replicas are available. |


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
LiveDeploymentState: typing_extensions.TypeAlias = typing.Literal[
    "ACTIVE", "STARTING", "DEGRADED", "DISABLED", "FAILED"
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LiveDeploymentState.md)
