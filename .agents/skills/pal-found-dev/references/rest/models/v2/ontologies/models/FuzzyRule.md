# foundry_sdk.v2.ontologies.models.FuzzyRule


Matches intervals containing terms that are similar to the provided term, within an edit distance
defined by fuzziness. An edit is a single character change needed to make a term match, including
character insertion, deletion, substitution, or transposition of two adjacent characters.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| term | term | str | required; no default | The term to match. |
| fuzziness | fuzziness | typing.Optional[int] | None | Maximum edit distance allowed for matching. Valid values are 0, 1, or 2. Defaults to 2. |
| type | type | typing.Literal['fuzzy'] | 'fuzzy' | No additional field description in SDK source. |

```python
class FuzzyRule(core.ModelBase):
    """
    Matches intervals containing terms that are similar to the provided term, within an edit distance
    defined by fuzziness. An edit is a single character change needed to make a term match, including
    character insertion, deletion, substitution, or transposition of two adjacent characters.
    """

    term: str
    """The term to match."""

    fuzziness: typing.Optional[int] = None
    """Maximum edit distance allowed for matching. Valid values are 0, 1, or 2. Defaults to 2."""

    type: typing.Literal["fuzzy"] = "fuzzy"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FuzzyRule.md)
