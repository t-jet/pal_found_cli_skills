# v2.language_models.OpenAiModel.embeddings


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning



## SDK invocation contract

```python
def embeddings(self, open_ai_model_model_id: language_models_models.LanguageModelApiName, *, input: language_models_models.OpenAiEmbeddingInput, attribution: typing.Optional[core_models.Attribution]=None, dimensions: typing.Optional[int]=None, encoding_format: typing.Optional[language_models_models.OpenAiEncodingFormat]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> language_models_models.OpenAiEmbeddingsResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| open_ai_model_model_id | language_models_models.LanguageModelApiName | required | Value shape and constraints are in its referenced local type definition. |
| input | language_models_models.OpenAiEmbeddingInput | required | Input text to embed, encoded as an array of strings. Each input must not exceed the max input tokens for the model (8192 tokens for all embedding models). |
| attribution | typing.Optional[core_models.Attribution] | None | Value shape and constraints are in its referenced local type definition. |
| dimensions | typing.Optional[int] | None | The number of dimensions the resulting output embeddings should have. Only supported in text-embedding-3 and later models. |
| encoding_format | typing.Optional[language_models_models.OpenAiEncodingFormat] | None | The format to return the embeddings in. Can be either float or base64. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| OpenAiEmbeddingsPermissionDenied | Could not embeddings the OpenAiModel. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/languageModels/openAi/{openAiModelModelId}/embeddings'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'openAiModelModelId': open_ai_model_model_id}
```

**header_params**

```python
{'attribution': attribution, 'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
language_models_models.OpenAiEmbeddingsRequest(input=input, dimensions=dimensions, encoding_format=encoding_format)
```

**response_type**

```python
language_models_models.OpenAiEmbeddingsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'OpenAiEmbeddingsPermissionDenied': language_models_errors.OpenAiEmbeddingsPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `language_models_models.OpenAiEmbeddingsResponse`. Ordinary async return: `typing.Awaitable[language_models_models.OpenAiEmbeddingsResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | language_models_models.OpenAiEmbeddingsResponse |
| sync_raw | ApiResponse[language_models_models.OpenAiEmbeddingsResponse] |
| sync_streaming | StreamingContextManager[language_models_models.OpenAiEmbeddingsResponse] |
| async_ordinary | typing.Awaitable[language_models_models.OpenAiEmbeddingsResponse] |
| async_raw | Awaitable[AsyncApiResponse[language_models_models.OpenAiEmbeddingsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[language_models_models.OpenAiEmbeddingsResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.Attribution](../../../../models/v2/core/models/Attribution.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.language_models.errors.OpenAiEmbeddingsPermissionDenied](../../../../models/v2/language_models/errors/OpenAiEmbeddingsPermissionDenied.md)
- [foundry_sdk.v2.language_models.errors.OpenAiEmbeddingsPermissionDeniedParameters](../../../../models/v2/language_models/errors/OpenAiEmbeddingsPermissionDeniedParameters.md)
- [foundry_sdk.v2.language_models.models.LanguageModelApiName](../../../../models/v2/language_models/models/LanguageModelApiName.md)
- [foundry_sdk.v2.language_models.models.OpenAiEmbeddingInput](../../../../models/v2/language_models/models/OpenAiEmbeddingInput.md)
- [foundry_sdk.v2.language_models.models.OpenAiEmbeddingTokenUsage](../../../../models/v2/language_models/models/OpenAiEmbeddingTokenUsage.md)
- [foundry_sdk.v2.language_models.models.OpenAiEmbeddingsRequest](../../../../models/v2/language_models/models/OpenAiEmbeddingsRequest.md)
- [foundry_sdk.v2.language_models.models.OpenAiEmbeddingsResponse](../../../../models/v2/language_models/models/OpenAiEmbeddingsResponse.md)
- [foundry_sdk.v2.language_models.models.OpenAiEncodingFormat](../../../../models/v2/language_models/models/OpenAiEncodingFormat.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/language_models/OpenAiModel.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](embeddings.md)
