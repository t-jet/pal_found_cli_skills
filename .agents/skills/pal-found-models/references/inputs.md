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

`live-deployment transform-json --input-json` is a JSON object whose keys and
value shapes follow the live deployment's model API. Experiment table and
series Parquet commands save streamed data through `--output`.
