# foundry_sdk.v2.media_sets.models.ContrastBinarize


Binarize contrast operation.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| threshold | threshold | typing.Optional[int] | None | The threshold value (0-255). Pixels with intensity below this value become black,<br>    others become white. If not specified, the threshold is computed automatically. |
| type | type | typing.Literal['binarize'] | 'binarize' | No additional field description in SDK source. |

```python
class ContrastBinarize(core.ModelBase):
    """Binarize contrast operation."""

    threshold: typing.Optional[int] = None
    """
    The threshold value (0-255). Pixels with intensity below this value become black,
    others become white. If not specified, the threshold is computed automatically.
    """

    type: typing.Literal["binarize"] = "binarize"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ContrastBinarize.md)
