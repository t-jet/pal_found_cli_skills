# foundry_sdk.v2.media_sets.models.PaletteInterpretation


The palette interpretation of a band.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
PaletteInterpretation: typing_extensions.TypeAlias = typing.Literal[
    "GRAY", "RGB", "RGBA", "CMYK", "HLS"
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PaletteInterpretation.md)
