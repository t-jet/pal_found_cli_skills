# LinkedObject operations

[REST development](../../../rest-api.md) | [Ontology service](index.md) | [Operation catalog](../../catalog.md)

## Concept and lifecycle

Link traversal starts from a known source object and outgoing link type. A link definition and an actual visible linked object are different; pagination may observe changing data.

## Prerequisites

Use the frozen Foundry Python SDK 1.101.0 and an authorized Ontology, branch, resource identifier, acting identity and exact type/parameter names from the enrollment. Prepare the linked local models before a live request. Synthetic examples run offline with the prepared SDK and mock transport; real reads or writes require enrollment access, resource permissions and any listed beta enablement. An administrator or resource owner supplies missing grants and capability access.

## Procedure and operation choices

Select the operation below, read its exact request/response/error model, then adapt the linked SDK fixture with authorized resource values. The fixture uses synthetic identifiers and checks serialized transport; it does not assert tenant behavior. Record branch, version, page/snapshot context, response and named errors for the actual call.

### `LinkedObject.get_linked_object`

Stage: Stable. Required SDK arguments: `ontology`, `object_type`, `primary_key`, `link_type`, `linked_object_primary_key`.

Get one target from a source object's outgoing link. The [Palantir get example](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/linked-objects/get-linked-object) uses object type API name `employee`, source key `50030`, link `directReport`, and target key `80060`. The fixture checks a matching target object. Handle `LinkedObjectNotFound` through the SDK's `NotFoundError`; the wire error can also mean the token cannot access the target.

Read [exact contract](../../contracts/v2/ontologies/LinkedObject/get_linked_object.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/LinkedObject/invoke_get_linked_object.py): `python -B examples/rest/081/v2/ontologies/LinkedObject/invoke_get_linked_object.py` from skill root. Named failure in source text: `LinkedObjectNotFound`.

### `LinkedObject.list_linked_objects`

Stage: Stable. Required SDK arguments: `ontology`, `object_type`, `primary_key`, `link_type`.

List targets for an outgoing link. The [Palantir list example](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/linked-objects/list-linked-objects) shows `employee` key `50030` with `directReport` targets. Continue through empty pages with a new `nextPageToken`, within finite page, item and time budgets. Pages can change during traversal; use `snapshot=True` when consistency matters. Object Storage V1 limits results to 10,000; `ObjectsExceededLimit` arrives as SDK `BadRequestError` with wire name `ObjectsExceededLimit` and code `INVALID_ARGUMENT`. Object Storage V2 has no such object count limit.

Read [exact contract](../../contracts/v2/ontologies/LinkedObject/list_linked_objects.md) for optional parameters, response modes, model fields and wire errors. [Offline SDK fixture](../../../../examples/rest/081/v2/ontologies/LinkedObject/invoke_list_linked_objects.py): `python -B examples/rest/081/v2/ontologies/LinkedObject/invoke_list_linked_objects.py` from skill root. Named failure in source text: `ObjectsExceededLimit`.

## Worked example

With a configured `foundry_sdk.v2.FoundryClient` named `client`, list the outgoing `directReport` targets for an authorized `employee` key. Replace these illustrative values with your Ontology, source key, link API name and authorized target key. The list method normally yields an iterator; its raw wrapper exposes page tokens.

```python
from time import monotonic

links = client.ontologies.LinkedObject

page_token = None
target_keys = []
seen_tokens = set()
max_pages, max_items = 20, 1000
deadline = monotonic() + 30
incomplete_reason = None
for page_number in range(max_pages):
    remaining = deadline - monotonic()
    if remaining < 1:
        incomplete_reason = "time budget exhausted before next request"
        break
    raw = links.with_raw_response.list_linked_objects(
        ontology="palantir", object_type="employee", primary_key="50030",
        link_type="directReport",
        page_size=min(100, max_items - len(target_keys)),
        page_token=page_token, snapshot=True, request_timeout=int(remaining),
    )
    try:
        page = raw.decode()
    finally:
        raw.close()
    available = max_items - len(target_keys)
    target_keys.extend(obj["__primaryKey"] for obj in page.data[:available])
    page_token = page.next_page_token
    if len(page.data) > available:
        incomplete_reason = "item budget exhausted"
        break
    if page_token is None:
        break
    if page_token in seen_tokens:
        incomplete_reason = "repeated continuation token"
        break
    seen_tokens.add(page_token)
    if len(target_keys) >= max_items:
        incomplete_reason = "item budget exhausted"
        break
else:
    incomplete_reason = "page budget exhausted"

list_result = {"keys": target_keys, "complete": incomplete_reason is None,
               "incomplete_reason": incomplete_reason, "next_page_token": page_token}
if not list_result["complete"]:
    print(f"Partial linked-object list: {incomplete_reason}; {len(target_keys)} keys")


target = links.get_linked_object(
    ontology="palantir", object_type="employee", primary_key="50030",
    link_type="directReport", linked_object_primary_key="80060",
)
assert target["__primaryKey"] == 80060
assert target["__apiName"] == "Employee"
if list_result["complete"]:
    assert 80060 in target_keys
```

The local list fixture checks two raw pages, forwards `nextPageToken` as `pageToken`, and checks both target identities. `list_result` identifies partial results; do not use its keys as a complete inventory unless `complete` is true. The deadline stops new requests after its check, but does not interrupt an in-flight SDK call. SDK retry behavior can also consume the time budget. The get fixture checks `LinkedObjectNotFound`; a missing or inaccessible target needs caller and link checks before retry.

The linked operation fixtures show actual SDK method invocation, serialized request and decoded response/error using a local mock transport. Their synthetic values are test data. Replace them with authorized identifiers and typed payloads from each linked contract; verify the live result under the intended identity before asserting a platform effect.

## Expected result and checks

Record exact operation ID, API version, release stage, branch, requested IDs, returned IDs, page/snapshot token, response mode and decoded result. For effectful calls, inspect validation/commit state and fresh target data; a successful HTTP response alone may not establish the business result. For lists, finish pagination before claiming completeness.

## Failures and recovery

On a missing or filtered result, verify Ontology/type/API names, branch and effective caller permissions. On schema rejection, compare payload fields, requiredness, aliases and discriminator values with the linked models. On a timeout after an effectful call, reconcile target or transaction state before retrying. Bound pages, streamed bytes and time windows; close streaming/raw responses according to [client lifetimes](../../client-behavior.md). Missing beta enablement is a prerequisite to resolve with the enrollment owner.
