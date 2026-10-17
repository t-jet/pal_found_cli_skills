# v2.language_models.AnthropicModel.messages


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning



## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.language_models.AnthropicModel.messages`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def messages(self, anthropic_model_model_id: language_models_models.LanguageModelApiName, *, max_tokens: int, messages: typing.List[language_models_models.AnthropicMessage], attribution: typing.Optional[core_models.Attribution]=None, output_config: typing.Optional[language_models_models.AnthropicOutputConfig]=None, preview: typing.Optional[core_models.PreviewMode]=None, stop_sequences: typing.Optional[typing.List[str]]=None, system: typing.Optional[typing.List[language_models_models.AnthropicSystemMessage]]=None, temperature: typing.Optional[float]=None, thinking: typing.Optional[language_models_models.AnthropicThinkingConfig]=None, tool_choice: typing.Optional[language_models_models.AnthropicToolChoice]=None, tools: typing.Optional[typing.List[language_models_models.AnthropicTool]]=None, top_k: typing.Optional[int]=None, top_p: typing.Optional[float]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> language_models_models.AnthropicMessagesResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| anthropic_model_model_id | language_models_models.LanguageModelApiName | required | Value shape and constraints are in its referenced local type definition. |
| max_tokens | int | required | The maximum number of tokens to generate before stopping. |
| messages | typing.List[language_models_models.AnthropicMessage] | required | Input messages to the model. This can include a single user-role message or multiple messages with alternating user and assistant roles. |
| attribution | typing.Optional[core_models.Attribution] | None | Value shape and constraints are in its referenced local type definition. |
| output_config | typing.Optional[language_models_models.AnthropicOutputConfig] | None | Configuration to control the shape of the model's output |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| stop_sequences | typing.Optional[typing.List[str]] | None | Custom text sequences that will cause the model to stop generating. |
| system | typing.Optional[typing.List[language_models_models.AnthropicSystemMessage]] | None | A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. As of now, sending multiple system prompts is not supported. |
| temperature | typing.Optional[float] | None | Amount of randomness injected into the response. Ranges from 0.0 to 1.0. Note that even with temperature of 0.0, the results will not be fully deterministic. Defaults to 1.0 |
| thinking | typing.Optional[language_models_models.AnthropicThinkingConfig] | None | Configuration for enabling Claude's extended thinking. |
| tool_choice | typing.Optional[language_models_models.AnthropicToolChoice] | None | How the model should use the provided tools. |
| tools | typing.Optional[typing.List[language_models_models.AnthropicTool]] | None | Definitions of tools that the model may use. |
| top_k | typing.Optional[int] | None | Only sample from the top K options for each subsequent token. |
| top_p | typing.Optional[float] | None | Use nucleus sampling. You should either alter temperature or top_p, but not both |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| AnthropicMessagesPermissionDenied | Could not messages the AnthropicModel. |
| MultipleSystemPromptsNotSupported | Multiple system prompts are not currently supported, but will be in the future. |
| MultipleToolResultContentsNotSupported | Multiple tool result contents are not currently supported, but will be in the future. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/languageModels/anthropic/{anthropicModelModelId}/messages'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'anthropicModelModelId': anthropic_model_model_id}
```

**header_params**

```python
{'attribution': attribution, 'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
language_models_models.AnthropicMessagesRequest(messages=messages, max_tokens=max_tokens, stop_sequences=stop_sequences, system=system, temperature=temperature, thinking=thinking, tool_choice=tool_choice, tools=tools, top_k=top_k, top_p=top_p, output_config=output_config)
```

**response_type**

```python
language_models_models.AnthropicMessagesResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'AnthropicMessagesPermissionDenied': language_models_errors.AnthropicMessagesPermissionDenied, 'MultipleSystemPromptsNotSupported': language_models_errors.MultipleSystemPromptsNotSupported, 'MultipleToolResultContentsNotSupported': language_models_errors.MultipleToolResultContentsNotSupported}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `language_models_models.AnthropicMessagesResponse`. Ordinary async return: `typing.Awaitable[language_models_models.AnthropicMessagesResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | language_models_models.AnthropicMessagesResponse |
| sync_raw | ApiResponse[language_models_models.AnthropicMessagesResponse] |
| sync_streaming | StreamingContextManager[language_models_models.AnthropicMessagesResponse] |
| async_ordinary | typing.Awaitable[language_models_models.AnthropicMessagesResponse] |
| async_raw | Awaitable[AsyncApiResponse[language_models_models.AnthropicMessagesResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[language_models_models.AnthropicMessagesResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.Attribution](../../../../models/v2/core/models/Attribution.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.language_models.errors.AnthropicMessagesPermissionDenied](../../../../models/v2/language_models/errors/AnthropicMessagesPermissionDenied.md)
- [foundry_sdk.v2.language_models.errors.AnthropicMessagesPermissionDeniedParameters](../../../../models/v2/language_models/errors/AnthropicMessagesPermissionDeniedParameters.md)
- [foundry_sdk.v2.language_models.errors.MultipleSystemPromptsNotSupported](../../../../models/v2/language_models/errors/MultipleSystemPromptsNotSupported.md)
- [foundry_sdk.v2.language_models.errors.MultipleSystemPromptsNotSupportedParameters](../../../../models/v2/language_models/errors/MultipleSystemPromptsNotSupportedParameters.md)
- [foundry_sdk.v2.language_models.errors.MultipleToolResultContentsNotSupported](../../../../models/v2/language_models/errors/MultipleToolResultContentsNotSupported.md)
- [foundry_sdk.v2.language_models.errors.MultipleToolResultContentsNotSupportedParameters](../../../../models/v2/language_models/errors/MultipleToolResultContentsNotSupportedParameters.md)
- [foundry_sdk.v2.language_models.models.AnthropicAnyToolChoice](../../../../models/v2/language_models/models/AnthropicAnyToolChoice.md)
- [foundry_sdk.v2.language_models.models.AnthropicAutoToolChoice](../../../../models/v2/language_models/models/AnthropicAutoToolChoice.md)
- [foundry_sdk.v2.language_models.models.AnthropicBase64PdfDocumentSource](../../../../models/v2/language_models/models/AnthropicBase64PdfDocumentSource.md)
- [foundry_sdk.v2.language_models.models.AnthropicCacheControl](../../../../models/v2/language_models/models/AnthropicCacheControl.md)
- [foundry_sdk.v2.language_models.models.AnthropicCharacterLocationCitation](../../../../models/v2/language_models/models/AnthropicCharacterLocationCitation.md)
- [foundry_sdk.v2.language_models.models.AnthropicCompletionCitation](../../../../models/v2/language_models/models/AnthropicCompletionCitation.md)
- [foundry_sdk.v2.language_models.models.AnthropicCompletionContent](../../../../models/v2/language_models/models/AnthropicCompletionContent.md)
- [foundry_sdk.v2.language_models.models.AnthropicCompletionRedactedThinking](../../../../models/v2/language_models/models/AnthropicCompletionRedactedThinking.md)
- [foundry_sdk.v2.language_models.models.AnthropicCompletionText](../../../../models/v2/language_models/models/AnthropicCompletionText.md)
- [foundry_sdk.v2.language_models.models.AnthropicCompletionThinking](../../../../models/v2/language_models/models/AnthropicCompletionThinking.md)
- [foundry_sdk.v2.language_models.models.AnthropicCompletionToolUse](../../../../models/v2/language_models/models/AnthropicCompletionToolUse.md)
- [foundry_sdk.v2.language_models.models.AnthropicCustomTool](../../../../models/v2/language_models/models/AnthropicCustomTool.md)
- [foundry_sdk.v2.language_models.models.AnthropicDisableParallelToolUse](../../../../models/v2/language_models/models/AnthropicDisableParallelToolUse.md)
- [foundry_sdk.v2.language_models.models.AnthropicDisabledThinking](../../../../models/v2/language_models/models/AnthropicDisabledThinking.md)
- [foundry_sdk.v2.language_models.models.AnthropicDocument](../../../../models/v2/language_models/models/AnthropicDocument.md)
- [foundry_sdk.v2.language_models.models.AnthropicDocumentCitations](../../../../models/v2/language_models/models/AnthropicDocumentCitations.md)
- [foundry_sdk.v2.language_models.models.AnthropicDocumentSource](../../../../models/v2/language_models/models/AnthropicDocumentSource.md)
- [foundry_sdk.v2.language_models.models.AnthropicEffort](../../../../models/v2/language_models/models/AnthropicEffort.md)
- [foundry_sdk.v2.language_models.models.AnthropicEnabledThinking](../../../../models/v2/language_models/models/AnthropicEnabledThinking.md)
- [foundry_sdk.v2.language_models.models.AnthropicEphemeralCacheControl](../../../../models/v2/language_models/models/AnthropicEphemeralCacheControl.md)
- [foundry_sdk.v2.language_models.models.AnthropicImage](../../../../models/v2/language_models/models/AnthropicImage.md)
- [foundry_sdk.v2.language_models.models.AnthropicImageBase64Source](../../../../models/v2/language_models/models/AnthropicImageBase64Source.md)
- [foundry_sdk.v2.language_models.models.AnthropicImageSource](../../../../models/v2/language_models/models/AnthropicImageSource.md)
- [foundry_sdk.v2.language_models.models.AnthropicJsonSchemaOutputFormat](../../../../models/v2/language_models/models/AnthropicJsonSchemaOutputFormat.md)
- [foundry_sdk.v2.language_models.models.AnthropicMediaType](../../../../models/v2/language_models/models/AnthropicMediaType.md)
- [foundry_sdk.v2.language_models.models.AnthropicMessage](../../../../models/v2/language_models/models/AnthropicMessage.md)
- [foundry_sdk.v2.language_models.models.AnthropicMessageContent](../../../../models/v2/language_models/models/AnthropicMessageContent.md)
- [foundry_sdk.v2.language_models.models.AnthropicMessageRole](../../../../models/v2/language_models/models/AnthropicMessageRole.md)
- [foundry_sdk.v2.language_models.models.AnthropicMessagesRequest](../../../../models/v2/language_models/models/AnthropicMessagesRequest.md)
- [foundry_sdk.v2.language_models.models.AnthropicMessagesResponse](../../../../models/v2/language_models/models/AnthropicMessagesResponse.md)
- [foundry_sdk.v2.language_models.models.AnthropicNoneToolChoice](../../../../models/v2/language_models/models/AnthropicNoneToolChoice.md)
- [foundry_sdk.v2.language_models.models.AnthropicOutputConfig](../../../../models/v2/language_models/models/AnthropicOutputConfig.md)
- [foundry_sdk.v2.language_models.models.AnthropicOutputFormat](../../../../models/v2/language_models/models/AnthropicOutputFormat.md)
- [foundry_sdk.v2.language_models.models.AnthropicRedactedThinking](../../../../models/v2/language_models/models/AnthropicRedactedThinking.md)
- [foundry_sdk.v2.language_models.models.AnthropicSystemMessage](../../../../models/v2/language_models/models/AnthropicSystemMessage.md)
- [foundry_sdk.v2.language_models.models.AnthropicText](../../../../models/v2/language_models/models/AnthropicText.md)
- [foundry_sdk.v2.language_models.models.AnthropicTextDocumentSource](../../../../models/v2/language_models/models/AnthropicTextDocumentSource.md)
- [foundry_sdk.v2.language_models.models.AnthropicThinking](../../../../models/v2/language_models/models/AnthropicThinking.md)
- [foundry_sdk.v2.language_models.models.AnthropicThinkingConfig](../../../../models/v2/language_models/models/AnthropicThinkingConfig.md)
- [foundry_sdk.v2.language_models.models.AnthropicTokenUsage](../../../../models/v2/language_models/models/AnthropicTokenUsage.md)
- [foundry_sdk.v2.language_models.models.AnthropicTool](../../../../models/v2/language_models/models/AnthropicTool.md)
- [foundry_sdk.v2.language_models.models.AnthropicToolChoice](../../../../models/v2/language_models/models/AnthropicToolChoice.md)
- [foundry_sdk.v2.language_models.models.AnthropicToolResult](../../../../models/v2/language_models/models/AnthropicToolResult.md)
- [foundry_sdk.v2.language_models.models.AnthropicToolResultContent](../../../../models/v2/language_models/models/AnthropicToolResultContent.md)
- [foundry_sdk.v2.language_models.models.AnthropicToolToolChoice](../../../../models/v2/language_models/models/AnthropicToolToolChoice.md)
- [foundry_sdk.v2.language_models.models.AnthropicToolUse](../../../../models/v2/language_models/models/AnthropicToolUse.md)
- [foundry_sdk.v2.language_models.models.JsonSchema](../../../../models/v2/language_models/models/JsonSchema.md)
- [foundry_sdk.v2.language_models.models.LanguageModelApiName](../../../../models/v2/language_models/models/LanguageModelApiName.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/language_models/AnthropicModel.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](messages.md)
