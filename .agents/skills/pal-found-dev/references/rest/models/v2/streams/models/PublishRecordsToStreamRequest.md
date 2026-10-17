# foundry_sdk.v2.streams.models.PublishRecordsToStreamRequest


PublishRecordsToStreamRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| records | records | typing.List[Record] | required; no default | The records to publish to the stream |
| view_rid | viewRid | typing.Optional[ViewRid] | default None | If provided, this endpoint will only write to the stream corresponding to the specified view RID. If<br>    not provided, this endpoint will write to the latest stream on the branch.<br><br>    Providing this value is an advanced configuration, to be used when additional control over the<br>    underlying streaming data structures is needed. |

```python
class PublishRecordsToStreamRequest(core.ModelBase):
    """PublishRecordsToStreamRequest"""

    records: typing.List[Record]
    """The records to publish to the stream"""

    view_rid: typing.Optional[ViewRid] = pydantic.Field(alias=str("viewRid"), default=None)  # type: ignore[literal-required]
    """
    If provided, this endpoint will only write to the stream corresponding to the specified view RID. If
    not provided, this endpoint will write to the latest stream on the branch.

    Providing this value is an advanced configuration, to be used when additional control over the
    underlying streaming data structures is needed.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.streams.models.Record](Record.md)
- [foundry_sdk.v2.streams.models.ViewRid](ViewRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PublishRecordsToStreamRequest.md)
