# Live deployment operations

These records describe the `live_deployment` commands in `pal-found-models`. Each record gives inputs, behavior, results, and examples.

### live_deployment.transform_json

- **Purpose and behavior:** Performs inference on the live deployment.
- **CLI inputs:** positionals `live_deployment_rid`; required `--input-json`.
- **Input meaning:** `--input-json`: JSON object matching the deployment model API inputs. `live_deployment_rid`: Resource identifier (RID) of the named Foundry resource.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The live deployment is available and accepts input matching its model API.
- **Result:** Returns the deployment transform result for the supplied JSON input; this invokes live inference.
- **Failure:** Unknown deployment, input incompatible with its model API, or denied inference returns a structured error. A timeout leaves the response unknown.
- **Example:** `pal-found-models live-deployment transform-json <LIVE_DEPLOYMENT_RID> --input-json '{"input_df":[{"feature_1":1.0,"feature_2":2}]}'`
