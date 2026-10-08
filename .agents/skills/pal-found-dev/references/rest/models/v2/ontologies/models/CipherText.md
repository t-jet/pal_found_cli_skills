# foundry_sdk.v2.ontologies.models.CipherText



A value encrypted with [Cipher](https://palantir.com/docs/foundry/cipher/overview/), stored in its envelope form which encodes
the Cipher Channel used to encrypt it (for example `CIPHER::{cipherChannelRid}::<ciphertext>::CIPHER`).


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
CipherText: typing_extensions.TypeAlias = str
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CipherText.md)
