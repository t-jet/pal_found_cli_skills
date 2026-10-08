# v2.ontologies.CipherTextProperty.encrypt


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Encrypt a plaintext value into a CipherText value for the given object's CipherText property.

The Cipher Channel used is resolved based on the supplied `cipherChannelStrategy`, using the channel of the
object's existing ciphertext value and/or the default channel configured for the property in ontology metadata.

## SDK invocation contract

```python
def encrypt(self, ontology: ontologies_models.OntologyIdentifier, object_type: ontologies_models.ObjectTypeApiName, primary_key: ontologies_models.PropertyValueEscapedString, property: ontologies_models.PropertyApiName, *, plaintext: ontologies_models.Plaintext, branch: typing.Optional[core_models.FoundryBranch]=None, cipher_channel_strategy: typing.Optional[ontologies_models.CipherChannelStrategy]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.EncryptionResult: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| object_type | ontologies_models.ObjectTypeApiName | required | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**. |
| primary_key | ontologies_models.PropertyValueEscapedString | required | The primary key of the object with the CipherText property. |
| property | ontologies_models.PropertyApiName | required | The API name of the CipherText property. To find the API name for your CipherText property, check the **Ontology Manager** or use the **Get object type** endpoint. |
| plaintext | ontologies_models.Plaintext | required | Value shape and constraints are in its referenced local type definition. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to read from. If not specified, the default branch will be used. |
| cipher_channel_strategy | typing.Optional[ontologies_models.CipherChannelStrategy] | None | The strategy controlling which Cipher Channel is used to encrypt the value. If not specified, defaults to `PREFER_EXISTING`. |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

No named operation errors are listed in this method's docstring; transport and generic API failures remain possible.

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/ciphertexts/{property}/encrypt'
```

**query_params**

```python
{'branch': branch, 'cipherChannelStrategy': cipher_channel_strategy, 'preview': preview}
```

**path_params**

```python
{'ontology': ontology, 'objectType': object_type, 'primaryKey': primary_key, 'property': property}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
ontologies_models.EncryptionRequest(plaintext=plaintext)
```

**response_type**

```python
ontologies_models.EncryptionResult
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `ontologies_models.EncryptionResult`. Ordinary async return: `typing.Awaitable[ontologies_models.EncryptionResult]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.EncryptionResult |
| sync_raw | ApiResponse[ontologies_models.EncryptionResult] |
| sync_streaming | StreamingContextManager[ontologies_models.EncryptionResult] |
| async_ordinary | typing.Awaitable[ontologies_models.EncryptionResult] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.EncryptionResult]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.EncryptionResult]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../../../models/v2/core/models/FoundryBranch.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.ontologies.models.CipherChannelStrategy](../../../../models/v2/ontologies/models/CipherChannelStrategy.md)
- [foundry_sdk.v2.ontologies.models.CipherText](../../../../models/v2/ontologies/models/CipherText.md)
- [foundry_sdk.v2.ontologies.models.EncryptionRequest](../../../../models/v2/ontologies/models/EncryptionRequest.md)
- [foundry_sdk.v2.ontologies.models.EncryptionResult](../../../../models/v2/ontologies/models/EncryptionResult.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.Plaintext](../../../../models/v2/ontologies/models/Plaintext.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](../../../../models/v2/ontologies/models/PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyValueEscapedString](../../../../models/v2/ontologies/models/PropertyValueEscapedString.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/CipherTextProperty.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](encrypt.md)
