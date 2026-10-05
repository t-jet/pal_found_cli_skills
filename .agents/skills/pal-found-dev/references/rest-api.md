# Develop with the Foundry REST API

The Foundry REST API exposes platform resources through HTTPS endpoints. Use it when an integration needs direct HTTP access to datasets, Ontology resources, functions, or administrative services. Each operation has its own request shape, required permissions, response type, and release stage. Start with its endpoint page in the [API reference](https://www.palantir.com/docs/foundry/api/) rather than assuming that related operations share parameters.

The [Foundry platform Python SDK](https://www.palantir.com/docs/foundry/api/v2/general/overview/sdks) wraps platform API endpoints. Use it when typed methods, authentication helpers, and response handling fit the application. For an application built around the objects, links, and Actions defined in one enrollment's Ontology, consider its generated [Ontology SDK](https://www.palantir.com/docs/foundry/ontology-sdk). The platform SDK also exposes Ontology endpoints, including metadata such as object types and action types. The installed `pal_found_cli` is another interface with its own supported command set; an API endpoint appearing here does not imply a corresponding CLI command.

## Host, version, and endpoint

Send requests to the HTTPS hostname of the target Foundry enrollment, followed by `/api/v2/...` or the version shown on the endpoint page. For example, [Get Dataset](https://www.palantir.com/docs/foundry/api/v2/datasets-v2-resources/datasets/get-dataset) is `GET /api/v2/datasets/{datasetRid}` and is marked Stable in the Python SDK's v2 method reference. A dataset RID identifies the resource; its display name does not replace the RID in this path. Find the hostname in the browser URL for that enrollment. [Getting started](https://www.palantir.com/docs/foundry/api/general/overview/getting-started) explains the host and first request.

The major API version is part of the URL. A change from v1 to v2 can change request or response contracts. Within a major version, clients must tolerate additions such as response fields and enum values. Check an endpoint's release stage and deprecation notice before depending on it. [Versioning](https://www.palantir.com/docs/foundry/api/general/overview/versioning) describes these guarantees.

## Authentication and permissions

Every request carries `Authorization: Bearer <access token>`. A temporary user token has its creator's permissions and is suitable for local development; keep it in an environment variable and revoke it when finished. Production applications use OAuth2. The authorization-code grant acts on behalf of a signed-in user; client credentials act as a service user. Register the application and request the scopes shown on each endpoint page. Effective access also depends on the user or service user's Foundry permissions. A scope alone does not grant access to a resource. See [API authentication](https://www.palantir.com/docs/foundry/api/general/overview/authentication) and [OAuth2 client setup](https://www.palantir.com/docs/foundry/platform-security-third-party/writing-oauth2-clients).

This read-only example uses a development token and an enrollment hostname without a scheme:

```bash
export FOUNDRY_HOSTNAME="example.palantirfoundry.com"
export FOUNDRY_TOKEN="<temporary-user-token>"
export DATASET_RID="ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da"

curl --fail-with-body --connect-timeout 10 --max-time 30 \
  -H "Authorization: Bearer ${FOUNDRY_TOKEN}" \
  "https://${FOUNDRY_HOSTNAME}/api/v2/datasets/${DATASET_RID}"
```

The Get Dataset endpoint requires `api:datasets-read` when called by a third-party OAuth2 application. A successful response is JSON containing the dataset's `rid`, `name`, and `parentFolderRid`. The token must also be allowed to read that dataset. [Get Dataset](https://www.palantir.com/docs/foundry/api/v2/datasets-v2-resources/datasets/get-dataset) documents both the scope and response.

## Requests and responses

Read the operation page for its HTTP method, path, query parameters, JSON body, headers, response content type, and errors. Use `Content-Type: application/json` for a JSON request body. Do not assume every response is JSON: table reads and file or media content can return Arrow, CSV, or binary content. Handle those as bytes or streams according to their endpoint contract. [Getting started](https://www.palantir.com/docs/foundry/api/general/overview/getting-started) shows GET and POST requests; the [API reference](https://www.palantir.com/docs/foundry/api/) supplies operation contracts.

For a write, confirm the target branch, resource RID, and body before sending. Dataset files, transactions, and Ontology Actions have different commit and validation behavior; an HTTP success only proves the documented operation returned successfully. If the operation starts asynchronous work, use its status endpoint to determine the outcome.

## Paging

List endpoints that return multiple objects can return a `data` array and `nextPageToken`. Repeat the same request with `pageToken=<nextPageToken>` until no next token remains. Treat tokens as opaque and short-lived. `pageSize` is a requested size, not a guaranteed response length. Data may change between pages; snapshot pagination exists only on endpoints that explicitly offer it. The [List Objects endpoint](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-objects/list-objects) has a 10,000-object cross-page limit for Object Storage V1 backed objects; Object Storage V2 backed objects have no such platform limit. Bound total work in your client and narrow the query when a platform limit applies. See [Paging](https://www.palantir.com/docs/foundry/api/general/overview/paging).

```python
import os

import requests

host = os.environ["FOUNDRY_HOSTNAME"]
token = os.environ["FOUNDRY_TOKEN"]
ontology = os.environ["ONTOLOGY_RID"]
object_type = os.environ["OBJECT_TYPE_API_NAME"]
url = f"https://{host}/api/v2/ontologies/{ontology}/objects/{object_type}"
headers = {"Authorization": f"Bearer {token}"}
page_token = None
seen = 0
max_objects = 10_000  # Example client limit; OSv1 has the same platform ceiling.
max_pages = 100
used_tokens = set()

for _ in range(max_pages):
    params = {"pageSize": min(100, max_objects - seen)}
    if page_token:
        if page_token in used_tokens:
            raise RuntimeError("Repeated page token; stop to avoid an endless loop")
        used_tokens.add(page_token)
        params["pageToken"] = page_token
    response = requests.get(url, headers=headers, params=params, timeout=30)
    response.raise_for_status()
    page = response.json()
    for obj in page["data"]:
        if seen >= max_objects:
            raise RuntimeError("Client retrieval limit reached; narrow the query")
        print(obj["properties"])
        seen += 1
    page_token = page.get("nextPageToken")
    if not page_token:
        break
    if seen >= max_objects:
        raise RuntimeError("Client retrieval limit reached; narrow the query")
else:
    raise RuntimeError("Client page limit reached; narrow the query")
```

The endpoint and fields follow Palantir's [paging example](https://www.palantir.com/docs/foundry/api/general/overview/paging). Install `requests` for this direct HTTP example. Use the Python SDK's iterator when direct control of page requests is unnecessary.

## Errors, throttling, and retries

Foundry errors use HTTP `4xx` or `5xx` status codes and a JSON body with `errorCode`, `errorName`, `errorInstanceId`, and `parameters`. Record the instance ID when diagnosing a failed call. A `404` may mean the resource is missing or the caller cannot access it, as [Get Dataset](https://www.palantir.com/docs/foundry/api/v2/datasets-v2-resources/datasets/get-dataset) states. Fix invalid input, authentication, or permissions before retrying a `400`, `401`, or `403`. The [error reference](https://www.palantir.com/docs/foundry/api/general/overview/errors) lists operation-specific errors.

Foundry can throttle calls with `429` or `503`; [API limits](https://www.palantir.com/docs/foundry/api/general/overview/limits) recommends exponential backoff. Bound retry count and concurrency. Before retrying a create, upload, Action, or other write after a timeout, check its operation semantics and whether the first attempt may already have succeeded. Blind replay can produce duplicate effects.

## Python SDK relationship

Install `foundry-platform-sdk` and create `FoundryClient` with the enrollment hostname and an auth provider. `UserTokenAuth` is useful for development. For service applications, the SDK supports `ConfidentialClientAuth` with a registered OAuth2 client and scopes; it handles token refresh for that flow. Do not embed credentials in source. The [platform SDK overview](https://www.palantir.com/docs/foundry/api/v2/general/overview/sdks) explains when to choose this generic interface rather than an Ontology SDK.

```python
import os

import foundry_sdk

client = foundry_sdk.FoundryClient(
    auth=foundry_sdk.UserTokenAuth(os.environ["FOUNDRY_TOKEN"]),
    hostname=os.environ["FOUNDRY_HOSTNAME"],
)
dataset = client.datasets.Dataset.get(os.environ["DATASET_RID"])
print(dataset.name, dataset.rid)
```

The SDK groups operations by API version and resource. Its resource iterators fetch later pages as you iterate. SDK methods validate typed arguments and raise exceptions for API errors; catch a specific documented exception where recovery is possible, or `PalantirRPCException` for a general API failure. For large binary responses, use the resource's `with_streaming_response` interface and close it with a context manager. Check the SDK method reference for the exact arguments and result type before translating a raw REST request.

## Development workflow

1. Locate the operation in the [API reference](https://www.palantir.com/docs/foundry/api/). Check version, release stage, required scope, permissions, request schema, response type, and documented errors.
2. Try a read-only request against a non-production resource using a short-lived development token. Confirm the target enrollment and RID.
3. Implement paging, bounded timeouts, and error handling. Add backoff for throttling; define write replay behavior before retrying writes.
4. Test writes against a development branch or resource, then move to production OAuth2 credentials and the least scopes required by those endpoints.

The API contract belongs to the endpoint page. Examples here illustrate request shape; substitute identifiers and scopes from the operation being implemented.

[Back to development guide](../SKILL.md)
