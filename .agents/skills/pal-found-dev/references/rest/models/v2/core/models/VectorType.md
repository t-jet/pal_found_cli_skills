# foundry_sdk.v2.core.models.VectorType


Represents a fixed size vector of floats. These can be used for vector similarity searches.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| dimension | dimension | int | required; no default | The dimension of the vector. |
| supports_search_with | supportsSearchWith | typing.List[VectorSimilarityFunction] | required; no default | No additional field description in SDK source. |
| embedding_model | embeddingModel | typing.Optional[EmbeddingModel] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['vector'] | 'vector' | No additional field description in SDK source. |

```python
class VectorType(core.ModelBase):
    """Represents a fixed size vector of floats. These can be used for vector similarity searches."""

    dimension: int
    """The dimension of the vector."""

    supports_search_with: typing.List[VectorSimilarityFunction] = pydantic.Field(alias=str("supportsSearchWith"))  # type: ignore[literal-required]
    embedding_model: typing.Optional[EmbeddingModel] = pydantic.Field(alias=str("embeddingModel"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["vector"] = "vector"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.EmbeddingModel](EmbeddingModel.md)
- [foundry_sdk.v2.core.models.VectorSimilarityFunction](VectorSimilarityFunction.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](VectorType.md)
