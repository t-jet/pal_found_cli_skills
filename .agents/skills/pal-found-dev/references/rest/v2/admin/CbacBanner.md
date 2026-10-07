# v2 admin: CbacBanner

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

A classification banner expresses the classification represented by a set of marking IDs
using a string and colors. Use it for display after resolving actual marking identities.
Banner rendering is separate from permission enforcement.

## Prepare the application

Use prepared SDK 1.101.0 and an authorized identity for the intended enrollment. Resolve
the resource identities and complete request models linked below before calling a
method. Offline fixtures use synthetic identities and an actual SDK HTTP transport; they
need prepared Python, SDK and httpx and contact no enrollment.

Verify the application grants, resource permissions and capability enablement in the
tenant. SDK source does not enumerate a universal role or scope for every operation;
operation-specific documented requirements below take precedence. Source does not
provide a universal idempotency guarantee. For uncertain writes, retain request identity
and reconcile through authorized reads before repeating.

## Operations and outcome checks

### get

Supply resolved marking IDs and inspect the returned banner text and colors. Use them
for classification display; enforce access through actual resource permissions and
markings.

[Exact parameters, request, result and error models](../../contracts/v2/admin/CbacBanner/get.md).

[Executable SDK example](../../../../examples/rest/072/v2/admin/CbacBanner/get.py):

```bash
python -B examples/rest/072/v2/admin/CbacBanner/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CbacBannerNotFound | The given CbacBanner could not be found. |
| CbacUnavailable | CBAC is not available. |
| GetCbacBannerPermissionDenied | The provided token does not have permission to get the CBAC banner for the markings. |
| UnknownClassificationBannerDisplayType | The provided classification banner display type is not recognized. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
