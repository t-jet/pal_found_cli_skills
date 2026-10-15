# Model studio trainer operations

These records describe the `model_studio_trainer` commands in `pal-found-models`. Each record gives inputs, behavior, results, and examples.

### model_studio_trainer.get

- **Purpose and behavior:** Gets details about a specific trainer by its ID and optional version.
- **CLI inputs:** positionals `model_studio_trainer_trainer_id`; optional `--version`.
- **Input meaning:** `model_studio_trainer_trainer_id`: Identifier of the trainer advertised by Model Studio. `--version`: Specific version of the trainer to retrieve. If omitted, returns the latest version.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The trainer ID identifies a trainer available to the caller.
- **Result:** Returns `ModelStudioTrainer` for the selected model studio trainer.
- **Failure:** Unknown trainer ID or denied access returns a structured error.
- **Example:** `pal-found-models model-studio-trainer get <MODEL_STUDIO_TRAINER_TRAINER_ID>`

### model_studio_trainer.list

- **Purpose and behavior:** Lists all available trainers for Model Studios.
- **CLI inputs:** None beyond shared CLI options.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can list available Model Studio trainers.
- **Result:** Returns `ListModelStudioTrainersResponse` with visible trainers in `data`. An empty `data` list means none are visible.
- **Failure:** Denied access returns a structured error; an empty list means no visible trainers.
- **Example:** `pal-found-models model-studio-trainer list`
