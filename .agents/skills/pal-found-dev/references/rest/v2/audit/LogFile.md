# LogFile: audit operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

Audit log files expose records for an authorized audit workflow. Decide a bounded time or page window and retain the file identity used for later review. Content is a byte response; close its stream and enforce a size limit.

Prepare SDK 1.101.0 and an identity authorized for the exact tenant resource. Check each contract for its API stage and endpoint-specific restrictions. No universal role or retry guarantee is implied by these operations. For an uncertain write, read the exact RID and effect before repeating it.

## Python client route

With a configured `FoundryClient` named `client`, use `client.audit.Organization.LogFile` for this resource. Each operation below is a method on that resource client. The linked contracts identify available `with_raw_response` and `with_streaming_response` wrappers. The multi-page fixture uses the public root client with a fake HTTP transport and no tenant access.

## Operations

### content

Read one selected log file as bytes. Limit total bytes and close the response; preserve file identity and retrieval window for audit traceability.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/audit/LogFile/content.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/audit/LogFile/content.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### list

Discover available log files with bounded pagination. Carry the returned continuation token and record partial discovery if the budget ends.

Choose a fixed inclusive date window for a finite historical search. The
initial request requires `start_date` even though the Python parameter is
optional; `end_date` may be omitted for ongoing polling, whose result cannot
be called complete while new logs arrive. A `ResourceIterator` exposes its
already fetched page as `.data` and its continuation as `.next_page_token`.
Read those properties without iterating the object, since iteration can make
more requests than the application budget permits.

```python
from datetime import date
from time import monotonic

start_date = date(2026, 10, 1)  # replace with the approved audit window
end_date = date(2026, 10, 7)
if start_date > end_date:
    raise ValueError("The audit start date must be on or before the end date")
deadline = monotonic() + 30
cursor = None
seen = set()
files = []
result = {"complete": False, "reason": "page_budget", "cursor": None}
for _ in range(5):
    remaining = deadline - monotonic()
    if remaining <= 0:
        result = {"complete": False, "reason": "time_budget", "cursor": cursor}
        break
    page = client.audit.Organization.LogFile.list(
        organization_rid, start_date=start_date, end_date=end_date,
        page_size=100, page_token=cursor,
        request_timeout=min(5, max(1, int(remaining))),
    )
    batch = page.data  # read only the fetched page; do not iterate the iterator
    if len(files) + len(batch) > 500:
        files.extend(batch[:500 - len(files)])
        result = {"complete": False, "reason": "item_budget", "cursor": cursor}
        break
    files.extend(batch)
    following = page.next_page_token
    if following is None:
        result = {"complete": True, "reason": None, "cursor": None}
        break
    if following == cursor or following in seen:
        result = {"complete": False, "reason": "repeated_token", "cursor": following}
        break
    seen.add(following)
    cursor = following
    result["cursor"] = cursor
# Use files with result. A false complete flag means this is only a prefix.
```

An empty page may still carry a continuation token. Continue within the
budget; claim complete only when the fixed-window response has no next token.
The [multi-page offline fixture](../../../../examples/rest/073/v2/audit/LogFile/list_pagination.py)
checks a populated page, an empty page with continuation, repeated tokens,
page, item and time budgets, and the named `MissingStartDate` error without
connecting to a tenant. Each incomplete result retains a reason and cursor.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/audit/LogFile/list.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/audit/LogFile/list.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.
