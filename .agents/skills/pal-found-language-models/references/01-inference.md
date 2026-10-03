# Inference operations

This part documents the `anthropic_model` (1) and `open_ai_model` (1) resource
clients (2 operations).

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/language_models/scripts/pal_found_language_models_cli.py`;
SDK `foundry_sdk/v2/language_models/{anthropic_model,open_ai_model}.py` at
pinned commit `2da67907`. Reviewer architect (CODEREVIEW-049), 2026-10-03. QA
baseline TESTCASE-012.

## Operation records

### anthropic_model.messages

- **Class**: execute (inference). Sends a message prompt to an Anthropic model.
- **Preconditions**: a model configured for the tenant.
- **Effect**: returns the model's completion; consumes inference usage.
- **Inputs**: `--messages-json`, `--tools-json`, `--model-rid`, and inference
  options.
- **Success**: the model's message/response.
- **Failure**: exit 5 on timeout (do not assume completion); exit 3 permission.
- **Example**: `pal-found-language-models anthropic-model messages --model-rid <MODEL_RID> --messages-json '{"messages":[]}'`.

### open_ai_model.embeddings

- **Class**: execute (inference). Computes embeddings for input text.
- **Preconditions**: an embeddings model configured.
- **Effect**: returns embedding vectors for the input; consumes usage.
- **Inputs**: `--input-json`, `--model-rid`.
- **Success**: the embedding result.
- **Failure**: exit 1 invalid input; exit 5 timeout.

## Evidence and review

Both operations run inference and consume model usage (AC-D-013-09). Reviewed
against the installed `pal-found-language-models` parser and pinned SDK
sources (commit `2da67907`). A timeout means the CLI did not get a conclusive
response; the model may still have processed the request. No unsupported
operation is documented as callable.
