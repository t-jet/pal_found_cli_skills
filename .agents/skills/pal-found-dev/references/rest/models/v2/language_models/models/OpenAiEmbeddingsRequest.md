# foundry_sdk.v2.language_models.models.OpenAiEmbeddingsRequest


OpenAiEmbeddingsRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| input | input | OpenAiEmbeddingInput | required; no default | Input text to embed, encoded as an array of strings. Each input must not exceed the max input <br>    tokens for the model (8192 tokens for all embedding models). |
| dimensions | dimensions | typing.Optional[int] | None | The number of dimensions the resulting output embeddings should have. <br>    Only supported in text-embedding-3 and later models. |
| encoding_format | encodingFormat | typing.Optional[OpenAiEncodingFormat] | default None | The format to return the embeddings in. Can be either float or base64. |

```python
class OpenAiEmbeddingsRequest(core.ModelBase):
    """OpenAiEmbeddingsRequest"""

    input: OpenAiEmbeddingInput
    """
    Input text to embed, encoded as an array of strings. Each input must not exceed the max input 
    tokens for the model (8192 tokens for all embedding models).
    """

    dimensions: typing.Optional[int] = None
    """
    The number of dimensions the resulting output embeddings should have. 
    Only supported in text-embedding-3 and later models.
    """

    encoding_format: typing.Optional[OpenAiEncodingFormat] = pydantic.Field(alias=str("encodingFormat"), default=None)  # type: ignore[literal-required]
    """The format to return the embeddings in. Can be either float or base64."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.language_models.models.OpenAiEmbeddingInput](OpenAiEmbeddingInput.md)
- [foundry_sdk.v2.language_models.models.OpenAiEncodingFormat](OpenAiEncodingFormat.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OpenAiEmbeddingsRequest.md)
