# SDK clients, response modes and finite work

[REST development](../rest-api.md) | [Operation catalog](catalog.md)

## Client and API version

`from foundry_sdk import FoundryClient, AsyncFoundryClient` selects v2.
For v1 use the clients exported by `foundry_sdk.v1`. An operation ID includes
its API version. Do not reuse a v2 signature or model for a v1 method.
SDK 1.101.0 is the verified release; its OpenAPI document version is 1.1697.0.
Repository placeholder `0.0.0` metadata is not the prepared runtime version.

The operation contract retains actual synchronous and asynchronous return
annotations. Select handling from those annotations and the response mode.
`_sdk_internal` is a transport mechanism used by SDK wrappers, not an
authorization option or ordinary business input.

## Response modes

| Mode | Sync handling | Async handling |
| --- | --- | --- |
| Ordinary decoded result | Call the method; use its typed result. | Await a method returning `Awaitable[...]`. |
| Ordinary paged result | Iterate `ResourceIterator`; impose a finite object budget. | Iterate `AsyncResourceIterator` with `async for`; the iterator itself is not awaitable. |
| `with_raw_response` | Result is `ApiResponse[T]`; inspect `status_code`, then `decode()` and `close()`. | Await `AsyncApiResponse[T]`; `decode()` is synchronous, then `await aclose()`. |
| `with_streaming_response` | Use `with` around the returned context manager, consume `iter_bytes()` and leave the context. | Use `async with` around the context manager, consume `aiter_bytes()` and leave the context; do not await the context manager itself. |
| Table/Arrow/Parquet or SSE | Follow the operation's actual return type and stream format. | Follow its actual async return type and event/container lifetime. |

Raw paging returns a page model rather than an automatically traversed object
iterator. Its `data` and `next_page_token` fields are SDK names; wire aliases
are `data` and `nextPageToken`. Empty `data` with a next token is an intermediate
page. It does not signal completion.

## Bounded pagination

Use [the local page helper](../../examples/rest/common/bounded_pages.py) when
page counts, resumable partial results or repeated-token checks matter. Bind
the resource and filters to a raw-response method, then pass it to `fetch_pages`.

```python
from functools import partial

# The helper is examples/rest/common/bounded_pages.py in this skill.
fetch_page = partial(
    client.filesystem.Folder.with_raw_response.children,
    folder_rid=folder_rid, page_size=100, request_timeout=30,
)
result = fetch_pages(fetch_page, max_pages=10, max_items=1000)
if not result.complete:
    # Retain items, any remaining_on_page, cursor and reason for continuation.
    print(result.reason, result.next_page_token)
```

`fetch_pages_async` accepts the asynchronous raw-response method. Its helper
awaits each page, decodes it and closes the response. It cannot consume an
ordinary asynchronous object iterator. The helpers stop on repeated tokens,
page or item budgets and report partial progress. An oversized final page
retains `remaining_on_page`; process those values before following its cursor.
Tokens are opaque. Do not construct them from resource names or restart a
mutation because a read reached its retrieval budget.

Object Storage V1-backed Ontology list operations have a 10,000-object
cross-page limit where documented. Object Storage V2 and other resource lists
have different limits. Keep the operation's own restriction and a finite
application budget; one resource family's limit is not a universal rule.

## Serialization and local types

SDK model attributes use Python names. JSON uses declared aliases, for example
`parent_folder_rid` becomes `parentFolderRid`. The SDK serializes model bodies
with aliases and omits model fields whose value is `None`. A raw bytes body
passes as bytes; a JSON list/dictionary is encoded as JSON. Read the method's
body and content-type contract before sending binary data.

`Optional[T]` permits null; it does not by itself make a Pydantic field
optional to supply. A default controls omission. TypedDict `NotRequired`
keys may be omitted. Enum/union alternatives and discriminators are retained
in the local definitions. RID/UUID patterns, long-integer JSON serialization,
timezone-aware datetimes and positive request timeouts have complete
[SDK primitive definitions](models/_core/RID.md) with related local links.

Path values are percent-encoded by the SDK; query entries with `None` are
omitted and list query values are repeated. Generic JSON/Ontology property
maps still require the task's supplied synthetic schema or permitted metadata.

## Table results and server-sent events

An ordinary table result can be `ArrowTableResponse` or `ParquetTableResponse`,
depending on the operation's requested format. Both extend `bytes`: they contain
the complete response payload, rather than an open HTTP response. They have no
`close()` method. `to_pyarrow()` parses the corresponding Arrow IPC stream or
Parquet file and caches the resulting Arrow table. `to_pandas()`, `to_polars()`
and `to_duckdb()` convert that table using the prepared optional libraries.
Missing conversion dependencies raise `ImportError`; malformed table bytes are
a format failure, rather than an empty successful table.

Ordinary table decoding buffers the payload. A row limit alone does not establish
a byte limit, especially for wide or binary columns. For a strict download budget,
use the operation's streaming-response wrapper, accumulate only up to the chosen
byte limit, close the context on exhaustion, then parse the complete bounded bytes
using the requested format. A raw-response wrapper returns its declared raw bytes
when decoded; do not assume that it performs the ordinary table conversion.

Operations whose actual return is `SseContextManager[...]` use `with`; their
asynchronous counterpart uses `async with` on `AsyncSseContextManager[...]`.
These context managers close their underlying HTTP response when the block ends,
including an early stop or exception. Iterate the synchronous response with
`iter_sse()` and the asynchronous response with `aiter_sse()`. Each `SseEvent`
contains a typed `data` payload and the framing fields `event`, `id` and `retry`.
The framing identifier is not automatically a business-message identifier or a
guarantee that reconnecting resumes an operation.

The SDK skips SSE dispatches with empty data. Nonempty data must be valid JSON
matching the operation's event model. Invalid content type, invalid event payload
and repeated consumption are reported as `SseContentTypeError`,
`SseEventDecodeError` and `StreamConsumedError`. Set a finite event budget and
deadline; a request timeout alone is insufficient for a continuously active
stream. If the task requires cancellation of server work, follow that operation's
separate cancellation contract. Closing its response establishes client cleanup,
not cancellation or completion of the server's effect.

## Timeouts, throttling and uncertain writes

Set a default timeout with `Config(timeout=...)` and an operation-specific
positive integer `request_timeout` where needed. Set finite attempts and a
total application deadline separately from per-request timeout.

In this release's synchronous retry middleware, `max_retries` feeds the
maximum attempt count, defaults to 4, and uses a truthy fallback: zero selects
the default. Use `max_retries=1` for one attempt. Throttling errors `429` and
`503` are the middleware's retryable conditions when automatic QoS retry is
selected; server retry hints can forbid retry. The example client propagates
those errors to an explicitly bounded caller. Async return/lifetime behavior
must be handled from its actual client; do not infer a sync retry guarantee for
a coroutine. Application-level deadlines and attempts remain explicit.

After a timeout on a create, upload, Action, commit, deployment or agent
interaction, the effect may be uncertain. Retain the request/resource IDs and
inspect the resource-specific state or supported lookup described locally.
If reconciliation cannot establish the outcome, report uncertainty to its
owner before another mutation. A request ID is not an idempotency key unless
the operation contract documents that behavior.

## Errors and cleanup

Named method errors have local parameter models. Generic `PalantirRPCException`
attributes are `name`, `error_code`, `error_instance_id`, `parameters` and
`error_description`, corresponding to wire fields `errorName`, `errorCode`,
`errorInstanceId`, `parameters` and `errorDescription`. An absent field is `None`;
do not assume that every failed HTTP response supplies a structured RPC envelope.
Keep the available identifiers for diagnosis. Correct invalid input, identity or permission before a
retry. An unavailable API, denied capability and missing resource need distinct
recovery. `429`/`503` alone do not authorize an unbounded retry or a write replay.

Close raw responses and streams after success, cancellation and failure.
For byte streams, bound accumulated bytes and validate the expected content
format before interpreting them as JSON, table data or model output. For a
long-running job/session/build, use a finite status-poll budget and explicit
terminal states from that resource contract. Budget exhaustion is a pending
outcome, not completed work.
