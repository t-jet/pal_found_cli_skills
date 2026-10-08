# foundry_sdk.v2.admin.models.ClassificationBannerDisplayType


The display type of the classification banner. BANNER_LINE is the long classification string used in the header of a document; PORTION_MARKING is a short classification string used for individual paragraphs

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ClassificationBannerDisplayType: typing_extensions.TypeAlias = typing.Literal[
    "BANNER_LINE", "PORTION_MARKING"
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ClassificationBannerDisplayType.md)
