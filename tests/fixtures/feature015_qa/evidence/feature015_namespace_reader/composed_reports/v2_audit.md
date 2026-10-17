# v2.audit: staged composed-client reader

## Capability and lifecycle choice

LogFile.list discovers audit files. Use raw pages with max_pages/max_items, preserve opaque next_page_token even after an empty page, and report partial discovery on budget exhaustion. Selected `client.audit.Organization.LogFile.list` (Stable, SDK 1.101.0). Local evidence: `references/rest/contracts/v2/audit/LogFile/list.md#purpose-and-parameter-meaning` and `#public-python-client-route` in the isolated skill. This reads or changes only the effect named by that method; fixture success is not a live tenant outcome.

## Prerequisites, version and access boundary

Prepared Python, `foundry-platform-sdk==1.101.0`, `httpx`, synthetic IDs and `httpx.MockTransport` suffice locally. For enrollment execution, configure an authorized host and acting token, verify the exact resource/branch access, and check capability provision or preview enablement with an administrator where applicable. No public internet is needed to author or run this fixture. The reader denied DNS and sockets (`PUBLIC_NETWORK_DENIED`); no localhost exception was used. The isolated skill tree SHA256 is `707a17db544513e1cf911a4825aae0fc92582b7ac455179c38a86ead8e4d1d32`; installed SDK Python tree SHA256 is `50798bf53dc0ec0e55c4ab5497cd1982cfcb9165aca25850a1b692054d2f7511`. Fixture evidence cannot establish live permission, availability, or result.

## Exact steps and adaptable code

The isolated contract's `#sdk-invocation-contract` states `def list(self, organization_rid: core_models.OrganizationRid, *, end_date: typing.Optional[date]=None, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, start_date: typing.Optional[date]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[audit_models.LogFile]: ...`. The composed call below uses the parameters from the staged runnable fixture. Replace the synthetic host/token/IDs only after authorization. For binary or unbounded results, use the operation's streaming/paging guidance and finite byte/page budgets.

```python
from foundry_sdk import FoundryClient
from foundry_sdk import Config, UserTokenAuth

client = FoundryClient(
    hostname="offline.example.invalid",
    auth=UserTokenAuth(token="offline-fixture-token"),
    config=Config(timeout=30, max_retries=1,
                  propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
)
raw = client.audit.Organization.LogFile.with_raw_response.list(organization_rid='ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001', request_timeout=30)
try:
    value = raw.decode()
finally:
    raw.close()
```

The runnable synthetic artifact is `.ept/tmp/feature015_namespace_reader/run_composed.py`; its fake transport supplies the staged example at `examples/rest/073/v2/audit/LogFile/list.py`. Run from repository root with `python .ept/tmp/feature015_namespace_reader/run_composed.py`. The fixture asserts method/path, query/header/body serialization, decoded result and raw-response closure; generic application code must make its own result assertions.

## Result and checks

Observed `GET /api/v2/audit/organizations/ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001/logFiles`; decoded synthetic result shape: `data`. One success plus `2` named-error requests passed through the public composed route. Exact result is in `composed_results.json` and stdout in `composed_stdout.txt`. A successful read gives metadata or bytes only; it does not prove a later build, release or mutation effect.

## Failure and bounded recovery

Named errors exercised: `ListLogFilesPermissionDenied, MissingStartDate`. A repeated token stops traversal; authorization errors need audit access review, while throttling needs a bounded retry. The isolated contract's `#documented-operation-errors` and `#wire-request` identify the error envelope and request. Stop after finite attempts; preserve IDs and report partial/pending state on page, byte or poll budget exhaustion. For an uncertain mutation, reconcile its supported status before replay.

## Evidence limit

This composed-route run verifies one synthetic request and its named-error fixtures. It does not independently establish multi-page traversal, strict binary byte limiting, live enrollment behavior, or all six semantic dimensions. Those require separate QA scoring and task-specific exercises. J11/J12 historical failures remain unchanged.
