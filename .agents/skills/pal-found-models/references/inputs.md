# Model identifiers and JSON inputs

Model, model version, experiment, Model Studio, and deployment arguments are
resource RIDs; artifact table and series arguments are names within an
experiment. `model create` and `model-studio create` need a resource name and
the RID of an existing parent folder. `model promote-version` takes the target
model RID and `--source-model-version-rid`; the copied version receives a new
RID on the target model.

`model-version create` requires model API, model files, backing repositories,
and Conda requirements. `--model-api-json` describes `inputs` and `outputs`
with their types. `--model-files-json` names the serialization form and
artifact data. The two list flags are JSON arrays. These values must match
the model adapter and files being registered; the SDK example illustrates
syntax, not a deployable model by itself.

`model-studio-config-version create` needs a trainer ID, compute resource
configuration, and worker configuration. The worker object has `inputs` and
`outputs` maps keyed by aliases, plus optional `customConfig` matching the
trainer's schema. Discover trainer IDs with `model-studio-trainer list` and
inspect the trainer before constructing a configuration. `model-studio launch`
uses the latest configuration version and returns a run; inspect runs to
check completion.

## Model Studio worker configuration

`TrainerId` is a resource RID. List trainers, then get the chosen returned
`trainerId`; use `--version` to inspect a specific advertised version. Read
`inputs` and `outputs` to identify required aliases, column specification IDs,
and restrictions. Read `customConfigSchema` for the JSON Schema governing
`customConfig`. These three trainer fields are typed as `Any` in SDK 1.101.0:
there is no universal nested trainer specification schema to assume locally.
Use the actual trainer response; if it does not explain a required binding,
obtain that trainer's contract from its owner before launching.

SDK 1.101.0 worker inputs support dataset bindings only:

```json
{"type":"dataset","rid":"<DATASET_RID>","columnMapping":{"<COLUMN_SPEC_ID>":["<COLUMN_NAME>"]},"ignoreColumns":[],"selectColumns":[]}
```

`columnMapping` maps trainer column specification IDs to lists of dataset column
names. `ignoreColumns` excludes columns; empty `selectColumns` selects all
columns not ignored. Supply all required keys, even when an allowed list/map is
empty. Confirm selected columns and types against the dataset schema and trainer
requirements. Worker outputs support model bindings only:
`{"type":"model","modelRid":"<OUTPUT_MODEL_RID>"}`. The output model must
already exist and be writable; configuration validation can reject missing
outputs or outputs in a different project.

Assemble `{"inputs":{"<INPUT_ALIAS>":<DATASET_BINDING>},"outputs":{"<OUTPUT_ALIAS>":<MODEL_BINDING>},"customConfig":{}}`
using the trainer's exact aliases. Replace the schematic binding markers with
the objects above, and replace or omit `customConfig` according to its schema.
Empty maps in the operation example only illustrate syntax; they are usable
only when the chosen trainer permits them. No trainer-specific aliases, column
IDs, or hyperparameters are fixed by this skill.

`--resources-json` requires string `memory` and `cpu`, with optional `gpu`.
Allocation is subject to the project resource queue. A valid configuration
response is not proof that capacity is available or training has completed.
Read [runs](./model-studio-run.md) for bounded completion checks and outputs.

## Experiment filters

Read [search JSON](./experiment.md#search-json) for all supported discriminators,
fields, operators, recursive shapes, and ordering. JSON flag values use camelCase
SDK request aliases; response prose uses the CLI's SDK field aliases.

`live-deployment transform-json --input-json` is a JSON object whose keys and
value shapes follow the live deployment's model API. Experiment table and
series Parquet commands save streamed data through `--output`.
