# Container configuration and lifecycle

[Ontology and Compute topics](../ontology-compute.md) · [Development guide](../../SKILL.md)

## Concept and lifecycle

A Compute Module connects a container image to Foundry execution. An image packages
code and dependencies; a container is its running instance. A module configuration
selects image, resources, execution mode and Sources. Each replica runs its configured
containers. Choose a module when the workload needs its own runtime or existing
containerized libraries; compare native [Functions](../ontology/functions.md) and
[Python transforms](../pipelines/python-transforms.md) first.

## Prerequisites

Prepare Docker, a target architecture matching the Foundry resource queue, a cached
Python base image, and approved dependency wheels. The example assumes Python 3.12,
`foundry-compute-modules` and its dependencies already available in `wheels/`.
Record and retain their resolved versions with the build. This incubating SDK can
change; verify its `add_functions` and `start_compute_module` exports before use.

Local code/fixture validation needs no platform connection. Image upload, module
creation/configuration, start and query require authorized enrollment access and
Artifact repository/module permissions. Administrators supply queues and unavailable
network policies. [Execution mode](execution.md) determines identity; [integration](integration.md)
determines Sources and resource bindings. Credentials belong in runtime configuration.

## Procedure

1. Author a pure calculation and typed adapter. The [example files](../../examples/compute/app.py)
   register the adapter with the real Compute Module SDK and start its worker.
   SDK transport manages Foundry discovery/invocation; a generic container HTTP
   server does not implement that protocol.
2. Use the [Dockerfile](../../examples/compute/Dockerfile) with a numeric non-root
   user. Build against a prepared local wheel directory and cached base image:
   `docker build --pull=false --network=none -t compute-score:demo .`
   Run this from the example directory after supplying the declared prepared assets.
3. Inspect `docker image inspect compute-score:demo`: verify architecture, user,
   command and image ID. Execute the local fixture before upload. Running the SDK
   entrypoint without Foundry's mounted runtime values is not a platform smoke test.
4. In Foundry, create/select an Artifact repository. Its Publish to DOCKER page
   supplies enrollment-specific registry address and credentials. Tag the image with
   that exact repository path, authenticate through the authorized registry flow and
   push it. Record the image digest; do not substitute a public registry address.
5. Create Compute Module from the desired project folder. In Configure > Add Container,
   select the Artifact repository/image, choose mode/resources and save with Update
   configuration. Start from Overview; inspect replica logs and readiness.
6. For Function mode, import discovered functions through Functions > Import after
   the module is responsive. Test the selected endpoint in Query with
   `{"amount": 12, "factor": 3}`. Confirm output `36` and the imported input/output schema.

An alternative prepared Python Compute Module Code Repository builds an image when
you Tag version; select that repository and version under Add Container. A code
revision, created image, saved configuration and running replica are separate states.

## Worked example

The local example's `score(context, event)` accepts a typed struct containing integer
`amount` and `factor`, rejects negative values and returns their integer product.
Business calculation lives in `logic.py`; `app.py` binds it to SDK registration.
The Dockerfile sets user `5000` and launches `python app.py`. It has no embedded
Foundry token or invented HTTP request route.

```text
Function mode: no platform permissions
Image: approved Artifact repository image/digest
CPU/memory: queue-approved values
Minimum replicas: 0 for intermittent demonstrations
Maximum replicas: 1
Concurrency: 1
Query endpoint: score
Input: {"amount":12,"factor":3}
Expected output: 36
```

This is a configuration worksheet, not an importable Foundry YAML schema. Adapt
resource allocations and operational minimum to the workload; see [scaling](execution.md).

## Expected result and checks

Run `python verify_fixture.py` in the example directory. It validates calculation,
invalid input, resource-map interpretation and the bounded stream adapter using
synthetic data and a fake session only. Prepared `requests` is required for the
adapter import; the fixture sends no network requests.

At deployment, inspect image pull/start logs, replica readiness, function discovery,
schema import and query outcome separately. An exec readiness probe succeeds at exit
code zero; configure a command that checks actual initialization, not merely process
existence. Readiness failure removes query routing; liveness failure restarts a
container. Neither signal proves business results or dataset commit.

## Failures and recovery

| Observation | Diagnosis and next step |
| --- | --- |
| Image cannot pull/start | Verify registry permission, architecture, numeric user, command and dependencies. |
| Replica running but functions absent | Verify SDK worker startup and typed registration; inspect discovery/schema logs. |
| Probe fails during warmup | Check initialization and timeout; fix the cause before increasing timeout. |
| Repeated restarts | Inspect liveness failure and memory use; do not use restarts to mask an invalid configuration. |
| Negative calculation input | Correct the payload; retrying the same input cannot succeed. |
| Missing wheels/base image | Author and inspect locally; image build is blocked until prepared assets arrive. |

Optional source attribution: [Compute overview](https://www.palantir.com/docs/foundry/compute-modules/overview),
[image deployment](https://www.palantir.com/docs/foundry/compute-modules/get-started),
[container configuration](https://www.palantir.com/docs/foundry/compute-modules/containers),
[probe behavior](https://www.palantir.com/docs/foundry/compute-modules/probes),
[SDK worker](https://github.com/palantir/python-compute-module),
[Function registration](https://www.palantir.com/docs/foundry/compute-modules/functions).
