# v2.models resources and operations


Use Model metadata and version resources to choose a deployed or published artifact before invoking an inference operation. Experiment and live deployment results have distinct formats and lifecycle states; inspect the requested format and model availability before decoding the payload. Read the selected operation contract before invocation; stage, API version and result lifetime remain operation-specific.

| Operation | Stage |
| --- | --- |
| [v2.models.Experiment.get](../../contracts/v2/models/Experiment/get.md) | Public Beta |
| [v2.models.Experiment.search](../../contracts/v2/models/Experiment/search.md) | Public Beta |
| [v2.models.ExperimentArtifactTable.json](../../contracts/v2/models/ExperimentArtifactTable/json.md) | Public Beta |
| [v2.models.ExperimentArtifactTable.parquet](../../contracts/v2/models/ExperimentArtifactTable/parquet.md) | Public Beta |
| [v2.models.ExperimentSeries.json](../../contracts/v2/models/ExperimentSeries/json.md) | Public Beta |
| [v2.models.ExperimentSeries.parquet](../../contracts/v2/models/ExperimentSeries/parquet.md) | Public Beta |
| [v2.models.LiveDeployment.create](../../contracts/v2/models/LiveDeployment/create.md) | Public Beta |
| [v2.models.LiveDeployment.get](../../contracts/v2/models/LiveDeployment/get.md) | Public Beta |
| [v2.models.LiveDeployment.list](../../contracts/v2/models/LiveDeployment/list.md) | Public Beta |
| [v2.models.LiveDeployment.replace](../../contracts/v2/models/LiveDeployment/replace.md) | Public Beta |
| [v2.models.LiveDeployment.transform_json](../../contracts/v2/models/LiveDeployment/transform_json.md) | Public Beta |
| [v2.models.Model.create](../../contracts/v2/models/Model/create.md) | Public Beta |
| [v2.models.Model.get](../../contracts/v2/models/Model/get.md) | Public Beta |
| [v2.models.Model.promote_version](../../contracts/v2/models/Model/promote_version.md) | Public Beta |
| [v2.models.ModelFunction.create](../../contracts/v2/models/ModelFunction/create.md) | Public Beta |
| [v2.models.ModelFunction.get](../../contracts/v2/models/ModelFunction/get.md) | Public Beta |
| [v2.models.ModelFunction.replace](../../contracts/v2/models/ModelFunction/replace.md) | Public Beta |
| [v2.models.ModelStudio.create](../../contracts/v2/models/ModelStudio/create.md) | Public Beta |
| [v2.models.ModelStudio.get](../../contracts/v2/models/ModelStudio/get.md) | Public Beta |
| [v2.models.ModelStudio.launch](../../contracts/v2/models/ModelStudio/launch.md) | Public Beta |
| [v2.models.ModelStudioConfigVersion.create](../../contracts/v2/models/ModelStudioConfigVersion/create.md) | Public Beta |
| [v2.models.ModelStudioConfigVersion.get](../../contracts/v2/models/ModelStudioConfigVersion/get.md) | Public Beta |
| [v2.models.ModelStudioConfigVersion.latest](../../contracts/v2/models/ModelStudioConfigVersion/latest.md) | Public Beta |
| [v2.models.ModelStudioConfigVersion.list](../../contracts/v2/models/ModelStudioConfigVersion/list.md) | Public Beta |
| [v2.models.ModelStudioRun.list](../../contracts/v2/models/ModelStudioRun/list.md) | Public Beta |
| [v2.models.ModelStudioTrainer.get](../../contracts/v2/models/ModelStudioTrainer/get.md) | Public Beta |
| [v2.models.ModelStudioTrainer.list](../../contracts/v2/models/ModelStudioTrainer/list.md) | Public Beta |
| [v2.models.ModelVersion.create](../../contracts/v2/models/ModelVersion/create.md) | Private Beta |
| [v2.models.ModelVersion.get](../../contracts/v2/models/ModelVersion/get.md) | Public Beta |
| [v2.models.ModelVersion.list](../../contracts/v2/models/ModelVersion/list.md) | Public Beta |

[All services](../../catalog.md) | [SDK handling](../../client-behavior.md)

[Part 1](index.md)
