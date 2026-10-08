# foundry_sdk.v2.ontologies.models.NearestNeighborsQueryText


Automatically embed the text in a vector using the embedding model configured for the given propertyIdentifier.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| value | value | str | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['text'] | 'text' | No additional field description in SDK source. |

```python
class NearestNeighborsQueryText(core.ModelBase):
    """Automatically embed the text in a vector using the embedding model configured for the given propertyIdentifier."""

    value: str
    type: typing.Literal["text"] = "text"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NearestNeighborsQueryText.md)
