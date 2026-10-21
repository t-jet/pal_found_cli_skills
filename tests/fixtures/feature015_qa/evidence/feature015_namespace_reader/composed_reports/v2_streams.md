# v2.streams: staged composed-client reader

## Capability and lifecycle choice

Stream.get_records reads a bounded partition batch from a stream branch and start offset. Preserve view RID; offsets may be sparse, so advance from returned offsets rather than start plus count. No dataset transaction is involved. Selected `client.streams.Dataset.Stream.get_records` (Public Beta, SDK 1.101.0). Local evidence: `references/rest/contracts/v2/streams/Stream/get_records.md#purpose-and-parameter-meaning` and `#public-python-client-route` in the isolated skill. This reads or changes only the effect named by that method; fixture success is not a live tenant outcome.

## Prerequisites, version and access boundary

Prepared Python, `foundry-platform-sdk==1.101.0`, `httpx`, synthetic IDs and `httpx.MockTransport` suffice locally. For enrollment execution, configure an authorized host and acting token, verify the exact resource/branch access, and check capability provision or preview enablement with an administrator where applicable. No public internet is needed to author or run this fixture. The reader denied DNS and sockets (`PUBLIC_NETWORK_DENIED`); no localhost exception was used. The isolated skill tree SHA256 is `707a17db544513e1cf911a4825aae0fc92582b7ac455179c38a86ead8e4d1d32`; installed SDK Python tree SHA256 is `50798bf53dc0ec0e55c4ab5497cd1982cfcb9165aca25850a1b692054d2f7511`. Fixture evidence cannot establish live permission, availability, or result.

## Exact steps and adaptable code

The isolated contract's `#sdk-invocation-contract` states `def get_records(self, dataset_rid: core_models.DatasetRid, stream_branch_name: core_models.BranchName, *, limit: int, partition_id: streams_models.PartitionId, preview: typing.Optional[core_models.PreviewMode]=None, start_offset: typing.Optional[core.Long]=None, view_rid: typing.Optional[streams_models.ViewRid]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> streams_models.GetRecordsResponse: ...`. The composed call below uses the parameters from the staged runnable fixture. Replace the synthetic host/token/IDs only after authorization. For binary or unbounded results, use the operation's streaming/paging guidance and finite byte/page budgets.

```python
from foundry_sdk import FoundryClient
from foundry_sdk import Config, UserTokenAuth

client = FoundryClient(
    hostname="offline.example.invalid",
    auth=UserTokenAuth(token="offline-fixture-token"),
    config=Config(timeout=30, max_retries=1,
                  propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
)
raw = client.streams.Dataset.Stream.with_raw_response.get_records(dataset_rid='ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001', stream_branch_name='synthetic-value', limit=1, partition_id='synthetic-value', request_timeout=30)
try:
    value = raw.decode()
finally:
    raw.close()
```

The runnable synthetic artifact is `.ept/tmp/feature015_namespace_reader/run_composed.py`; its fake transport supplies the staged example at `examples/rest/089/v2/streams/Stream/invoke_get_records.py`. Run from repository root with `python .ept/tmp/feature015_namespace_reader/run_composed.py`. The fixture asserts method/path, query/header/body serialization, decoded result and raw-response closure; generic application code must make its own result assertions.

## Result and checks

Observed `GET /api/v2/highScale/streams/datasets/ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001/streams/synthetic-value/getRecords`; decoded synthetic result shape: `list`. One success plus `1` named-error requests passed through the public composed route. Exact result is in `composed_results.json` and stdout in `composed_stdout.txt`. A successful read gives metadata or bytes only; it does not prove a later build, release or mutation effect.

## Failure and bounded recovery

Named errors exercised: `GetRecordsFromStreamPermissionDenied`. On denied or missing stream, verify branch/RID and grants; after a reset, reconcile view RID before continuing. The isolated contract's `#documented-operation-errors` and `#wire-request` identify the error envelope and request. Stop after finite attempts; preserve IDs and report partial/pending state on page, byte or poll budget exhaustion. For an uncertain mutation, reconcile its supported status before replay.

## Evidence limit

This composed-route run verifies one synthetic request and its named-error fixtures. It does not independently establish multi-page traversal, strict binary byte limiting, live enrollment behavior, or all six semantic dimensions. Those require separate QA scoring and task-specific exercises. J11/J12 historical failures remain unchanged.
