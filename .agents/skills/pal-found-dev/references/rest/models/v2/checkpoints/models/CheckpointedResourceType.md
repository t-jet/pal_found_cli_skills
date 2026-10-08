# foundry_sdk.v2.checkpoints.models.CheckpointedResourceType


Type of resource that was captured.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
CheckpointedResourceType: typing_extensions.TypeAlias = typing.Literal[
    "CONTOUR_ANALYSIS",
    "CONTOUR_SOURCE_DATASET",
    "DATA_CONNECTION_SYNC",
    "DATA_CONNECTION_SOURCE",
    "DATA_CONNECTION_SYNC_TARGET_DATASET",
    "HUBBLE_OBJECT_TYPE",
    "EXPORTED_RESOURCE",
    "IMPORTED_RESOURCE",
    "REPORT",
    "CIPHER_CHANNEL",
    "CIPHER_LICENSE",
    "PARENT_RESOURCE",
    "ATTACHMENT",
    "SLATE_APPLICATION",
    "NOTEPAD",
    "DATASET",
    "MEDIA_SET",
    "CODE_REPOSITORY",
    "CODE_WORKBOOK",
    "CODE_WORKSPACE",
    "TELEMETRY_CONTAINER",
    "REFERENCED_RESOURCE",
    "ROLE_GRANT_RESOURCE",
    "PROJECT",
    "STORE",
    "THIRD_PARTY_APPLICATION",
    "BUILDER_PIPELINE",
    "MODEL",
    "MODEL_VERSION",
    "AGENT",
    "WORKSHOP_MODULE",
    "WALKTHROUGH",
    "FLOW_CAPTURE",
    "PEERING_CONNECTION",
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CheckpointedResourceType.md)
