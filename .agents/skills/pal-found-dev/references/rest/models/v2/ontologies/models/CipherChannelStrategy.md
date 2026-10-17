# foundry_sdk.v2.ontologies.models.CipherChannelStrategy



Controls which Cipher Channel is used when encrypting a value. If not specified, defaults to `PREFER_EXISTING`.

- `PREFER_EXISTING`: use the Cipher Channel parsed from the existing ciphertext value; fall back to the default channel configured in ontology metadata.
- `PREFER_DEFAULT`: use the default channel configured in ontology metadata; fall back to the channel parsed from the existing ciphertext value.
- `EXISTING_ONLY`: use the channel parsed from the existing ciphertext value only; error if the value is not already encrypted.
- `DEFAULT_ONLY`: use the default channel configured in ontology metadata only; error if none is configured.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
CipherChannelStrategy: typing_extensions.TypeAlias = typing.Literal[
    "PREFER_EXISTING", "PREFER_DEFAULT", "EXISTING_ONLY", "DEFAULT_ONLY"
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CipherChannelStrategy.md)
