# CipherTextProperty operations

[REST development](../../../rest-api.md) | [Ontology service](index.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

Ciphertext properties use configured Cipher Channels. Encrypt/decrypt endpoints perform protected operations; channel selection and caller grants determine whether a value can be used.

## Prerequisites

Use the frozen Foundry Python SDK 1.101.0 and an authorized Ontology, branch, resource identifier, acting identity and exact type/parameter names from the enrollment. Prepare the linked local models before a live request. Synthetic examples run offline with the prepared SDK and mock transport; real reads or writes require enrollment access, resource permissions and any listed beta enablement. An administrator or resource owner supplies missing grants and capability access.

## Procedure and operation choices

Select the operation below, read its exact request/response/error model, then adapt the linked SDK fixture with authorized resource values. The fixture uses synthetic identifiers and checks serialized transport; it does not assert tenant behavior. Record branch, version, page/snapshot context, response and named errors for the actual call.

### `CipherTextProperty.decrypt`

Stage: Stable. Required SDK arguments: `ontology`, `object_type`, `primary_key`, `property`.

Decrypt the value of a ciphertext property.

Read [exact contract](../../contracts/v2/ontologies/CipherTextProperty/decrypt.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/CipherTextProperty/invoke_decrypt.py): `python -B examples/rest/083/v2/ontologies/CipherTextProperty/invoke_decrypt.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `CipherTextProperty.encrypt`

Stage: Private Beta. Required SDK arguments: `ontology`, `object_type`, `primary_key`, `property`, `plaintext`.

Encrypt a plaintext value into a CipherText value for the given object's CipherText property. The Cipher Channel used is resolved based on the supplied `cipherChannelStrategy`, using the channel of the object's existing ciphertext value and/or the default channel configured for the property in ontology metadata.

Read [exact contract](../../contracts/v2/ontologies/CipherTextProperty/encrypt.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/CipherTextProperty/invoke_encrypt.py): `python -B examples/rest/083/v2/ontologies/CipherTextProperty/invoke_encrypt.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

### `CipherTextProperty.encrypt_with_default_channel`

Stage: Private Beta. Required SDK arguments: `ontology`, `object_type`, `property`, `plaintext`.

Encrypt a plaintext value into a CipherText value for the given object type property. The Cipher Channel used is the default channel configured for the property in ontology metadata. This endpoint requires the CipherText property to have a configured `defaultCipherChannelRid`; if none is configured an error will be thrown. To encrypt against the channel of an existing object's value, use the **Encrypt** endpoint that accepts a `primaryKey` instead.

Read [exact contract](../../contracts/v2/ontologies/CipherTextProperty/encrypt_with_default_channel.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/083/v2/ontologies/CipherTextProperty/invoke_encrypt_with_default_channel.py): `python -B examples/rest/083/v2/ontologies/CipherTextProperty/invoke_encrypt_with_default_channel.py` from skill root. Named failure in source text: none listed; handle transport and generic API failures.

## Worked example

Use an approved test object/property. Encrypt a synthetic secret through its selected or default channel, store only the resulting ciphertext in the intended authorized path, then decrypt under a permitted identity. Do not print plaintext or tokens into logs.

The linked operation fixtures show actual SDK method invocation, serialized request and decoded response/error using a local mock transport. Their synthetic values are test data. Replace them with authorized identifiers and typed payloads from each linked contract; verify the live result under the intended identity before asserting a platform effect.

## Expected result and checks

Record exact operation ID, API version, release stage, branch, requested IDs, returned IDs, page/snapshot token, response mode and decoded result. For effectful calls, inspect validation/commit state and fresh target data; a successful HTTP response alone may not establish the business result. For lists, finish pagination before claiming completeness.

## Failures and recovery

On a missing or filtered result, verify Ontology/type/API names, branch and effective caller permissions. On schema rejection, compare payload fields, requiredness, aliases and discriminator values with the linked models. On a timeout after an effectful call, reconcile target or transaction state before retrying. Bound pages, streamed bytes and time windows; close streaming/raw responses according to [client lifetimes](../../client-behavior.md). Missing beta enablement is a prerequisite to resolve with the enrollment owner.
