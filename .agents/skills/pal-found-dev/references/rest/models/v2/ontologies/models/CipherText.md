# foundry_sdk.v2.ontologies.models.CipherText


An encrypted Cipher value is a string envelope in the form `CIPHER::{cipherChannelRid}::<ciphertext>::CIPHER`. Preserve the whole envelope and its channel RID; do not treat the ciphertext segment as a plaintext property value.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
CipherText: typing_extensions.TypeAlias = str
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CipherText.md)
