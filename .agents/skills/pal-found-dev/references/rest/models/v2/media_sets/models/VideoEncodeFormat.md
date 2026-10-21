# foundry_sdk.v2.media_sets.models.VideoEncodeFormat


The output format for encoding video.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
VideoEncodeFormat: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "Mp4VideoContainerFormat",
        "MovVideoContainerFormat",
        "MkvVideoContainerFormat",
        "TsVideoContainerFormat",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.media_sets.models.MkvVideoContainerFormat](MkvVideoContainerFormat.md)
- [foundry_sdk.v2.media_sets.models.MovVideoContainerFormat](MovVideoContainerFormat.md)
- [foundry_sdk.v2.media_sets.models.Mp4VideoContainerFormat](Mp4VideoContainerFormat.md)
- [foundry_sdk.v2.media_sets.models.TsVideoContainerFormat](TsVideoContainerFormat.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](VideoEncodeFormat.md)
