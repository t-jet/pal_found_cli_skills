# foundry_sdk.v2.widgets.errors.InvalidManifestParameters


The provided manifest could not be parsed or is not well formed.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| reason | reason | str | TypedDict key required | No additional field description in SDK source. |
| value | value | typing_extensions.NotRequired[typing.Any] | TypedDict key may be omitted | No additional field description in SDK source. |

```python
class InvalidManifestParameters(typing_extensions.TypedDict):
    """The provided manifest could not be parsed or is not well formed."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    reason: str
    value: typing_extensions.NotRequired[typing.Any]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidManifestParameters.md)
