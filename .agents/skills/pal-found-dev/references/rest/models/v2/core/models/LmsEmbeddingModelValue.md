# foundry_sdk.v2.core.models.LmsEmbeddingModelValue


LmsEmbeddingModelValue

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
LmsEmbeddingModelValue: typing_extensions.TypeAlias = typing.Literal[
    "OPENAI_TEXT_EMBEDDING_ADA_002",
    "TEXT_EMBEDDING_3_LARGE",
    "TEXT_EMBEDDING_3_SMALL",
    "SNOWFLAKE_ARCTIC_EMBED_M",
    "INSTRUCTOR_LARGE",
    "BGE_BASE_EN_V1_5",
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LmsEmbeddingModelValue.md)
