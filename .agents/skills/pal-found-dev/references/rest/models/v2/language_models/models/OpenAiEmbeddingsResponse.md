# foundry_sdk.v2.language_models.models.OpenAiEmbeddingsResponse


OpenAiEmbeddingsResponse

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| data | data | typing.List[typing.List[float]] | required; no default | List of embedding vectors |
| model | model | str | required; no default | The ID of the model used |
| usage | usage | OpenAiEmbeddingTokenUsage | required; no default | Usage statistics for the request |

```python
class OpenAiEmbeddingsResponse(core.ModelBase):
    """OpenAiEmbeddingsResponse"""

    data: typing.List[typing.List[float]]
    """List of embedding vectors"""

    model: str
    """The ID of the model used"""

    usage: OpenAiEmbeddingTokenUsage
    """Usage statistics for the request"""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.language_models.models.OpenAiEmbeddingTokenUsage](OpenAiEmbeddingTokenUsage.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OpenAiEmbeddingsResponse.md)
