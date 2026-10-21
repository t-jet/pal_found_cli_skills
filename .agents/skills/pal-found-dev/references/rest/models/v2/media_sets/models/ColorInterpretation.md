# foundry_sdk.v2.media_sets.models.ColorInterpretation


The color interpretation of a band.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ColorInterpretation: typing_extensions.TypeAlias = typing.Literal[
    "UNDEFINED",
    "GRAY",
    "PALETTE_INDEX",
    "RED",
    "GREEN",
    "BLUE",
    "ALPHA",
    "HUE",
    "SATURATION",
    "LIGHTNESS",
    "CYAN",
    "MAGENTA",
    "YELLOW",
    "BLACK",
    "Y_CB_CR_SPACE_Y",
    "Y_CB_CR_SPACE_CB",
    "Y_CB_CR_SPACE_CR",
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ColorInterpretation.md)
