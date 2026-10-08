# foundry_sdk.v2.ontologies.models.MatchRule


Matches intervals containing the terms in the query

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| query | query | str | required; no default | No additional field description in SDK source. |
| max_gaps | maxGaps | typing.Optional[int] | default None | The maximum gaps between matched terms in the interval. For example, in the text "quick brown fox",<br>    the terms "quick" and "fox" have a gap of one. If not set, then gaps are not considered. |
| ordered | ordered | bool | required; no default | If true, the matched terms must occur in order. |
| type | type | typing.Literal['match'] | 'match' | No additional field description in SDK source. |

```python
class MatchRule(core.ModelBase):
    """Matches intervals containing the terms in the query"""

    query: str
    max_gaps: typing.Optional[int] = pydantic.Field(alias=str("maxGaps"), default=None)  # type: ignore[literal-required]
    """
    The maximum gaps between matched terms in the interval. For example, in the text "quick brown fox",
    the terms "quick" and "fox" have a gap of one. If not set, then gaps are not considered.
    """

    ordered: bool
    """If true, the matched terms must occur in order."""

    type: typing.Literal["match"] = "match"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MatchRule.md)
