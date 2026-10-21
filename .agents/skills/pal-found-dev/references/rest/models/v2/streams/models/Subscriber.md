# foundry_sdk.v2.streams.models.Subscriber


Subscriber

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| subscriber_id | subscriberId | SubscriberId | required; no default | No additional field description in SDK source. |
| read_position | readPosition | typing.Optional[ReadPosition] | default None | Where to start reading from. Defaults to `earliest` if not specified.<br><br>    The `readPosition` determines where the subscriber will start reading:<br>    - `earliest`: Start from the beginning of each partition (offset 0). Use this to process<br>      all historical data.<br>    - `latest`: Start from the current end of each partition. Use this to skip historical data<br>      and only process new records arriving after registration.<br>    - `specific`: Start from explicit offsets for each partition. Use this to resume from a<br>      known checkpoint. |
| dataset_rid | datasetRid | core_models.DatasetRid | required; no default | The RID of the dataset the subscriber is bound to. |
| branch_name | branchName | core_models.BranchName | required; no default | The branch of the stream the subscriber is bound to. |
| view_rid | viewRid | ViewRid | required; no default | The current view RID being read from. This may change over time if the stream's<br>    schema is migrated to a new view. |
| start_offsets | startOffsets | PartitionOffsets | required; no default | The offsets where reading began for each partition, based on the initial read position. |
| created_time | createdTime | core_models.CreatedTime | required; no default | Timestamp when the subscriber was registered. |

```python
class Subscriber(core.ModelBase):
    """Subscriber"""

    subscriber_id: SubscriberId = pydantic.Field(alias=str("subscriberId"))  # type: ignore[literal-required]
    read_position: typing.Optional[ReadPosition] = pydantic.Field(alias=str("readPosition"), default=None)  # type: ignore[literal-required]
    """
    Where to start reading from. Defaults to `earliest` if not specified.

    The `readPosition` determines where the subscriber will start reading:
    - `earliest`: Start from the beginning of each partition (offset 0). Use this to process
      all historical data.
    - `latest`: Start from the current end of each partition. Use this to skip historical data
      and only process new records arriving after registration.
    - `specific`: Start from explicit offsets for each partition. Use this to resume from a
      known checkpoint.
    """

    dataset_rid: core_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    """The RID of the dataset the subscriber is bound to."""

    branch_name: core_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    """The branch of the stream the subscriber is bound to."""

    view_rid: ViewRid = pydantic.Field(alias=str("viewRid"))  # type: ignore[literal-required]
    """
    The current view RID being read from. This may change over time if the stream's
    schema is migrated to a new view.
    """

    start_offsets: PartitionOffsets = pydantic.Field(alias=str("startOffsets"))  # type: ignore[literal-required]
    """The offsets where reading began for each partition, based on the initial read position."""

    created_time: core_models.CreatedTime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """Timestamp when the subscriber was registered."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../core/models/DatasetRid.md)
- [foundry_sdk.v2.streams.models.PartitionOffsets](PartitionOffsets.md)
- [foundry_sdk.v2.streams.models.ReadPosition](ReadPosition.md)
- [foundry_sdk.v2.streams.models.SubscriberId](SubscriberId.md)
- [foundry_sdk.v2.streams.models.ViewRid](ViewRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Subscriber.md)
