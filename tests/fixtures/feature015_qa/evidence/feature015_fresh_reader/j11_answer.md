# J11 source-blind reader answer

## Capability and lifecycle

Use v2 `client.filesystem.Folder.with_raw_response.children` for bounded child pages, `client.datasets.Dataset.get` for metadata, and `client.datasets.Dataset.File.with_streaming_response.content` for file bytes. A child can be any resource type. Dataset metadata does not establish permission to read its files. A successful content response is the bytes in the chosen branch view, not proof of a later pipeline build.

## Prerequisites, version and identity

Prepared Foundry Platform SDK and distribution: 1.101.0. Synthetic folder and dataset RIDs, file path, branch `master`, Python/httpx, and a fake user token are supplied. The client uses v2, `UserTokenAuth`, `Config(timeout=30, max_retries=1, propagate_qos="PROPAGATE_429_AND_503_TO_CALLER")`, and positive operation timeouts. A live call needs the exact enrollment hostname, an authorized identity, resource visibility and access, and known branch/file identifiers. No universal scope can be inferred from metadata.

## Ordered steps and example

1. Bind the known folder RID and `page_size=2` to the raw `children` method. Call the local `fetch_pages` helper with `max_pages=3`, `max_items=2`. Decode and close every raw page. Follow an empty page when `nextPageToken` exists.
2. Read dataset metadata with its RID and check its returned RID and parent folder before selecting its file.
3. Stream the selected file from the explicit `master` view. Close the streaming context after success or failure. Stop if accumulated bytes exceed eight. Validate the complete bytes before interpreting content.
4. On a repeated page token, keep the one discovered child, token and partial reason; do not issue a third request for the same cursor. On partial binary consumption, discard it as incomplete and reconcile the view before reuse.

Runnable code: [j11_reader.py](j11_reader.py). Exact SDK paths, serialized method/path/query/headers, result fields, cleanup, and the bounded adverse paths are asserted there. Output: [j11_output.json](j11_output.json).

## Observable results

The fixture run returns one child after an empty intermediate page, completes in two pages, checks the dataset RID and parent, and reads six bytes. A repeated token returns `complete=False`, `reason="repeated-token"` after two pages. A four-byte budget raises before accepting the six-byte payload. Twelve requests went only to `httpx.MockTransport`; both DNS lookup and socket connect were patched to fail.

## Failure and recovery

401 means repair authentication; 403 means check grants and resource policy; 404 means verify dataset, branch, path and visibility. 429 and 503 need finite backoff/status handling under an application deadline; neither authorizes unbounded retry. The fixture verifies that SDK 1.101.0 raises the 401 generic `UnauthorizedError`, typed file permission/missing errors for 403/404, and QoS exceptions for 429/503. A malformed or unsupported content type is a format failure; do not interpret bytes as a valid table or JSON without validating that format. Page or byte budget exhaustion is partial retrieval, never a complete read.

## Access boundary and exact local headings read

Local authoring, synthetic fixture validation and this run require prepared tools only. Live reads require authorized enrollment connectivity and access. The fixture does not establish either.

- `SKILL.md`: `Develop on Foundry`; `Choose a development path`; `Read by task`; `Evidence before delivery`.
- `references/rest-api.md`: `Discover and author any frozen SDK REST operation`; `Concept and lifecycle`; `Prerequisites`; `Procedure`; `Expected result and checks`; `Failures and recovery`; `Access boundary`.
- `references/rest/catalog.md`: `Services`; `Task selection`.
- `references/rest/authentication.md`: `Credentials and acting identity`; `Prepared client`.
- `references/rest/client-behavior.md`: `Client and API version`; `Response modes`; `Bounded pagination`; `Table results and server-sent events`; `Timeouts, throttling and uncertain writes`; `Errors and cleanup`.
- `references/rest/v2/filesystem/Folder.md`: `Folder navigation and creation`; `Concept and lifecycle`; `Prerequisites`; `Procedure`; `Expected result and checks`; `Failures and recovery`; `Access boundary`; `Python client route`.
- `references/rest/v2/datasets/Dataset.md`: `v2 datasets: Dataset`; `Capability and lifecycle`; `Prepare the application`; `Operations and outcome checks`; `get`.
- `references/rest/v2/datasets/File.md`: `v2 datasets: File`; `Capability and lifecycle`; `Prepare the application`; `Client route and bounded content read`; `content`.
- `references/rest/contracts/v2/filesystem/Folder/children.md`: `Purpose and parameter meaning`; `Public Python client route`; `SDK invocation contract`; `Documented operation errors`; `Wire request`; `Response modes`.
- `references/rest/contracts/v2/datasets/Dataset/get.md`: same contract headings.
- `references/rest/contracts/v2/datasets/File/content.md`: same contract headings.
- `examples/rest/common/bounded_pages.py`, `examples/rest/common/mock_transport.py`, `examples/rest/common/response_modes.py`, `examples/rest/073/folders.py`, `examples/rest/074/v2/datasets/file_client_route_regression.py`: local executable patterns.

This is a fixture result, not a tenant execution or self-approval.
